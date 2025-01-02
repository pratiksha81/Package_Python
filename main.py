# Importing functions from the utils package
from utils.string_utils import reverse_string, capitalize_words
from utils.math_utils import add, multiply

# Using functions from string_utils
print(reverse_string("hello world"))  # Output: "dlrow olleh"
print(capitalize_words("python programming"))  # Output: "Python Programming"

# Using functions from math_utils
print(add(5, 3))  # Output: 8
print(multiply(4, 7))  # Output: 28
