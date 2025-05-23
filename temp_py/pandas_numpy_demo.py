#!/usr/bin/env python3
# Simple demonstration of pandas and numpy

import numpy as np
import pandas as pd

# Create a numpy array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("NumPy Array:")
print(array)
print("\nArray shape:", array.shape)
print("Array sum:", np.sum(array))
print("Array mean:", np.mean(array))

# Create a pandas DataFrame
df = pd.DataFrame(array, columns=['A', 'B', 'C'])
print("\nPandas DataFrame:")
print(df)

# Basic pandas operations
print("\nDataFrame statistics:")
print(df.describe())

# Adding a new column based on calculation
df['D'] = df['A'] + df['B'] + df['C']
print("\nDataFrame with new column:")
print(df)

# Filter rows where column A > 2
filtered_df = df[df['A'] > 2]
print("\nFiltered DataFrame (A > 2):")
print(filtered_df)

# Group by example
df['category'] = ['X', 'Y', 'Z']
print("\nGrouped by category (mean):")
print(df.groupby('category').mean()) 