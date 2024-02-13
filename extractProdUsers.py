import json

# Read the JSON file
with open('prodUsers.json', 'r') as file:
    data = json.load(file)

# Extract login values and write to a new text file
with open('login_values.txt', 'w') as output_file:
    for user_record in data:
        login_value = user_record.get('login')
        if login_value:
            output_file.write(f"{login_value},\n")

print("Login values have been extracted and saved to 'login_values.txt'.")
