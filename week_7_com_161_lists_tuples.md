# Week 7 — COM161: Lists & Tuples

---

## summary
This week is all about **sequences** in Python—especially **lists** (mutable) and **tuples** (immutable). You’ll create, traverse, slice, search, sort, copy, and process lists (including **2‑D lists**). We’ll also use **list methods**, the **`in`** operator, the **repetition** (`*`) and **concatenation** (`+`) operators, and finish with a quick intro to **tuples**, **lambdas**, and **list comprehensions**. Exercises and solutions match the lecture/tutorial tasks.

---

## Table of contents
1. Sequences at a glance
2. Lists: create, index, slice
3. Traversal: `for` (items) vs `for` (indices)
4. Operators: `+`, `*`, `in`, `not in`, `+=`
5. List methods & useful built‑ins
6. Copying lists (and common gotchas)
7. Processing lists (totals/averages)
8. 2‑D lists (nested lists) & nested loops
9. List comprehensions & lambda `key=`
10. Tuples: quick overview
11. Exercises — with solutions
12. Common pitfalls & tips
13. Cheat‑sheet
14. Mini‑projects & the advanced exercise (pie chart)

---

# 1) Sequences at a glance
- A **sequence** stores items **in order** and supports operations like indexing, slicing, membership tests, and iteration.
- Python’s common sequences: **list**, **tuple**, **str**.
- Core difference we focus on: **list is mutable**; **tuple is immutable**.

---

# 2) Lists — create, index, slice
**Create**
```python
even_nums = [2, 4, 6, 8, 10]
mixed = [1, "two", 3.0, True]
numbers = list(range(5))   # [0,1,2,3,4]
```

**Index** (0‑based; negatives from the end)
```python
numbers = [1, 2, 3, 4, 5]
print(numbers[0])   # 1
print(numbers[-2])  # 4
```

**Slice** `list[start:end:step]` (end exclusive)
```python
days = ['Mon','Tues','Wed','Thur','Fri','Sat','Sun']
print(days[2:3])   # ['Wed']
print(days[:3])    # first 3
print(days[::2])   # every other
```

---

# 3) Traversal patterns
**By item** (read‑only / simple processing):
```python
for course in ["History","Math","Physics","CompSci"]:
    print(course)
```
**By index** (when you need to **write** into the list):
```python
numbers = [1, 2, 3, 4]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2   # update
```

---

# 4) Operators on lists
```python
# concatenation
new_list = [1,2,3,4] + [3,4,5]
# repetition
repeated = [1,2,3] * 3
# membership
print('History' in ["History","Math"])    # True
# augmented concatenation
nums = [1,2,3]; nums += [4,4,4]
```

---

# 5) List methods & useful built‑ins
```python
courses = ['History','Math','Physics','CompSci']

courses.append('Art')              # add at end
courses.insert(1, 'German')        # add at index
courses.extend(['French','Spanish'])

print(courses.index('Art'))        # find first index of item
# print(courses.index('Missing'))  # ValueError if not found

courses.remove('French')           # remove first occurrence
last = courses.pop()               # remove last and return it

courses.reverse()                  # in-place reverse
courses.sort()                     # in-place ascending sort
nums = [1,5,3,7,2]
nums.sort(reverse=True)            # descending in-place
asc_copy = sorted(nums)            # new sorted list (ascending)

print(min(nums), max(nums), sum(nums))

del courses[0]                     # delete by index
```

---

# 6) Copying lists (and why `=` is not a copy)
```python
t1 = [1, 2]
t2 = t1            # NOT a copy; both names point to same list

# Good ways to copy (shallow copy):
copy1 = t1[:]              # slicing
copy2 = list(t1)           # constructor
copy3 = t1.copy()          # method

# For nested lists, use deepcopy if you need independent inner lists:
import copy
deep = copy.deepcopy([[1,2],[3,4]])
```
**Gotcha:** `t2 = t1.append(3)` → `t1` becomes `[1,2,3]` but `t2` is **`None`** because `append` modifies in place and returns nothing.

---

# 7) Processing lists (totals/averages)
Use accumulators.
```python
values = [10, 20, 30]
# total
total = 0
for v in values:
    total += v
# average
avg = total / len(values)
```

---

# 8) 2‑D lists (nested lists)
Think rows × columns; process with **nested loops**.
```python
a = [[1,2,3], [4,5,6], [7,8,9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

# per-row sums
for row in a:
    s = 0
    for elem in row:
        s += elem
    print("row sum:", s)
```

---

# 9) List comprehensions & lambda keys
**List comprehension**
```python
squares_of_even = [x*x for x in range(10) if x % 2 == 0]
```
**`key=` with `min`, `max`, `sorted`** (e.g., on nested lists)
```python
actor_grade_list = [
    ['B001','James','Bond', 1, 45.0],
    ['B002','Daniel','Craig', 2, 30.0],
    ['B007','Dr','Who', 3, 70.9],
]
lowest = min(actor_grade_list, key=lambda row: row[4])
```

---

# 10) Tuples — quick overview
- **Tuple** = immutable sequence: `(item1, item2, ...)`.
- Supports indexing, slicing, `len`, `min`, `max`, `in`, `+`, `*`.
- No mutating methods (`append`, `remove`, `insert`, `reverse`, `sort`).
- Fast, hashable (when elements are hashable), good for **fixed** data.
- Convert with `tuple(list_obj)` and `list(tuple_obj)`.

---

# 11) Exercises — with solutions

