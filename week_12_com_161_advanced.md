# Week 12 — COM161: Advanced Python Topics

---

## summary
This week covers advanced Python programming concepts that build upon all previous weeks. You'll explore advanced topics including recursion, lambda functions, list comprehensions, error handling best practices, working with modules and packages, file I/O advanced techniques, and practical applications that integrate multiple concepts. This week consolidates your Python knowledge and prepares you for more complex programming challenges.

### Key terms & definitions (glossary)
- **recursion:** A programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar sub-problems.
- **base case:** The condition in a recursive function that stops the recursion and prevents infinite loops.
- **recursive case:** The part of a recursive function that calls itself with modified parameters.
- **lambda function:** An anonymous, small function defined using the `lambda` keyword. Also called lambda expressions or anonymous functions.
- **list comprehension:** A concise way to create lists using a single line of code with an expression and optional conditions.
- **dictionary comprehension:** Similar to list comprehensions but creates dictionaries.
- **set comprehension:** Similar to list comprehensions but creates sets.
- **generator expression:** Similar to list comprehensions but creates generators that produce values on-demand.
- **higher-order function:** A function that takes another function as an argument or returns a function. Examples: `map()`, `filter()`, `reduce()`.
- **map():** A built-in function that applies a function to every item in an iterable.
- **filter():** A built-in function that filters items in an iterable based on a condition.
- **reduce():** A function from `functools` that applies a function cumulatively to items in an iterable.
- **module:** A file containing Python code (functions, classes, variables) that can be imported and used in other programs.
- **package:** A collection of related modules organized in a directory structure.
- **import statement:** A statement used to bring modules or specific functions/classes into your program.
- **context manager:** A Python construct that manages resources (like files) using the `with` statement, ensuring proper cleanup.
- **exception chaining:** The practice of catching one exception and raising another while preserving the original exception information.
- **decorator:** A function that modifies the behavior of another function or class (advanced topic).

---

## Table of contents
1. Introduction: Advanced Python concepts
2. Recursion
3. Lambda functions
4. List comprehensions and comprehensions
5. Higher-order functions (map, filter, reduce)
6. Advanced error handling
7. Modules and packages
8. Advanced file operations
9. Practical applications and integration
10. Worked examples
11. Exercises — with solutions
12. Common pitfalls & tips
13. Cheat‑sheet
14. Mini‑projects

---

# 1) Introduction: Advanced Python concepts

Throughout this course, you've learned fundamental Python concepts:
- **Weeks 1-2:** Variables, data types, input/output
- **Week 3:** Decision structures and boolean logic
- **Week 4:** Loops and repetition
- **Week 5:** Functions
- **Week 6:** Files and exceptions
- **Week 7:** Lists and tuples
- **Week 8:** Dictionaries, sets, and pickling
- **Week 9:** Classes and objects
- **Week 10:** Encapsulation and inheritance
- **Week 11:** Strings

This week brings together these concepts and introduces advanced techniques that will:
- Make your code more concise and efficient
- Enable you to solve complex problems
- Prepare you for real-world programming challenges
- Demonstrate Python's powerful features

**What makes these topics "advanced"?**
- They require understanding of multiple fundamental concepts
- They involve more abstract thinking
- They provide powerful tools for experienced programmers
- They demonstrate Python's elegance and expressiveness

---

# 2) Recursion

**Recursion** is a technique where a function calls itself to solve a problem by breaking it down into smaller instances of the same problem.

## 2.1) Understanding recursion

**Key components:**
1. **Base case:** The stopping condition that prevents infinite recursion
2. **Recursive case:** The part where the function calls itself with a simpler input

**How recursion works:**
```
factorial(5)
  → 5 * factorial(4)
       → 4 * factorial(3)
            → 3 * factorial(2)
                 → 2 * factorial(1)
                      → 1 (base case)
```

## 2.2) Simple recursion examples

**Example 1: Factorial**

```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Test
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(3))  # Output: 6
```

**Example 2: Countdown**

```python
def countdown(n):
    if n <= 0:  # Base case
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)  # Recursive case

countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Blast off!
```

**Example 3: Sum of numbers**

