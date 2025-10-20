# Week 5 — COM161: Functions (Solved)

---

## summary
Functions let us **modularise** programs (divide‑and‑conquer): each task lives in a small, named block you can **call** (and reuse) from anywhere. This week you’ll learn how to **define**, **call**, and **organise** functions; pass **arguments** (positional & keyword); return **values**; use **modules**; and apply the **random** library. The end includes a full **Lab 5** set with step‑by‑step solutions (coin tosses, temperature converters, Boolean predicates, circle module/menu, turtle projects, dice, etc.).

---

## Table of contents
1. Why functions? Benefits & vocabulary
2. Defining & naming functions
3. Calling functions (positional vs. keyword args)
4. Scope: locals & (discouraged) globals; global **constants**
5. Value‑returning functions & the standard library
6. The `random` module (games/simulations)
7. Organising code into **modules** and importing
8. Common patterns & tips
9. Cheat‑sheet
10. Lab 5 tasks — solved
   - 10.1 Modify `multiple_args` → multiply & average
   - 10.2 Enhanced `coin_toss`: counts + “pure run of 10”
   - 10.3 Temperature tables (°C↔°F)
   - 10.4 Boolean predicates: `is_even`, `is_negative`, `is_too_big`
   - 10.5 Using a circle **module** + menu‑driven app
   - 10.6 Turtle: random squares & user‑specified squares
   - 10.7 Turtle: random walk
   - 10.8 Dice roller
11. Extra practice

---

# 1) Why functions?
**Functions** package a small task behind a name. Benefits:
- **Clarity:** small chunks with descriptive names
- **Reuse:** one definition, many calls
- **Testing:** unit‑test small parts
- **Collaboration:** interfaces between teammates

Vocabulary: *define*, *call*, *parameter* (name in def), *argument* (value at call‑site), *return value*, *module*.

---

# 2) Defining & naming functions
```python
def function_name(param1, param2):
    """Short docstring describing what and why."""
    # work
    return result
```
**Naming rules (Python):** start with letter/underscore; no spaces; avoid keywords; case‑sensitive; prefer verb‑y, meaningful names (e.g., `calculate_pay`, `print_address`).

---

# 3) Calling functions
- **Positional arguments** (most common): order matters.
- **Keyword arguments** (explicit): `draw_square(x=100, y=50, size=40, color="blue")`.
- Mix allowed; positional must come **before** keyword.

---

# 4) Scope & constants
- Names created **inside** a function are **local** to that function.
- Avoid **global variables** (hard to reason about). Prefer **global constants** (UPPER_CASE) defined once at the top.

---

# 5) Value‑returning functions & the standard library
A value‑returning function finishes with `return expression`. Examples you’ve used: `len(s)`, `range(n)`, `input()` (returns a string). You can use `import` to access more functionality.

---

# 6) The `random` module
```python
import random
random.randint(1, 6)      # inclusive both ends
random.randrange(5)       # 0..4
random.randrange(5, 10)   # 5..9
random.random()           # float in [0.0, 1.0)
random.uniform(1.0, 3.0)  # float in [1.0, 3.0]
```
Use these for games, dice, walks, sampling, etc.

---

# 7) Modules & imports
Put related functions into a **module** file (e.g., `circle.py`) and `import circle`. Call with **dot notation**: `circle.area(r)`. Keep modules in the same folder (or on `PYTHONPATH`).

---

# 8) Common patterns & tips
- Put program structure in a `main()` and call it from:
  ```python
  if __name__ == "__main__":
      main()
  ```
- Short, single‑purpose functions; compose them.
- Validate inputs near the boundary (before the heavy work).
- Return values from computation functions; print in a thin UI layer.

---

# 9) Cheat‑sheet
**Define:** `def name(params): ... return value`

**Call:** `name(args)` or `name(key=value)`

**Random:** `randint(a,b)`, `randrange([start], stop[, step])`, `random()`, `uniform(a,b)`

**Module:**
```python
import module
module.func()
from module import func  # then call func()
```

---

# 10) Lab 5 — solved tasks

## 10.1 Modify `multiple_args` → multiply & average
```python
def main():
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print(f"Product: {multiply(a, b)}")
    x = float(input("Average x: "))
    y = float(input("Average y: "))
    z = float(input("Average z: "))
    show_average(x, y, z)


def multiply(x, y):
    return x * y


def show_average(x, y, z):
    avg = (x + y + z) / 3
    print(f"Average of {x}, {y}, {z} is {avg}")


if __name__ == "__main__":
    main()
```

---

