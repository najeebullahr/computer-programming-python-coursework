# -*- coding: utf-8 -*-
"""
Created on Mon May 19 14:20:21 2025

@author: NuR
"""

# Open and read the file at F:\spyder\my_data.txt
with open(r"F:\spyder\my_data.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)

# Opening a file for reading line by line
with open(r"F:\spyder\my_data.txt", 'r') as file:
    for line in file:
        # Process each line
        print(line.strip())  # Removes leading/trailing whitespace
with open(r"F:\spyder\basic_text.txt", "w") as file:
    file.write("This is a simple string.\n")
    file.write("Written to a text file.\n")
# List of fruits
data = ['mango', 'orange', 'grapes']

# Writing list to a text file (one item per line)
with open(r'F:\spyder\fruits.txt', 'w') as file:
    for item in data:
        file.write(f"{item}\n")  # Each fruit on a new line

# Tuple of numbers
numbers = (1, 2, 3, 4, 5)

# Writing tuple to a text file as comma-separated string
with open(r'F:\spyder\numbers.txt', 'w') as file:
    file.write(','.join(map(str, numbers)))  # "1,2,3,4,5"
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['London', 'Paris', 'New York']
}

df = pd.DataFrame(data)

# Write to CSV (without row indices)
df.to_csv(r'F:\spyder\output.csv', index=False)

print("CSV file 'output.csv' created successfully.")

import csv

# === Reading a CSV File ===
try:
    with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader, None)  # Read the header row
        print('Header:', header)
        for row in reader:
            print('Row:', row)
except FileNotFoundError:
    print("Error: 'data.csv' file not found.")

# === Writing to a CSV File ===
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'London'],
    ['Peter', '32', 'France'],
    ['Lin', '24', 'China'],
    ['Nishida', '24', 'Japan']
]

with open('Your_Output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    print("\nData successfully written to 'Your_Output.csv'")
    
    import csv

# === Reading a CSV File ===
try:
    with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader, None)  # Read the header row
        print('Header:', header)
        for row in reader:
            print('Row:', row)
except FileNotFoundError:
    print("Error: 'data.csv' file not found.")

# === Writing to a CSV File ===
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'London'],
    ['Peter', '32', 'France'],
    ['Lin', '24', 'China'],
    ['Nishida', '24', 'Japan']
]

with open('Your_Output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    print("\nData successfully written to 'Your_Output.csv'")

