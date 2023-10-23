import re
# Input from the user
pattern = input("Enter the pattern to search for: ")
replacement = input("Enter the replacement string: ")
file_path = input("Enter the file name: ")
try:
    with open(file_path, 'r') as file:
        file_content = file.read()
    # Use re.sub to replace the pattern with the replacement
    modified_content = re.sub(pattern, replacement, file_content)
    # Open the file for writing and overwrite its content with the modified content
    with open(file_path, 'w') as file:
        file.write(modified_content)
    if modified_content == file_content:
        raise Exception(f"Pattern '{pattern}' not found in {file_path}")
    print(f"Pattern '{pattern}' replaced with '{replacement}' in {file_path}")
except FileNotFoundError:
    print(f"File {file_path} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
