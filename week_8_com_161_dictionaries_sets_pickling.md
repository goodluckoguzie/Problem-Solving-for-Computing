# Week 8 — COM161: Dictionaries, Sets & Pickling (Solved)

---

## summary
This week focuses on **mappings** and **mathematical sets** in Python, plus a short intro to **serialising (pickling)** Python objects. You’ll learn to create and manipulate **dictionaries** (key→value), use common **dictionary methods**, iterate safely with **`in`/`get`/`items`**, build **sets** and perform set operations (∪, ∩, −, ⊕), and save/load Python objects with **`pickle`**. Exercises mirror the lecture “Try it out” prompts—with **worked solutions**.

### Key terms & definitions (glossary)
- **dictionary (dict):** A mapping of **unique keys** to **values**. Written with `{key: value}` pairs.
- **key:** The lookup **identifier** in a dict; must be **immutable & hashable** (e.g., `str`, `int`, `tuple` of immutables). Example: in `{'age': 21}`, `'age'` is the key.
- **value:** The data **stored for a key**. Example: in `{'age': 21}`, `21` is the value.
- **item / entry:** A **key–value pair** treated together. From a dict, `d.items()` yields items like `('age', 21)`.
- **mapping:** A data structure that **associates** keys to values. Python’s built‑in mapping type is `dict`.
- **index:** A **numeric position** used with ordered sequences (lists/tuples/strings), e.g., `names[0]`. ⚠️ **Dictionaries and sets do not use indices** for access; you access dicts by **key** (`d['age']`) and sets by **membership**.
- **membership test:** Using `in` to ask “is this present?”. In dicts, `k in d` checks **keys**; in sets, `x in S` checks **elements**.
- **view objects:** Dynamic views returned by `d.keys()`, `d.values()`, `d.items()`; reflect live changes to the dict.
- **set:** An **unordered** collection of **unique** (hashable) elements; supports maths‑style operations like ∪, ∩, −, ⊕.
- **subset / superset:** `A ⊆ B` (every element of A is in B), `A ⊇ B` (B’s elements are all in A). In Python: `A <= B`, `A >= B`.
- **union / intersection / difference / symmetric difference:** `A|B`, `A&B`, `A-B`, `A^B` respectively.
- **hashable:** An object with a **stable hash and equality** (`__hash__`/`__eq__`) so it can be a dict **key** or set **element**.
- **serialise / pickle:** Convert a Python object to **bytes** for storage (`pickle.dump`); **unpickle** to reconstruct it (`pickle.load`). Only unpickle **trusted** data.

---

## Table of contents
1. Dictionaries at a glance
2. Accessing & updating entries
3. Iteration patterns over dictionaries
4. Dictionary methods you’ll actually use
5. Worked examples (dict)
6. Sets: create, size, membership
7. Core set operations (union, intersection, difference, symmetric difference)
8. Mutating sets & removal semantics
9. Worked examples (sets)
10. Serialising with `pickle` (dump/load)
11. Exercises — with solutions
12. Common pitfalls & tips
13. Cheat‑sheet
14. Mini‑projects

---

# 1) Dictionaries at a glance
- **Dictionary** = mapping from **immutable key** → **value**.
- Curly braces with key:value pairs: `{key1: value1, key2: value2}`.
- Keys must be **hashable** (e.g., `str`, `int`, `tuple` of immutables). Values can be anything.

```python
students = { 'Mark': '111010', 'Sarah': '100010', 'Julie': '202020', 'Bill': '123492' }
student = { 'name': 'Steve', 'age': 21, 'courses': ['Math', 'CompSci'] }
```

---

# 2) Accessing & updating entries
**Index by key** and handle missing keys carefully.
```python
# read
sid = students['Mark']          # may raise KeyError if key missing
sid = students.get('Mark')      # returns None (or default) if missing
sid = students.get('Peter', 'Not found')

# write / update
students['Holly'] = '847321'    # add new pair
students['Sarah'] = '111221'    # update existing value

# delete
del students['Bill']            # KeyError if missing
removed = students.pop('Bill', None)   # safe removal
```

---

# 3) Iteration patterns over dictionaries
```python
# keys (default)
for name in students:
    print(name)

# keys explicitly
for name in students.keys():
    print(name)

# values
for sid in students.values():
    print(sid)

# key and value together (tuple unpacking)
for name, sid in students.items():
    print(name, '--', sid)
```

