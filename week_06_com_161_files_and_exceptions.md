# Week 6 — COM161: Files & Exceptions

---

## summary
So far our programs forget everything when they stop. This week is about **persistence**: how to save data in text files, read it back later, store multi-line "records", safely update an existing file (temp file + rename trick), and stop crashes with `try`/`except`. You’ll build mini data files (daily sales, coffee inventory with search/modify) and add basic error handling so bad input doesn’t explode your program. We’re basically moving from "toy scripts" to "tiny databases". We also look at common file patterns (open-process-close, append vs write, numeric conversion, etc.) and exception types (`ValueError`, `IOError` / `FileNotFoundError`, etc.).

---

## Table of contents
1. Why files? (persistence)
2. Opening & writing files (`open`, `write`, `close`)
3. Reading files (`read`, `readline`, loops, stripping `\n`)
4. Append vs write; numbers in files (string ↔ number)
5. Records (multi-line structured data)
6. Safely updating a record (temp file + `os.remove` / `os.rename`)
7. Exceptions (`try`/`except`) to prevent crashes
8. Common patterns & tips
9. Cheat-sheet
10. Lab 6 tasks — solved  
   - 10.1 `write_sales.py`: write daily sales to a file  
   - 10.2 `read_sales2.py`: total & average sales from file  
   - 10.3 `add_coffee_record.py`: append inventory records  
   - 10.4 `search_coffee_record.py`: find stock by description  
   - 10.5 `modify_coffee_records.py`: update a record in place (safely)  
   - 10.6 `gross_pay2.py`: input validation with `try`/`except`
11. Extra practice

---

# 1) Why files?
**Problem:** variables disappear when the program ends.

**Solution:** write data to a file on disk so you can read it next run.

Why this matters:
- **Persistence:** keep sales totals, inventory lists, user accounts, etc.
- **Sharing:** other programs (Excel, etc.) can read your `.txt` data.
- **Automation:** scripts can build logs / reports every day with no manual copy-paste.
- **Mini database:** by giving each "record" a fixed layout (like description line + quantity line), a plain text file becomes a tiny searchable database.

Vocabulary:
- **file:** named area on disk.
- **record:** one stored item (e.g. 1 coffee product).
- **field:** one piece inside a record (e.g. quantity).
- **newline `\n`:** marks the end of a line in the file.

---

# 2) Opening & writing files
Basic 3-step pattern for output is:
1. `open(...)`
2. `write(...)`
3. `close()`

```python
# Step 1: open a file for WRITING.
# 'w' = write mode (starts a NEW file / erases old contents)
outfile = open('customers.txt', 'w')

# Step 2: write strings.
outfile.write('John Cleese\n')
outfile.write('Terry Gilliam\n')

# Step 3: close so data is actually saved.
outfile.close()
```

Key points:
- You MUST close the file. This flushes the buffer, frees the file.
- `.write()` only writes *strings*. If you want to write numbers you must `str()` them first (we’ll come back to that).
- You control newlines. If you want each item on its own line, you must include `\n` yourself.

Windows path tip:
```python
data_file = open(r"C:\Users\you\Desktop\sales.txt", 'w')
# r"..." makes it a raw string so backslashes don't act like escapes.
```

---

# 3) Reading files
To read, we still use open → process → close, but in `'r'` mode.

## (a) Read the whole file at once
```python
infile = open('customers.txt', 'r')
contents = infile.read()   # one big string
print(contents)
infile.close()
```
Good for short files.

## (b) Read one line at a time with `readline()`
```python
infile = open('customers.txt', 'r')

line1 = infile.readline()   # includes the '\n'
line2 = infile.readline()
line3 = infile.readline()

# strip newline so print() doesn't double-space
line1 = line1.rstrip('\n')
line2 = line2.rstrip('\n')
line3 = line3.rstrip('\n')

print(line1)
print(line2)
print(line3)

infile.close()
```

## (c) Loop over all lines
Most common in practice:
```python
infile = open('customers.txt', 'r')

for line in infile:                # stops automatically at end of file
    clean = line.rstrip('\n')      # remove trailing newline
    print(clean)

infile.close()
```

