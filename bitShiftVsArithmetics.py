import timeit

# Define test functions
def multiply():
    x = 1
    for _ in range(10**5):
        x *= 2

def bit_shift():
    x = 1
    for _ in range(10**5):
        x <<= 1

# Measure execution time
multiply_time = timeit.timeit(multiply, number=10)
bit_shift_time = timeit.timeit(bit_shift, number=10)

# Print results
print(f"Multiplication time: {multiply_time:.6f} seconds")
print(f"Bit shift time: {bit_shift_time:.6f} seconds")
print(f"Bit shift is {multiply_time / bit_shift_time:.2f} times faster")