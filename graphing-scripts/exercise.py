import argparse
import pandas as pd
import matplotlib.pyplot as plt

# Define command-line arguments
parser = argparse.ArgumentParser(description='Generate a performance graph from a CSV file.')
parser.add_argument('csv_file', type=str, help='Path to the CSV file containing exercise data')
parser.add_argument('column_name', type=str, help='Name of the exercise column')
args = parser.parse_args()

# Read CSV file
csv_file = args.csv_file
df = pd.read_csv(csv_file)

# Select data for the specified exercise column
exercise_column = args.column_name
exercise_data = df[['Week#', exercise_column]]

# Convert non-numeric values to zero
for index, value in enumerate(exercise_data[exercise_column]):
    try:
        numeric_value = float(value)
        exercise_data.loc[index, exercise_column] = numeric_value
    except ValueError:
        exercise_data.loc[index, exercise_column] = 0

# Create a line plot using Matplotlib
plt.figure(figsize=(12, 6))
plt.plot(exercise_data['Week#'], exercise_data[exercise_column], marker='o')
plt.title(f'Performance on {exercise_column} Across Weeks')
plt.xlabel('Week')
plt.ylabel(exercise_column)
plt.xticks(rotation=45, ha='right')

# Save the plot as a PNG image
plt.tight_layout()
plt.savefig(f'{csv_file.replace(".csv", "")}_{exercise_column.lower()}.png')

# Show the plot
plt.show()
