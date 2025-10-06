# Week 3 — COM161: Decisions & Boolean Logic — Solved Exercises

---

## summary
We use **decision structures** to choose different paths: `if`, `if…else`, and `if…elif…else`. We build tests with **relational operators** (`>`, `<`, `==`, `!=`, `>=`, `<=`) and combine them with **logical operators** (`and`, `or`, `not`). We can compare **numbers** and **strings**, and store truth values in **Boolean** variables (`True`/`False`).

---

## Table of contents
1. Decision tools recap
2. Exercise 1 — Pass/Fail from three test scores (if/else)
3. Exercise 2 — Grade calculator A–F (if/elif ladder)
4. Exercise 3 — Simple login (string comparisons)
5. Exercise 4 — Discount eligibility (and/or/not)
6. Exercise 5 — Leap year checker (compound condition)
7. Cheat-sheet

---

# 1) Decision tools recap (fast)
- **if** runs a block only when a condition is `True`.
- **if / else** chooses between two routes.
- **if / elif / else** chooses among many routes (ladder).
- **Relational operators:** `>`, `<`, `>=`, `<=`, `==`, `!=` compare values.
- **Logical operators:** `and` (both), `or` (either), `not` (flip True/False).
- **Strings can be compared**. Equality is common (`name == "Alex"`). Ordering uses character codes.
- **Boolean variables** hold `True`/`False` and are great as flags, e.g., `is_student = True`.

---

# 2) Exercise 1 — Pass/Fail from three test scores (if/else)

### Plain-English steps (algorithm)
1. Ask for three test scores out of 100.
2. Compute the average.
3. If average ≥ 50 → print **Pass**; else → print **Fail**.

### Pseudocode
```
BEGIN
  INPUT s1, s2, s3
  avg = (s1 + s2 + s3) / 3
  IF avg >= 50 THEN
    DISPLAY "Pass"
  ELSE
    DISPLAY "Fail"
  ENDIF
END
```

### Python script
```python
# Exercise 1: Pass/Fail from three test scores
s1 = float(input("Score 1 (0–100): "))
s2 = float(input("Score 2 (0–100): "))
s3 = float(input("Score 3 (0–100): "))

avg = (s1 + s2 + s3) / 3
print("Average:", format(avg, '.1f'))

if avg >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
```

### Sample run
**Input**
```
Score 1 (0–100): 60
Score 2 (0–100): 45
Score 3 (0–100): 55
```
**Output**
```
Average: 53.3
Result: Pass
```

### Line-by-line explanation
- Read three numbers as `float` so decimals are allowed.
- Compute the mean.
- `if avg >= 50:` decides the path; only one of the two prints will execute.

---

# 3) Exercise 2 — Grade calculator A–F (if/elif ladder)

**Rule (example boundaries):**
- `A` ≥ 70
- `B` ≥ 60
- `C` ≥ 50
- `D` ≥ 40
- else `F`

### Pseudocode
```
BEGIN
  INPUT score
  IF score >= 70 THEN grade = 'A'
  ELIF score >= 60 THEN grade = 'B'
  ELIF score >= 50 THEN grade = 'C'
  ELIF score >= 40 THEN grade = 'D'
  ELSE grade = 'F'
  DISPLAY grade
END
```

### Python script
```python
# Exercise 2: Letter grade from a single score
score = float(input("Score (0–100): "))

if score >= 70:
    grade = 'A'
elif score >= 60:
    grade = 'B'
elif score >= 50:
    grade = 'C'
elif score >= 40:
    grade = 'D'
else:
    grade = 'F'

print("Grade:", grade)
```

### Sample run
```
Score (0–100): 66
Grade: B
```

### Line-by-line explanation
- Conditions are checked **top to bottom**. The first `True` block runs and the rest are skipped.

---

# 4) Exercise 3 — Simple login (string comparisons)

### Plain-English steps
1. Store the correct username and password in variables.
2. Ask the user to enter both.
3. If both match → welcome; else → show error.

### Python script
```python
# Exercise 3: Simple login (case-insensitive username, case-sensitive password)
correct_user = "alex"
correct_pass = "Python123"  # demo only — never hard-code real passwords!

user = input("Username: ").strip().lower()
password = input("Password: ")

if (user == correct_user) and (password == correct_pass):
    print("Welcome,", user)
else:
    print("Login failed: check username or password.")
```

### Sample run (success)
```
Username: ALEX
Password: Python123
Welcome, alex
```

### Explanation
- We normalise the username with `.strip().lower()` so `ALEX` equals `alex`.
- Password comparison is case-sensitive.

---

# 5) Exercise 4 — Discount eligibility (and/or/not)

**Rule:** 20% discount if the customer is **under 18 or 65+**, or if they are a **student**. No discount otherwise.

### Pseudocode
```
BEGIN
  INPUT age
  INPUT student (yes/no)
  IF (age < 18 OR age >= 65) OR (student == yes) THEN
     DISPLAY "Discount applies"
  ELSE
     DISPLAY "No discount"
  ENDIF
END
```

### Python script
```python
# Exercise 4: Discount eligibility using logical operators
age = int(input("Age: "))
student = input("Student? (yes/no): ").strip().lower()

eligible = (age < 18) or (age >= 65) or (student == 'yes')

if eligible:
    print("Discount applies: 20% off")
else:
    print("No discount")
```

### Sample run
```
Age: 19
Student? (yes/no): yes
Discount applies: 20% off
```

### Explanation
- We build a **compound** test and store it in a Boolean `eligible` (a flag) for clarity.

---

# 6) Exercise 5 — Leap year checker (compound condition)

**Rule:** A year is a leap year if it is **divisible by 400**, or **divisible by 4 but not by 100**.

### Pseudocode
```
BEGIN
  INPUT year
  IF (year % 400 == 0) OR ((year % 4 == 0) AND (year % 100 != 0)) THEN
     DISPLAY "Leap year"
  ELSE
     DISPLAY "Not a leap year"
  ENDIF
END
```

### Python script
```python
# Exercise 5: Leap year checker
year = int(input("Enter a year: "))

is_leap = (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))

if is_leap:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
```

### Sample run
```
Enter a year: 2000
2000 is a leap year
```

### Explanation
- `%` is the remainder operator. We combine conditions with `and`/`or` and group them with parentheses for readability.

---

# 7) Cheat-sheet (decisions)
- **if**
  ```python
  if condition:
      # do something
  ```
- **if / else**
  ```python
  if condition:
      ...
  else:
      ...
  ```
- **if / elif / else**
  ```python
  if c1:
      ...
  elif c2:
      ...
  else:
      ...
  ```
- **Relational:** `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical:** `and`, `or`, `not`
- **Booleans & flags:** `is_member = True` then `if is_member: ...`
- **String checks:** `name == "Mia"`; `password != "letmein"`.

---

> Mini‑project idea: Write a “Cinema Kiosk” that asks age, student status, and day of week, prints the ticket price, and shows a message if the user qualifies for a family or senior deal.

