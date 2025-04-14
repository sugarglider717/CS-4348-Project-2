# CS-4348-Project-2

## April 13, 2025 - 4:30 PM

### Thoughts So Far:
This is a thread synchronization project simulating a bank with three tellers and 50 customers. Each teller and customer is a thread. Tellers interact with customers, the bank manager, and the safe. Shared resources include the manager (1 at a time), the safe (2 tellers at a time), and the bank door (2 customers at a time). Proper use of semaphores and coordination is essential.

The most complex part will be managing the interaction between customers and tellers without deadlocks or race conditions. I’ll use Python with `threading` and `threading.Semaphore`.

---

### Plan for This Session:
- Initialize all necessary semaphores:
  - `bank_open`: coordination so customers don't enter before tellers are ready.
  - `manager_access`: only 1 teller can speak to manager at a time.
  - `safe_access`: only 2 tellers in the safe at once.
  - `door_access`: only 2 customers in bank at a time.
  - Semaphores/queues to handle teller-customer pairing.

- Create `Teller` thread class with:
  - Ready signal
  - Transaction process (get permission if withdraw)
  - Access to safe
  - Notify customer

- Create `Customer` thread class with:
  - Wait for bank open
  - Random delay and transaction
  - Wait for teller
  - Go through full transaction

- Print logs in correct format
- Use random sleep for timing actions

---

### During Session Notes:
- Used `random.randint()` and `time.sleep()` to simulate wait periods.
- Used `Queue` to pair customers and tellers dynamically.
- Faced deadlock during safe access—fixed by ensuring teller releases the safe semaphore even on error.
- Initially forgot to signal customer when teller is done—added semaphore between customer and teller for transaction done notification.
- Tested with 5 customers, then 10, then 50. Output scrolls too fast but verified correct sequence.
- Used locks around shared variables like “customers served” counter.

---

### End of Session Reflection (10:00 PM):
- Completed full implementation of the simulation in one go.
- Printed all required logs for actions.
- Verified synchronization using semaphores.
- All 50 customers served correctly. Program exits after bank closes.
- Would optimize log readability next time by redirecting logs to file or adding delays between thread starts.

### Ending Thoughts:
Overall, this project was a great exercise and learning experience in thread synchronization and simulating real world concurrency problems. Beinb able to Coordinate 50 something customers and 3 tellers while managing access to shared resources like the manager and safe required careful planning and use of semaphores. I was able to complete the project in a single session, and I'm confident the solution is stable and meets the requirements. This experience helped reinforce the importance of controlling thread interactions and debugging concurrent behavior. If I had more time, I would improve the structure of the code and enhance the logging to make the simulation easier to follow during execution.