```python
def sum_numbers(n):
    if n == 0:  # Base case
        return 0
    else:
        return n + sum_numbers(n - 1)  # Recursive case

print(sum_numbers(5))  # Output: 15 (5+4+3+2+1)
```

## 2.3) More complex recursion

**Example 4: Fibonacci sequence**

```python
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 1:  # Base cases
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test
for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")
```

**Example 5: Power function**

```python
def power(base, exponent):
    """Calculate base^exponent using recursion."""
    if exponent == 0:  # Base case
        return 1
    else:
        return base * power(base, exponent - 1)

print(power(2, 5))  # Output: 32
print(power(3, 3))  # Output: 27
```

**Example 6: String reversal**

```python
def reverse_string(s):
    """Reverse a string using recursion."""
    if len(s) <= 1:  # Base case
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

print(reverse_string("Hello"))  # Output: olleH
print(reverse_string("Python"))  # Output: nohtyP
```

## 2.4) Recursion vs iteration

**When to use recursion:**
- Problem naturally divides into similar sub-problems
- Tree or graph traversal
- Mathematical sequences (factorial, Fibonacci)
- Divide-and-conquer algorithms

**When to use iteration (loops):**
- Simple counting or accumulation
- Performance is critical (recursion has overhead)
- Risk of deep recursion (stack overflow)

**Comparison:**

```python
# Iterative factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive factorial
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Both produce the same result
print(factorial_iterative(5))   # 120
print(factorial_recursive(5))   # 120
```

---

# 3) Lambda functions

**Lambda functions** are small, anonymous functions defined using the `lambda` keyword. They can have any number of arguments but only one expression.

## 3.1) Basic syntax

```python
# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y

print(add(3, 5))         # Output: 8
print(add_lambda(3, 5))  # Output: 8
```

**Syntax:** `lambda arguments: expression`

## 3.2) Lambda function examples

**Example 1: Simple operations**

```python
# Square a number
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Check if even
is_even = lambda x: x % 2 == 0
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False

# Concatenate strings
concat = lambda s1, s2: s1 + " " + s2
print(concat("Hello", "World"))  # Output: Hello World
```

**Example 2: Lambda with multiple arguments**

```python
# Calculate area of rectangle
area = lambda length, width: length * width
print(area(5, 3))  # Output: 15

# Find maximum of three numbers
max_three = lambda a, b, c: max(a, max(b, c))
print(max_three(10, 25, 15))  # Output: 25
```

**Example 3: Lambda in sorting**

```python
# Sort list of tuples by second element
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students.sort(key=lambda x: x[1])
print(students)
# Output: [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Sort strings by length
words = ["python", "is", "awesome", "fun"]
words.sort(key=lambda x: len(x))
print(words)  # Output: ['is', 'fun', 'python', 'awesome']
```

## 3.3) When to use lambda functions

**Good use cases:**
- Short, simple operations
- One-time use functions
- As arguments to higher-order functions
- Sorting with custom keys

**When NOT to use lambda:**
- Complex logic (use regular functions)
- Multiple statements needed
- Need for documentation (docstrings)
- Reusable functions

---

# 4) List comprehensions and comprehensions

**List comprehensions** provide a concise way to create lists. They're more readable and often faster than traditional loops.

## 4.1) Basic list comprehensions

**Syntax:** `[expression for item in iterable]`

