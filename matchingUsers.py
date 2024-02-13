def read_usernames_file(file_path):
    with open(file_path, 'r') as file:
        return [username.strip() for username in file.readlines()]

def search_and_write_occurrences(usernames, prod_users_file, output_file, output_users_file):
    with open(prod_users_file, 'r') as prod_file, open(output_file, 'w') as output, open(output_users_file, 'w') as output_users:
        matching_users = set()
        
        for line in prod_file:
            for username in usernames:
                if username in line:
                    matching_users.add(username)
                    output.write(f"Username '{username}' found in prodUsers.txt:\n{line}\n\n")

        # Write matching users to a new file
        output_users.write('\n'.join(matching_users))

def main():
    usernames_file = 'usernames.txt'
    prod_users_file = 'prodUsers.txt'
    output_file = 'search_results.txt'
    output_users_file = 'matching_users.txt'

    usernames = read_usernames_file(usernames_file)
    search_and_write_occurrences(usernames, prod_users_file, output_file, output_users_file)

    print('### Done ###')

if __name__ == "__main__":
    main()
