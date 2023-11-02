import ctypes

# Load the shared library
add = ctypes.CDLL('./add.so')

# Define the argument types and return type of the Add function
add.Add.argtypes = [ctypes.c_int64, ctypes.c_int64]
add.Add.restype = ctypes.c_int64

# Call the Add function with first two arguments given
# by the user and print the result
# python add.py 1 2
# 3
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
result = add.Add(a, b)
print(result)  # Outputs: 3
