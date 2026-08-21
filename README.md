# Personal Data Collector
## Overview
The **Personal Data Collector** is a simple Python program that collects basic personal information from the user, displays the entered data along with its data type and memory address, and calculates the user's approximate birth year.
This project is suitable for beginners who are learning:
- User input in Python
- Data types
- Type conversion
- Variables
- The `type()` function
- The `id()` function
- Basic arithmetic operations
- Output formatting using `print()`
---
## Features
- Collects the user's:
  - Name
  - Age
  - Height (in centimeters)
  - Favourite number
- Displays:
  - Entered value
  - Data type
  - Memory address using `id()`
- Calculates the approximate birth year.
- Prints a thank-you message after execution.
---
## Requirements
- Python 3.x
---
## How to Run
1. Save the program as:
```
personal_data_collector.py
```
2. Open a terminal or command prompt.
3. Navigate to the folder containing the file.
4. Run the program:
```bash
python personal_data_collector.py
```
or
```bash
python3 personal_data_collector.py
```
---
## Example Output
```
Welcome to the interactive personal data collector!
Please enter your name: Alice
Please enter your age: 20
Please enter your height in cm: 165.5
Please enter your favourite number: 7
Thank you! Here is the information we collected:
Name: Alice <class 'str'> Memory Address : 140583728
Age: 20 <class 'int'> Memory Address : 9793696
Height: 165.5 <class 'float'> Memory Address : 140584016
Favourite Number: 7 <class 'int'> Memory Address : 9793280
Your birth year is approximately 2006 (based on your age of 20)
Thank you for using the Personal Data Collector! Have a great day!
```
---
## Concepts Demonstrated
- Variables
- User Input (`input()`)
- Type Conversion (`int()`, `float()`)
- String Handling
- Integer and Float Data Types
- `type()` Function
- `id()` Function
- Arithmetic Operations
- Printing Output
---
## Notes
- The birth year is **approximate** because it is calculated using:
```python
2026 - age
```
It does not consider whether the user's birthday has already occurred this year.
- The memory addresses displayed by `id()` may differ every time the program is executed.
---
## Author
Created as a beginner Python project for learning variables, data types, user input, and basic programming concepts.
