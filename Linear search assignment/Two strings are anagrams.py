# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    char_count1 = {}
    char_count2 = {}
    
    for char in str1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1
    
    for char in str2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1
    
    return char_count1 == char_count2

def main():
    try:
        str1 = input("Enter the first string: ")
        str2 = input("Enter the second string: ")
        
        if are_anagrams(str1, str2):
            print(f'"{str1}" and "{str2}" are anagrams.')
        else:
            print(f'"{str1}" and "{str2}" are not anagrams.')
        
    except ValueError:
        print("Invalid input. Please enter valid strings.")

# if __name__ == "_main_":
main()