#convert string to binary string via utf-8
string = "This is a string."
print(f"string: {string}")
binary_string = string.encode('utf-8')
print("This string becomes a binary string")
print(f"binary string: {binary_string}")

#convert binary string to string via utf-8, some unprintable byte will be ommitted, like `\x01`
binary_string = b'Hello\x01World'
print(f"binary string: {binary_string}")
print("This binary string becomes a string")
string = binary_string.decode('utf-8')
print(f"string: {string}")
