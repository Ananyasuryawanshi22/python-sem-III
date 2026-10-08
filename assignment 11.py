import pandas as pd
import numpy as np

np.random.seed(42)

data = np.random.uniform(10, 100, size=10)
series = pd.Series(data, index=[f"Day {i}" for i in range(1, 11)])

print("--- Original Series ---")
print(series)

first_element = series.iloc[0]         
day_5_val = series.loc['Day 5']          
first_three = series.iloc[:3]           

print("\n--- Indexing Examples ---")
print(f"First element (iloc[0]): {first_element:.2f}")
print(f"Value at 'Day 5' (loc['Day 5']): {day_5_val:.2f}")
print("First 3 elements:\n", first_three.round(2))

above_50 = series[series > 50]

print("\n--- Filtering Example (Values > 50) ---")
print(above_50.round(2))

mean_val = series.mean()
median_val = series.median()
min_val = series.min()
max_val = series.max()

print("\n--- Statistical Summary ---")
print(f"Mean   : {mean_val:.2f}")
print(f"Median : {median_val:.2f}")
print(f"Min    : {min_val:.2f}")
print(f"Max    : {max_val:.2f}")

print("\n--- Pandas describe() Summary ---")
print(series.describe().round(2))