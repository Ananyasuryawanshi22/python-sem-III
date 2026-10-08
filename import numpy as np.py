import numpy as np

temperatures = np.array([22.5, 24.0, 23.8, 25.1, 27.0, 26.5, 28.2, 26.0, 24.5, 23.0])

first_3 = temperatures[:3]
print("First 3 days:", first_3)

day_5_to_8 = temperatures[4:8]
print("Day 5 to Day 8:", day_5_to_8)

avg_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
total_temp = np.sum(temperatures)

print(f"\nAverage Temperature: {avg_temp:.2f}°C")
print(f"Maximum Temperature: {max_temp}°C")
print(f"Minimum Temperature: {min_temp}°C")
print(f"Total Temperature:   {total_temp:.2f}°C")

modified_temperatures = temperatures + 2

print("\nModified Temperatures (+2°C):", modified_temperatures)