## 10.2 Enhanced `coin_toss`: counts + “pure run of 10”
```python
import random


def coin(tosses):
    """Simulate N tosses; return (heads_count, tails_count)."""
    heads = 0
    tails = 0
    for _ in range(tosses):
        if random.randint(1, 2) == 1:
            heads += 1
            print("Heads")
        else:
            tails += 1
            print("Tails")
    return heads, tails


def runs_until_pure(run_size=10):
    """Repeat runs of `run_size` tosses until a run is all Heads or all Tails.
    Return (runs_required, side_str, last_run)."""
    runs = 0
    while True:
        runs += 1
        run = ["H" if random.randint(1, 2) == 1 else "T" for _ in range(run_size)]
        if all(s == "H" for s in run):
            return runs, "Heads", run
        if all(s == "T" for s in run):
            return runs, "Tails", run


def main():
    tosses = int(input("How many tosses? "))
    h, t = coin(tosses)
    print(f"Heads: {h}, Tails: {t}")

    runs, side, last = runs_until_pure(10)
    print(f"Pure run achieved after {runs} run(s): {side}\nLast run: {''.join(last)}")


if __name__ == "__main__":
    main()
```

---

## 10.3 Temperature tables (°C↔°F)
```python
def fahrenheit_from_c(c):
    return c * 1.8 + 32


def centigrade_from_f(f):
    return (f - 32) * 5 / 9


def table_c_to_f():
    print("C  ->  F")
    for c in range(0, 101, 10):
        print(f"{c:3d} -> {fahrenheit_from_c(c):6.1f}")


def table_f_to_c():
    print("F  ->  C")
    for f in range(0, 101, 10):
        print(f"{f:3d} -> {centigrade_from_f(f):6.1f}")


def main():
    table_c_to_f()
    print()
    table_f_to_c()


if __name__ == "__main__":
    main()
```

---

## 10.4 Boolean predicates
**Corrected** `is_even` and two new predicates + quick tests.
```python
def is_even(number):
    return (number % 2) == 0


def is_negative(number):
    return number < 0


def is_too_big(number):
    return number > 100


# quick tests
for n in [-5, 0, 2, 101]:
    print(n, "even=", is_even(n), "negative=", is_negative(n), "too_big=", is_too_big(n))
```

---

## 10.5 Using a circle module + menu‑driven app
**circle.py** (as a module):
```python
PI = 3.1415


def area(radius):
    return PI * radius ** 2


def circumference(radius):
    return 2 * PI * radius
```

**menu app:**
```python
import circle  # ensure circle.py is in the same folder


def main():
    while True:
        print("\nMenu: (a) Area  (b) Circumference  (c) End")
        choice = input("Choice: ").strip().lower()
        if choice == "a":
            r = float(input("Radius: "))
            print(f"Area = {circle.area(r):.4f}")
        elif choice == "b":
            r = float(input("Radius: "))
            print(f"Circumference = {circle.circumference(r):.4f}")
        elif choice == "c":
            print("Goodbye!")
            break
        else:
            print("Please choose a, b, or c.")


if __name__ == "__main__":
    main()
```

> Tip: for more precision, you could use `import math` and `math.pi` inside `circle.py`.

---

## 10.6 Turtle: random squares & user‑specified set
```python
import random
import turtle as t


def square(x, y, size, color):
    t.penup(); t.goto(x, y); t.pendown()
    t.fillcolor(color); t.begin_fill()
    for _ in range(4):
        t.forward(size); t.left(90)
    t.end_fill()


def random_squares(n=3):
    t.hideturtle(); t.speed(0)
    colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    for _ in range(n):
        x = random.randint(-250, 200)
        y = random.randint(-200, 200)
        size = random.randint(30, 150)
        color = random.choice(colors)
        square(x, y, size, color)


def user_squares():
    t.hideturtle(); t.speed(0)
    n = int(input("How many squares? "))
    for i in range(1, n + 1):
        print(f"Square {i}")
        x = int(input("x: "))
        y = int(input("y: "))
        size = int(input("size: "))
        color = input("color: ")
        square(x, y, size, color)


if __name__ == "__main__":
    # random_squares()
    user_squares()
    t.done()
```

---

## 10.7 Turtle: random walk
```python
import random
import turtle as t


def random_walk(steps):
    t.hideturtle(); t.speed(0)
    for _ in range(steps):
        t.setheading(random.randint(0, 359))
        t.forward(random.randint(10, 20))


def main():
    steps = int(input("How many steps? "))
    random_walk(steps)
    t.done()


if __name__ == "__main__":
    main()
```

---

## 10.8 Dice roller
```python
import random


def roll_dice(n, sides=6):
    rolls = [random.randint(1, sides) for _ in range(n)]
    return sum(rolls), rolls


def main():
    n = int(input("How many dice? "))
    total, rolls = roll_dice(n)
    print("Rolls:", rolls)
    print("Total:", total)


if __name__ == "__main__":
    main()
```

---

# 11) Extra practice
- Turn the menu app into a **looping toolkit** with: circle, rectangle area/perimeter, triangle area (Heron’s formula).
- Write a `read_float(prom