Why `rstrip('\n')`?
- When you `print(line)` you already get the newline from the file AND `print()` adds another newline → ugly blank lines.
- `rstrip('\n')` cleans that.

---

# 4) Append vs write; numbers in files
## Modes recap
- `'w'`  = **write**. Creates a NEW file or erases the old one first.
- `'a'`  = **append**. Opens an existing file and adds to the END. If the file doesn’t exist yet, it’s created.
- `'r'`  = **read**. Opens for reading (file must exist).

If you’re adding *more* records to an inventory, use `'a'`.  
If you’re starting fresh for the day, use `'w'`.

Example (append mode):
```python
logfile = open('log.txt', 'a')
logfile.write("New entry...\n")
logfile.close()
```

## Numbers are still TEXT in files
When you write:
```python
outfile = open('numbers.txt', 'w')
n = 42
outfile.write(str(n) + '\n')   # convert number → string yourself
outfile.close()
```

When you read:
```python
infile = open('numbers.txt', 'r')
line = infile.readline()
value = int(line)              # convert string → int
print(value * 10)              # now it's math-able
infile.close()
```

Same idea for `float(...)`.

---

# 5) Records (multi-line structured data)
Instead of “one line = one thing”, sometimes each thing needs multiple pieces.  
Example: coffee inventory.

Each *record* in `coffee.txt` will be:
1. description (string, e.g. `"Colombian Dark Roast"`)
2. quantity (int/float kg, but stored as text)

So `coffee.txt` might look like:
```text
Colombian Dark Roast
12
Ethiopian Light Roast
5
House Decaf
3
...
```

To ADD a record, we:
- open the file in append mode (`'a'`)
- ask the user for description + quantity
- write each on its own line
- loop until they say stop

To READ records back:
- read description line
- read quantity line
- (strip `\n`)
- repeat until `readline()` gives `''` (end of file)

This “2 lines per record” pattern is how we fake a database using plain text.

---

# 6) Safely updating a record
Editing the *middle* of a plain text file is awkward. You cannot just “insert” in place easily.

Standard safe pattern to MODIFY or DELETE one record:
1. Open original file for reading.
2. Open a **temporary** file for writing.
3. Copy records from old → temp.
4. When you reach the record you want to change, write the *new* data instead.
5. Close both.
6. Use `os.remove` to delete the old file, then `os.rename` to rename the temp file to the original name.

Skeleton:
```python
import os

orig_name = 'coffee.txt'
temp_name = 'coffee_tmp.txt'

orig_file = open(orig_name, 'r')
temp_file = open(temp_name, 'w')

# read a record (2 lines)
descr = orig_file.readline()
while descr != '':
    qty_line = orig_file.readline()

    # clean text
    d_clean = descr.rstrip('\n')
    q_clean = qty_line.rstrip('\n')

    if d_clean.lower() == "colombian dark roast".lower():
        # write UPDATED record
        temp_file.write(d_clean + "\n")
        temp_file.write("99\n")   # <-- new qty
    else:
        # copy record unchanged
        temp_file.write(d_clean + "\n")
        temp_file.write(q_clean + "\n")

    # move to next record
    descr = orig_file.readline()

orig_file.close()
temp_file.close()

os.remove(orig_name)           # throw away old
os.rename(temp_name, orig_name)  # temp becomes the official file
```

That’s the pattern we’ll reuse in `modify_coffee_records.py`.

---

# 7) Exceptions (`try` / `except`)
When something goes wrong at runtime, Python raises an **exception**.
Examples:
- User types `"ten"` where you expected `10` → `ValueError` when you try `int("ten")`.
- You try to `open('coffee.txt','r')` but that file doesn’t exist → `IOError` / `FileNotFoundError`.

Normally the program just crashes and prints a traceback.

We can intercept and recover:

```python
try:
    hours = float(input("Hours worked: "))
    rate = float(input("Hourly rate: "))
    pay = hours * rate
    print(f"Gross pay: £{pay:.2f}")
except ValueError:
    print("Error: please enter numbers only.")
```

