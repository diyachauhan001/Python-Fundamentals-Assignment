# Smallest Letter Greater than Target


def next_greatest_letter(letters, target):
    l = 0
    r = len(letters)

    while l < r:
        m = (l + r) // 2
        if letters[m] > target:
            r = m
        else:
            l = m + 1

    return letters[l % len(letters)]


letters = ["c","f","j"]
target = "a"

print(next_greatest_letter(letters, target))