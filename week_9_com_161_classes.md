# Week 9 — COM161: Classes and Objects

---

## summary
This week introduces **object-oriented programming (OOP)** in Python. You'll learn to define **classes** (blueprints for objects), create **objects** (instances of classes), understand **properties** (attributes/state) and **behaviours** (methods), and work with real-world entities like students, cars, and books. Exercises include creating student objects, managing lists of objects, and performing operations like deletion and filtering.

### Key terms & definitions (glossary)
- **class:** A **blueprint** or template that defines the structure and behaviour of objects. Like engineering drawings for a car.
- **object (instance):** A **concrete entity** created from a class. Each object has its own identity, properties, and can perform behaviours defined by the class.
- **property (attribute/state):** **Data fields** that describe an object's characteristics. Example: a Student object has properties like `name`, `regNo`, `course`, `year`.
- **behaviour (method):** **Functions** that belong to an object and define what actions the object can perform. Methods are called on objects to ask them to perform actions.
- **instantiation:** The process of **creating an object** from a class using the class name followed by parentheses: `student1 = Student()`.
- **instance variable:** A **property** that belongs to a specific object instance. Each object has its own copy of instance variables.
- **method:** A **function** defined inside a class that operates on the object's data. Methods are called using dot notation: `object.method()`.
- **self:** A reference to the **current object instance** within a class method. Used to access the object's properties and methods.
- **object-oriented programming (OOP):** A programming paradigm where **objects** are at the centre of the program structure, representing both data and the overall program organization.
- **procedural programming:** A programming paradigm that structures a program like a recipe with sequential steps, functions, and code blocks.
- **encapsulation:** The bundling of data (properties) and methods (behaviours) together within a class. (Will be covered in more detail next week.)

---

## Table of contents
1. Introduction: Why OOP?
2. Objects: properties and behaviours
3. Real-world example: The Car as an Object
4. Procedural vs Object-Oriented Programming
5. Classes in Python: syntax and structure
6. Creating a simple class
7. Creating objects (instantiation)
8. Accessing properties and methods
9. The `self` parameter
10. Worked example: Student class
11. Working with lists of objects
12. Exercises — with solutions
13. Common pitfalls & tips
14. Cheat‑sheet
15. Mini‑projects

---

# 1) Introduction: Why OOP?

So far, you've been solving problems using:
- Variables
- Selection (if/elif/else)
- Loops (for, while)
- File Handling
- Lists
- Functions

At some stage, we want to deal with **complex real-world scenarios**. The concepts we've used so far can't effectively deal with:
- Students in a university
- Cars in a showroom
- Books in a library
- And so on

So we must use a new concept or paradigm called **object-oriented programming** to enable us to develop large-scale software and real-world concepts effectively.

**OOP involves programming using objects.** Objects represent an entity in the real world that can be distinctly identified. For example, a house, a square, and even your student fees could be seen as an object.

---

# 2) Objects: properties and behaviours

An object has a **unique identity**, **properties**, and **behaviours** (actions).

- **Properties** (also known as **state** or **attributes**) are represented by data fields with their current values.
- The **behaviour** of an object is defined by **methods** (methods in objects are functions that belong to the object). To call a function on an object is to ask the object to perform an action.

**Example:** If a person were an object:
- **Properties:** name, age, address, etc.
- **Behaviours:** walking, talking, breathing, running

OOP also provides support for managing the relations between things:
- Companies → employees
- Students → teachers
- Tasks → task steps

---

# 3) Real-world example: The Car as an Object

- Suppose you want to drive a car and make it go faster by pressing its accelerator pedal.
- Before you can drive a car, someone has to **design it**.
- A car typically begins as **engineering drawings**, similar to the blueprints that describe the design of a house.
- Drawings include the design for the pedals and steering etc...
- Pedal **hides from the driver** the complex mechanisms that actually make the car go faster,
- just as the brake pedal hides the mechanisms that slow the car,
- and the steering wheel hides the mechanisms that turn the car.

This enables people with little or no knowledge of how engines, braking and steering mechanisms work to drive a car easily.

- Before you can drive a car, it must be **built from the engineering drawings** that describe it.
- A completed car has an actual accelerator pedal to make the car go faster, but even that's not enough:
- the car won't accelerate on its own (hopefully!), so the **driver must press the pedal** to accelerate the car.

