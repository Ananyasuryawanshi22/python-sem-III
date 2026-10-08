import numpy as np

arr = np.arange(1, 11)
print("Original Array:", arr)

first_five = arr[:5]
print("First 5 elements:", first_five)

middle_elements = arr[3:7]
print("Elements from index 3 to 6:", middle_elements)

step_elements = arr[::2]
print("Every second element:", step_elements)

reversed_arr = arr[::-1]
print("Reversed Array:", reversed_arr)

total_sum = np.sum(arr)     # or arr.sum()
mean_val  = np.mean(arr)    # or arr.mean()
max_val   = np.max(arr)     # or arr.max()
min_val   = np.min(arr)     # or arr.min()

print(f"Sum: {total_sum}")   # Output: 55
print(f"Mean: {mean_val}")   # Output: 5.5
print(f"Max: {max_val}")     # Output: 10
print(f"Min: {min_val}")     # Output: 1

scaled_arr = arr * 10
print("Array scaled by 10:", scaled_arr)

arr += 5
print("Original array after in-place addition of 5:", arr)
