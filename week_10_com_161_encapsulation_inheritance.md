# Week 10 — COM161: Encapsulation and Inheritance

---

## summary
This week builds on object-oriented programming (OOP) concepts from Week 9. You'll learn about **encapsulation** (hiding internal details and protecting data) through access modifiers, and **inheritance** (creating new classes based on existing ones) to promote code reuse and create hierarchical relationships between classes. You'll understand private attributes using name mangling, parent-child class relationships, the `super()` function, and method overriding.

### Key terms & definitions (glossary)
- **encapsulation:** The bundling of data (properties) and methods (behaviours) together within a class, and the restriction of access to certain components. It's about hiding internal implementation details and protecting data from unauthorized access.
- **access modifier:** A mechanism to control the accessibility of class members (attributes and methods). In Python, this is achieved through naming conventions rather than strict modifiers.
- **private attribute:** An attribute that is intended to be accessed only from within the class. In Python, private attributes are indicated by a double underscore prefix (`__attribute_name`).
- **name mangling:** Python's mechanism for implementing private attributes. When you prefix an attribute with `__`, Python internally renames it to `_ClassName__attribute_name`, making it harder (but not impossible) to access from outside the class.
- **public attribute:** An attribute that can be accessed and modified from anywhere in the program. By default, all attributes in Python are public.
- **inheritance:** A mechanism in OOP that allows a new class (child/subclass) to inherit properties and methods from an existing class (parent/superclass/base class). This promotes code reuse and establishes an "is-a" relationship.
- **parent class (superclass/base class):** The class that is being inherited from. It provides attributes and methods to child classes.
- **child class (subclass/derived class):** A class that inherits from a parent class. It can have additional attributes and methods, or override inherited methods.
- **is-a relationship:** A relationship indicating that a child class is a specialized version of the parent class. For example, a `House` is-a `Building`.
- **method overriding:** The ability of a child class to provide a specific implementation of a method that is already defined in the parent class.
- **super():** A built-in function in Python that gives you access to methods in the parent class. It's commonly used in the `__init__` method to initialize the parent class before initializing the child class.
- **code reuse:** The practice of writing code once and using it multiple times, which is one of the main benefits of inheritance.

---

## Table of contents
1. Introduction: Why encapsulation and inheritance?
2. Encapsulation: Protecting data
3. Private attributes in Python
4. Accessing private attributes
5. Inheritance: Building on existing classes
6. Creating child classes
7. The `super()` function
8. Method overriding
9. Multiple levels of inheritance
10. Worked examples
11. Exercises — with solutions
12. Common pitfalls & tips
13. Cheat‑sheet
14. Mini‑projects

---

# 1) Introduction: Why encapsulation and inheritance?

Last week, we learned about classes and objects. We discovered that we could create objects and access their properties directly:

```python
student1 = Student("John", "B001", "CompSci", "1")
print(student1.name)  # Direct access
student1.name = "Jane"  # Direct modification
```

This works, but it raises some concerns:
- **Security:** What if someone accidentally or intentionally changes important data?
- **Control:** What if we want to validate data before it's changed?
- **Maintenance:** What if we want to change how data is stored internally?

**Encapsulation** solves these problems by controlling access to an object's internal state.

Additionally, we often find ourselves creating similar classes:
- `Student`, `PartTimeStudent`, `FullTimeStudent`
- `Building`, `House`, `School`, `Office`
- `Vehicle`, `Car`, `Motorcycle`, `Truck`

Rather than copying code between similar classes, **inheritance** allows us to create a base class and extend it, promoting code reuse and maintaining relationships between classes.

---

# 2) Encapsulation: Protecting data

**Encapsulation** is one of the four fundamental principles of OOP (along with Inheritance, Polymorphism, and Abstraction). It serves two main purposes:

1. **Data hiding:** Prevent external code from directly accessing or modifying internal data
2. **Controlled access:** Provide controlled ways to access and modify data (often through methods)

