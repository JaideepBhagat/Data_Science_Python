numbers = [5, 2, 9, 1, 5, 6]

# Sorting the list
sorted_numbers = sorted(numbers)

# Filtering out even numbers
filtered_numbers = [num for num in sorted_numbers if num % 2 != 0]

# Calculating the sum
sum_numbers = sum(filtered_numbers)

print(f"Sorted numbers: {sorted_numbers}")
print(f"Filtered numbers: {filtered_numbers}")
print(f"Sum of filtered numbers: {sum_numbers}")
