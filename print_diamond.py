# Define a function to print a diamond pattern with asterisks
def print_diamond():
    if n % 2 == 0:
        print("Please provide an odd integer.")
        return

    # Print the top half of the diamond
    for diamond in range(1, n, 2):
        print(" " * ((n - diamond) // 2) + "*" * diamond)

    # Print the middle row with all asterisks
    print("*" * n)

    # Print the bottom half of the diamond
    for diamond in range(n - 2, 0, -2):
        print(" " * ((n - diamond) // 2) + "*" * diamond)

# Get user input for n
try:
    n = int(input("Enter an odd integer: "))
    print_diamond()
except ValueError:
    print("Please provide a valid integer.")