**Benefits:**
- Prevents accidental modification of important data
- Allows validation of data before it's stored
- Makes code easier to maintain and modify
- Provides a clear interface for interacting with objects

**Real-world analogy:** 
- You don't need to know how a car's engine works to drive it (the complexity is hidden)
- You interact with the car through a controlled interface (steering wheel, pedals, etc.)

---

# 3) Private attributes in Python

In Python, there are no strict "private" attributes like in Java or C++. Instead, Python uses naming conventions to indicate intent.

**Naming conventions:**
- **Public:** No prefix (e.g., `self.name`)
- **Protected:** Single underscore prefix (e.g., `self._name`) - indicates "internal use", but still accessible
- **Private:** Double underscore prefix (e.g., `self.__name`) - triggers name mangling

**Private attributes example:**

```python
class Student:
    def __init__(self, name, reg_no, course, year):
        self.__name = name  # Private attribute
        self.regNo = reg_no  # Public attribute
        self.course = course  # Public attribute
        self.year = year  # Public attribute
    
    def printDetails(self):
        print("Student Name:", self.__name)  # Accessible within class
        print("Student ID:", self.regNo)
        print("Course:", self.course)
        print("Year:", self.year)
```

**Key points:**
- Attributes with `__` prefix are intended to be private
- They can still be accessed within the class methods
- Python performs "name mangling" to make them harder to access from outside

---

# 4) Accessing private attributes

**Within the class:**
Private attributes can be freely accessed within class methods:

```python
class Student:
    def __init__(self, name):
        self.__name = name
    
    def getName(self):  # Getter method
        return self.__name
    
    def setName(self, name):  # Setter method
        if len(name) > 0:  # Validation
            self.__name = name
        else:
            print("Error: Name cannot be empty")
```

**From outside the class:**
Direct access to private attributes is discouraged, but still possible through name mangling:

```python
student1 = Student("John")
# This won't work (attribute not found):
# print(student1.__name)  # AttributeError

# But this works (using mangled name):
print(student1._Student__name)  # Output: John
```

**Best practice:** Use getter and setter methods to access private attributes:

```python
student1 = Student("John")
print(student1.getName())  # Output: John
student1.setName("Jane")
print(student1.getName())  # Output: Jane
```

**Complete example:**

```python
class Student:
    def __init__(self, name, reg_no, course, year):
        self.__name = name
        self.regNo = reg_no
        self.course = course
        self.year = year
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name!")
    
    def printDetails(self):
        print("Student Name:", self.__name)
        print("Student ID:", self.regNo)
        print("Course:", self.course)
        print("Year:", self.year)

# Usage
s1 = Student("Fred Jones", "B001", "Computing Systems", "Two")
print(s1.getName())  # Fred Jones
s1.setName("Frederick Jones")
s1.printDetails()
```

---

# 5) Inheritance: Building on existing classes

**Inheritance** allows you to create a new class based on an existing class. The new class:
- Inherits all attributes and methods from the parent class
- Can add new attributes and methods
- Can override inherited methods
- Establishes an "is-a" relationship

**Benefits:**
- **Code reuse:** Don't repeat code that's already written
- **Maintainability:** Changes to parent class automatically affect child classes
- **Organization:** Models real-world relationships (e.g., a House is a Building)
- **Extensibility:** Easy to add new specialized classes

**Real-world examples:**
- `Animal` → `Dog`, `Cat`, `Bird`
- `Vehicle` → `Car`, `Motorcycle`, `Truck`
- `Building` → `House`, `School`, `Office`
- `Employee` → `Manager`, `Developer`, `Designer`

---

# 6) Creating child classes

**Basic syntax:**

```python
class ParentClass:
    # Parent class definition
    pass

class ChildClass(ParentClass):
    # Child class definition
    pass
```

**Simple example:**

```python
# Parent class
class Dog:
    species = 'mammal'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Child class (inherits from Dog)
class Bulldog(Dog):
    def run(self, speed):
        return f"{self.name} runs {speed}"

# Usage
jim = Bulldog("Jim", 12)
print(jim.description())  # Inherited method
print(jim.speak("Woof"))  # Inherited method
print(jim.run("slowly"))  # New method specific to Bulldog
```