**Analogy to programming:**
- **Class** = engineering drawings (blueprint)
- **Object** = the actual car built from those drawings
- **Method** = pressing the accelerator pedal (action you can perform)
- **Property** = current speed, fuel level, etc. (state of the car)

---

# 4) Procedural vs Object-Oriented Programming

In Week 1, we discussed **Procedural Programming**, which structures a program like a recipe:
- provides a set of steps, in the form of functions and code blocks, which flow sequentially in order to complete a task.

**The key difference to OOP** is that **objects are at the centre** of the OOP programming paradigm, not only representing the data, as in procedural programming, but in the overall structure of the program as well.

**Remember** — Python is a **multi-paradigm programming language** so you can:
- choose the paradigm that best suits the problem at hand
- mix different paradigms in one program
- switch from one paradigm to another as your program evolves

---

# 5) Classes in Python: syntax and structure

A **class** is a blueprint for creating objects. It defines:
- What **properties** (attributes) objects will have
- What **behaviours** (methods) objects can perform

**Basic syntax:**
```python
class ClassName:
    def __init__(self, param1, param2, ...):
        # Initialize properties
        self.property1 = param1
        self.property2 = param2
    
    def method_name(self):
        # Define behaviour
        pass
```

**Key points:**
- Class names should start with a **capital letter** (convention: `PascalCase`)
- `__init__` is a special method called a **constructor** — it runs when you create a new object
- `self` refers to the current object instance
- Properties are accessed using `self.property_name`
- Methods are functions defined inside the class

---

# 6) Creating a simple class

Let's start with a simple example:

```python
class Student:
    def __init__(self, name, reg_no, course, year):
        self.name = name
        self.regNo = reg_no
        self.course = course
        self.year = year
    
    def printDetails(self):
        print("Student Name:", self.name)
        print("Student ID:", self.regNo)
        print("Course:", self.course)
        print("Year:", self.year)
```

**What's happening:**
- `__init__` method initializes the object with four properties: `name`, `regNo`, `course`, `year`
- `printDetails` is a method that displays the student's information
- `self` is used to refer to the current object's properties

---

# 7) Creating objects (instantiation)

To create an object from a class, you **call the class name** like a function:

```python
# Create a student object
student1 = Student("Bobby Smith", "B0001", "Computing Systems", "Two")

# Create another student
student2 = Student("Alice Johnson", "A0002", "Computer Science", "One")
```

**What happens:**
1. Python calls the `__init__` method
2. The properties are set for this specific object
3. The object is returned and assigned to the variable

Each object is **independent** — changing `student1.name` doesn't affect `student2.name`.

---

# 8) Accessing properties and methods

**Accessing properties:**
```python
# Direct access (can read and write)
print(student1.name)        # Read: "Bobby Smith"
student1.name = "Jimmy Smith"  # Write: change the name
print(student1.name)        # Now: "Jimmy Smith"
```

**Calling methods:**
```python
# Call a method using dot notation
student1.printDetails()
```

**Complete example:**
```python
class Student:
    def __init__(self, name, reg_no, course, year):
        self.name = name
        self.regNo = reg_no
        self.course = course
        self.year = year
    
    def printDetails(self):
        print("Student Name:", self.name)
        print("Student ID:", self.regNo)
        print("Course:", self.course)
        print("Year:", self.year)

# Create and use objects
student1 = Student("Bobby Smith", "B0001", "Computing Systems", "Two")
student1.printDetails()

# Modify property
print("\nThe student's name in the first location is", student1.name)
student1.name = "Jimmy Smith"
print("The student's new name is", student1.name)
```

**Output:**
```
Student Name: Bobby Smith
Student ID: B0001
Course: Computing Systems
Year: Two

The student's name in the first location is Bobby Smith
The student's new name is Jimmy Smith
```

> ⚠️ **Security consideration:** Direct access to properties means users can overwrite values. Are there security implications here? What could happen if your Bank details could be accessed directly like this? In next week's lecture, we'll see how we can stop the values of the properties of an object being changed from outside the class (using **encapsulation**).

---

