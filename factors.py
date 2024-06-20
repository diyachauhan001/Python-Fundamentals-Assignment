# Function to find the factors of a given number
def find_factors(number):
    if number <= 0:
        return "Factors are only defined for positive integers."
    
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def main():
    try:
        number = int(input("Enter a positive integer: "))
        
        if number <= 0:
            print("Please enter a positive integer.")
        else:
            factors = find_factors(number)
        
            print(f"The factors of {number} are: {factors}")
        
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "_main_":
    main()