**What gets inherited:**
- All attributes (instance variables and class variables)
- All methods (instance methods)
- The ability to override methods

---

# 7) The `super()` function

The `super()` function gives you access to methods in the parent class. It's commonly used in the `__init__` method to initialize the parent class first.

**Why use `super()`?**
- Ensures parent class is properly initialized
- Avoids hardcoding the parent class name
- Supports multiple inheritance (advanced topic)

**Syntax:**
```python
super().__init__(parameters)
super().method_name(parameters)
```

**Example: Building inheritance hierarchy**

```python
class Building:
    def __init__(self, stories, address):
        self.stories = stories
        self.address = address
    
    def printDetails(self):
        print("Building Details")
        print("The number of stories is", self.stories)
        print("The address is", self.address)

class House(Building):
    def __init__(self, stories, address, bedrooms, heating):
        super().__init__(stories, address)  # Initialize parent class
        self.bedrooms = bedrooms
        self.heating = heating
    
    def printDetails(self):
        print("House Details")
        print("The number of stories is", self.stories)
        print("The address is", self.address)
        print("The number of bedrooms is", self.bedrooms)
        print("The heating is", self.heating)

class School(Building):
    def __init__(self, stories, address, principal, typeOfSchool):
        super().__init__(stories, address)
        self.principal = principal
        self.typeOfSchool = typeOfSchool
    
    def printDetails(self):
        print("School Details")
        print("The number of stories is", self.stories)
        print("The address is", self.address)
        print("The principal is", self.principal)
        print("The School is a", self.typeOfSchool, "school")

# Usage
building1 = Building(2, "12 Main Street")
building1.printDetails()

house1 = House(1, "14 Main Street", 2, "oil")
house1.printDetails()

school1 = School(2, "15 Main Street", "Mr. Meadows", "secondary")
school1.printDetails()
```

**Output:**
```
Building Details
The number of stories is 2
The address is 12 Main Street
House Details
The number of stories is 1
The address is 14 Main Street
The number of bedrooms is 2
The heating is oil
School Details
The number of stories is 2
The address is 15 Main Street
The principal is Mr. Meadows
The School is a secondary school
```

---

# 8) Method overriding

Method overriding allows a child class to provide a specific implementation of a method that is already defined in the parent class.

**When to override:**
- When the child class needs different behavior than the parent
- When you want to extend the parent's method and add more functionality

**Example:**

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):  # Override parent's speak method
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):  # Override parent's speak method
        return f"{self.name} meows"

# Usage
animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(animal.speak())  # Generic Animal makes a sound
print(dog.speak())     # Buddy barks
print(cat.speak())     # Whiskers meows
```

**Calling parent method from override:**

You can call the parent's method from within the override:

```python
class Building:
    def printDetails(self):
        print("Building Details")
        print("Address:", self.address)

class House(Building):
    def printDetails(self):
        super().printDetails()  # Call parent's method
        print("Bedrooms:", self.bedrooms)  # Add more details
```

---

# 9) Multiple levels of inheritance

Inheritance can span multiple levels:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __init__(self, name, has_fur):
        super().__init__(name)
        self.has_fur = has_fur

class Dog(Mammal):
    def __init__(self, name, has_fur, breed):
        super().__init__(name, has_fur)
        self.breed = breed

# Dog inherits from Mammal, which inherits from Animal
buddy = Dog("Buddy", True, "Golden Retriever")
print(buddy.name)      # From Animal
print(buddy.has_fur)   # From Mammal
print(buddy.breed)     # From Dog
```

---

# 10) Worked examples

## Example 1: Student with encapsulation

