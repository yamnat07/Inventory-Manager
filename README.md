# Inventory Manager

A console program, written in Python, for keeping track of stock in a small shop or store room. Products are grouped into categories (for example *pens* and *notebooks*), and each product has a quantity. Everything is saved in a JSON file, so the inventory is still there the next time you run the program.

It uses only Python's standard library, so there is nothing to install.

## Contents

- [Why I built this](#why-i-built-this)
- [Features](#features)
- [Requirements](#requirements)
- [How to run](#how-to-run)
- [The menu](#the-menu)
- [Example](#example)
- [What to expect when you use it](#what-to-expect-when-you-use-it)
- [How your data is stored](#how-your-data-is-stored)
- [How it handles problems](#how-it-handles-problems)
- [Testing](#testing)
- [Known limitations](#known-limitations)
- [Files in this repository](#files-in-this-repository)
- [How it was built](#how-it-was-built)
- [Ideas for the future](#ideas-for-the-future)

## Why I built this

I finished a Python course and started a 30-day plan of revision and practice. This project was part of that practice. I wanted a real program that reads and writes files, so I first learned how to work with JSON and CSV files, and then used JSON to store the inventory.

The first version kept its data inside a Python module and lost every change when the program closed. Moving the data into `products.json` made the changes permanent, and the program grew from there into a full menu with validation, cancel, and delete features.

## Features

- View the whole inventory, one category, or the quantity of a single product
- Update the quantity of a product (including setting it to 0 for "out of stock")
- Create a new category with its first product
- Add a new product to a category that already exists
- Delete a product or a whole category
- Type `cancel` at any prompt to stop the current task and go back to the menu
- Friendly messages for mistakes: empty input, unknown names, and quantities that are not valid numbers
- Input is cleaned up for you, so `  Pens `, `PENS` and `pens` all mean the same thing
- Changes are saved immediately, in a way that cannot leave the data file half-written

## Requirements

- Python 3 (developed and tested with Python 3.13; the code uses f-strings, so Python 3.6 or newer is needed)
- No extra libraries

## How to run

1. Put `inventory-manager.py` and `products.json` in the same folder.
2. Open a terminal **in that folder** and run:

```
python inventory-manager.py
```

(On some systems the command is `python3` instead of `python`.)

The program looks for `products.json` in the folder you run it from, so run it from the folder that contains the file. If the file is missing, the program will tell you and stop. It does not create the file for you.

## The menu

```
~~~~~~~~~~~~~~~~~~~~~~~~~
WELCOME TO THE INVENTORY
~~~~~~~~~~~~~~~~~~~~~~~~~
1.See Whole Inventory.
2.See a category.
3.See a product.
4.Update inventory.
5.Create a new category.
6.Delete a category/product.
7.Create a new Product.
8.Exit.
```

| Choice | What it does |
|--------|--------------|
| 1 | Prints every category with its products and quantities |
| 2 | Asks for a category and prints its products |
| 3 | Asks for a category and a product and prints the quantity available |
| 4 | Asks for a category, a product that already exists, and a new quantity, then saves it |
| 5 | Asks for a new category name, its first product and that product's quantity |
| 6 | Opens a small menu to delete either a whole category or a single product |
| 7 | Asks for an existing category, a new product name and its quantity, then saves it |
| 8 | Exits the program |

Choice 4 only changes products that already exist. To add a product that is not in the inventory yet, use choice 7 (or choice 5 for a brand-new category).

## Example

```
Enter your choice:4
Categories Available:
Notebooks
Pens
Pencils
Erasers
Enter the category:pens
Enter product`s name:blue
Enter quantity of product:abc
Enter a number for quantity!!
Enter quantity of product:-3
Product`s quantity must be 0 or greater!!
Enter quantity of product:75
Products updated successfully.
```

A full recorded session that goes through every feature, including cancelling and damaged-file cases, is in [`demo_session.txt`](demo_session.txt).

## What to expect when you use it

- **Every task starts with a reminder** that you can type `cancel` in any input line. Cancelling never changes your data and returns you to the menu.
- **Typing nothing** (just pressing Enter) never breaks anything. The program says what it expects and asks again.
- **Names are not case sensitive** and extra spaces are ignored.
- **Quantities must be whole numbers, 0 or greater.** Letters, decimals and negative numbers are refused with a message.
- **After a successful task** you are returned to the menu, so you can do something else straight away.
- **Your data is saved the moment a task succeeds.** There is no separate "save" step, and nothing is lost if you close the program afterwards.
- **The program reads the file again each time the menu comes back,** so the file is always the source of truth.

## How your data is stored

The inventory lives in `products.json`. It is a dictionary of categories, and each category is a dictionary of products and their quantities:

```json
{
    "notebooks": {
        "a4": 20,
        "a5": 15
    },
    "pens": {
        "blue": 50,
        "black": 40
    }
}
```

Things to know:

- Category and product names are stored in lowercase.
- Quantities are whole numbers, 0 or greater.
- The program changes `products.json` whenever you update, create or delete something. Keep a copy of the original if you want to go back to the starting data.
- If you edit the file by hand, keep the same structure (categories containing products containing whole-number quantities) and use lowercase names.

## How it handles problems

| Situation | What happens |
|-----------|--------------|
| You press Enter without typing anything | It tells you what is expected and asks again |
| A category or product does not exist | It says so and asks again (or type `cancel`) |
| A quantity is not a whole number, or is negative | It explains the rule and asks again |
| You try to create a category that already exists | It refuses, so existing products can never be overwritten by accident |
| You try to add a product that already exists in a category | It says so and asks for another name (use choice 4 to change its quantity) |
| `products.json` is missing | It prints "The Products file isn't found!" and exits |
| `products.json` is empty, broken, or not readable text | It prints "The Products file is Damaged!" and exits |
| The program is stopped while saving | Data is first written to a temporary file (`products.tmp`) and then swapped in, so `products.json` is never left half-written |

## Testing

I tested the program thoroughly by running the real program with scripted answers on copies of the data (so the real data was never touched), and checking what it printed and what it saved.

- [`checks_passed.txt`](checks_passed.txt) lists **every check the program passed, in plain language**: 102 numbered checks (menu, looking things up, updating, creating, deleting, saving, cancel at every prompt, empty inventory, missing and damaged files, and the new-product feature), 5 save-safety tests where the program was stopped on purpose in the middle of saving, and 500 random sessions.
- [`demo_session.txt`](demo_session.txt) is a recorded run of the program that shows each feature working, with the answers typed shown after each prompt.

The same file also lists the things the checks do **not** cover, so you know the limits.

## Known limitations

- Deleting the last product in a category leaves the category in the file, empty.
- Products cannot be renamed. To fix a typo, add the correct product and delete the wrong one.
- Choice 4 (update) does not offer to create a product that does not exist. Use choice 7 for that. I kept them separate on purpose, to keep the program simple.
- The program expects `products.json` to have the structure shown above. If you edit the file by hand and break that structure, the program may stop with an error.
- Quantities have no upper limit, and Python's number rules apply, so a few unusual spellings such as `+5` or `1_000` are accepted.
- Pressing Ctrl+C or closing the terminal in the middle of a prompt ends the program with Python's standard message.
- It has been tested with Python 3.13 only.

## Files in this repository

| File | Purpose |
|------|---------|
| `inventory-manager.py` | The program |
| `products.json` | The inventory data (sample data included) |
| `README.md` | This file |
| `checks_passed.txt` | Plain-language list of every check the program passed |
| `demo_session.txt` | A recorded run through every feature |

## How it was built

The program is a set of small functions, one for each task, and a `menu()` that loads the data and calls them. Each function receives the data as a parameter and saves it through one shared `save_data()` function.

The main things I practised:

- Reading and writing JSON files (`json.load` and `json.dump`)
- Nested dictionaries
- Input validation with nested loops, `break` and `continue`
- Splitting a program into functions that share data
- Handling errors with `try` / `except`
- Writing files safely with a temporary file and `os.replace`
- Testing a program by feeding it scripted answers

I wrote the program step by step. Claude, an AI assistant, reviewed my code, tested it, and suggested fixes along the way. A few small pieces, such as the starter data and the safe-saving function, came from those suggestions. How the program should behave was my decision.

## Ideas for the future

- Rename products and categories
- Remove a category automatically when its last product is deleted
- Offer to create a missing product directly from the update task
- Warn about low stock
- Export the inventory to a CSV file
- Search for a product across all categories
