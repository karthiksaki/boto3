import re
import os

# Prompt the user for the directory and log file name
directory = input("Enter the directory path where the log file is located: ")
log_file = input("Enter the name of the log file: ")

# Combine the directory and log file path
log_file_path = os.path.join(directory, log_file)

# Define the pattern you want to search for
pattern = r"500"  # Change the pattern to the desired error code

# Initialize a count variable to keep track of the number of occurrences
count = 0

# Check if the specified log file exists
if os.path.exists(log_file_path):
    # Open the log file for reading
    with open(log_file_path, "r") as file:
        # Read the contents of the file
        text = file.read()
        
        # Use the findall() function to find all occurrences of the pattern
        matches = re.findall(pattern, text)
        
        # Count the number of matches
        count = len(matches)

    # Print the count of occurrences
    print(f"Pattern '{pattern}' found {count} times in the log file.")
else:
    print(f"The specified log file '{log_file_path}' does not exist.")
