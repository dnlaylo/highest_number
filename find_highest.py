# Method for finding the highest number
def find_highest(entries):
    # Assume that the first entry is the highest
    highest = entries[0]
    # A loop that compares each entry to "highest" using an if statement
    for num in entries:
        if num > highest:
            # Reassign the current highest number
            highest = num
    # Return the highest number
    return highest
# Prompt the user to put their number entries
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
num5 = float(input("Enter number 5: "))
# A list to store all entries
# Call the method that finds the highest number
# Print the highest number