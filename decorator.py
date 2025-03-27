def my_decorator(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} Before calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{prefix} After calling {func.__name__}")
            return result
        return wrapper
    return decorator

@my_decorator("DEBUG:")
def greet(name):
    print(f"Hello, {name}!")

greet("John")