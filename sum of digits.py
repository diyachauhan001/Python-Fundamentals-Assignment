# Function to find the sum of digits of a number
def sum_of_digits(number):
    number = abs(number)
    number_str = str(number)
    total = sum(int(digit) for digit in number_str)
    return total

def main():
    try:
        number = int(input("Enter an integer: "))
        
        total = sum_of_digits(number)
        
        print(f"The sum of the digits of {number} is {total}.")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "_main_":
    main()