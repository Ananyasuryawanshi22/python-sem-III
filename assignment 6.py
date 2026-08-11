print("0/1 KNAPSACK PROBLEM")
print("--------------------")

print("\nItems:")
for i in range(len(weights)):
    print(
        f"Item {i + 1}: Weight = {weights[i]}, "
        f"Value = {values[i]}"
    )

print("\nKnapsack Capacity:", capacity)

# Bottom-Up
value1, items1, dp_table = knapsack_bottom_up(
    weights, values, capacity
)

print("\n--- Bottom-Up Approach ---")
print("Maximum Value:", value1)
print("Selected Items:", items1)

# Top-Down
value2, items2 = knapsack_top_down(
    weights, values, capacity
)

print("\n--- Top-Down Approach ---")
print("Maximum Value:", value2)
print("Selected Items:", items2)

