import re
from typing import Callable, Generator

# Function to specify all real numbers in text(string) and to return them as generator
def generator_numbers(text: str):
    pattern = r"\d+\.*\d*"
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield number

# Function to sum the numbers after converting them to float
def sum_profit(text: str, func: Callable[[str], Generator[str, None, None]]) -> float:
    sum = 0
    for number in func(text):
        sum += float(number)
    return sum

# Input text for function check
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# Calculate total income
total_income = sum_profit(text, generator_numbers)

print(f"Total income: {total_income} usd")






#A little bit diferent code down here:

# import re
# from typing import Callable, Generator

# # Generator function to yield number strings
# def generator_numbers(text: str):
#     for match in re.finditer(r"\d+\.\d+", text):
#         yield match.group()

# # Function to sum the numbers after converting them to float
# def sum_profit(text: str, func: Callable):
#     return sum(float(num) for num in func(text))

# # Input text for function check
# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# # Calculate total income
# total_income = sum_profit(text, generator_numbers)

# print(f"Total income: {total_income}")