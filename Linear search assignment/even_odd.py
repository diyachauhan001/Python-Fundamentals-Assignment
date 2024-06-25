# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def check_sign(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

def main():
    try:
        number = float(input("Enter a number: "))
        
        even_odd = check_even_odd(number)
        
        sign = check_sign(number)
        

        print(f"The number {number} is {even_odd} and {sign}.")
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "_main_":
    main()