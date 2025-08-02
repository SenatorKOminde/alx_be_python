# pattern_drawing.py

# Prompt user for size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Loop through each row
while row < size:
    # Print one row of asterisks
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
