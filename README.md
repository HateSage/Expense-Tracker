# Expense Tracker

A simple command-line expense tracker built with Python. The application allows users to record their expenses, view their spending, calculate total expenses, analyze spending by category, delete expenses, and save their data using JSON.

## Features

- Add expenses
- View all expenses
- Calculate total spending
- View spending by category
- Delete expenses
- Save expenses to a JSON file
- Load saved expenses when the program starts
- Simple interactive command-line menu

## Technologies Used

- Python
- JSON
- File Handling
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements

## Data Structure

Each expense is stored as a Python dictionary:

```python
{
    "amount": 5000,
    "category": "Food",
    "description": "Lunch"
}
```

Multiple expenses are stored inside a list:

```python
expenses = [
    {
        "amount": 5000,
        "category": "Food",
        "description": "Lunch"
    },
    {
        "amount": 2000,
        "category": "Transport",
        "description": "Bus fare"
    }
]
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate into the project

```bash
cd expense-tracker
```

### 3. Run the program

```bash
python main.py
```

## Usage

When the program starts, you will see a menu:

```text
===== EXPENSE TRACKER =====
1. Add expense
2. View expenses
3. Total spending
4. Spending by category
5. Delete expense
6. Exit
```

Choose an option by entering the corresponding number.

### Add Expense

Enter:

- Amount
- Category
- Description

Example:

```text
Enter amount: 5000
Enter category: Food
Enter description: Lunch
```

### View Expenses

Displays all recorded expenses with their numbers, amounts, categories, and descriptions.

### Total Spending

Calculates the total amount spent across all recorded expenses.

### Spending by Category

Groups expenses by category and calculates how much was spent in each category.

Example:

```text
Food : 8000
Transport : 3500
Data : 2000
```

### Delete Expense

Select an expense by its displayed number and remove it from the tracker.

## Data Storage

Expenses are stored in:

```text
expenses.json
```

The JSON file allows the expenses to remain available after the program is closed and restarted.

Example:

```json
[
    {
        "amount": 5000,
        "category": "Food",
        "description": "Lunch"
    }
]
```

## Project Structure

```text
expense-tracker/
│
├── main.py
├── expenses.json
└── README.md
```

## Learning Objectives

This project was built to practice fundamental Python programming concepts, including:

- Variables and data types
- Lists
- Dictionaries
- `if` / `elif` / `else`
- `for` and `while` loops
- Functions
- Parameters and arguments
- Return values
- File handling
- JSON serialization and deserialization
- Basic program structure
- Command-line interaction

## Author

**Abdullahi**

Built as a Python learning project.
