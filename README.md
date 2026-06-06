# 🏃 BMI Calculator - Task 1 | Oasis Infobyte Python Internship

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Internship](https://img.shields.io/badge/Internship-Oasis%20Infobyte-orange)
![Level](https://img.shields.io/badge/Level-Beginner-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A command-line **BMI (Body Mass Index) Calculator** built in Python as part of the **Oasis Infobyte Python Programming Internship**. This project takes user inputs like weight and height, calculates the BMI, and classifies it into standard WHO health categories. It supports both **Metric** and **Imperial** unit systems with proper input validation and error handling.

## Author
**Yuvaraj.T.K** — Python Intern @ Oasis Infobyte

## How to Run

```bash
python bmi_calculator.py
```

## Features

- Supports both **Metric** (kg/meters) and **Imperial** (lbs/inches) units
- Calculates BMI using the formula: `BMI = weight / (height × height)`
- Classifies BMI into health categories
- Handles invalid inputs gracefully
- Allows multiple calculations in one session

## BMI Categories

| BMI Range     | Category      |
|---------------|---------------|
| Below 18.5    | Underweight   |
| 18.5 – 24.9   | Normal weight |
| 25.0 – 29.9   | Overweight    |
| 30.0 & above  | Obese         |

## Sample Output

```
=============================================
    🏃 WELCOME TO BMI CALCULATOR 🏃
=============================================

  Select unit system:
  1. Metric   (kg / meters)
  2. Imperial (lbs / inches)
  Enter 1 or 2: 1

  Enter your weight (in kg)    : 70
  Enter your height (in meters): 1.75

=============================================
         📊  BMI CALCULATOR RESULT
=============================================
  Weight        : 70.0 kg
  Height        : 1.75 m
  Your BMI      : 22.86
  Category      : Normal weight
---------------------------------------------
  ✅  Great! You have a healthy BMI. Keep it up!
=============================================
```

## Program Flow

```
START
  │
  ▼
Show Welcome Message + BMI Chart
  │
  ▼
Select Unit System (Metric / Imperial)
  │
  ├── Metric   → Enter weight (kg) + height (meters)
  │
  └── Imperial → Enter weight (lbs) + height (inches)
                      │
                      ▼
                 Convert to kg & meters
  │
  ▼
Validate Input
  ├── Invalid (letters/negative) → ❌ Ask again
  └── Valid → Continue
  │
  ▼
Calculate BMI
  BMI = weight / (height × height)
  │
  ▼
Classify BMI
  ├── Below 18.5  → Underweight
  ├── 18.5 – 24.9 → Normal weight
  ├── 25.0 – 29.9 → Overweight
  └── 30.0 above  → Obese
  │
  ▼
Display Result
  │
  ▼
Calculate Again?
  ├── yes → Go back to Select Unit System
  └── no  → END
```

## Concepts Used

- Functions
- User input & validation
- Exception handling (try/except)
- If/elif/else conditions
- While loops
- Unit conversion

#oasisinfobyte #oasisinfobytefamily #internship #python
