def first_non_repeated_char(input_str):
    char_count = {}

    # Count occurrences of each character
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first non-repeated character
    for char in input_str:
        if char_count[char] == 1:
            return char

    # If no non-repeated character is found
    return None

# input string
print("Enter the string : ")
input_string = str(input())
result = first_non_repeated_char(input_string)

if result is not None:
    print(f"The first non-repeated character in '{input_string}' is: {result}")
else:
    print("No non-repeated character found.")
