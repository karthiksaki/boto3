import re
import pandas as pd
# Sample log data (you would replace this with actual log data)
log_data = """
2023-03-15 08:15:22 INFO: Application started
2023-03-15 08:20:10 ERROR: Critical error in moduleA
2023-03-15 08:22:45 DEBUG: Request received from 192.168.1.100
2023-03-15 08:25:30 INFO: Application shutdown
"""
# Define regular expressions to extract relevant information
timestamp_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
log_level_pattern = r'INFO|ERROR|DEBUG'
message_pattern = r': (.+)'
# Initialize lists to store extracted data
timestamps = []
log_levels = []
messages = []
# Extract data using regular expressions
for line in log_data.strip().split('\n'):
    match = re.match(f'({timestamp_pattern}) ({log_level_pattern}){message_pattern}', line)
    if match:
        timestamp, log_level, message = match.groups()
        timestamps.append(timestamp)
        log_levels.append(log_level)
        messages.append(message)
# Create a Pandas DataFrame to work with the data
log_df = pd.DataFrame({
    'Timestamp': timestamps,
    'Log Level': log_levels,
    'Message': messages
})
# Summarize log data
log_summary = log_df.groupby('Log Level').count()
# Print the log summary
print(log_summary)
