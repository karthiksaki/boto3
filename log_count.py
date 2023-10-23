import re

# Define the pattern you want to search for
pattern = input("Enter the pattern you want to search for: ")

# Initialize a count variable to keep track of the number of occurrences
count = 0

# Open a file for reading
with open("your_file.txt", "r") as file:
    # Read the contents of the file
    text = file.read()
    
    # Use the findall() function to find all occurrences of the pattern
    matches = re.findall(pattern, text)
    
    # Count the number of matches
    count = len(matches)

if count > 1:
    print(f"Pattern {pattern} found {count} times in the file.")
else:
    print(f"no matches found for {pattern}")

# Print the count of occurrences
# print(f"Pattern {pattern} found {count} times in the file.")
