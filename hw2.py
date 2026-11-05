import re


def generator_numbers(text):
    numbers = re.findall(r"\b\d+\.\d+\b", text)

    for number in numbers:
        yield float(number)


text = "Income includes 1000.01 and 27.45 and 324.00"

for number in generator_numbers(text):
    print(number)
