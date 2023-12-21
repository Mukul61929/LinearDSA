def reverse_array_in_place(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        # Swap elements at start and end indices
        arr[start], arr[end] = arr[end], arr[start]

        # Move indices towards the center
        start += 1
        end -= 1

# Example usage:
print("Enter the length of the array: ")
n=int(input())
my_array = []
for i in range(n):
    print(f"Enter the {i+1} no element in the array: ")
    k=int(input())
    my_array.append(k)

print("Original Array:", my_array)

reverse_array_in_place(my_array)
print("Reversed Array:", my_array)
