# Week 4 — COM161: Repetition & Loops

---

## summary
We use **repetition structures** (loops) to repeat work without duplicating code. You’ll master **condition‑controlled** loops (Python `while`) and **count‑controlled** loops (`for` with lists or `range`). We’ll also cover **augmented assignment** operators, **sentinel** values, **input validation** loops, and a fun **turtle** section for geometric patterns.

---

## Table of contents
1. Repetition structures at a glance
2. `while`: condition‑controlled loops
3. `for`: count‑controlled loops
   - 3.1 `for` with lists/iterables
   - 3.2 `for` with `range` (1, 2, or 3 args)
4. Augmented assignment operators (+=, -=, …)
5. Sentinel‑controlled loops
6. Input validation loops
7. Exercises (step‑by‑step, with solutions)
8. Common pitfalls & tips
9. Cheat‑sheet
10. Teaching tips & mini‑project ideas
11. Extra practice (with solutions)

---

# 1) Repetition structures at a glance
- **Why loops?** Avoid duplicating code and make updates in one place.
- **Two families:**
  - **Condition‑controlled** (repeat while a condition is `True`): Python `while`.
  - **Count‑controlled** (repeat a set number of times): Python `for` (often with `range`).

**Flow mindset:**
1. Initialise variables (counters/accumulators/flags).
2. Loop while the condition holds (or for N iterations).
3. Update state each pass (increment counters, add to totals, etc.).

---

# 2) The `while` loop — condition‑controlled
**Syntax**
```python
while condition:
    # repeated statements
    # make sure something changes so the condition can become False
```
**Key ideas**
- Evaluate the condition **before** each iteration.
- If the condition is initially `False`, the body may never run.
- Always ensure **progress** (update the variable(s) used in the condition).

**Example A — simple counter**
```python
count = 5
while count > 0:
    print("T‑minus", count)
    count -= 1
print("Liftoff!")
```

**Example B — accumulate until target**
```python
goal = 100
saved = 0
while saved < goal:
    deposit = float(input("Deposit amount (0 to stop): "))
    if deposit == 0:
        break
    saved += deposit
print(f"Total saved: £{saved:.2f}")
```

---

# 3) The `for` loop — count‑controlled
`for` iterates **over items** in a sequence (list, string, range, etc.).

## 3.1 `for` with lists/iterables
```python
for colour in ["red", "green", "blue"]:
    print(colour)

for ch in "CS101":
    print(ch)
```

## 3.2 `for` with `range`
`range(stop)` → 0..stop‑1  
`range(start, stop)` → start..stop‑1  
`range(start, stop, step)` (step can be negative)

```python
for i in range(5):         # 0,1,2,3,4
    print(i)

for n in range(3, 7):     # 3,4,5,6
    print(n)

for k in range(10, 0, -2):  # 10,8,6,4,2
    print(k)
```
**Off‑by‑one tip:** `stop` is **exclusive**. To include `N`, use `range(..., N+1)`.

---

# 4) Augmented assignment operators
Instead of writing `x = x + 2`, use `x += 2`. Common forms:

| Augmented | Equivalent   | Meaning                   |
|-----------|--------------|---------------------------|
| `x += a`  | `x = x + a`  | add and assign            |
| `x -= a`  | `x = x - a`  | subtract and assign       |
| `x *= a`  | `x = x * a`  | multiply and assign       |
| `x /= a`  | `x = x / a`  | divide and assign (float) |
| `x %= a`  | `x = x % a`  | modulo and assign         |

---

# 5) Sentinel‑controlled loops
A **sentinel** is a special value that signals **end of input**. Pick a value that cannot be confused with real data (e.g., `-1` for counts that are normally non‑negative).

**Example — running total until sentinel**
```python
print("Enter marks one per line, -1 to finish")
count = 0
total = 0
mark = float(input("mark: "))

while mark != -1:
    total += mark
    count += 1
    mark = float(input("mark: "))

if count == 0:
    print("No marks entered")
else:
    print("Average:", total / count)
```

---

# 6) Input validation loops
**GIGO**: Garbage In → Garbage Out. Use a loop to **reject bad input** and re‑prompt until valid.

**Pattern**
```python
age = int(input("Age (0..130): "))
while age < 0 or age > 130:
    print("Out of range, try again.")
    age = int(input("Age (0..130): "))
print("Thanks, age accepted.")
```

---

# 7) Exercises — with solutions

## Exercise 1 — Countdown (while)
**Goal:** Print `5 4 3 2 1 GO!`
```python
n = 5
while n > 0:
    print(n, end=" ")
    n -= 1
print("GO!")
```

## Exercise 2 — Sum 1..N (for + range)
```python
N = int(input("N: "))
acc = 0
for i in range(1, N + 1):
    acc += i
print("Sum:", acc)
```

## Exercise 3 — Factorial N! (for)
```python
n = int(input("n: "))
fact = 1
for i in range(2, n + 1):
    fact *= i
print(f"{n}! = {fact}")
```

