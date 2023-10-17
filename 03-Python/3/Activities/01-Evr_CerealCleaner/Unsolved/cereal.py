import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal_bonus.csv")
# We can also add conditional logic (if statements) to a list comprehension
july_temperatures = [87, 85, 92, 79, 106]
hot_days = []
for temp in july_temperatures:
    if temp < 90:
        hot_days.append(temp)
    print(hot_days)
    
    # We can also add conditional logic (if statements) to a list comprehension
july_temperatures = [87, 85, 92, 79, 106]
hot_days = []
for temp in july_temperatures:
    if temp > 80:
        hot_days.append(temp)
    print(hot_days)