# 9) The `self` parameter

**`self`** is a reference to the **current object instance**. It's automatically passed when you call a method.

**Why `self`?**
- When you call `student1.printDetails()`, Python automatically passes `student1` as the first argument
- Inside the method, `self` refers to `student1`
- This allows the method to access and modify the object's properties

**Example:**
```python
class Student:
    def __init__(self, name, reg_no):
        self.name = name      # self.name refers to THIS object's name
        self.regNo = reg_no   # self.regNo refers to THIS object's regNo
    
    def printDetails(self):
        # self refers to the object that called this method
        print(self.name, self.regNo)

student1 = Student("Bob", "B001")
student2 = Student("Alice", "A002")

student1.printDetails()  # self = student1, prints "Bob B001"
student2.printDetails()  # self = student2, prints "Alice A002"
```

---

# 10) Worked example: Student class

**Complete program: Create multiple students and display them**

```python
class Student:
    def __init__(self, name, reg_no, course, year):
        self.name = name
        self.regNo = reg_no
        self.course = course
        self.year = year
    
    def printDetails(self):
        print("Student Name:", self.name)
        print("Student ID:", self.regNo)
        print("Course:", self.course)
        print("Year:", self.year)

# Create a list to store students
studentList = []

# Allow user to create multiple students
while True:
    name = input("Enter the Student Name: ")
    reg_no = input("Enter the Student ID: ")
    course = input("Enter the Course: ")
    year = input("Enter the Year: ")
    
    # Create a new Student object
    newStudent = Student(name, reg_no, course, year)
    studentList.append(newStudent)
    
    # Ask if user wants to continue
    choice = input("Do you want to add another student? ('y' for yes): ")
    if choice.lower() != 'y':
        break

# Display results
print(f"\nNo of students created: {len(studentList)}")
for student in studentList:
    student.printDetails()
    print()

# Access individual student
print("The student's name in the first location is", studentList[0].name)
studentList[0].name = "Jimmy Smith"
print("The student's new name is", studentList[0].name)
```

**Sample run:**
```
Enter the Student Name: Bobby Smith
Enter the Student ID: B0001
Enter the Course: Computing Systems
Enter the Year: Two
Do you want to add another student? ('y' for yes): n

No of students created: 1
Student Name: Bobby Smith
Student ID: B0001
Course: Computing Systems
Year: Two

The student's name in the first location is Bobby Smith
The student's new name is Jimmy Smith
```

---

# 11) Working with lists of objects

You can store objects in lists and perform operations on them:

```python
studentList = [
    Student("Simon", "8001", "CompSci", "1"),
    Student("Tom", "8002", "CompSci", "2"),
    Student("Bill", "8003", "CompSci", "2")
]

# Iterate through list
for student in studentList:
    student.printDetails()
    print()

# Access by index
first_student = studentList[0]
print(first_student.name)

# Filter by property
computing_students = []
for student in studentList:
    if student.course == "Computing Systems":
        computing_students.append(student)
```

---

# 12) Exercises — with solutions

## Exercise 1: Delete a student by Student ID
**Task:** Allow the user to delete a student if they enter the correct Student Number.

**Expected output:**
```
No of students created: 3
Student Name: Simon
Student ID: 8001
Course: CompSci
Year: 1
Student Name: Tom
Student ID: 8002
Course: CompSci
Year: 2
Student Name: Bill
Student ID: 8003
Course: CompSci
Year: 2
Which Student do you want to delete: 8001
Student deleted!
Student Name: Tom
Student ID: 8002
Course: CompSci
Year: 2
Student Name: Bill
Student ID: 8003
Course: CompSci
Year: 2
```

**Solution 1: Using `remove()`**
```python
class Student:
    def __init__(self, name, reg_no, course, year):
        self.name = name
        self.regNo = reg_no
        self.course = course
        self.year = year
    
    def printDetails(self):
        print("Student Name:", self.name)
        print("Student ID:", self.regNo)
        print("Course:", self.course)
        print("Year:", self.year)

# Assume studentList is already populated
studentList = [
    Student("Simon", "8001", "CompSci", "1"),
    Student("Tom", "8002", "CompSci", "2"),
    Student("Bill", "8003", "CompSci", "2")
]

userChoice = input("Which Student do you want to delete: ")

found = False
for student in studentList:
    if userChoice == student.regNo:
        studentList.remove(student)
        found = True
        break

if found:
    print("Student deleted!")
else:
    print("Student not found")

for student in studentList:
    student.printDetails()
    print()
```

