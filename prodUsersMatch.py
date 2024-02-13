# Read username values from 'usernames.txt'
with open('usernames.txt', 'r') as usernames_file:
    usernames = [username.strip() for username in usernames_file.readlines()]

# Read login values from 'login_values.txt'
with open('login_values.txt', 'r') as login_values_file:
    login_values = [login_value.strip() for login_value in login_values_file.readlines()]

# Find matching usernames
matching_usernames = set(usernames) & set(login_values)

# Write matching usernames to 'matchingUsersProd.txt'
with open('matchingUsersProd.txt', 'w') as matching_users_file:
    for username in matching_usernames:
        matching_users_file.write(f"{username}\n")

print("Matching usernames have been written to 'matchingUsersProd.txt'.")
