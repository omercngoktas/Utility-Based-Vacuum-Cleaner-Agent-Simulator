# Utility-Based Vacuum Cleaner Agent Simulator

## Project Description
Consider an extended vacuum cleaner world with three locations: rooms A, B, and C. Each room may be clean or dirty. Initially, all three rooms are dirty, and the robot is located in Room B. The vacuum agent perceives the room it is in and whether it is clean or dirty. At any given time step, the agent can move left, move right, suck up the dirt, or do nothing (no-op).
- The agent gets rewarded one point for each clean room at the end of each time step.
- The agent gets penalized 0.5 points for each move action.
- Simulate the performances of two proposed agents (Agent A and Agent B) for 1000 time steps.

## Inputs and Outputs
- Command-line Inputs: Utility values Pa, Pb, and Pc
- Output Text Files:
  - `a.txt`: State – Action information for Agent A
  - `b.txt`: State – Action information for Agent B
  - The format for both files is specified in the assignment description.

## Usage
Execute main.py file under src folder.
Take outputs from output folder.
