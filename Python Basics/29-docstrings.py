# Python Docstrings are the string literals that appear right after the definition of a function, method, class, or module.
# Docstring would be at right after the definition of a function.

def square(n):
    """Takes in a number n, returns the square of n"""  # Docstring
    print(n**2)

square(5)
print(square.__doc__)