**Solution 2: Using index and `del`**
```python
userChoice = input("Which Student do you want to delete: ")

found = False
for index in range(len(studentList)):
    if userChoice == studentList[index].regNo:
        del studentList[index]
        found = True
        break

if found:
    print("Student deleted!")
else:
    print("Student not found")

for student in studentList:
    student.printDetails()
    print()
```

## Exercise 2: Count students by course
**Task:** Allow the user to find out how many students do "Computing Systems".

**Expected output:**
```
Student Name: Simon
Student ID: B001
Course: Computing Systems
Year: 4
Student Name: Bob
Student ID: B002
Course: Computer Science
Year: 4
Student Name: Tim
Student ID: B003
Course: Computing Systems
Year: 4
The number of students who do Computing Systems is 2
```

**Solution 1: Using `for...in`**
```python
count = 0
for student in studentList:
    if student.course == "Computing Systems":
        count += 1

print("The number of students who do Computing Systems is", count)
```

**Solution 2: Using index**
```python
count = 0
for index in range(len(studentList)):
    if studentList[index].course == "Computing Systems":
        count += 1

print("The number of students who do Computing Systems is", count)
```

---

# 13) Common pitfalls & tips

- **Forgetting `self`:** Always include `self` as the first parameter in instance methods. Python automatically passes the object, but you must declare it.
- **Direct property access:** Properties can be accessed and modified directly. Consider if this is appropriate for your use case (encapsulation will be covered next week).
- **Modifying during iteration:** Be careful when modifying a list while iterating over it. Consider collecting items to remove first, then removing them.
- **Class vs instance:** Remember that a class is a blueprint; objects are instances created from that blueprint. Each object has its own copy of properties.
- **Naming conventions:** Use `PascalCase` for class names (e.g., `Student`, `Car`, `Book`) and `camelCase` or `snake_case` for method and property names (e.g., `printDetails`, `student_name`).
- **`__init__` is not a constructor:** Technically, `__init__` initializes an object that's already been created. The actual object creation happens before `__init__` is called.

---

# 14) Cheat‑sheet

```python
# Define a class
class ClassName:
    def __init__(self, param1, param2):
        self.property1 = param1
        self.property2 = param2
    
    def method_name(self):
        # Use self.property1, self.property2
        pass

# Create an object
obj = ClassName(value1, value2)

# Access properties
obj.property1
obj.property1 = new_value

# Call methods
obj.method_name()

# Work with lists of objects
obj_list = [ClassName(...), ClassName(...)]
for obj in obj_list:
    obj.method_name()

# Filter objects
filtered = [obj for obj in obj_list if obj.property1 == value]
```

---

# 15) Mini‑projects

1. **Student Management System** — Create a menu-driven program to:
   - Add students
   - Delete students by ID
   - Search for students by name or ID
   - Count students by course or year
   - Display all students

2. **Library Book System** — Create a `Book` class with properties like `title`, `author`, `isbn`, `available`. Create a list of books and:
   - Mark books as available/unavailable
   - Search for books by author or title
   - Count available books

3. **Car Showroom** — Create a `Car` class with properties like `make`, `model`, `year`, `price`, `color`. Create a list of cars and:
   - Filter cars by price range
   - Filter cars by make or model
   - Calculate average price
   - Display cars sorted by price

> Copy any snippet into your editor and run it. I can export these as `.py` files or a single `.zip` on request.

---

# To think about

- Do we want the user to overwrite object properties directly?
- Are there security implications here?
- What could happen if your Bank details could be accessed directly like this?

In next week's lecture, we'll see how we can stop the values of the properties of an object being changed from outside the class (using **encapsulation** and **access modifiers**).

**Extension topic:** Say we want to have more specialised classes based on a certain class. For example, a Student class does not show if a student can be part-time or full-time. How can we extend the functionality of an existing class and add more to it? This will be covered in next week's lecture (using **inheritance**).

