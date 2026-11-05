import re


def generator_numbers(text):
    numbers = re.findall(r"\b\d+\.\d+\b", text)
    return numbers


text = "Income includes 1000.01 and 27.45 and 324.00"

print(generator_numbers(text))