---

# 4) Dictionary methods you’ll actually use
- `get(key, default)` — safe lookup
- `items()` / `keys()` / `values()` — views for iteration
- `pop(key, default)` — remove by key and **return** value
- `popitem()` — remove & return an arbitrary (Py≥3.7: last) item
- `clear()` — empty the dict
- `update(mapping_or_pairs)` — bulk add/update

```python
register = {}
register.update({'Pete': 23, 'Sandra': 21})
print(register.get('Sandra', 'Person not found'))    # 21
print(register.get('Sandy', 'Person not found'))     # default

for k, v in register.items():
    print(k, v, sep=' -- ')

k, v = register.popitem()   # returns a (key, value) pair
```

---

# 5) Worked examples (dict)
**A) Build a register from input & report**
```python
register = {}
for _ in range(4):
    name = input("Please enter the student's name: ")
    age = int(input("Please enter the student's age: "))
    register[name] = age

print("The register contains:", len(register), "students")
for stud in register:
    print(stud, register[stud], sep='->')
```

**B) Tally occurrences in a list**
```python
def tally(names):
    counts = {}
    for n in names:
        counts[n] = counts.get(n, 0) + 1
    return counts

staff_list = ['Simon','Mark','Mark','Peter','Leo','George','George','Ian','Ian','Pat','Nicola','Ian']
for k, v in tally(staff_list).items():
    print(k + ':', v)
```

**C) Actors to films (dict of lists) + sorting with `key=`**
```python
actors = {
    'Daniel Craig': ['Casino Royale', 'Skyfall', 'Spectre'],
    'Tom Cruise':   ['Mission Impossible', 'Vanilla Sky', 'Top Gun', 'Minority Report'],
    'Rowan Atkinson': ['Mr Bean', 'Johnny English']
}

# iterate pairs
for actor, films in actors.items():
    print(actor, films)

# list length per actor
for actor in actors:
    print(actor, len(actors[actor]))

# order actors by number of films
for actor, films in sorted(actors.items(), key=lambda pair: len(pair[1])):
    print(actor)
```

**D) Anagram checker via character tallies**
```python
def char_tally(s: str) -> dict:
    d = {}
    for ch in s.lower():
        d[ch] = d.get(ch, 0) + 1
    return d

w1 = input('Enter the first word: ')
w2 = input('Enter the second word: ')
print(char_tally(w1) == char_tally(w2))
```

> Extension: for visual comparison, compare `sorted(w1.lower())` and `sorted(w2.lower())`.

---

# 6) Sets — create, size, membership
- **Set** = unordered collection of **unique** items.
- Construct from any iterable with `set(iterable)` or with a literal `{...}`.
- Elements must be **immutable**.

```python
set1 = set(['History','Math','Physics','CompSci','Math'])   # duplicates removed
letters = set('Hello')    # {'H','e','l','o'} — unique characters only
words  = {'Art', 'Design', 'Math'}
print(len(words), 'Math' in words)
```

---

# 7) Core set operations
Let `A` and `B` be sets.

```python
A | B                # union
A.union(B)
A & B                # intersection
A.intersection(B)
A - B                # difference (in A but not in B)
A.difference(B)
A ^ B                # symmetric difference (in A or B, but not both)
A.symmetric_difference(B)

A <= B               # subset test (A ⊆ B)
A.issubset(B)
A >= B               # superset test (A ⊇ B)
A.issuperset(B)
```

---

# 8) Mutating sets & removal semantics
- `add(x)` — add one element; `update(iterable)` — add many
- `remove(x)` — KeyError if `x` not present; `discard(x)` — silent if missing
- `clear()` — empty the set

```python
S = {'g','e','k'}
S.add('s'); S.add('s')      # adding twice keeps one copy
nums = {5,6,7}
nums.update([1,2,3]); nums.update({10,11,12})

nums.discard(2)
try:
    nums.remove(1)
except KeyError:
    print('something went wrong')
```

---

# 9) Worked examples (sets)
**A) Unique words from a file**
```python
import re

def unique_words(path):
    store = set()
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            for w in re.findall(r"[A-Za-z']+", line.lower()):
                store.add(w)
    return store

print(unique_words('somefile.txt'))
```

