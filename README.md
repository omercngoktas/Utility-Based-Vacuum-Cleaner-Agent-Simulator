# Utility-Based Vacuum Cleaner Agent Simulator

## Overview
This project implements a simulator for a utility-based vacuum cleaner agent. The agent operates in an extended vacuum cleaner world with three rooms (A, B, and C), where each room can be in a clean or dirty state. The agent's objective is to clean the rooms efficiently while maximizing its utility, which is defined as the number of clean rooms at the end of each time step.

The simulator allows users to:
- Add different types of questions to the question bank, including multiple-choice, true/false, fill-in-the-blank, and classic questions.
- Remove questions from the question bank based on specific criteria.
- List all questions in the question bank or filter them based on various criteria such as question text, answer options, correct answer, point value, and difficulty level.
- Generate three types of exams: test (only multiple-choice questions), classic exam (only classic questions), and mixed exam (questions from all types).
- Save exam results to a text file named "exam_results.txt".
- Display the exam score for test exams.

## Features
- Implementation of a utility-based vacuum cleaner agent simulator with various functionalities.
- Support for adding, removing, and listing questions in the question bank.
- Filtering questions based on specified criteria.
- Generation of different types of exams with random questions.
- Saving exam results to a text file.
- Displaying exam scores for specific exam types.
- Design document describing classes, methods, and functionalities used in the project.

## Project Structure
- `src/`: Contains the source code for the vacuum cleaner agent simulator implementation
- `docs/`: Includes the design document and other relevant documentation

## Usage
Execute main.py file under src folder.
Results are saved under output folder.
