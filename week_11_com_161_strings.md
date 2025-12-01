# Week 11 — COM161: Strings in Python

---

## summary
This week focuses on **strings** — one of Python's most fundamental data types. You'll learn about string creation (hardcoded, user input, file reading), string operations and methods, string manipulation, string formatting, and practical applications including reading strings from files and basic text processing. This builds on your knowledge of file handling from Week 6 and prepares you for more advanced string processing tasks.

### Key terms & definitions (glossary)
- **string:** A sequence of characters (letters, numbers, symbols) enclosed in quotes. In Python, strings are immutable sequences of Unicode characters.
- **string literal:** A string value written directly in code, such as `"Hello World"` or `'Python'`.
- **immutable:** A property of strings meaning they cannot be changed after creation. Any operation that appears to modify a string actually creates a new string.
- **string concatenation:** Combining two or more strings together using the `+` operator.
- **string indexing:** Accessing individual characters in a string using their position (index). Indexing starts at 0 in Python.
- **string slicing:** Extracting a portion (substring) of a string using the syntax `string[start:end]`.
- **escape sequence:** Special characters that begin with a backslash (`\`) used to represent characters that are difficult to type directly (e.g., `\n` for newline, `\t` for tab).
- **string method:** A function that belongs to the string class and operates on string objects. Examples: `upper()`, `lower()`, `strip()`, `split()`.
- **string formatting:** The process of inserting values into strings. Methods include f-strings (f"..."), `.format()`, and `%` formatting.
- **substring:** A portion of a string extracted from a larger string.
- **whitespace:** Characters that represent spaces in text (spaces, tabs, newlines).

---

## Table of contents
1. Introduction: What are strings?
2. Creating strings
3. String operations
4. String indexing and slicing
5. String methods
6. String formatting
7. Escape sequences
8. Reading strings from different sources
9. Common string operations
10. String manipulation examples
11. Exercises — with solutions
12. Common pitfalls & tips
13. Cheat‑sheet
14. Mini‑projects

---

# 1) Introduction: What are strings?

A **string** is a sequence of characters. In Python, strings are used to represent text data. Almost everything you work with that contains text is a string:
- Names, addresses, descriptions
- File contents
- User input
- Messages and output

**Why strings are important:**
- User interfaces: All input/output involves strings
- Data processing: Text files, web scraping, data parsing
- Communication: Messages, emails, logs
- File handling: Reading and writing text files

**String characteristics:**
- **Immutable:** Once created, strings cannot be changed (you create new strings instead)
- **Ordered:** Characters have a specific position (index)
- **Indexable:** You can access individual characters by position
- **Slicable:** You can extract portions of strings

---

# 2) Creating strings

There are three main ways to create strings in Python:

## 2.1) Hardcoded strings (string literals)

Strings written directly in your code:

```python
# Single quotes
name = 'John'

# Double quotes
message = "Hello World"

# Triple quotes (for multi-line strings)
paragraph = """This is a
multi-line string
that spans several lines"""

# All are valid:
str1 = 'Single quotes'
str2 = "Double quotes"
str3 = '''Triple single quotes'''
str4 = """Triple double quotes"""
```

## 2.2) Reading from user input

Using the `input()` function:

```python
name = input("Enter your name: ")
print("Hello,", name)
```

## 2.3) Reading from files

Using file operations:

```python
file = open("StringFile.txt", "r")
line = file.readline()
file.close()
print("String read from file:", line)
```

## 2.4) Complete example

```python
def main():
    # Hardcoded string
    hardCoded = "This is an example of a hardcoded String"
    
    # String from user input
    userInput = input("Read in a String: ")
    
    # String from file
    stringFile = open("StringFile.txt", "r")
    line = stringFile.readline()
    stringFile.close()
    
    print("Hardcoded variable:", hardCoded)
    print("String read in from the keyboard:", userInput)
    print("String read in from a file:", line)

main()
```

**Sample output:**
```
Read in a String: Hello from keyboard
Hardcoded variable: This is an example of a hardcoded String
String read in from the keyboard: Hello from keyboard
String read in from a file: There was a hole here, it's gone now
```

---

# 3) String operations

## 3.1) Concatenation (combining strings)

Use the `+` operator to join strings:

```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

greeting = "Hello, " + first_name
print(greeting)  # Output: Hello, John
```

## 3.2) Repetition (multiplying strings)

Use the `*` operator to repeat strings:

```python
line = "-" * 40
print(line)  # Output: ----------------------------------------

exclamation = "Ha" * 3
print(exclamation)  # Output: HaHaHa
```

## 3.3) Length

Use `len()` to get the number of characters:

```python
text = "Python"
print(len(text))  # Output: 6

name = "John Doe"
print(f"'{name}' has {len(name)} characters")  # Output: 'John Doe' has 8 characters
```

## 3.4) Membership testing

Use `in` and `not in` to check if a substring exists:

```python
text = "Python Programming"
print("Python" in text)      # Output: True
print("Java" in text)        # Output: False
print("gram" not in text)    # Output: False
```

---

# 4) String indexing and slicing

## 4.1) Indexing (accessing single characters)

Strings are indexed starting from 0:

```python
text = "Hello"
print(text[0])   # Output: H
print(text[1])   # Output: e
print(text[4])   # Output: o
print(text[-1])  # Output: o (last character)
print(text[-2])  # Output: l (second from last)
```

**Index positions:**
```
 H  e  l  l  o
 0  1  2  3  4
-5 -4 -3 -2 -1
```

## 4.2) Slicing (extracting substrings)

Extract portions using `[start:end]`:

```python
text = "Python Programming"

# Basic slicing
print(text[0:6])      # Output: Python
print(text[7:18])     # Output: Programming
print(text[:6])       # Output: Python (from start to index 6)
print(text[7:])       # Output: Programming (from index 7 to end)
print(text[:])        # Output: Python Programming (entire string)

# With step
print(text[0:6:2])    # Output: Pto (every 2nd character)
print(text[::-1])     # Output: gnimmargorP nohtyP (reversed)
```

**Slicing syntax:** `string[start:end:step]`
- `start`: Starting index (inclusive)
- `end`: Ending index (exclusive)
- `step`: How many characters to skip

---

# 5) String methods

String methods are functions that operate on string objects. Here are some commonly used ones:

## 5.1) Case conversion

```python
text = "Hello World"

print(text.upper())       # Output: HELLO WORLD
print(text.lower())       # Output: hello world
print(text.title())       # Output: Hello World
print(text.capitalize())  # Output: Hello world
print(text.swapcase())    # Output: hELLO wORLD
```

## 5.2) Searching and checking

```python
text = "Python Programming"

print(text.find("Prog"))      # Output: 7 (index where found)
print(text.find("Java"))      # Output: -1 (not found)
print(text.count("m"))        # Output: 2 (count occurrences)
print(text.startswith("Py"))  # Output: True
print(text.endswith("ing"))   # Output: True
```

## 5.3) Whitespace handling

```python
text = "  Hello World  "

print(text.strip())      # Output: Hello World (removes both sides)
print(text.lstrip())     # Output: Hello World   (removes left)
print(text.rstrip())     # Output:   Hello World (removes right)
```

## 5.4) Splitting and joining

```python
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']

words = "Hello World Python".split()
print(words)  # Output: ['Hello', 'World', 'Python']

# Joining
fruits = ['apple', 'banana', 'orange']
result = ", ".join(fruits)
print(result)  # Output: apple, banana, orange
```

## 5.5) Replacement

```python
text = "Hello World"
new_text = text.replace("World", "Python")
print(new_text)  # Output: Hello Python

text = "spam spam spam"
print(text.replace("spam", "eggs"))  # Output: eggs eggs eggs
print(text.replace("spam", "eggs", 2))  # Output: eggs eggs spam (replace first 2)
```

## 5.6) Checking content

```python
text1 = "12345"
text2 = "Hello123"
text3 = "   "
text4 = "Hello"

print(text1.isdigit())    # Output: True (all digits)
print(text2.isdigit())    # Output: False
print(text2.isalnum())    # Output: True (alphanumeric)
print(text4.isalpha())    # Output: True (all letters)
print(text3.isspace())    # Output: True (all whitespace)
```

---

# 6) String formatting

String formatting allows you to insert values into strings. Python provides several methods:

## 6.1) F-strings (recommended - Python 3.6+)

```python
name = "John"
age = 25
score = 95.5

message = f"My name is {name} and I am {age} years old"
print(message)  # Output: My name is John and I am 25 years old

# With expressions
print(f"Next year I will be {age + 1}")  # Output: Next year I will be 26

# Formatting numbers
print(f"Score: {score:.2f}")  # Output: Score: 95.50
print(f"Percentage: {score:.1f}%")  # Output: Percentage: 95.5%
```

## 6.2) `.format()` method

```python
name = "John"
age = 25

message = "My name is {} and I am {} years old".format(name, age)
print(message)

# With named parameters
message = "My name is {name} and I am {age} years old".format(name="John", age=25)
print(message)

# With indices
message = "I am {1} and my name is {0}".format(name, age)
print(message)  # Output: I am 25 and my name is John
```

## 6.3) Old-style `%` formatting

```python
name = "John"
age = 25

message = "My name is %s and I am %d years old" % (name, age)
print(message)

# Format codes:
# %s - string
# %d - integer
# %f - float
# %.2f - float with 2 decimal places
```

---

# 7) Escape sequences

Escape sequences allow you to include special characters in strings:

```python
# Newline
print("Line 1\nLine 2")
# Output:
# Line 1
# Line 2

# Tab
print("Column1\tColumn2\tColumn3")
# Output: Column1    Column2    Column3

# Quote marks
print("He said, \"Hello\"")  # Output: He said, "Hello"
print('It\'s a nice day')    # Output: It's a nice day

# Backslash
print("C:\\Users\\Documents")  # Output: C:\Users\Documents

# Common escape sequences:
# \n - newline
# \t - tab
# \" - double quote
# \' - single quote
# \\ - backslash
# \r - carriage return
```

---

# 8) Reading strings from different sources

## 8.1) Reading from a file (single line)

```python
file = open("StringFile.txt", "r")
line = file.readline()  # Reads one line
file.close()
print("Line from file:", line)
```

## 8.2) Reading from a file (all lines)

```python
file = open("data.txt", "r")
content = file.read()  # Reads entire file as one string
file.close()
print("File content:", content)
```

## 8.3) Reading from a file (line by line)

```python
file = open("data.txt", "r")
for line in file:
    print(line.strip())  # strip() removes newline character
file.close()
```

## 8.4) Reading from a file (list of lines)

```python
with open("data.txt", "r") as file:
    lines = file.readlines()  # Returns list of lines

for line in lines:
    print(line.strip())
```

---

# 9) Common string operations

## 9.1) Removing punctuation

```python
import string

text = "Hello, World! How are you?"
# Remove punctuation
clean_text = text.translate(str.maketrans("", "", string.punctuation))
print(clean_text)  # Output: Hello World How are you
```

## 9.2) Splitting into words

```python
text = "Python is a great programming language"
words = text.split()
print(words)  # Output: ['Python', 'is', 'a', 'great', 'programming', 'language']
print(f"Number of words: {len(words)}")
```

## 9.3) Counting words in text

```python
def count_words(text):
    # Remove punctuation and split into words
    import string
    clean_text = text.translate(str.maketrans("", "", string.punctuation))
    words = clean_text.split()
    return len(words)

text = "Python is a great programming language. It's easy to learn!"
word_count = count_words(text)
print(f"The text has {word_count} words.")  # Output: The text has 10 words.
```

## 9.4) Finding most common words

```python
import collections

text = "python is great python is fun python is powerful"
words = text.lower().split()

# Count word occurrences
word_count = collections.Counter(words)
most_common = word_count.most_common(3)

print("Most common words:")
for word, count in most_common:
    print(f"{word}: {count}")
```

---

# 10) String manipulation examples

## Example 1: Basic string operations

```python
def main():
    # Hardcoded string
    hardCoded = "This is an example of a hardcoded String"
    
    # User input
    userInput = input("Read in a String: ")
    
    # File input
    stringFile = open("StringFile.txt", "r")
    line = stringFile.readline()
    stringFile.close()
    
    print("Hardcoded variable:", hardCoded)
    print("String read in from the keyboard:", userInput)
    print("String read in from a file:", line)

main()
```

## Example 2: Text processing and analysis

```python
import string
import collections

def totalWords(filename):
    """Count total words in a file."""
    file = open(filename, "r")
    text = file.read()
    file.close()
    
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Split into words
    words = text.split()
    
    # Count words
    word_count = len(words)
    
    print(f"The text file has {word_count} words.")
    return word_count

def commonWords(filename, num_words=5):
    """Find and display most common words."""
    with open(filename, 'r') as file:
        words = file.read().lower().split()
    
    # Count word occurrences
    word_count = collections.Counter(words)
    most_common_words = word_count.most_common(num_words)
    
    print(f"\n{num_words} most common words:")
    for word, count in most_common_words:
        print(f"{word}: {count}")

# Usage
totalWords("text_file.txt")
commonWords("text_file.txt", 5)
```

## Example 3: String validation

```python
def validate_email(email):
    """Basic email validation."""
    if "@" not in email:
        return False
    
    parts = email.split("@")
    if len(parts) != 2:
        return False
    
    username, domain = parts
    if len(username) == 0 or len(domain) == 0:
        return False
    
    if "." not in domain:
        return False
    
    return True

# Test
emails = ["user@example.com", "invalid", "user@domain", "@domain.com"]
for email in emails:
    result = validate_email(email)
    print(f"{email}: {'Valid' if result else 'Invalid'}")
```

---

# 11) Exercises — with solutions

## Exercise 1: Reverse a string
**Task:** Write a program that takes a string from the user and prints it in reverse.

**Solution:**
```python
text = input("Enter a string: ")
reversed_text = text[::-1]
print(f"Reversed: {reversed_text}")
```

## Exercise 2: Count vowels and consonants
**Task:** Count the number of vowels and consonants in a string.

**Solution:**
```python
text = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
```

## Exercise 3: Palindrome checker
**Task:** Check if a string is a palindrome (reads the same forwards and backwards).

**Solution:**
```python
text = input("Enter a string: ").lower().replace(" ", "")
reversed_text = text[::-1]

if text == reversed_text:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
```

## Exercise 4: Word frequency counter
**Task:** Read a file and count how many times each word appears.

**Solution:**
```python
import string
import collections

filename = input("Enter filename: ")
file = open(filename, "r")
text = file.read()
file.close()

# Remove punctuation and convert to lowercase
text = text.translate(str.maketrans("", "", string.punctuation))
words = text.lower().split()

# Count word frequencies
word_count = collections.Counter(words)

print("Word frequencies:")
for word, count in word_count.most_common():
    print(f"{word}: {count}")
```

## Exercise 5: Text formatter
**Task:** Create a function that formats a string: removes extra spaces, capitalizes first letter, adds period if missing.

**Solution:**
```python
def format_text(text):
    # Remove extra whitespace
    text = " ".join(text.split())
    
    # Capitalize first letter
    text = text.capitalize()
    
    # Add period if missing
    if text and text[-1] not in ".!?":
        text += "."
    
    return text

# Test
test_cases = [
    "  hello   world  ",
    "this is a test",
    "already formatted.",
    "ALL CAPS"
]

for test in test_cases:
    print(f"'{test}' -> '{format_text(test)}'")
```

## Exercise 6: Extract email domains
**Task:** Read a file containing email addresses (one per line) and extract all unique domains.

**Solution:**
```python
filename = input("Enter filename: ")
file = open(filename, "r")
emails = file.readlines()
file.close()

domains = set()
for email in emails:
    email = email.strip()
    if "@" in email:
        domain = email.split("@")[1]
        domains.add(domain)

print("Unique domains:")
for domain in sorted(domains):
    print(domain)
```

---

# 12) Common pitfalls & tips

**Common pitfalls:**
- **Immutability confusion:** Remember that strings can't be changed; operations create new strings
- **Index out of range:** Always check string length before indexing
- **Forgetting to strip:** When reading from files, remember to strip newlines
- **Case sensitivity:** String comparison is case-sensitive; use `.lower()` or `.upper()` for case-insensitive comparison
- **Mutable vs immutable:** Don't try to modify strings in place; assign the result to a variable

**Tips:**
- Use f-strings for formatting (cleanest syntax)
- Use `.strip()` when reading user input or file content
- Always close files or use `with` statements
- Use `.split()` and `.join()` for working with word lists
- Use `in` and `not in` for substring checking (more readable than `.find() != -1`)
- Remember that string methods return new strings; they don't modify the original
- Use triple quotes for multi-line strings
- Escape special characters properly (especially backslashes in file paths on Windows)

**Performance tips:**
- Use `.join()` instead of `+` for concatenating many strings
- Use list comprehensions with strings when appropriate
- Consider using `collections.Counter` for frequency counting

---

# 13) Cheat‑sheet

```python
# Creating strings
str1 = "Hello"
str2 = input("Enter text: ")
str3 = file.readline()

# Operations
combined = str1 + " " + str2        # Concatenation
repeated = str1 * 3                  # Repetition
length = len(str1)                   # Length
exists = "Hello" in str1             # Membership

# Indexing and slicing
char = str1[0]                       # First character
substring = str1[0:5]                # Slice
reversed = str1[::-1]                # Reverse

# Common methods
str1.upper()                         # Convert to uppercase
str1.lower()                         # Convert to lowercase
str1.strip()                         # Remove whitespace
str1.split()                         # Split into list
" ".join(list)                       # Join list into string
str1.replace("old", "new")           # Replace substring
str1.find("sub")                     # Find substring index
str1.count("char")                   # Count occurrences
str1.startswith("prefix")            # Check prefix
str1.endswith("suffix")              # Check suffix

# Formatting
name = "John"
f"Hello, {name}"                     # F-string (preferred)
"Hello, {}".format(name)             # .format()
"Hello, %s" % name                   # Old-style

# File reading
file = open("file.txt", "r")
content = file.read()                # Read all
line = file.readline()               # Read one line
lines = file.readlines()             # Read all lines as list
file.close()

# With statement (recommended)
with open("file.txt", "r") as file:
    content = file.read()
```

---

# 14) Mini‑projects

1. **Text Analyzer** — Create a program that reads a text file and provides statistics:
   - Total characters (with and without spaces)
   - Total words
   - Total sentences
   - Average word length
   - Most common words

2. **Password Validator** — Create a function that validates passwords:
   - At least 8 characters
   - Contains uppercase and lowercase letters
   - Contains at least one digit
   - Contains at least one special character

3. **Simple Text Editor** — Create a menu-driven program to:
   - Read text from a file
   - Display text statistics
   - Search and replace text
   - Convert case (upper/lower/title)
   - Save modified text to a new file

4. **Word Frequency Analyzer** — Create a program that:
   - Reads a text file
   - Counts word frequencies
   - Displays top N most common words
   - Creates a bar chart (using matplotlib if available)

5. **Email Extractor** — Create a program that:
   - Reads a file containing mixed text
   - Extracts all email addresses using string methods
   - Lists unique email domains
   - Counts emails per domain

> Copy any snippet into your editor and run it. I can export these as `.py` files or a single `.zip` on request.

---

# To think about

- What's the difference between `read()`, `readline()`, and `readlines()`?
- Why are strings immutable in Python? What are the benefits?
- How would you handle very large text files efficiently?
- What's the difference between `find()` and `index()` methods?
- How can string methods be chained together?

**Next steps:** In future courses, you'll learn about:
- **Regular expressions (regex):** Advanced pattern matching in strings
- **Text parsing:** Extracting structured data from unstructured text
- **Natural language processing:** Working with human language at scale
- **Encoding and Unicode:** Understanding how text is stored and represented

---

