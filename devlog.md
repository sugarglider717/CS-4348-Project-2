# CS-4348-Project-2

## April 13, 2025 - 4:30 PM

### Thoughts So Far:
This is a thread synchronization project simulating a bank with three tellers and 50 customers. Each teller and customer is a thread. Tellers interact with customers, the bank manager, and the safe. Shared resources include the manager (1 at a time), the safe (2 tellers at a time), and the bank door (2 customers at a time). Proper use of semaphores and coordination is essential.

The most complex part will be managing the interaction between customers and tellers without deadlocks or race conditions. I’ll use Python with `threading` and `threading.Semaphore`.

---

## Plan for This Session (4:30 PM - 10:00 PM):

- **Initialization (4:30 PM):**
  - Initialize all necessary semaphores:
    - `bank_open`: ensures customers don't enter until tellers are ready.
    - `manager_semaphore`: allows only one teller to interact with the manager at a time.
    - `safe_semaphore`: limits safe access to 2 tellers at a time.
    - `door_semaphore`: limits entry to 2 customers at a time.
  - Prepare mechanisms (semaphores/queues) to manage teller-customer pairing.
  
- **Class Design:**
  - Create the `Teller` thread class with:
    - Ready signal and waiting for a customer.
    - Transaction process including manager permission for withdrawals.
    - Safe access and logging.
  - Create the `Customer` thread class with:
    - Waiting for the bank to open.
    - Random delay and choice of transaction.
    - Selecting a teller and completing the transaction.
  
- **Output Logs:**
  - Ensure logs are printed in the proper format as described in the assignment.
  
- **Testing Strategy:**
  - Test incrementally (start with fewer customers then scale up to 50).
  - Use random sleep to simulate timing delays during transactions.

---

## During Session

### 4:30 PM - 5:00 PM
- **Setup and Initial Coding:**  
  Created and initialized all semaphores, locks, and events. Defined the basic structure for `Teller` and `Customer` classes. Ensured that logging followed the required format.
  
### 5:15 PM - 5:45 PM
- **Implementing Teller Transactions:**  
  Developed the teller thread logic including:
  - Waiting for customers.
  - Logging transaction requests.
  - Handling both deposit and withdrawal cases.
  - Implementing manager interaction for withdrawals.
  
### 6:00 PM - 6:30 PM
- **Debugging Safe Access:**  
  Encountered a deadlock issue during safe access. Fixed the issue by ensuring that the teller always properly releases the safe semaphore even on errors. Added sleep statements to help simulate realistic transaction times.
  
### 7:00 PM - 7:45 PM
- **Integrating Customer Actions:**  
  Completed the customer thread code. Added the flow where:
  - Customers wait for the `bank_open` event.
  - Announce their chosen transaction.
  - Enter the bank and select a teller.
  - Log messages for selecting a teller, and leaving after their transaction is complete.
  
### 8:30 PM - 9:15 PM
- **Incremental Testing:**  
  Tested the simulation first with 5 customers, then 10, and finally with 50 customers. Verified that the output sequence closely matched the professor’s example.
  - Observed thread output behavior and made minor adjustments to logging order to accommodate concurrency.
  
### 9:30 PM - 10:00 PM
- **Final Debugging and Output Verification:**  
  Performed final testing and verified that:
  - All 50 customers are served without deadlocks.
  - The log output format exactly matches the example provided by the professor.
  - All synchronization constraints (manager, safe, and door access) are met.
  - The simulation terminates correctly with `"The bank closes for the day."` logged at the end.

---

## End of Session Reflection (10:00 PM)
- Completed the full implementation of the simulation in one go.
- Printed all required logs for each step (tellers’ readiness, customer arrivals, transaction handling, safe access, and thread termination).
- Verified synchronization using semaphores, ensuring proper coordination and termination.
- All 50 customers were served correctly and the simulation ended with the expected closing message.
- Next time, I’d consider optimizing log readability (possibly redirecting logs to a file) and further modularizing the code for maintainability.

---

### Ending Thoughts:
Overall, this project was a great exercise and learning experience in thread synchronization and simulating real-world concurrency problems. Coordinating 50 customers and 3 tellers while managing access to shared resources like the manager and safe required careful planning and use of semaphores. I completed the project in a single session, and I am confident the solution is stable and meets the requirements. This experience reinforced the importance of controlling thread interactions and debugging concurrent behavior. If I had more time, I would improve the structure of the code and further enhance the logging to make the simulation even easier to follow during execution.
