# Assignment 4 - Python Solutions

## Language Used
Python 3

---

# Project 1: Project Euler Solutions

## Description
This project contains Python solutions for the assigned Project Euler problems.  
Each program has been executed successfully and output screenshots are included for reference.

---

# Problems Solved

## 1. Problem 63 — Powerful Digit Counts

### Problem Link
https://projecteuler.net/problem=63

### Python File
solution(P63).py

### Expected Output
```bash
Total Count = 49
```

---

## 2. Problem 313 — Sliding Game

### Problem Link
https://projecteuler.net/problem=313

### Python File
solution(P313).py

### Expected Output
```bash
Answer = 2057774861813004
```

---

# Project Structure

```text
Assignment4/

├── .gitignore
├── README.md
│
├── Ass4EulerPj/
│   │
│   ├── Problem63/
│   │   ├── solution(P63).py
│   │   └── P63_Output.png
│   │
│   └── Problem313/
│       ├── solution(P313).py
│       └── P313_Output.png
│
└── ExeOSCmds/
    ├── execute_commands.py
    └── Output(A4).png
```

---

# How to Run the Programs

## Run Problem 63
```bash
python "solution(P63).py"
```

## Run Problem 313
```bash
python "solution(P313).py"
```

---

# Project 2: Execute OS Commands

## Description
This project executes multiple OS commands using Python and displays the output in dictionary/JSON format.

---

## Features
- Executes multiple OS commands
- Removes duplicate commands
- Handles invalid commands
- Continues execution after errors
- Displays structured JSON output

---

## Python File
execute_commands.py

---

## How to Run

```bash
python execute_commands.py
```

---

# Screenshots Included

- P63_Output.png → Successful execution output of Problem 63
- P313_Output.png → Successful execution output of Problem 313
- Output(A4).png → Successful execution output of Execute OS Commands project

---

# .gitignore

```text
__pycache__/
*.pyc
```