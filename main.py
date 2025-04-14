import threading
import time
import random

# Semaphores and locks
manager_semaphore = threading.Semaphore(1)
safe_semaphore = threading.Semaphore(2)
door_semaphore = threading.Semaphore(2)
teller_ready = threading.Semaphore(0)
transaction_lock = threading.Lock()
bank_open = threading.Event()

NUM_TELLERS = 3
NUM_CUSTOMERS = 50

customer_threads = []
teller_threads = []
ready_tellers = 0
all_customers_served = threading.Event()

# Teller class
class Teller(threading.Thread):
    def __init__(self, teller_id):
        super().__init__()
        self.teller_id = teller_id
        self.current_customer = None

    def run(self):
        global ready_tellers
        print(f"Teller {self.teller_id} []: ready to serve")
        with transaction_lock:
            ready_tellers += 1
            if ready_tellers == NUM_TELLERS:
                bank_open.set()

        while True:
            if all_customers_served.is_set() and not any(thread.is_alive() for thread in customer_threads):
                break

            teller_ready.release()
            with transaction_lock:
                print(f"Teller {self.teller_id} []: waiting for a customer")
                if self.current_customer is not None:
                    cust_id = self.current_customer.customer_id
                    print(f"Teller {self.teller_id} [Customer {cust_id}]: asks for transaction")
                    time.sleep(0.01)

                    if self.current_customer.transaction_type == "Withdrawal":
                        print(f"Teller {self.teller_id} [Customer {cust_id}]: going to the manager")
                        with manager_semaphore:
                            print(f"Teller {self.teller_id} [Customer {cust_id}]: getting manager's permission")
                            time.sleep(random.uniform(0.005, 0.03))
                            print(f"Teller {self.teller_id} [Customer {cust_id}]: got manager's permission")

                    print(f"Teller {self.teller_id} [Customer {cust_id}]: going to safe")
                    with safe_semaphore:
                        print(f"Teller {self.teller_id} [Customer {cust_id}]: enter safe")
                        time.sleep(random.uniform(0.01, 0.05))
                        print(f"Teller {self.teller_id} [Customer {cust_id}]: leaving safe")

                    print(f"Teller {self.teller_id} [Customer {cust_id}]: finishes {self.current_customer.transaction_type.lower()} transaction.")
                    print(f"Teller {self.teller_id} [Customer {cust_id}]: wait for customer to leave")
                    self.current_customer = None

            time.sleep(0.01)

        print(f"Teller {self.teller_id} []: leaving for the day")

# Customer class
class Customer(threading.Thread):
    def __init__(self, customer_id):
        super().__init__()
        self.customer_id = customer_id
        self.transaction_type = random.choice(["Deposit", "Withdrawal"])

    def run(self):
        print(f"Customer {self.customer_id} []: wants to perform a {self.transaction_type.lower()} transaction")
        bank_open.wait()
        print(f"Customer {self.customer_id} []: going to bank.")
        door_semaphore.acquire()
        print(f"Customer {self.customer_id} []: entering bank.")
        print(f"Customer {self.customer_id} []: getting in line.")
        print(f"Customer {self.customer_id} []: selecting a teller.")

        teller_ready.acquire()
        with transaction_lock:
            for teller in teller_threads:
                if teller.current_customer is None:
                    teller.current_customer = self
                    print(f"Customer {self.customer_id} [Teller {teller.teller_id}]: selects teller")
                    print(f"Customer {self.customer_id} [Teller {teller.teller_id}] introduces itself")
                    break

        time.sleep(0.01)
        print(f"Customer {self.customer_id} [Teller {teller.teller_id}]: leaves teller")
        print(f"Customer {self.customer_id} []: goes to door")
        print(f"Customer {self.customer_id} []: leaves the bank")
        door_semaphore.release()

# Start tellers
for i in range(NUM_TELLERS):
    teller = Teller(teller_id=i)
    teller_threads.append(teller)
    teller.start()

# Start customers
for i in range(NUM_CUSTOMERS):
    customer = Customer(customer_id=i)
    customer_threads.append(customer)
    customer.start()

# Wait for all customers to finish
for customer in customer_threads:
    customer.join()

all_customers_served.set()

# Wait for all tellers to finish
for teller in teller_threads:
    teller.join()

print("The bank closes for the day.")
