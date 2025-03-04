"""
Super Simple Decorator Example
This shows the most basic concept of a decorator.
"""

# A simple decorator that adds a border around printed text
def add_border(func):
    def wrapper():
        print("**********")  # Print border before
        func()              # Run the original function
        print("**********")  # Print border after
    return wrapper

# Using the decorator
# @add_border
# def print_message():
#     print("Hello, World!")
def print_hello():
    print("Hello!")
print_hello = add_border(print_hello)

# Run the example
if __name__ == "__main__":
    # print_message()
    print_hello()