We can also catch file problems:

```python
try:
    f = open('sales.txt', 'r')
    # ... process file ...
    f.close()
except IOError:
    print("Could not open sales.txt")
```

You can stack multiple `except` blocks for different error types.

---

# 8) Common patterns & tips
- Keep program “flow” in a `main()` and call it under the standard guard:
  ```python
  if __name__ == "__main__":
      main()
  ```
- Always `close()` files you `open()`.
- When reading numeric data from a file, `int(line)` / `float(line)` will raise `ValueError` if the line isn’t a valid number — wrap it in `try`/`except` if needed.
- Use `'a'` (append) instead of `'w'` (write) if you’re *adding to* an inventory / log.
- Be consistent with your record layout (e.g. always: description line, then quantity line). Your search / modify code assumes this format.
- Use `rstrip('\n')` before printing lines from a file to avoid ugly blank lines.
- Use `os.remove` + `os.rename` to “edit” files safely without corrupting them.

---

# 9) Cheat-sheet
**Open (modes):**
```python
f = open('file.txt', 'r')   # read
f = open('file.txt', 'w')   # write NEW / overwrite existing
f = open('file.txt', 'a')   # append to end
```

**Write text:**
```python
f.write("hello\n")
```

**Close:**
```python
f.close()
```

**Read lines:**
```python
line = f.readline()         # includes trailing '\n'
clean = line.rstrip('\n')  # strip newline
```

**Loop through file:**
```python
for line in f:
    ...
```

**Numbers:**
```python
# writing
f.write(str(num) + "\n")

# reading
num = int(line)         # or float(line)
```

**Records (2-line coffee example):**
```text
Description
Quantity
Description
Quantity
...
```

**Safe update:**
- read old file → write temp file
- `os.remove(old)`
- `os.rename(temp, old)`

**Exceptions:**
```python
try:
    risky_stuff()
except SomeError:
    recovery()
```

---

# 10) Lab 6 — solved tasks

## 10.1 `write_sales.py`: write daily sales to a file
Goal: ask the user for N days of sales, then save each amount on its own line in `sales.txt`.

```python
def main():
    # open file for WRITE (this overwrites old sales.txt)
    sales_file = open('sales.txt', 'w')

    num_days = int(input("How many days of sales? "))

    for day in range(1, num_days + 1):
        amount = float(input(f"Sales for day {day}: "))
        # remember: write() needs a string, and we add '\n'
        sales_file.write(str(amount) + '\n')

    sales_file.close()
    print("Sales data written to sales.txt")

if __name__ == "__main__":
    main()
```

---

## 10.2 `read_sales2.py`: total & average sales
Goal: read every line from `sales.txt`, convert each to `float`, total them, and compute the average.

```python
def main():
    sales_file = open('sales.txt', 'r')

    total = 0.0
    count = 0

    for line in sales_file:
        amount = float(line)   # string -> float
        print(f"Read sale: {amount}")
        total += amount
        count += 1

    sales_file.close()

    print(f"Number of entries: {count}")
    print(f"Total sales: {total}")
    if count > 0:
        print(f"Average sale: {total / count}")

if __name__ == "__main__":
    main()
```

---

## 10.3 `add_coffee_record.py`: append inventory records
Goal: grow `coffee.txt`.  
Each record = description line, then quantity line.  
We open in `'a'` (append) so we don’t erase old data.

```python
# This program adds coffee inventory records to
# the coffee.txt file.

def main():
    # Create a variable to control the loop.
    another = 'y'

    # Open the coffee.txt file in append mode.
    coffee_file = open('coffee.txt', 'a')

    # Add records to the file.
    while another == 'y' or another == 'Y':
        # Get the coffee record data.
        print('Enter the following coffee data:')
        descr = input('Description: ')
        qty = int(input('Quantity (in kg): '))

        # Append the data to the file.
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        # Determine whether the user wants to add
        # another record to the file.
        print('Do you want to add another record?')
        another = input('Y = yes, anything else = no: ')

    # Close the file.
    coffee_file.close()
    print('Data appended to coffee.txt.')

# Call the main function.
main()
```

