# Password Strength Checker

A lightweight command-line tool written in Python to evaluate password strength based on common password security criteria.

The project is designed as a small Software Engineering and Cyber Security fundamentals project, focusing on password evaluation, secure input handling, and clean CLI implementation.

## Features

- Secure password input using hidden terminal input
- Password length evaluation
- Lowercase character detection
- Uppercase character detection
- Number detection
- Special character detection
- Basic common-password detection
- Password strength scoring
- Strength classification:
  - Very Weak
  - Weak
  - Medium
  - Strong
  - Very Strong
- No password storage
- No external dependencies

## How It Works

The checker evaluates the password against several criteria:

```text
Password
   │
   ▼
Input Validation
   │
   ├── Length
   ├── Lowercase
   ├── Uppercase
   ├── Numbers
   ├── Special Characters
   └── Common Password Check
   │
   ▼
Score Calculation
   │
   ▼
Strength Classification
```

Each criterion contributes to the overall password strength score.

The password itself is never stored, logged, or displayed after input.

## Project Structure

```text
password-strength-checker/
├── src/
│   ├── __init__.py
│   ├── checker.py
│   └── main.py
├── tests/
│   └── test_checker.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.10+
- Git

The project uses Python's standard library and does not require third-party packages.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/password-strength-checker.git
```

Enter the project directory:

```bash
cd password-strength-checker
```

No additional package installation is required.

## Usage

Run the application:

```bash
python src/main.py
```

Enter your password when prompted.

The password input is hidden from the terminal using Python's `getpass` module.

Example output:

```text
================================
    Password Strength Checker
================================

Enter password: ********

Password Strength: Strong
Score: 4/5

Criteria:
[✓] Minimum length
[✓] Lowercase letter
[✓] Uppercase letter
[✓] Number
[✓] Special character
```

> The actual password is never printed in the output.

## Strength Criteria

The initial scoring model evaluates the following characteristics:

| Criterion | Description |
|---|---|
| Length | Checks whether the password meets the minimum length requirement |
| Lowercase | Contains at least one lowercase character |
| Uppercase | Contains at least one uppercase character |
| Number | Contains at least one numeric character |
| Special Character | Contains at least one non-alphanumeric character |
| Common Password | Checks against a small list of commonly used passwords |

The final score is mapped to a strength level.

```text
0–1  → Very Weak
2    → Weak
3    → Medium
4    → Strong
5    → Very Strong
```

The scoring system is intended for educational purposes and should not be considered a complete password-security assessment.

## Security Considerations

This project intentionally follows several basic security principles:

- Passwords are entered using hidden terminal input.
- Passwords are not stored in files.
- Passwords are not written to logs.
- Passwords are not printed after input.
- No network connection is required.
- No external service receives the password.
- The project does not attempt to recover, crack, or expose passwords.

The tool evaluates the password locally on the user's machine.

## Testing

Unit tests are provided using Python's built-in `unittest` framework.

Run:

```bash
python -m unittest discover -s tests
```

Example:

```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

## Limitations

This project is intentionally simple and designed for learning.

It does not currently provide:

- Entropy calculation
- Dictionary attack simulation
- Pattern detection
- Keyboard-pattern detection
- Breached-password database checking
- Password generation
- Cryptographic password storage

A strong score from this tool does not guarantee that a password is secure.

## Future Improvements

Possible future improvements include:

- More comprehensive password pattern analysis
- Entropy estimation
- Larger common-password dictionaries
- Detection of repeated characters
- Detection of sequential characters
- Detection of keyboard patterns
- JSON output mode
- Interactive CLI options
- Automated CI testing with GitHub Actions

## Learning Objectives

This project is intended to practice:

- Python fundamentals
- Object-oriented or modular programming
- CLI application development
- Input validation
- Regular expressions
- Unit testing
- Secure input handling
- Basic cyber security concepts
- Git and GitHub workflow


---

# Developer

**Author:** galhkoernia  
**Project Type:** Cyber Security Fundamentals  
**Language:** Python