```python
class Student:
    def __init__(self, name, reg_no, course, year):
        self.__name = name  # Private
        self.regNo = reg_no
        self.course = course
        self.year = year
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        if isinstance(name, str) and len(name.strip()) > 0:
            self.__name = name
        else:
            print("Error: Invalid name")
    
    def printDetails(self):
        print("Student Name:", self.__name)
        print("Student ID:", self.regNo)
        print("Course:", self.course)
        print("Year:", self.year)

# Create student list
studentList = []

userChoice = 'y'
while userChoice == 'y':
    name = input("Enter the Student Name: ")
    regNo = input("Enter the Student ID: ")
    course = input("Enter the Course: ")
    year = input("Enter the Year: ")
    
    studentList.append(Student(name, regNo, course, year))
    userChoice = input("Do you want to add another student? ('y' for yes): ")

# Display all students
for student in studentList:
    student.printDetails()
    print()

# Try to access private attribute (won't work directly)
# print(studentList[0].__name)  # AttributeError

# Access through getter
print("First student's name:", studentList[0].getName())

# Modify through setter
studentList[0].setName("Jimmy Smith")
print("Updated name:", studentList[0].getName())
```

## Example 2: Vehicle inheritance hierarchy

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__mileage = 0  # Private
    
    def getMileage(self):
        return self.__mileage
    
    def addMileage(self, miles):
        if miles > 0:
            self.__mileage += miles
    
    def displayInfo(self):
        print(f"{self.year} {self.make} {self.model}")
        print(f"Mileage: {self.__mileage} miles")

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
    
    def displayInfo(self):
        super().displayInfo()
        print(f"Doors: {self.doors}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
    
    def displayInfo(self):
        super().displayInfo()
        print(f"Engine Size: {self.engine_size}cc")

# Usage
car1 = Car("Toyota", "Camry", 2023, 4)
car1.addMileage(5000)
car1.displayInfo()

bike1 = Motorcycle("Honda", "CBR600", 2023, 600)
bike1.addMileage(2000)
bike1.displayInfo()
```

---

# 11) Exercises — with solutions

## Exercise 1: Protected student name
**Task:** Create a `Student` class with a private `__name` attribute. Add getter and setter methods. Ensure the setter validates that the name is not empty.

**Solution:**
```python
class Student:
    def __init__(self, name, reg_no):
        self.__name = name
        self.regNo = reg_no
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        if isinstance(name, str) and len(name.strip()) > 0:
            self.__name = name
            print("Name updated successfully")
        else:
            print("Error: Name cannot be empty")
    
    def printDetails(self):
        print("Student Name:", self.__name)
        print("Student ID:", self.regNo)

# Test
s1 = Student("John Doe", "B001")
print(s1.getName())
s1.setName("Jane Doe")
s1.setName("")  # Should show error
s1.printDetails()
```

## Exercise 2: Bank account with encapsulation
**Task:** Create a `BankAccount` class with a private balance. Include methods to deposit (with validation), withdraw (with validation for sufficient funds), and check balance.

**Solution:**
```python
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Error: Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive")
        elif amount > self.__balance:
            print(f"Error: Insufficient funds. Balance: ${self.__balance}")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
    
    def getBalance(self):
        return self.__balance
    
    def displayInfo(self):
        print(f"Account: {self.account_number}")
        print(f"Balance: ${self.__balance}")

# Test
account = BankAccount("12345", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Should fail
account.displayInfo()
```

## Exercise 3: Animal inheritance
**Task:** Create an `Animal` parent class with `name` and `age`. Create `Dog` and `Cat` child classes that override a `speak()` method.

**Solution:**
```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return f"{self.name} makes a sound"
    
    def displayInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def speak(self):
        return f"{self.name} barks: Woof!"
    
    def displayInfo(self):
        super().displayInfo()
        print(f"Breed: {self.breed}")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        return f"{self.name} meows: Meow!"
    
    def displayInfo(self):
        super().displayInfo()
        print(f"Color: {self.color}")

# Test
dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Orange")

print(dog.speak())
dog.displayInfo()
print()
print(cat.speak())
cat.displayInfo()
```

## Exercise 4: Employee hierarchy
**Task:** Create an `Employee` class with name and employee_id. Create `Manager` and `Developer` subclasses that add specific attributes and override a `displayRole()` method.

**Solution:**
```python
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def displayRole(self):
        print(f"{self.name} is an Employee")

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department
    
    def displayRole(self):
        print(f"{self.name} is a Manager in {self.department}")

class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language
    
    def displayRole(self):
        print(f"{self.name} is a Developer specializing in {self.programming_language}")

# Test
manager = Manager("Alice Johnson", "M001", "Engineering")
developer = Developer("Bob Smith", "D001", "Python")

manager.displayRole()
developer.displayRole()
```

---

# 12) Common pitfalls & tips

**Encapsulation pitfalls:**
- **Forgetting `self`:** Always use `self` when accessing private attributes within methods
- **Trying to access `__attribute` directly:** Use getter/setter methods instead
- **No true privacy:** Remember that Python's privacy is based on convention, not strict enforcement
- **Over-encapsulation:** Don't make everything private; only protect what needs protection

**Inheritance pitfalls:**
- **Forgetting `super().__init__()`:** Always initialize the parent class in child `__init__` methods
- **Calling `super()` incorrectly:** Use `super()` without arguments in Python 3
- **Circular inheritance:** Make sure your inheritance hierarchy doesn't create circular dependencies
- **Deep inheritance:** Avoid too many levels of inheritance (2-3 levels is usually enough)

**Tips:**
- Use encapsulation when you need to protect data or validate input
- Use inheritance when classes share common attributes/behaviors
- Always use `super()` instead of hardcoding parent class names
- Override methods only when you need different behavior
- Document which attributes should be private (use docstrings)
- Consider using properties (advanced) for more Pythonic getters/setters

---

# 13) Cheat‑sheet

```python
# Encapsulation - Private attributes
class MyClass:
    def __init__(self, value):
        self.__private = value  # Private attribute
        self.public = value     # Public attribute
    
    def getPrivate(self):
        return self.__private
    
    def setPrivate(self, value):
        self.__private = value

# Inheritance - Basic syntax
class Parent:
    def __init__(self, param):
        self.param = param
    
    def method(self):
        pass

class Child(Parent):
    def __init__(self, param, extra):
        super().__init__(param)  # Initialize parent
        self.extra = extra
    
    def method(self):  # Override
        super().method()  # Call parent method
        # Add child-specific code

# Creating objects
parent_obj = Parent(value)
child_obj = Child(value, extra_value)

# Access
obj.public          # Public attribute
obj.getPrivate()    # Private via getter
obj.setPrivate(val) # Private via setter
obj.method()        # Method call
```

---

# 14) Mini‑projects

1. **Library Management System** — Create a `Book` class with private attributes for ISBN and availability. Create `FictionBook` and `NonFictionBook` subclasses that inherit from `Book` and add genre-specific attributes.

2. **University System** — Create a `Person` class with name and ID. Create `Student` and `Lecturer` subclasses. Use encapsulation to protect sensitive information like grades and salary.

3. **Vehicle Rental System** — Create a `Vehicle` base class with private mileage. Create `Car`, `Motorcycle`, and `Truck` subclasses with vehicle-specific attributes. Implement methods to track mileage privately.

4. **Banking System** — Create an `Account` class with private balance. Create `SavingsAccount` and `CheckingAccount` subclasses with different interest rates and withdrawal rules.

> Copy any snippet into your editor and run it. I can export these as `.py` files or a single `.zip` on request.

---

# To think about

- What's the difference between encapsulation and inheritance?
- When should you use private attributes vs public attributes?
- Why is `super()` preferred over directly calling the parent class?
- How does inheritance promote code reuse?
- What happens if you don't call `super().__init__()` in a child class?

**Next steps:** In future courses, you'll learn about:
- **Polymorphism:** Using objects of different classes through a common interface
- **Multiple inheritance:** A class inheriting from multiple parent classes
- **Abstract classes:** Classes that cannot be instantiated, only inherited from
- **Interfaces:** Contracts that classes must follow

---

