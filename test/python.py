import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        
    def add_column(self, name, value):
        self.data[name] = value
        
    def compute_statistics(self):
        return self.data.describe()

data = {'A': np.random.randint(0, 100, 10), 'B': np.random.randint(0, 100, 10)}
processor = DataProcessor(data)
processor.add_column('C', np.random.randint(0, 100, 10))
print(processor.compute_statistics())

# Load data
df = pd.read_csv('data.csv')

# Data Cleaning
df.dropna(inplace=True)  # Drop rows with missing values

# Data Transformation
df['new_column'] = df['old_column'] * 2  # Add a new column based on an existing one

# Data Aggregation
grouped_df = df.groupby('category_column').mean()  # Group by a column and calculate the mean

# Data Filtering
filtered_df = df[df['value_column'] > 50]  # Filter rows based on a condition

# Saving the results
grouped_df.to_csv('grouped_data.csv')
filtered_df.to_csv('filtered_data.csv')

# Display results
print("Grouped Data:")
print(grouped_df)
print("\nFiltered Data:")
print
