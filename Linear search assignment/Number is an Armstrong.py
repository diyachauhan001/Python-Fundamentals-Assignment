# Function to check if a number is an Armstrong number
def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    sum_of_powers = sum(int(digit)**num_digits for digit in num_str)
    
    return sum_of_powers == number

def main():
    try:
        number = int(input("Enter a number to check if it's an Armstrong number: "))
        
        if is_armstrong_number(number):
            print(f"{number} is an Armstrong number.")
        else:
            print(f"{number} is not an Armstrong number.")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "_main_":
    main()