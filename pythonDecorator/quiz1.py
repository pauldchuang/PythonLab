

def add_nono(func):
    def wrapper():
        print("NONO")
        func()
        print("NONO")
    return wrapper

@add_nono
def print_hi():
    print("Hi!")
if __name__ == "__main__":
    print_hi()