## Exercise 1 — Product ID search (`in` operator)
```python
def main():
    prod_nums = ['V475','F987','Q143','R688']
    target = input('Enter product code: ').strip().upper()
    if target in prod_nums:
        print('Product found!')
    else:
        print('Not found.')

if __name__ == '__main__':
    main()
```

## Exercise 2 — Gross pay per employee + average
```python
NUM_EMPLOYEES = 6

def main():
    hours = [0.0] * NUM_EMPLOYEES
    for i in range(NUM_EMPLOYEES):
        hours[i] = float(input(f'Hours for employee {i+1}: '))

    rate = float(input('Hourly pay rate: '))

    total_pay = 0.0
    for i in range(NUM_EMPLOYEES):
        gross = hours[i] * rate
        total_pay += gross
        print(f'Gross pay for employee {i+1}: £{gross:,.2f}')

    avg_pay = total_pay / NUM_EMPLOYEES
    print(f'Average gross pay: £{avg_pay:,.2f}')

if __name__ == '__main__':
    main()
```

## Exercise 3 — Actor grades file: summary, average, minimum, search by surname
**Data file format** (extend to: `id,first,surname,year,mark`), with optional header lines beginning `#`.

```python
# actor_grades.txt (example lines)
# id,first,surname,year,mark
B001,James,Bond,1,45
B002,Daniel,Craig,2,30
B007,Dr,Who,3,70.9
B008,Jonny,English,2,60.2
B009,Ethan,Hunt,1,20
```

**Program**
```python
def read_file(path):
    data = []
    with open(path, 'r', encoding='utf-8') as f:
        for row in f:
            if row.startswith('#') or not row.strip():
                continue
            # strip newline, split by comma, and tidy fields
            parts = [p.strip() for p in row.rstrip('\n').split(',')]
            parts[3] = int(parts[3])          # year
            parts[4] = float(parts[4])        # mark
            data.append(parts)
    return data


def print_summary(records):
    total = 0.0
    for r in records:
        print(f"{r[0]} -> {r[1]} {r[2]} -> {r[4]}")
        total += r[4]
    print(f"\nCombined Scores: {total:.2f}")
    print(f"Average Score: {total/len(records):.2f}")


def minimum_record(records):
    return min(records, key=lambda row: row[4])


def search_by_surname(records, surname):
    surname = surname.strip().lower()
    return [r for r in records if r[2].lower() == surname]


def main():
    records = read_file('actor_grades.txt')
    print_summary(records)
    print('Lowest:', minimum_record(records))
    # search
    s = input('Surname to search: ')
    matches = search_by_surname(records, s)
    if matches:
        for r in matches:
            print('Match:', r)
    else:
        print('No matches')

if __name__ == '__main__':
    main()
```

## Exercise 4 — Interrogating a list (quick demo)
```python
courses = ['History','Math','Physics','CompSci']
print(len(courses))        # 4
print(courses[0], courses[-1])
print(courses[0:2])        # slice
print('History' in courses)
```

## Exercise 5 — 2‑D list printing & per‑row totals
```python
a = [[1,2,3,4],[5,6],[7,8,9]]
for row in a:
    s = 0
    for x in row:
        print(x, end=' ')
        s += x
    print('| sum =', s)
```

---

# 12) Common pitfalls & tips
- **Mutability traps:** `b = a` doesn’t copy; use `a[:]`, `list(a)`, or `a.copy()`.
- **In‑place vs new object:** `list.sort()` changes the list and returns `None`, while `sorted(list)` returns a **new** list.
- **IndexErrors** from out‑of‑range indices; validate lengths.
- **Empty lists:** loops over `[]` do nothing; watch your averages (don’t divide by 0).
- **Slicing end is exclusive** → `list[:len(list)//2]` is common.
- **Heterogeneous lists** sort lexicographically only when comparable; better to use `key=`.

---

# 13) Cheat‑sheet
```python
# build
lst = [1,2,3]; lst2 = list(range(5))
# access
x = lst[0]; y = lst[-1]; sub = lst[1:4:2]
# ops
both = lst + lst2; thrice = lst * 3; found = (2 in lst)
# mutate
lst.append(4); lst.extend([5,6]); lst.insert(1, 99)
lst.remove(99); last = lst.pop(); del lst[0]
# sort
lst.sort(); asc_copy = sorted(lst, key=lambda v: v)
# copy
copy1 = lst[:]; copy2 = list(lst); copy3 = lst.copy()
# 2-D
grid = [[0]*3 for _ in range(3)]  # safe rows
# tuple
point = (10, 20); t = tuple(lst); lst_back = list(point)
```

---

# 14) Mini‑projects & advanced exercise
**Mini‑projects**
1) **Gradebook 2‑D** — each row: `[id, name, mark1, mark2, mark3]`; compute totals, averages, min/max with `key=`.
2) **Shopping list manager** — add/insert/remove/sort/search with a text menu.
3) **Tic‑Tac‑Toe board** — represent a 3×3 board as a 2‑D list; validate moves.

**Advanced exercise (with matplotlib pie chart)**
Create a text file with your last month’s expenses (one per line):
```
rent, 650
transport, 90
food, 210
clothing, 60
socializing, 85
misc, 40
```
Plot a pie chart of your spending:
```python
import matplotlib.pyplot as plt

def read_expenses(path):
    labels, values = [], []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip() or line.startswith('#'):
                continue
            name, amount = [p.strip() for p in line.split(',')]
            labels.append(name)
            values.append(float(amount))
    return labels, values

labels, values = read_expenses('expenses.txt')
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('Monthly Spending')
plt.axis('equal')
plt.show()
```

> Copy any snippet into your editor and run it. I can export these as `.py` files or a single `.zip` on request.