## Exercise 4 — Times table for a number (for)
```python
num = int(input("Table for: "))
for m in range(1, 13):
    print(f"{num} × {m} = {num*m}")
```

## Exercise 5 — Guessing game (while with attempts)
```python
import random
secret = random.randint(1, 20)
tries = 5

while tries > 0:
    guess = int(input("Guess 1..20: "))
    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
    tries -= 1

if tries == 0:
    print("Out of tries. The number was", secret)
```

## Exercise 6 — Average until sentinel (while)
```python
print("Enter positive numbers, -1 to finish")
count = 0
total = 0.0
x = float(input("x: "))

while x != -1:
    if x >= 0:
        total += x
        count += 1
    else:
        print("Ignoring negative value (use -1 only to end)")
    x = float(input("x: "))

print("Average:" if count else "No data", (total / count) if count else "")
```

## Exercise 7 — Input validation (mark 0..100)
```python
mark = float(input("Mark (0..100): "))
while not (0 <= mark <= 100):
    print("Invalid, try again")
    mark = float(input("Mark (0..100): "))
print("Accepted:", mark)
```

## Exercise 8 — Min & Max until sentinel
```python
print("Enter integers, 9999 to stop")
first = True
x = int(input("x: "))

while x != 9999:
    if first:
        mn = mx = x
        first = False
    else:
        if x < mn: mn = x
        if x > mx: mx = x
    x = int(input("x: "))

print("No data" if first else f"Min={mn}, Max={mx}")
```

## Exercise 9 — Pattern printing (nested loops)
```python
rows = 4
cols = 6
for r in range(rows):
    line = ""
    for c in range(cols):
        line += "*"
    print(line)
```

## Exercise 10 — Turtle squares & polygons (loops make it easy)
```python
import turtle as t

# square
def square(side):
    for _ in range(4):
        t.forward(side)
        t.right(90)

# regular n‑gon
def polygon(n, side):
    angle = 360 / n
    for _ in range(n):
        t.forward(side)
        t.right(angle)

square(100)
polygon(6, 80)

t.done()
```

---

# 8) Common pitfalls & tips
- **Forgetting to update** the loop variable → infinite loop.
- **Off‑by‑one errors** with `range` (stop is exclusive!).
- Mixing **`input()` strings** with numbers → convert with `int()`/`float()`.
- Choose **safe sentinels** (e.g., `-1` for counts that should be ≥ 0).
- Initialising **accumulators**: sums to `0`, products to `1`, `min/max` with a flag or first value.
- Prefer **clear names**: `total`, `count`, `index`, `done`.

---

# 9) Cheat‑sheet
**while**
```python
while condition:
    # body
    # update state
```

**for + list/iterable**
```python
for item in iterable:
    ...
```

**for + range**
```python
for i in range(stop):
    ...
for i in range(start, stop):
    ...
for i in range(start, stop, step):
    ...  # step may be negative
```

**Augmented assignment**: `+=`, `-=`, `*=`, `/=`, `%=`

**Loop patterns**
- **Counter**: `i = 0; while i < N: ...; i += 1`
- **Accumulator**: `total = 0; for x in data: total += x`
- **Search**: loop and break when found
- **Input validation**: loop until valid
- **Sentinel read**: read → while check → process → read

---

# 10) Teaching tips & mini‑project ideas
- **Trace tables** for counters/accumulators (columns: input, loop index, running total).
- **Flowcharts**: while/for; highlight condition checks and updates.
- **Boundary tests**: N=0, N=1, last iteration, negative inputs.

**Mini‑projects**
1) **Cash Till** — enter item prices until sentinel; output subtotal, tax, total.
2) **Step Tracker** — read daily steps for a month (for + range); report totals & best day.
3) **Menu‑driven App** — show options 1‑4 and loop until user chooses Exit.
4) **Pattern Lab** — generate triangles/boxes with nested loops & user sizes.

---

# 11) Extra practice (with solutions)

### A) Squares table (for + range)
```python
for n in range(1, 11):
    print(f"{n:2d} → {n*n:3d}")
```

### B) Even sum (while)
```python
limit = int(input("Upper limit: "))
num = 0
s = 0
while num <= limit:
    s += num
    num += 2
print("Sum of evens:", s)
```

### C) Multiplication grid (nested for)
```python
size = 5
for r in range(1, size + 1):
    row = []
    for c in range(1, size + 1):
        row.append(str(r * c).rjust(3))
    print(" ".join(row))
```

### D) Robust input (validation wrapper)
```python
def read_int(prompt, lo=None, hi=None):
    while True:
        try:
            x = int(input(prompt))
            if (lo is not None and x < lo) or (hi is not None and x > hi):
                print("Out of range.")
                continue
            return x
        except ValueError:
            print("Not an integer.")

age = read_int("Age 0..130: ", 0, 130)
print("OK:", age)
```

> Feel free to copy any code into your editor and run it. If you want, I can package these as separate `.py` files for you.

