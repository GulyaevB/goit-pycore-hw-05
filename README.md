# goit-pycore-hw-05

Homework 5 for the GoIT Python Core course: closures, generators, regular expressions and decorators.

Requires Python 3.9+ and nothing outside the standard library.

## Contents

| File | Task | What it shows |
|------|------|---------------|
| [hw1.py](hw1.py) | Fibonacci with caching | Closures, memoization |
| [hw2.py](hw2.py) | Summing income from text | Generators (`yield`), regex, higher-order functions |
| [hw4.py](hw4.py) | Console assistant bot | Decorators for error handling |

## Task 1: Caching Fibonacci (`hw1.py`)

`caching_fibonacci()` returns a `fibonacci(n)` function. The returned function computes the n-th Fibonacci number recursively and keeps the results in a `cache` dictionary held by the closure, so each value is calculated only once.

```python
from hw1 import caching_fibonacci

fib = caching_fibonacci()
fib(10)  # 55
fib(15)  # 610
```

Values of `n` that are 0 or less return `0`.

```bash
python hw1.py
```

## Task 2: Income generator (`hw2.py`)

- `generator_numbers(text)` yields every decimal number in `text` (for example `1000.01`) as a `float`. A number counts only when whitespace or the start or end of the string is on both sides of it.
- `sum_profit(text, func)` adds up all the numbers that `func` yields.

```python
from hw2 import generator_numbers, sum_profit

text = "Income: 1000.01 base, plus 27.45 and 324.00 extra."
sum_profit(text, generator_numbers)  # 1351.46
```

```bash
python hw2.py
# Загальний дохід: 1351.46
```

## Task 4: Assistant bot (`hw4.py`)

An interactive command-line contact book. Contacts are kept in memory only and are lost when the bot exits. Command names and contact names are case-insensitive, and names are stored in lowercase.

```bash
python hw4.py
```

| Command | Description |
|---------|-------------|
| `hello` | Greeting |
| `add <name> <phone>` | Add a contact, or overwrite an existing one |
| `change <name> <phone>` | Change the phone of an existing contact |
| `phone <name>` | Show a contact's phone |
| `all` | List all contacts |
| `exit` / `close` | Quit (Ctrl+C and Ctrl+D also work) |

The `@input_error` decorator turns exceptions from the command handlers into messages for the user, so bad input never crashes the bot:

| Exception | Message |
|-----------|---------|
| `ValueError` | `Give me name and phone please.` |
| `IndexError` | `Enter user name` |
| `KeyError` | `Contact not found.` |

Example session:

```text
Welcome to the assistant bot!
Enter a command: add John 1234567890
Contact added.
Enter a command: phone john
1234567890
Enter a command: change Bob 555
Contact not found.
Enter a command: add
Give me name and phone please.
Enter a command: all
john: 1234567890
Enter a command: exit
Good bye!
```
