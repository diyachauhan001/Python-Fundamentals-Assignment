# Function to check if a year is a leap year
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def main():
    try:
        year = int(input("Enter a year: "))
        
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
        
    except ValueError:
        print("Invalid input. Please enter a valid year.")

if __name__ == "_main_":
    main()