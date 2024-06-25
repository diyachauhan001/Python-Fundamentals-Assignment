# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    try:
        number = int(input("Enter a positive integer: "))
        
        if number <= 0:
            print("Please enter a positive integer.")
        else:
            prime = is_prime(number)
        
            if prime:
                print(f"The number {number} is prime.")
            else:
                print(f"The number {number} is not prime.")
        
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "_main_":
    main()