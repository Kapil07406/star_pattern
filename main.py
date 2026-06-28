# Python program to print a hash (#) pattern based on the number of rows specified by the user

# Get the number of rows from user
rows = int(input("Enter the number of rows: "))

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop for each column in the row
    for j in range(i):
        # Print #, end with space instead of new line
        print('#', end=' ')
    # Move to the next line after each row
    print()