```python
# Traditional approach
squares = []
for i in range(10):
    squares.append(i ** 2)

# List comprehension
squares = [i ** 2 for i in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**More examples:**

```python
# Create list of even numbers
evens = [i for i in range(20) if i % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Convert strings to uppercase
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# Extract first character
first_chars = [word[0] for word in words]
print(first_chars)  # Output: ['h', 'w', 'p']
```

## 4.2) List comprehensions with conditions

**Syntax:** `[expression for item in iterable if condition]`

```python
# Numbers divisible by 3
div_by_3 = [i for i in range(30) if i % 3 == 0]
print(div_by_3)  # Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

# Filter positive numbers
numbers = [-5, 3, -2, 8, -1, 7]
positives = [n for n in numbers if n > 0]
print(positives)  # Output: [3, 8, 7]

# Extract long words
words = ["hi", "hello", "hey", "goodbye", "welcome"]
long_words = [word for word in words if len(word) > 4]
print(long_words)  # Output: ['hello', 'goodbye', 'welcome']
```

## 4.3) Nested list comprehensions

```python
# Create 2D matrix
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
# Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 4.4) Dictionary comprehensions

**Syntax:** `{key_expression: value_expression for item in iterable}`

```python
# Create dictionary of squares
squares_dict = {i: i ** 2 for i in range(6)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Invert dictionary
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # Output: {1: 'a', 2: 'b', 3: 'c'}

# Filter dictionary
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
high_scores = {name: score for name, score in scores.items() if score >= 90}
print(high_scores)  # Output: {'Bob': 92, 'David': 95}
```

## 4.5) Set comprehensions

**Syntax:** `{expression for item in iterable}`

```python
# Create set of squares
squares_set = {i ** 2 for i in range(10)}
print(squares_set)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Unique first letters
words = ["apple", "banana", "apricot", "cherry", "avocado"]
first_letters = {word[0] for word in words}
print(first_letters)  # Output: {'a', 'b', 'c'}
```

---

# 5) Higher-order functions (map, filter, reduce)

**Higher-order functions** are functions that operate on other functions, either by taking them as arguments or returning them.

## 5.1) map() function

The `map()` function applies a function to every item in an iterable.

**Syntax:** `map(function, iterable)`

```python
# Square all numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Convert to uppercase
words = ["hello", "world", "python"]
upper = list(map(str.upper, words))
print(upper)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# Multiple iterables
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, nums1, nums2))
print(sums)  # Output: [5, 7, 9]
```

## 5.2) filter() function

The `filter()` function filters items based on a condition.

**Syntax:** `filter(function, iterable)`

```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]

# Filter positive numbers
numbers = [-5, 3, -2, 8, -1, 7]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)  # Output: [3, 8, 7]

# Filter long words
words = ["hi", "hello", "hey", "goodbye", "welcome"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)  # Output: ['hello', 'goodbye', 'welcome']
```

## 5.3) reduce() function

The `reduce()` function applies a function cumulatively to items in an iterable.

**Syntax:** `reduce(function, iterable)`

```python
from functools import reduce

# Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15

# Find maximum
numbers = [3, 7, 2, 9, 1, 5]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # Output: 9

# Concatenate strings
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda x, y: x + y, words)
print(sentence)  # Output: Hello World!
```

## 5.4) Combining map, filter, and reduce

```python
from functools import reduce

# Calculate sum of squares of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step by step
evens = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x ** 2, evens)
total = reduce(lambda x, y: x + y, squares)
print(total)  # Output: 220 (4 + 16 + 36 + 64 + 100)

# Chained
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers)))
print(result)  # Output: 220
```

---

# 6) Advanced error handling

Building on Week 6's exception handling, let's explore advanced techniques.

## 6.1) Multiple exception types

```python
def divide_numbers():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except Exception as e:
        print(f"Unexpected error: {e}")

divide_numbers()
```

## 6.2) Exception chaining

```python
def process_data(data):
    try:
        value = int(data)
        if value < 0:
            raise ValueError("Value must be positive")
        return value
    except ValueError as e:
        raise RuntimeError("Failed to process data") from e

try:
    result = process_data("-5")
except RuntimeError as e:
    print(f"Error: {e}")
    print(f"Original cause: {e.__cause__}")
```

## 6.3) Custom exceptions

```python
class InvalidAgeError(Exception):
    """Custom exception for invalid age values."""
    pass

class InvalidGradeError(Exception):
    """Custom exception for invalid grade values."""
    pass

def validate_student_data(age, grade):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Invalid age: {age}")
    if grade < 0 or grade > 100:
        raise InvalidGradeError(f"Invalid grade: {grade}")
    return True

# Usage
try:
    validate_student_data(25, 95)
    print("Data is valid")
except InvalidAgeError as e:
    print(f"Age error: {e}")
except InvalidGradeError as e:
    print(f"Grade error: {e}")
```

## 6.4) Finally clause

```python
def read_file_safely(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    finally:
        if file:
            file.close()
            print("File closed")

content = read_file_safely("data.txt")
```

## 6.5) Context managers (with statement)

```python
# Automatic resource management
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed

# Multiple context managers
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())
```

---

# 7) Modules and packages

## 7.1) Importing modules

```python
# Import entire module
import math
print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793

# Import specific functions
from math import sqrt, pi
print(sqrt(25))  # Output: 5.0
print(pi)        # Output: 3.141592653589793

# Import with alias
import math as m
print(m.sqrt(9))  # Output: 3.0

# Import all (not recommended)
from math import *
print(sqrt(36))  # Output: 6.0
```

## 7.2) Common useful modules

**math module:**
```python
import math

print(math.ceil(4.3))    # Output: 5 (round up)
print(math.floor(4.7))   # Output: 4 (round down)
print(math.pow(2, 3))    # Output: 8.0 (power)
print(math.factorial(5)) # Output: 120
print(math.gcd(48, 18))  # Output: 6 (greatest common divisor)
```

**random module:**
```python
import random

print(random.randint(1, 10))        # Random integer between 1 and 10
print(random.random())              # Random float between 0 and 1
print(random.choice([1, 2, 3, 4]))  # Random choice from list

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Shuffled list
```

**datetime module:**
```python
from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print(now)

# Create specific date
birthday = date(1990, 5, 15)
print(birthday)

# Date arithmetic
tomorrow = date.today() + timedelta(days=1)
print(tomorrow)
```

**os module:**
```python
import os

# Current working directory
print(os.getcwd())

# List files in directory
print(os.listdir('.'))

# Check if file exists
print(os.path.exists('data.txt'))

# Get file size
if os.path.exists('data.txt'):
    print(os.path.getsize('data.txt'))
```

## 7.3) Creating your own modules

**mymodule.py:**
```python
"""A simple module with utility functions."""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

PI = 3.14159
```

**Using your module:**
```python
import mymodule

print(mymodule.greet("Alice"))
print(mymodule.add(5, 3))
print(mymodule.PI)
```

---

# 8) Advanced file operations

## 8.1) Reading files efficiently

```python
# Read entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line (memory efficient)
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read specific number of lines
with open("data.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
    print(first_line, second_line)

# Read all lines into list
with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

## 8.2) Writing files

```python
# Write (overwrite existing content)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python is awesome!\n")

# Append (add to existing content)
with open("output.txt", "a") as file:
    file.write("New line appended\n")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

## 8.3) Working with CSV files

```python
import csv

# Write CSV
data = [
    ["Name", "Age", "Grade"],
    ["Alice", 20, 85],
    ["Bob", 22, 92],
    ["Charlie", 21, 78]
]

with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Read CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Read CSV as dictionary
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']}: {row['Grade']}")
```

## 8.4) Working with JSON

```python
import json

# Write JSON
data = {
    "students": [
        {"name": "Alice", "age": 20, "grade": 85},
        {"name": "Bob", "age": 22, "grade": 92}
    ]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Read JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
    for student in loaded_data["students"]:
        print(f"{student['name']}: {student['grade']}")
```

---

# 9) Practical applications and integration

## 9.1) Student grade analyzer

```python
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
    def letter_grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

# Create students
students = [
    Student("Alice", [85, 90, 88, 92]),
    Student("Bob", [78, 82, 75, 80]),
    Student("Charlie", [92, 95, 93, 98])
]

# Analyze using comprehensions and lambda
averages = list(map(lambda s: (s.name, s.average()), students))
high_achievers = list(filter(lambda s: s.average() >= 90, students))

print("All averages:")
for name, avg in averages:
    print(f"{name}: {avg:.2f}")

print("\nHigh achievers (>= 90):")
for student in high_achievers:
    print(f"{student.name}: {student.average():.2f}")
```

## 9.2) Text file analyzer

```python
import string
from collections import Counter

def analyze_text_file(filename):
    """Analyze a text file and return statistics."""
    try:
        with open(filename, 'r') as file:
            text = file.read()
        
        # Remove punctuation
        text_clean = text.translate(str.maketrans('', '', string.punctuation))
        
        # Split into words
        words = text_clean.lower().split()
        
        # Statistics
        stats = {
            'total_chars': len(text),
            'total_words': len(words),
            'unique_words': len(set(words)),
            'avg_word_length': sum(len(word) for word in words) / len(words) if words else 0,
            'most_common': Counter(words).most_common(5)
        }
        
        return stats
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None

# Usage
stats = analyze_text_file("sample.txt")
if stats:
    print(f"Total characters: {stats['total_chars']}")
    print(f"Total words: {stats['total_words']}")
    print(f"Unique words: {stats['unique_words']}")
    print(f"Average word length: {stats['avg_word_length']:.2f}")
    print("\nMost common words:")
    for word, count in stats['most_common']:
        print(f"  {word}: {count}")
```

## 9.3) Data processing pipeline

```python
def process_data_pipeline(data):
    """Process data through multiple stages."""
    # Stage 1: Filter valid numbers
    valid_data = list(filter(lambda x: isinstance(x, (int, float)), data))
    
    # Stage 2: Remove negatives
    positive_data = list(filter(lambda x: x > 0, valid_data))
    
    # Stage 3: Square the numbers
    squared_data = list(map(lambda x: x ** 2, positive_data))
    
    # Stage 4: Sort
    sorted_data = sorted(squared_data)
    
    return sorted_data

# Test
mixed_data = [5, -3, "hello", 2, 8, -1, 4, None, 7]
result = process_data_pipeline(mixed_data)
print(result)  # Output: [4, 16, 25, 49, 64]
```

---

# 10) Worked examples

## Example 1: Recursive directory tree

```python
import os

def print_directory_tree(path, indent=0):
    """Print directory structure recursively."""
    try:
        items = os.listdir(path)
        for item in items:
            print("  " * indent + "├── " + item)
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print_directory_tree(item_path, indent + 1)
    except PermissionError:
        print("  " * indent + "├── [Permission Denied]")

# Usage
print_directory_tree(".")
```

## Example 2: Data validation system

```python
class ValidationError(Exception):
    pass

def validate_email(email):
    """Validate email format."""
    if "@" not in email or "." not in email:
        raise ValidationError("Invalid email format")
    return True

def validate_age(age):
    """Validate age range."""
    if not isinstance(age, int) or age < 0 or age > 120:
        raise ValidationError("Invalid age")
    return True

def validate_user_data(data):
    """Validate complete user data."""
    validators = {
        'email': validate_email,
        'age': validate_age
    }
    
    errors = []
    for field, validator in validators.items():
        try:
            validator(data[field])
        except ValidationError as e:
            errors.append(f"{field}: {e}")
        except KeyError:
            errors.append(f"{field}: Missing field")
    
    return errors

# Test
user_data = {'email': 'user@example.com', 'age': 25}
errors = validate_user_data(user_data)
if errors:
    print("Validation errors:")
    for error in errors:
        print(f"  - {error}")
else:
    print("All data valid!")
```

## Example 3: Functional programming example

```python
from functools import reduce

# Calculate statistics using functional programming
def calculate_statistics(numbers):
    """Calculate various statistics using functional programming."""
    # Filter valid numbers
    valid = list(filter(lambda x: isinstance(x, (int, float)), numbers))
    
    if not valid:
        return None
    
    # Calculate statistics
    total = reduce(lambda x, y: x + y, valid)
    count = len(valid)
    average = total / count
    
    # Find min and max
    minimum = reduce(lambda x, y: x if x < y else y, valid)
    maximum = reduce(lambda x, y: x if x > y else y, valid)
    
    # Count evens and odds
    evens = len(list(filter(lambda x: x % 2 == 0, valid)))
    odds = count - evens
    
    return {
        'total': total,
        'count': count,
        'average': average,
        'min': minimum,
        'max': maximum,
        'evens': evens,
        'odds': odds
    }

# Test
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stats = calculate_statistics(data)
print("Statistics:")
for key, value in stats.items():
    print(f"  {key}: {value}")
```

---

# 11) Exercises — with solutions

## Exercise 1: Recursive sum of digits
**Task:** Write a recursive function that calculates the sum of digits in a number.

**Solution:**
```python
def sum_of_digits(n):
    """Calculate sum of digits recursively."""
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

# Test
print(sum_of_digits(12345))  # Output: 15 (1+2+3+4+5)
print(sum_of_digits(999))    # Output: 27 (9+9+9)
```

## Exercise 2: List comprehension exercises
**Task:** Use list comprehensions to solve the following:
1. Create a list of squares of even numbers from 0 to 20
2. Extract words longer than 5 characters from a list
3. Create a list of tuples (number, square, cube) for numbers 1-10

**Solution:**
```python
# 1. Squares of even numbers
squares = [i ** 2 for i in range(21) if i % 2 == 0]
print(squares)  # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

# 2. Long words
words = ["hi", "hello", "goodbye", "hey", "welcome", "python"]
long_words = [word for word in words if len(word) > 5]
print(long_words)  # ['goodbye', 'welcome']

# 3. Number, square, cube tuples
tuples = [(i, i**2, i**3) for i in range(1, 11)]
print(tuples)
# [(1, 1, 1), (2, 4, 8), (3, 9, 27), ...]
```

## Exercise 3: Map, filter, reduce
**Task:** Given a list of numbers, use map, filter, and reduce to:
1. Filter numbers greater than 5
2. Square them
3. Calculate the sum

**Solution:**
```python
from functools import reduce

numbers = [1, 3, 5, 7, 9, 11, 13, 15]

# Solution
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2,
        filter(lambda x: x > 5, numbers)))

print(result)  # Output: 620 (49 + 81 + 121 + 169 + 225)

# Step by step for clarity
filtered = list(filter(lambda x: x > 5, numbers))
print(f"Filtered: {filtered}")  # [7, 9, 11, 13, 15]

squared = list(map(lambda x: x ** 2, filtered))
print(f"Squared: {squared}")  # [49, 81, 121, 169, 225]

total = reduce(lambda x, y: x + y, squared)
print(f"Sum: {total}")  # 620
```

## Exercise 4: Custom exception handling
**Task:** Create a custom exception for invalid temperature values and a function that converts Celsius to Fahrenheit with validation.

**Solution:**
```python
class InvalidTemperatureError(Exception):
    """Exception for invalid temperature values."""
    pass

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit with validation."""
    # Absolute zero is -273.15°C
    if celsius < -273.15:
        raise InvalidTemperatureError(
            f"Temperature {celsius}°C is below absolute zero")
    
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test
try:
    print(celsius_to_fahrenheit(0))      # 32.0
    print(celsius_to_fahrenheit(100))    # 212.0
    print(celsius_to_fahrenheit(-300))   # Raises exception
except InvalidTemperatureError as e:
    print(f"Error: {e}")
```

## Exercise 5: File processing with error handling
**Task:** Write a function that reads a file containing numbers (one per line), filters out invalid entries, and returns the average.

**Solution:**
```python
def calculate_average_from_file(filename):
    """Read numbers from file and calculate average."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Parse numbers, skip invalid lines
        numbers = []
        for line in lines:
            try:
                num = float(line.strip())
                numbers.append(num)
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
        
        if not numbers:
            print("No valid numbers found")
            return None
        
        average = sum(numbers) / len(numbers)
        return average
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Test (create a test file first)
with open("numbers.txt", "w") as f:
    f.write("10\n20\ninvalid\n30\n40\n")

avg = calculate_average_from_file("numbers.txt")
if avg is not None:
    print(f"Average: {avg}")
```

## Exercise 6: Recursive palindrome checker
**Task:** Write a recursive function to check if a string is a palindrome.

**Solution:**
```python
def is_palindrome_recursive(s):
    """Check if string is palindrome using recursion."""
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Base cases
    if len(s) <= 1:
        return True
    
    # Check first and last characters
    if s[0] != s[-1]:
        return False
    
    # Recursive case: check middle portion
    return is_palindrome_recursive(s[1:-1])

# Test
print(is_palindrome_recursive("racecar"))      # True
print(is_palindrome_recursive("hello"))        # False
print(is_palindrome_recursive("A man a plan a canal Panama"))  # True
```

---

# 12) Common pitfalls & tips

**Recursion pitfalls:**
- **Missing base case:** Always include a base case to prevent infinite recursion
- **Stack overflow:** Deep recursion can cause stack overflow; consider iteration for deep calls
- **Inefficiency:** Some recursive solutions (like naive Fibonacci) are very inefficient

**Lambda pitfalls:**
- **Overuse:** Don't use lambdas for complex logic
- **Readability:** Sometimes a regular function is clearer
- **No docstrings:** Lambdas can't have documentation

**Comprehension pitfalls:**
- **Too complex:** Don't make comprehensions too complicated; use regular loops if needed
- **Nested comprehensions:** Can be hard to read; consider breaking into multiple steps
- **Memory:** List comprehensions create entire lists in memory; consider generators for large datasets

**Error handling pitfalls:**
- **Catching too broad:** Don't use bare `except:` clauses
- **Silent failures:** Always log or handle exceptions appropriately
- **Resource leaks:** Use `with` statements for file operations

**Tips:**
- Use recursion for naturally recursive problems (trees, graphs)
- Prefer list comprehensions for simple transformations
- Use `map()` and `filter()` when working with functions
- Always use context managers (`with`) for file operations
- Create custom exceptions for domain-specific errors
- Document your functions with docstrings
- Test edge cases thoroughly

---

# 13) Cheat‑sheet

```python
# Recursion
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

# Lambda functions
square = lambda x: x ** 2
add = lambda x, y: x + y

# List comprehensions
squares = [x ** 2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Dictionary comprehension
squares_dict = {x: x ** 2 for x in range(10)}

# Set comprehension
unique_squares = {x ** 2 for x in range(-5, 6)}

# map, filter, reduce
from functools import reduce
mapped = list(map(lambda x: x ** 2, [1, 2, 3]))
filtered = list(filter(lambda x: x > 5, [1, 5, 10]))
reduced = reduce(lambda x, y: x + y, [1, 2, 3, 4])

# Exception handling
try:
    risky_operation()
except ValueError as e:
    handle_error(e)
except Exception as e:
    handle_generic_error(e)
finally:
    cleanup()

# Context managers
with open("file.txt", "r") as file:
    content = file.read()

# Modules
import math
from datetime import datetime
import random as rnd

# Custom exceptions
class CustomError(Exception):
    pass

# File operations
with open("file.txt", "r") as f:
    lines = f.readlines()

with open("output.txt", "w") as f:
    f.write("Hello\n")
```

---

# 14) Mini‑projects

1. **Recursive File Explorer** — Create a program that recursively explores a directory structure, counts files by type, and calculates total size.

2. **Data Analysis Tool** — Build a tool that reads a CSV file, uses comprehensions to filter and transform data, and generates statistics using map/filter/reduce.

3. **Text Processing Pipeline** — Create a pipeline that reads multiple text files, processes them (remove punctuation, count words, find most common), and outputs a summary report.

4. **Grade Management System** — Build a complete system using classes, file I/O, exception handling, and comprehensions to manage student grades, calculate statistics, and generate reports.

5. **Configuration File Parser** — Create a program that reads configuration files (JSON or custom format), validates settings using custom exceptions, and provides a clean API for accessing configuration values.

6. **Recursive Math Solver** — Implement recursive solutions for mathematical problems: factorial, Fibonacci, GCD, power, combinations, permutations.

7. **Functional Data Transformer** — Build a data transformation tool that uses only functional programming concepts (map, filter, reduce, lambda) to process and analyze datasets.

> Copy any snippet into your editor and run it. I can export these as `.py` files or a single `.zip` on request.

---

# To think about

- When is recursion better than iteration, and vice versa?
- How do list comprehensions compare to map/filter in terms of readability?
- What are the trade-offs between using lambda functions vs regular functions?
- Why is the `with` statement preferred for file operations?
- How can you optimize recursive functions (memoization, tail recursion)?

**Next steps:** In future courses, you'll learn about:
- **Decorators:** Functions that modify other functions
- **Generators:** Functions that yield values on-demand
- **Async programming:** Handling concurrent operations
- **Type hints:** Adding type information to Python code
- **Testing:** Writing unit tests and test-driven development
- **Virtual environments:** Managing project dependencies
- **Web frameworks:** Building web applications with Flask/Django
- **Data science:** NumPy, Pandas, Matplotlib

---

**Congratulations on completing COM161!** You now have a solid foundation in Python programming and problem-solving. Keep practicing, building projects, and exploring new concepts. Happy coding! 🐍

---