**B) Quiz‑style snippets**
```python
y = set()
for n in [1,2,3,4,5,6,2,3]:
    y.add(n)
# y == {1,2,3,4,5,6}

x1 = {'foo','bar','baz'}
x2 = {'baz','qux','quux'}
print(x1 ^ x2)   # symmetric difference
print(x1 & x2)   # intersection → {'baz'}
```

---

# 10) Serialising with `pickle`
**Pickling** converts Python objects to bytes so you can write them to a file and later **unpickle** to reconstruct the object.

```python
import pickle

students = {'Chris': 21, 'Paula': 22, 'Lucy': 21, 'Sarah': 19, 'Michael': 20, 'Bruce': 21}

# write (pickle)
with open('student_store.dat', 'wb') as out_f:
    pickle.dump(students, out_f)

# read (unpickle)
with open('student_store.dat', 'rb') as in_f:
    restored = pickle.load(in_f)

for name, age in restored.items():
    print(name, age)
```

> ⚠️ **Safety note:** Only unpickle data from **trusted sources**. Unpickling can execute arbitrary code embedded in the pickle stream.

---

# 11) Exercises — with solutions

## 1) Name→age dictionary lookup
**Task:** Build a `people` dictionary of names→ages. Prompt for a name; report age or "not found".
```python
people = {'Martin': 20, 'Susan': 19, 'Laura': 21, 'Peter': 22}
name = input('Search for name: ').strip()
print(people.get(name, 'Not found'))
```

## 2) Register builder (4 entries) + count + list names
```python
register = {}
for _ in range(4):
    k = input("Name: ")
    v = int(input("Age: "))
    register[k] = v
print('Count:', len(register))
for k in register:
    print(k)
```

## 3) Count words in a list with a dictionary
```python
words = ['tea','tea','milk','tea','coffee','milk']
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)
```

## 4) Anagram checker (functions + print report)
```python
def tally(s):
    d = {}
    for ch in s.lower():
        d[ch] = d.get(ch, 0) + 1
    return d

w1 = input('Word 1: ')
w2 = input('Word 2: ')
d1, d2 = tally(w1), tally(w2)
print('Anagram?', d1 == d2)
print('w1:', d1) ; print('w2:', d2)
```

## 5) Sets — unique words from a text file
```python
path = input('Path to text file: ')
print(sorted(unique_words(path)))
```

## 6) Sets — practice with operations
```python
A = set(range(1,6))
B = set(range(4,9))
print('A∪B =', A|B)
print('A∩B =', A&B)
print('A−B =', A-B)
print('A⊕B =', A^B)
print('A⊆B?', A<=B, 'A⊇B?', A>=B)
```

## 7) Pickle — save & load any object
```python
import pickle
things = {'nums': [1,2,3], 'title': 'Demo', 'flag': True}
with open('things.pkl', 'wb') as f: pickle.dump(things, f)
with open('things.pkl', 'rb') as f: print(pickle.load(f))
```

---

# 12) Common pitfalls & tips
- **`KeyError`**: prefer `dict.get()` or check `if key in d` before indexing.
- **Views vs lists**: `d.items()`/`d.keys()`/`d.values()` return dynamic views; convert with `list(...)` if you need a snapshot.
- **Mutating while iterating**: don’t change dict size during iteration; collect changes, then apply.
- **Set order**: sets are **unordered**; don’t rely on printed order.
- **Hashability**: set elements & dict keys must be immutable; lists can’t be keys.
- **Pickle safety**: never unpickle data from untrusted sources.

---

# 13) Cheat‑sheet
```python
# dict basics
d = {'a':1}
d['b'] = 2; d['a'] = 99
val = d.get('z', 0)
for k,v in d.items(): ...

# set basics
S = {1,2,3}; T = set([3,4,5])
S.add(4); S.update([5,6])
S|T; S&T; S-T; S^T; S<=T; S>=T

# pickle
import pickle
with open('file.dat','wb') as f: pickle.dump(obj, f)
with open('file.dat','rb') as f: obj = pickle.load(f)
```

---

# 14) Mini‑projects
1) **Word stats** — read a `.txt` file; produce top‑10 word frequencies (dict tallies + sort by `value`).
2) **Class register** — menu‑driven CRUD on a name→age dict; save/load with pickle.
3) **Set explorer** — interactive tool to input two sets and visualise operations (∪, ∩, −, ⊕) on screen.

> Copy any snippet into your editor and run it. I can export these as `.py` files or a single `.zip` on request.

