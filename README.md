# CS4348 Project 2: Bank Simulation

## Overview
This project simulates a bank environment using thread synchronization in Python. The simulation involves three teller threads and 50 customer threads. Tellers interact with customers, obtain manager permission for withdrawal transactions, and access a safe (restricted to two tellers at a time). Additionally, the bank door limits entry to two customers at a time. The output is generated in a format closely matching the professor's example.

## Files and Their Roles
- **bank_simulation.py**  
  Contains the complete source code for the simulation. This file defines:
  - The `Teller` class for teller thread behavior.
  - The `Customer` class for customer thread behavior.
  - All synchronization primitives (semaphores, locks, and events) used to manage concurrent interactions and resource access.
- **devlog.md**  
  The development log documenting session-by-session progress, decisions, and troubleshooting. The devlog, along with the commit history, demonstrates the work performed during the project.
- **README.md**  
  This file explains the project purpose, file roles, command line instructions to run the simulation, and other relevant information for the TA.

## How to Compile/Run the Program

### Requirements:
- Python 3.x (use `python3` on the command line)

### Running the Simulation:
1. Open a terminal or command prompt.
2. Change the directory to the root of the repository.
3. Run the program using:
   ```bash
   python3 bank_simulation.py
