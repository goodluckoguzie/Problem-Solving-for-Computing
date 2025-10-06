# Week 3 — COM161: Decisions & Boolean Logic

---

## summary
We use **decision structures** to choose different paths: `if`, `if…else`, and `if…elif…else`. We build tests with **relational operators** (`>`, `<`, `==`, `!=`, `>=`, `<=`) and combine them with **logical operators** (`and`, `or`, `not`). We can compare **numbers** and **strings**, and store truth values in **Boolean** variables (`True`/`False`). We also care about **truth tables**, **operator precedence**, **short‑circuiting**, and **common pitfalls**.

---

## Table of contents
1. Decision tools recap
2. Exercise 1 — Pass/Fail from three test scores (if/else)
3. Exercise 2 — Grade calculator A–F (if/elif ladder)
4. Exercise 3 — Simple login (string comparisons)
5. Exercise 4 — Discount eligibility (and/or/not)
6. Exercise 5 — Leap year checker (compound condition)
7. Truth tables (and / or / not) + De Morgan’s law
8. Precedence, grouping & short‑circuit rules
9. Common pitfalls & tips
10. Cheat‑sheet
11. Teaching tips & mini‑project ideas
12. Extra practice with full solutions

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

---

# 3) Exercise 2 — Grade calculator A–F (if/elif ladder)

**Rule (example boundaries):**
- `A` ≥ 70
- `B` ≥ 60
- `C` ≥ 50
- `D` ≥ 40
- else `F`

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

---

# 4) Exercise 3 — Simple login (string comparisons)

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

---

# 5) Exercise 4 — Discount eligibility (and/or/not)

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

---

# 6) Exercise 5 — Leap year checker (compound condition)

```python
# Exercise 5: Leap year checker
year = int(input("Enter a year: "))

is_leap = (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))

if is_leap:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
```

---

# 7) Truth tables (and / or / not) + De Morgan’s law

| A | B | A and B | A or B |
|---|---|---------|--------|
| T | T |    T    |   T    |
| T | F |    F    |   T    |
| F | T |    F    |   T    |
| F | F |    F    |   F    |

`not A` flips True/False.  
**De Morgan’s law:** `not (A and B)` ⇔ `(not A) or (not B)`; `not (A or B)` ⇔ `(not A) and (not B)`.

**Python demo** (optional): generate the table and print it nicely.
```python
vals = [True, False]
print("A\tB\tA and B\tA or B\tnot A")
for A in vals:
    for B in vals:
        print(A, B, A and B, A or B, (not A), sep='\t')
```

---

# 8) Precedence, grouping & short‑circuit rules
- Boolean precedence (highest → lowest): **`not`**, then **`and`**, then **`or`**.
- Use **parentheses** to make intent obvious, especially when mixing with comparisons: `if (temp < 0) or (temp > 100): ...`.
- **Short‑circuiting:**
  - `A and B` stops early if `A` is False.
  - `A or B` stops early if `A` is True.

---

# 9) Common pitfalls & tips
- `=` **assigns**, `==` **compares**.
- Always **convert input** before comparing numbers: `age = int(input(...))`.
- **Case‑folding** for usernames: `user.lower()`; keep passwords case‑sensitive.
- **String ordering** uses character codes—be careful comparing upper/lowercase directly.
- Prefer **flags** for complex tests: `eligible = (...)` then `if eligible:`.
- Test **boundary values** (e.g., `59.9`, `60.0`, `60.1`).

---

# 10) Cheat‑sheet (decisions)
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

# 11) Teaching tips & mini‑project ideas
- **Trace tables** for `if/elif/else` — write columns for inputs, each condition, and the chosen branch.
- **Draw flowcharts** for Exercises 2 and 5 to reinforce decision diamonds.
- **Boundary testing** worksheet for grade cutoffs.

**Mini‑project options:**
1) **Cinema Kiosk** — ask age, student status, day of week; output ticket price & deal message.  
2) **Login + Password Rules** — re‑prompt until valid; lock out after 3 tries.  
3) **Safety Monitor** — read temperature and time; warn if out of safe range.

---

# 12) Extra practice with full solutions

## A) Triangle classifier (with validity check)
```python
# Extra A: Triangle type
print("Enter three side lengths:")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

valid = (a + b > c) and (a + c > b) and (b + c > a)
if not valid:
    print("Not a valid triangle")
elif (a == b) and (b == c):
    print("Equilateral")
elif (a == b) or (a == c) or (b == c):
    print("Isosceles")
else:
    print("Scalene")
```

## B) Password strength (simple rules)
```python
# Extra B: Password strength (length >= 8, has digit, has letter)
pw = input("Password: ")
has_digit = any(ch.isdigit() for ch in pw)
has_alpha = any(ch.isalpha() for ch in pw)
if (len(pw) >= 8) and has_digit and has_alpha:
    print("Strong enough")
else:
    print("Weak: use 8+ chars with letters and digits")
```

## C) Cinema kiosk (combined rules)
```python
# Extra C: Cinema kiosk with age bands, student, weekday/weekend
age = int(input("Age: "))
student = input("Student? (y/n): ").strip().lower() == 'y'
day = input("Day (mon..sun): ").strip().lower()

is_weekend = day in {"sat", "sun", "saturday", "sunday"}
base = 12.00 if is_weekend else 10.00

if age < 12:
    price = base * 0.5
elif age >= 65:
    price = base * 0.7
elif student:
    price = base * 0.8
else:
    price = base

print(f"Ticket £{price:.2f}")
```

> Feel free to copy any of the code blocks into your editor and run them one by one. The ZIP I’ve provided also contains each exercise as its own `.py` file for easy testing.
