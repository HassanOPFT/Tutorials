#SCAN 2
def add_numbers(first, second):
    return first + second

def subtract_numbers(first, second):
    return first - second

def main():
    # Variable initialization
    First = 0
    Second = 0

    # Input for the first number
    print("Enter The First Number : ")
    First = int(input())

    # Input for the second number
    print("Enter The Second Number : ")
    Second = int(input())

    # Calculate sum using the add_numbers function
    Sum = add_numbers(First, Second)

    # Calculate subtraction using the subtract_numbers function
    Subtraction = subtract_numbers(First, Second)

    # Output the results
    print(f"The Sum Of {First} And {Second} Is : {Sum}")
    print(f"The Subtraction Of {First} And {Second} Is : {Subtraction}")

# Call the main function
main()