How the loop works:
- sentinel variable `another` decides when to stop
- each pass writes TWO lines (descr then qty), matching our record format

---

## 10.4 `search_coffee_record.py`: look up a product
Goal: ask the user for a description (e.g. `"Colombian Dark Roast"`) and report how many kg are in stock.  
We read the file in 2-line chunks.

```python
def main():
    target = input("Which coffee description are you looking for? ")

    coffee_file = open('coffee.txt', 'r')
    found = False

    # read first description line
    descr = coffee_file.readline()

    while descr != '':
        qty_line = coffee_file.readline()

        # clean up newlines
        d_clean = descr.rstrip('\n')
        q_clean = qty_line.rstrip('\n')

        if d_clean.lower() == target.lower():
            print(f"FOUND: {d_clean} has {q_clean} kg in stock.")
            found = True

        # move to next record (next description line)
        descr = coffee_file.readline()

    coffee_file.close()

    if not found:
        print("That coffee was not found.")

if __name__ == "__main__":
    main()
```

Notice the pattern:
- Read 2 lines at a time.
- Stop when `readline()` gives `''` (end of file).
- Case-insensitive compare with `.lower()`.

---

## 10.5 `modify_coffee_records.py`: change a record safely
Goal: update the quantity for ONE coffee item in `coffee.txt`.  
We CANNOT just “edit line 47 in place”; we must build a new file.

```python
import os

def main():
    search_descr = input("Which coffee description do you want to update? ")
    new_qty = input("New quantity (in kg): ")

    orig_name = 'coffee.txt'
    temp_name = 'coffee_tmp.txt'

    orig_file = open(orig_name, 'r')
    temp_file = open(temp_name, 'w')

    found = False

    descr = orig_file.readline()
    while descr != '':
        qty_line = orig_file.readline()

        d_clean = descr.rstrip('\n')
        q_clean = qty_line.rstrip('\n')

        if d_clean.lower() == search_descr.lower():
            # write updated record
            temp_file.write(d_clean + '\n')
            temp_file.write(str(new_qty) + '\n')
            found = True
        else:
            # copy the original record
            temp_file.write(d_clean + '\n')
            temp_file.write(q_clean + '\n')

        descr = orig_file.readline()

    orig_file.close()
    temp_file.close()

    os.remove(orig_name)             # delete old
    os.rename(temp_name, orig_name)  # temp becomes new coffee.txt

    if found:
        print("Record updated.")
    else:
        print("That coffee description was not found.")

if __name__ == "__main__":
    main()
```

> Tip: exact same approach works to *delete* a record. You just skip writing the matching record into the temp file.

---

## 10.6 `gross_pay2.py`: safer input with `try` / `except`
Goal: calculate gross pay, but don’t crash if user types bad input.

```python
def main():
    try:
        hours = float(input("Hours worked: "))
        rate = float(input("Hourly rate: "))
        pay = hours * rate
        print(f"Gross pay: £{pay:.2f}")
    except ValueError:
        print("Error: please enter numbers only for hours and rate.")

if __name__ == "__main__":
    main()
```

Pattern:
- `try:` = risky stuff
- `except ValueError:` = what to do if the conversion to float fails
- User gets a friendly message instead of a traceback explosion

---

# 11) Extra practice
- Write a script to SUM all quantities in `coffee.txt` and print the total kg in stock.
- Add a “delete coffee” script:
  - Ask for a description.
  - Copy every *other* record into a temp file.
  - Replace the original using `os.remove` / `os.rename`.
- Add input validation to `read_sales2.py`: if any line in `sales.txt` isn’t a valid number, catch `ValueError`, skip that line, and print a warning instead of crashing.
- Write a function `safe_open(filename)` that does:
  ```python
  try:
      return open(filename, 'r')
  except IOError:
      print("File not found.")
      return None
  ```
  Then use it in a program so missing files don’t kill the run.
- Challenge: extend the coffee system with a small text menu (1=add, 2=search, 3=modify, 4=exit) that loops until the user chooses exit.

