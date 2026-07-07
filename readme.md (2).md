<div align="center">

# -- ! Data Analyzer — Functional Python Toolkit ! --
### *Interactive Console-Based Data Analysis Using Python Functions*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Functions](https://img.shields.io/badge/Functions-Recursion%20%2F%20Args%20%2F%20Kwargs-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![Lambda](https://img.shields.io/badge/Lambda-Map%20%2F%20Filter-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"Functions are the building blocks of clarity — break the problem down, and the code writes itself."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🔺 Part A — Core Data Functions](#-part-a--core-data-functions)
- [🔢 Part B — Advanced Function Concepts](#-part-b--advanced-function-concepts)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Data Analyzer** is a menu-driven Python console application built to demonstrate the core building blocks of **functions** in Python — from basic definitions to recursion, `*args`, `**kwargs`, lambda expressions, and global variables. The program lets the user load a dataset (sample or manual) and run a variety of analysis operations through a simple numbered menu.

This project is designed to:
- Strengthen understanding of function definitions, parameters, and return values
- Practice `*args` and `**kwargs` for flexible function signatures
- Apply recursion to solve classic problems like factorial
- Use lambda functions with `map()` and `filter()`
- Work with global variables and multi-value returns
- Handle 2D lists and sorting logic

---

## 🎯 Problem Statement

> **Objective:** Build a console-based interactive tool that analyzes numeric data using a wide range of Python function concepts.

You are building a utility program for students learning Python functions. The program must accept user choices from a menu and execute the corresponding task — from displaying summary statistics to finding duplicates, applying lambda filters, or generating factorials.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Input | Function | Loads sample data or accepts manual input |
| Summary Statistics | Built-in Functions | Length, sum, min, max |
| Duplicates & Uniques | Nested Loops | Finds repeated and one-off values |
| Args / Kwargs | Function Signatures | Demonstrates variable-length arguments |
| Recursion | Function | Computes factorial of a number |
| Lambda | Anonymous Functions | Filters and doubles values using `map`/`filter` |

The goal is to demonstrate **functional programming fundamentals** through a clean, menu-driven interactive program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit |
| 📥 **Flexible Data Input** | Choose between sample data or manual entry |
| 📊 **Summary Statistics** | Length, Sum, Minimum, and Maximum via built-ins |
| 🧮 **Average Calculation** | Computes mean of the dataset |
| 🔍 **Duplicate Detection** | Identifies and lists repeated values |
| 🌟 **Unique Value Finder** | Lists values that occur exactly once |
| 📦 **`*args` Example** | Demonstrates variable positional arguments |
| 🗂️ **`**kwargs` Example** | Demonstrates variable keyword arguments |
| 🔁 **Recursion** | Calculates factorial recursively |
| λ **Lambda Filtering** | Filters and doubles data using `map`/`filter` |
| 🌐 **Global Variable Usage** | Updates a shared summary dictionary |
| 🔀 **Multiple Return Values** | Returns min, max, and average together |
| 🧱 **2D List Handling** | Accepts and sorts a matrix row-by-row |
| ↕️ **Sorting** | Ascending or descending sort of the dataset |
| 📖 **Docstring Viewer** | Displays the docstring of every function |
| ⚠️ **Invalid Input Handling** | Detects and reports invalid menu choices |

---

## 🏗️ Project Structure

```
📦 data-analyzer/
│
├── 📄 pr4.py                ← Main Python script (entry point)
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│   Display Main Menu         │  ← 15 Function-Based Options
└────────────┬────────────────┘
             │
     ┌───────┴────────────────────┐
     ▼                            ▼
┌─────────────┐          ┌──────────────────┐
│ Input Data  │          │ Analyze / Explore│
│ (Sample/    │          │ (Summary, Dupes, │
│  Manual)    │          │  Unique, Sort..) │
└──────┬──────┘          └────────┬─────────┘
       │                          │
       ▼                          ▼
┌─────────────┐          ┌──────────────────┐
│ Function    │          │ Function Concept │
│ Concepts    │          │ (Recursion,      │
│ (args/kwargs│          │  Lambda, 2D List)│
└──────┬──────┘          └────────┬─────────┘
       │                          │
       ▼                          ▼
┌─────────────────────────────────────┐
│      Print Result to Console        │
└────────────────┬────────────────────┘
                 │
                 ▼
         Loop Back to Menu
                 │
          (Choice: 15) Exit ✅
```

---

## 🔺 Part A — Core Data Functions

### 📝 1. Data Input & Summary

> Loads data either from a hardcoded sample list or manual user entry, then reports basic statistics using Python built-ins.

**Logic:**
```python
def input_data():
    global data
    ch = int(input("1.Sample Data\n2.Manual Data\nEnter choice: "))
    if ch == 1:
        data = [24, 10, 56, 78, 42, 91, 90]
    else:
        data = list(map(int, input("Enter numbers separated by space: ").split()))
```

**Sample Output:**
```
Data = [24, 10, 56, 78, 42, 91, 90]
Length = 7
Sum = 391
Minimum = 10
Maximum = 91
```

---

### 🔍 2. Duplicates & Unique Values

> Uses nested loops to identify which values repeat and which appear exactly once.

**Logic:**
```python
for i in range(len(data)):
    count = 0
    for j in range(len(data)):
        if data[i] == data[j]:
            count += 1
    if count > 1:
        print(data[i])   # Duplicate
```

---

### ↕️ 3. Sorting

> Sorts the dataset in ascending or descending order based on user choice.

**Logic:**
```python
if ch == 1:
    data.sort()
else:
    data.sort(reverse=True)
```

---

## 🔢 Part B — Advanced Function Concepts

### 📦 4. `*args` and `**kwargs`

> Demonstrates how Python functions can accept a variable number of positional and keyword arguments.

**Logic:**
```python
def show_values(*args):
    for i in args:
        print(i)

def show_summary(**kwargs):
    for k in kwargs:
        print(k, ":", kwargs[k])
```

---

### 🔁 5. Recursion — Factorial

> A classic recursive function that calls itself until it reaches the base case.

**Logic:**
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

**Sample Output:**
```
Enter Number: 5
Factorial = 120
```

---

### λ 6. Lambda, Map & Filter

> Uses anonymous lambda functions combined with `filter()` and `map()` to process the dataset.

**Logic:**
```python
ans = list(filter(lambda x: x > value, data))
doubled = list(map(lambda x: x * 2, data))
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🌐 `global` keyword | Updates the shared `summary` dictionary across functions |
| 🔀 Multiple Return Values | `return min(data), max(data), average()` |
| 🧱 2D Lists | Nested loops build and sort a row-based matrix |
| 📖 `__doc__` | Displays each function's docstring dynamically |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🔁 **While Loop** | Built-in | Infinite menu loop control |
| 🔂 **For Loop** | Built-in | Iteration for lists, duplicates, and 2D data |
| 🧮 **Built-in Functions** | `len`, `sum`, `min`, `max`, `sorted` | Statistical calculations |
| λ **Lambda / map / filter** | Built-in | Functional-style data transformations |
| 🌐 **Global Variables** | Built-in | Shared state across functions |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |

---

## 📈 Results & Insights

After running the program, the following outputs are produced:

- ✅ **Accurate Summary Statistics** — Length, Sum, Min, Max computed instantly
- 🔍 **Duplicate & Unique Detection** — Clearly separates repeated vs one-off values
- 🔁 **Working Recursion** — Factorial computed correctly for any valid input
- λ **Functional Filtering** — Lambda-based filtering and doubling of values
- 🧱 **2D List Support** — Matrix input, display, and row-wise sorting
- 🔁 **Persistent Menu** — Program loops back after every task until manually exited
- ⚠️ **Error Feedback** — Invalid choices trigger a clear "Invalid Choice" message

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Covers functions, recursion, args/kwargs in one project |
| 🔄 **Reusability** | Each analysis operation lives in its own reusable function |
| 📚 **Educational** | Reinforces core function-based programming concepts |
| 🖥️ **No Dependencies** | Runs with pure Python — no external libraries needed |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🧪 **Extensible** | Easy to add new analysis functions or menu options |
| 📖 **Readable Code** | Clear `if-elif-else` structure makes logic easy to follow |
| 🛡️ **Input Safety** | Empty-data checks prevent crashes on statistics functions |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Your Name Here

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)

> *"Every function starts with a single purpose — just like every program starts with a single line."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India \
**🛠️ Skills:** Python · Functions · Recursion · Lambda · CLI Applications

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🔁 [Real Python — Functions](https://realpython.com/defining-your-own-python-function/) — In-depth function tutorials
- λ [Real Python — Lambda](https://realpython.com/python-lambda/) — Lambda function guide
- 🔂 [GeeksForGeeks — Recursion](https://www.geeksforgeeks.org/recursion/) — Recursion examples
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and programming courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 07 July, 2026*

</div>

---

## 🔗 Project Links

- 🔗 [Link 1](https://drive.google.com/file/d/1ixbV076Va1gNITOQfk5OdPMYe4BJ0M_d/view?usp=drive_link)
- 🔗 [Link 2](https://drive.google.com/file/d/1i_I-3gatDjlUshCqZi-WdC5EjmOMaTFt/view?usp=drive_link)
