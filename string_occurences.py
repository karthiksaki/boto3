import re

existing_string = "karthik is in the us now he has taken a huge risk by resigning to the existing job that he was doing in bangalore.karthik is working as devops enginer where hs is supporting for tesobank"
custom_value = input("Enter any string to check if that exists or not:: ")
occurrences = re.findall(custom_value, existing_string, re.IGNORECASE)
count = len(occurrences)
print(f"'{custom_value}' exists {count} times in the text.")
