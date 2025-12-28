import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Define the data based on the table in the PDF
data = {
    'sex': ['male', 'female'],
    'monthly income': [96500, 91300],
    'annual income': [1158000, 1095600]
}

# 2. Create the DataFrame
df = pd.DataFrame(data)

# Print the DataFrame to verify (Optional)
# print(df)
# --- 3. MATPLOTLIB: Plotting the Grouped Bar Chart ---

# Set the width of the bars
bar_width = 0.4
# Set position of bars on X axis
r1 = np.arange(len(df['sex'])) # [0, 1] for male and female
r2 = [x + bar_width for x in r1]

plt.figure(figsize=(12, 6))

# Create 'annual income' bars (the long red ones)
plt.barh(r1, df['annual income'], color='red', height=bar_width, edgecolor='grey', label='annual income')

# Create 'monthly income' bars (the short blue ones, slightly offset)
# We plot the monthly bars at position r2
plt.barh(r2, df['monthly income'], color='blue', height=bar_width, edgecolor='grey', label='monthly income')

# Add values labels (Optional, but makes it look like the source)
for index, value in enumerate(df['monthly income']):
    plt.text(value + 10000, r2[index], str(value), color='black', va='center')

for index, value in enumerate(df['annual income']):
    # Place text just inside or next to the long bar
    plt.text(value - 150000, r1[index], str(value), color='white', va='center', ha='left', fontsize=10)


# Custom Y-axis (Sex labels)
plt.yticks([r + bar_width/2 for r in r1], df['sex'], fontsize=12)
plt.ylabel('sex', fontsize=14)

# Custom X-axis (Income values)
plt.xlabel('Income', fontsize=14)
plt.ticklabel_format(style='plain', axis='x') # Prevents scientific notation on X-axis

# Remove X-axis ticks (as in the original plot)
plt.xticks([0, 250000, 500000, 750000, 1000000], ['0', '250000', '500000', '750000', '1000000'])

# Add the legend at the top
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)

# Display the plot
plt.show()
