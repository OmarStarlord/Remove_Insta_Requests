import json
import csv

# Load the JSON file
with open('pending_follow_requests.json', 'r') as file:
    data = json.load(file)

# Initialize an empty array to store the usernames
usernames = []

# Iterate through the relationships_follow_requests_sent
for entry in data.get('relationships_follow_requests_sent', []):
    # Extract the usernames from string_list_data
    for item in entry.get('string_list_data', []):
        usernames.append(item['value'])

# Define the CSV file name
csv_file = 'usernames.csv'

# Write the usernames to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Username'])  # Write the header
    for username in usernames:
        writer.writerow([username])  # Write each username in a new row

print(f"Usernames successfully saved to {csv_file}")
