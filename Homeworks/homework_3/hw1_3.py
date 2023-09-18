"""
check_data function takes two parameters - path to a file and a list of functions (validators).
You should:
- read data from file data.txt
- validate each line according to rules. Each rule is a function, that performs some specific check
- write a report to txt file and return absolute path to that file. For each line you should report
it if it doesn't conform with at least one rule, plus add a reason - the name of a validator that
doesn't pass (if there are more than one failed rules, get the name of the first one that fails)

Valid line should have 5 elements in this order:
email, amount, currency, account, date

You should also implement at least two rules:
- validate_line should check if a line has 5 elements
- validate_date should check if a date is valid. In our case valid date will be anything that follows
the pattern DDDD-DD-DD (four digits - two digits - two digits). Date always exists in a line, even
if this line is corrupted in some other way.
Feel free to add more rules!

For example, input lines:
foo@example.com 729.83 EUR accountName 2021-01:0
bar@example.com 729.83 accountName 2021-01-02
baz@example.com 729.83 USD accountName 2021-01-02

check_data(filepath, [validate_date, validate_line])

output lines:
foo@example.com 729.83 EUR accountName 2021-01:0 validate_date
bar@example.com 729.83 accountName 2021-01-02 validate_line
"""
from typing import Callable, Iterable
import os
from datetime import datetime
import re


def validate_line(line: str) -> bool:
    words = line.split()
    if len(words) == 5 and validate_string_ord(words):
        return True
    else:
        return False


def validate_date(date: str) -> bool:
    splitted_line = date.split()
    if len(splitted_line) != 5:
        return False
    expected_date = splitted_line[4]
    if expected_date[0:4].isdigit() and expected_date[4] == '-' and expected_date[5:7].isdigit()  and \
            expected_date[7] == '-' and expected_date[8:10].isdigit() and len(expected_date) == 10:
        return True
    else:
        return False


"""
def validate_date(date: str) -> bool:
    words = date.split()
    try:
        datetime.strptime(words[-1], '%Y-%m-%d')
        return True
    except (ValueError, IndexError):
        return False
"""


def validate_string_ord(words: list) -> bool:
    return (is_email(words[0]) and
            len(words[2]) == 3 and
            words[2].isupper() and
            is_number(words[1]) and
            is_string(words[3]))


def is_email(email: str) -> bool:
    emailpattern = r"^[^@]+@[^@.]+\.[^@. ]+$"
    if bool(re.match(emailpattern, email)):
        return True
    else:
        return False


def is_number(number: str) -> bool:
    try:
        float(number)
        return True
    except ValueError:
        return False


def is_string(account: str) -> bool:
    try:
        str(account)
        return True
    except ValueError:
        return False


def check_data(filepath: str, validators: Iterable[Callable]) -> str:
    result_filepath = os.path.abspath("validation_result.txt")

    with open(filepath, 'r', encoding='utf-8') as file, open(result_filepath, 'w', encoding='utf-8') as result_file:
        for row in file.readlines():
            for val in validators:
                if not val(row):
                    result_file.write(f'{row.strip()} {val.__name__}\n')
                    break

    return result_filepath


"""
def check_data(filepath: str, validators: Iterable[Callable]) -> str:
    result = path.abspath(filepath)
    with open(filepath, 'r', encoding='utf-8') as file:
        for row in file.readlines():
            for val in validators:
                if not val(row):
                    result += f'\n{row.strip()} {val.__name__}'
                    break

    return result


#if __name__ == "__main__":
#    print(check_data('data.txt', [validate_line, validate_date]))

"""
if __name__ == "__main__":
    print(check_data('data.txt', [validate_line, validate_date]))
