# Week 1 — COM161: Intro & Exercises (Student-friendly)


---

## Quick one-sentence summary
Computers take **input → process → output** — we design programs with pseudocode or flowcharts, then use `print`, `input`, **variables**, **data types**, **operators**, and **formatting** to make programs that work and look nice.

---

## Table of contents
1. Designing a program (recipe & flow)
2. Exercise 1 — Largest of two numbers
3. Exercise 2 — Print name & address
4. Exercise 3 — Ask name, age, income
5. Exercise 4 — Approximate age from year of birth (2 versions)
6. Exercise 5 — Format sales and compute leave %
7. Cheat-sheet
8. Teaching tips & mini-project ideas

---

# 1) Designing a program — like planning a recipe
**Idea:** Before coding, plan. Building a program = making a sandwich:
- Decide what sandwich (requirements).
- Write the steps (algorithm).
- Turn steps into pseudocode (plain-English steps) or draw a flowchart (boxes & arrows).
- Cook (code), taste-test (test), serve (deploy).

**Pseudocode** = fake code — plain English steps that read like code.

**Flowchart** = picture boxes showing the steps (Start → Input → Process → Decision → Output → End).

**Fun example pseudocode — pizza order**:
```
BEGIN
  Ask user: "Which pizza?"
  Ask user: "How many?"
  Calculate total price = price * quantity
  SHOW "Your total is £X"
END
```

---

# 2) Exercise 1 — Find the largest of two numbers

### Plain-English steps (algorithm)
1. Ask the user for the first number (A).
2. Ask the user for the second number (B).
3. Compare A and B.
4. If A > B → tell the user A is largest.
5. Else if B > A → tell the user B is largest.
6. Else → say they are equal.

### Pseudocode
```
BEGIN
  INPUT A
  INPUT B
  IF A > B THEN
    DISPLAY "A is largest"
  ELSE IF B > A THEN
    DISPLAY "B is largest"
  ELSE
    DISPLAY "A and B are equal"
  ENDIF
END
```

### Python script
```python
# Exercise 1: largest of two numbers (with equal case)
a = float(input("Enter the first number (A): "))   # read A as a number (accepts decimals)
b = float(input("Enter the second number (B): "))  # read B as a number

# Compare the two numbers and print which is largest or if they are equal
if a > b:
    print("The largest number is", a)
elif b > a:
    print("The largest number is", b)
else:
    print("Both numbers are equal:", a)
```

### Sample run
**Input**:
```
Enter the first number (A): 4.5
Enter the second number (B): 7
```
**Output**:
```
The largest number is 7.0
```

### Line-by-line explanation
- `a = float(input(...))` — `input()` shows the prompt and returns text; `float()` converts that text into a decimal number and stores it in variable `a`.
- `b = float(input(...))` — same for `b`.
- `if a > b:` — checks if `a` is greater than `b`. If True it runs the next indented line.
- `print("The largest number is", a)` — shows the result if `a` is larger.
- `elif b > a:` — only checked if the first `if` was False; tests if `b` is larger.
- `print("The largest number is", b)` — prints `b` when it is larger.
- `else:` — runs only when neither `a > b` nor `b > a` (so they are equal).
- `print("Both numbers are equal:", a)` — prints the equality result.

---

# 3) Exercise 2 — Print name & address (simple output)

### Plain-English steps
1. Print the student's name.
2. Print address lines (each on its own line).

### Pseudocode
```
BEGIN
  DISPLAY name line 1
  DISPLAY name line 2
  DISPLAY name line 3
END
```

### Python script
```python
# Exercise 2: Print name and address lines
print("Alex Johnson")           # line 1: name
print("Flat 3B, 7 Park Lane")   # line 2: street & flat
print("Your Town University")   # line 3: city / institution
```

### Output
```
Alex Johnson
Flat 3B, 7 Park Lane
Your Town University
```

### Line-by-line explanation
Each `print()` prints the text inside quotes and moves to the next line automatically. There's no input here — it simply displays the address.

---

# 4) Exercise 3 — Ask name, age, income and print them

### Plain-English steps
1. Ask the user for their name (text).
2. Ask for their age (whole number).
3. Ask for their income (decimal allowed).
4. Print each piece back to the screen labeled.

### Pseudocode
```
BEGIN
  INPUT name (string)
  INPUT age (convert to integer)
  INPUT income (convert to float)
  DISPLAY name
  DISPLAY age
  DISPLAY income
END
```

### Python script
```python
# Exercise 3: get name, age and income and display them
name = input("Name: ")                      # name stays as text (string)
age = int(input("Age: "))                   # convert input text to integer
income = float(input("Income (e.g., 1234.56): "))  # convert input text to float

# Print the values with labels
print("Name:", name)
print("Age:", age)
print("Income:", income)
```

### Sample run
**Input**:
```
Name: Mia
Age: 14
Income (e.g., 1234.56): 200.50
```
**Output**:
```
Name: Mia
Age: 14
Income: 200.5
```

