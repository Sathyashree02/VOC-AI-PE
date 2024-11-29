# Function to print multiplication table
def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Get user input
num = int(input("Enter a number: "))

# Print the multiplication table
print_multiplication_table(num)
