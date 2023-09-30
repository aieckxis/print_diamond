# Define a function to print a diamond pattern with asterisks
def print_diamond():
    if n % 2 == 0:
        return "Please provide an odd integer."

    # Print the top half of the diamond
    for diamond in range(1, n, 2):
        print(" " * ((n - diamond) // 2) + "*" * diamond)

    # Print the middle row with all asterisks

    # Print the bottom half of the diamond
    for diamond in range(n - 2, n, -2):
        print(" " * ((n - diamond) // 2) + "*" * diamond)

# Test the function with n = 5
n = 5
print_diamond()