### Line-by-line explanation
- `name = input("Name: ")` — gets text like "Mia" and stores it as a string.
- `age = int(input("Age: "))` — `input()` returns text like "14", `int()` turns it into the number `14`.
- `income = float(input(...))` — `input()` returns text (e.g., "200.50"), `float()` converts to decimal `200.5`.
- `print("Name:", name)` etc. — labels plus the stored values are printed.

---

# 5) Exercise 4 — Approximate age from year of birth
Two versions provided: (A) fixed CURRENT year and (B) better: use the computer's clock.

### A) Fixed current year (example from lecture)
#### Steps
1. Use a constant `CURRENT = 2020` (example).
2. Ask for year of birth.
3. Subtract year of birth from `CURRENT` to get approximate age.
4. Print result.

#### Pseudocode
```
CURRENT = 2020
INPUT yob
age = CURRENT - yob
DISPLAY age
```

#### Python script (fixed)
```python
# Version A: using a fixed CURRENT year (as in the slides)
CURRENT = 2020
yob = int(input("Enter the year you were born (e.g., 2006): "))
approx_age = CURRENT - yob
print("You are approximately", approx_age, "years old.")
```

#### Explanation
`CURRENT = 2020` — a named constant for clarity. If `yob` is 2006 then `2020 - 2006 = 14`.

### B) Better: use the actual current year (auto-updates)

#### Steps
1. Get the current year from the computer.
2. Ask user for year of birth.
3. Subtract to find age.
4. Print.

#### Pseudocode
```
CURRENT = current system year
INPUT yob
age = CURRENT - yob
DISPLAY age
```

#### Python script (auto)
```python
# Version B: use the computer's current year so the program stays correct
from datetime import datetime            # import the module to get dates
CURRENT = datetime.now().year           # get current year like 2025
yob = int(input("Enter the year you were born (e.g., 2006): "))
approx_age = CURRENT - yob
print("You are approximately", approx_age, "years old.")
```

#### Sample run (if today is 2025)
**Input**:
```
Enter the year you were born (e.g., 2006): 2011
```
**Output**:
```
You are approximately 14 years old.
```

#### Line-by-line explanation
- `from datetime import datetime` — brings a tool that knows the date/time.
- `CURRENT = datetime.now().year` — asks the tool the current year (e.g., 2025) and stores it.
- `yob = int(input(...))` — user enters birth year as a number.
- `approx_age = CURRENT - yob` — simple subtraction gives approximate age. (It is approximate because it doesn't check whether the user has already had their birthday this year.)

---

# 6) Exercise 5 — Format sales (2 decimals) and compute remaining leave %

### Plain-English steps
1. Ask the user for the sales amount (decimal).
2. Display the sales amount rounded to 2 decimal places.
3. Ask total annual leave days and days remaining.
4. Compute `percent_remaining = (remaining / total) * 100`.
5. Show the percentage rounded to one decimal place and followed by `%`.

### Pseudocode
```
INPUT sales (float)
DISPLAY sales formatted to 2 decimals
INPUT total_days (int)
INPUT remaining (int)
percent = (remaining / total_days) * 100
DISPLAY percent formatted to 1 decimal with a percent sign
```

### Python script
```python
# Exercise 5: format sales and compute remaining leave percentage
sales = float(input("Enter sales amount (e.g., 1234.567): "))
# Show sales rounded to 2 decimal places
print("Sales (2 decimals):", format(sales, '.2f'))

# Now calculate leave percentage
total_days = int(input("Enter total annual leave days (e.g., 28): "))
remaining = int(input("Enter days remaining (e.g., 7): "))

# Calculate percentage of leave remaining
percent_remaining = (remaining / total_days) * 100

# Print percentage rounded to 1 decimal and add % sign (as text)
print("Remaining leave:", format(percent_remaining, '.1f') + "%")
```

### Sample run
**Input**:
```
Enter sales amount (e.g., 1234.567): 1234.567
Enter total annual leave days (e.g., 28): 28
Enter days remaining (e.g., 7): 7
```
**Output**:
```
Sales (2 decimals): 1234.57
Remaining leave: 25.0%
```

### Line-by-line explanation
- `sales = float(input(...))` — read sales as decimal.
- `format(sales, '.2f')` — converts `1234.567` to the string `'1234.57'` (rounded to 2 decimals).
- `total_days = int(input(...))` and `remaining = int(input(...))` — read integer days.
- `percent_remaining = (remaining / total_days) * 100` — division gives fraction; multiply by 100 to convert to percent (e.g., `7/28 = 0.25` → `25.0`).
- `format(percent_remaining, '.1f') + "%" ` — formats to 1 decimal (e.g., `'25.0'`) then appends `%` to make `'25.0%'`.

---

# 7) Cheat-sheet (one-page quick reference)
- Print text: `print("Hello")`
- Input: `name = input("Your name: ")`
- Convert: `int("3")` → `3` ; `float("3.5")` → `3.5`
- Variables: `high_score = 9000`
- String quotes: single `' '`, double `" "`, triple `""" """`
- Comment: `# This explains code`
- Math: `+ - * / % **`
- Compare: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Format: `format(value, '.2f')`
- Constant: `PI = 3.14159` (by convention upper case for constants)
