def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen_numbers = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen_numbers:
            pairs.append((num, complement))
        seen_numbers.add(num)

    return pairs

# Example usage:
print("Enter the size of the array: ")
n=int(input())
arr = []
print("Enter the target sum: ")
target_sum=int(input())
for i in range(n):
    print(f"Enter the {i+1} no element in the array: ")
    k=int(input())
    arr.append(k)
print(f"Enter the Kth value that should be less than equal to {n}: ")


result = find_pairs_with_sum(arr, target_sum)

if result:
    print(f"Pairs with sum {target_sum}: {result}")
else:
    print(f"No pairs found with sum {target_sum}")
