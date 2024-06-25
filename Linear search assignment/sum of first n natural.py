# Function to calculate the sum of the first N natural numbers
def sum_of_natural_numbers(N):
    if N < 1:
        return 0
    return N * (N + 1) // 2

def main():
    try:
        N = int(input("Enter a positive integer N: "))
        
        if N <= 0:
            print("Please enter a positive integer.")
        else:
            sum_n = sum_of_natural_numbers(N)
        
            print(f"The sum of the first {N} natural numbers is {sum_n}.")
        
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "_main_":
    main()