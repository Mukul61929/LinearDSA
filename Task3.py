def are_strings_rotations(str1, str2):
    if len(str1) != len(str2):
        return False

    concatenated_str = str1 + str1

    # Check if str2 is a substring of concatenated_str
    if str2 in concatenated_str:
        return True
    else:
        return False

# Example
string1 = "abcde"
string2 = "cdeab"

if are_strings_rotations(string1, string2):
    print(f"{string1} and {string2} are rotations of each other.")
else:
    print(f"{string1} and {string2} are not rotations of each other.")
