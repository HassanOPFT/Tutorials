import openpyxl
import random

def read_excel_file(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(list(row))

    return data

def generate_random_malaysian_number():
    return '01{:08}'.format(random.randint(0, 99999999))

def main():
    # Read data from Excel file
    excel_data = read_excel_file('users.xlsx')

    # Prepare constant values
    email = 'hassan@fieldex.com'
    manager = 'machine@app.custella.com'
    role = 'STAFF'
    profile = 'Mstl'


    # Generate output data
    output_data = []

    header = 'firstName,lastName,email,userName,phone,manager,role,profile,geofence'
    output_data.append(header)

    for row in excel_data:
        first_name = row[0].strip() if row[0] else ''
        last_name = row[1].strip() if row[1] else ''
        user_name = row[2].strip() if row[2] else ''
        phone = generate_random_malaysian_number()

        output_data.append(f'{first_name},{last_name},{email},{user_name},{phone},{manager},{role},{profile},')

    # Write output to a new CSV file
    with open('output.csv', 'w') as output_file:
        output_file.write('\n'.join(output_data))

    print('Output written to output.csv')

if __name__ == "__main__":
    main()
