import argparse
import pandas as pd
import matplotlib.pyplot as plt

# Define command-line arguments
parser = argparse.ArgumentParser(description='Generate a performance graph from a CSV file.')
parser.add_argument('csv_file', type=str, help='Path to the CSV file containing exercise data')
parser.add_argument('row_name', type=str, help='Name of the row to visualize')
args = parser.parse_args()

# Read CSV file
csv_file = args.csv_file
df = pd.read_csv(csv_file)

# Select data for the specified row
row_name = args.row_name
row_data = df[df['Week#'] == row_name]

# Extract exercise names and values
exercise_names = list(row_data.columns)[1:]
exercise_values = row_data.iloc[0, 1:]

# Convert non-numeric values to zero
exercise_values_numeric = []
for value in exercise_values:
    try:
        numeric_value = float(value)
        exercise_values_numeric.append(numeric_value)
    except ValueError:
        exercise_values_numeric.append(0)

# Create a bar plot using Matplotlib
plt.figure(figsize=(12, 6))
plt.bar(exercise_names, exercise_values_numeric)
plt.title(f'Exercise Values for {row_name}')
plt.xlabel('Exercises')
plt.ylabel('Values')
plt.xticks(rotation=45, ha='right')

# Save the plot as a PNG image
plt.tight_layout()
plt.savefig(f'{csv_file.replace(".csv", "")}_{row_name.lower()}.png')

# Show the plot
plt.show()
