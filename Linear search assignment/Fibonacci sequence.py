# Function to generate Fibonacci sequence
def generate_fibonacci(n):
    if n <= 0:
        return "The number of terms must be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence

def main():
    try:
        n = int(input("Enter the number of terms for the Fibonacci sequence: "))
        
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_sequence = generate_fibonacci(n)
        
            print(f"The first {n} terms of the Fibonacci sequence are: {fibonacci_sequence}")
        
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "_main_":
    main()