"""
Example of a decorator that takes parameters
"""

def repeat(times):  # This is the decorator factory
    def decorator(func):  # This is the actual decorator
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator

# @repeat(times=3)  # Pass parameter to decorator
def greet():
    print("Hello!")
greet = repeat(times=3)(greet)

if __name__ == "__main__":
    greet()  # Will print "Hello!" three times