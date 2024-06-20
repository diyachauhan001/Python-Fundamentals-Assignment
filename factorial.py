# Function to calculate the factorial of a number
def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

def main():
    try:
        number = int(input("Enter a non-negative integer: "))
        
        if number < 0:
            print("Please enter a non-negative integer.")
        else:
            fact = factorial(number)
        
            print(f"The factorial of {number} is {fact}.")
        
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")

if __name__ == "_main_":
    main()