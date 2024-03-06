import time
from math import sqrt
from functools import reduce

#1
def multiply_list(lst):
    return reduce(lambda x, y: x*y, lst)

#2
def count_letters(s):
    upper, lower = sum(1 for char in s if char.isupper()), sum(1 for char in s if char.islower())
    return {"upper": upper, "lower": lower}

#3
def is_palindrome(s):
    return s == s[::-1]

#4
def calculate_square_root_after_delay(number, delay_ms):
    time.sleep(delay_ms / 1000.0) 
    result = sqrt(number)
    return f"Square root of {number} after {delay_ms} milliseconds is {result}"

#5
def all_true(t):
    return all(t)

test_list = [1, 2, 3, 4] #1
test_string = "Hello KBTU" #2
palindrome_test = "racecar" #3
tuple_test = (True, True, True) #5

#4
number = 25100
delay_ms = 2123

calculate_square_root_after_delay(number, delay_ms)

results = {
    "multiply_list": multiply_list(test_list),
    "count_letters": count_letters(test_string),
    "is_palindrome": is_palindrome(palindrome_test),
    "all_true": all_true(tuple_test),
}

results