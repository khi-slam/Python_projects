import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- 1. DATA SETUP: Generating synthetic data ---

months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
n_months = len(months)

# Synthetic Sales Data (DZD) - Fluctuating around 3.5 billion DZD
# Note: The PDF scale seems to suggest values close to 3.5e10 or 3.5e11. Using 10^10 for visualization clarity.
base_sales = np.array([35000000000, 34000000000, 36000000000, 38000000000,
                       34500000000, 34500000000, 37000000000, 34000000000,
                       35500000000, 35500000000, 34000000000, 38000000000])
# Add a small random noise
sales_dzd = base_sales + np.random.normal(0, 100000000, n_months)

# Synthetic Growth Data (%) - Small fluctuations around 0.02 (2%)
growth_pct = 1.0 + (sales_dzd / sales_dzd.mean() - 1) * 0.05 + np.random.normal(0, 0.005, n_months)
growth_pct = (growth_pct - 1) * 100 # Convert to actual percentage value (e.g., 2.1)

# 2. PANDAS: Organize into a DataFrame
df = pd.DataFrame({
    'Month': months,
    'Sales (DZD)': sales_dzd,
    'Growth (%)': growth_pct
})


# --- 3. MATPLOTLIB: Plotting the Combo Chart (Dual-Axis) ---

fig, ax1 = plt.subplots(figsize=(12, 6))

# Primary Y-axis (Left) for Sales (DZD)
color_sales = 'blue'
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales (DZD)', color=color_sales)

# Plot Sales as a shaded Area plot
ax1.fill_between(df['Month'], df['Sales (DZD)'], color=color_sales, alpha=0.3, label='Sales (DZD)')
# Plot the Sales line to define the top edge
ax1.plot(df['Month'], df['Sales (DZD)'], color=color_sales, linewidth=0.5)

# Format Sales Y-axis ticks to match the magnitude in the PDF
y_ticks = np.arange(0, 50000000000, 10000000000)
ax1.set_yticks(y_ticks)
ax1.ticklabel_format(style='plain', axis='y') # Avoids scientific notation

# Rotate X-axis labels for readability
plt.xticks(rotation=45, ha='right')
ax1.tick_params(axis='y', labelcolor=color_sales)


# Secondary Y-axis (Right) for Growth (%) - Must be created using twinx()
ax2 = ax1.twinx()
color_growth = 'red'
ax2.set_ylabel('Growth (%)', color=color_growth)

# Plot Growth as a Line plot
ax2.plot(df['Month'], df['Growth (%)'], color=color_growth, linewidth=2, label='Growth (%)')
ax2.tick_params(axis='y', labelcolor=color_growth)


# Final Formatting and Labels
plt.title('Sales (DZD) and Growth (%)', loc='left', fontsize=16)

# Create a combined legend (since Matplotlib doesn't do this automatically with twinx)
# Create proxy artists for the legend
from matplotlib.patches import Rectangle
area_legend = Rectangle((0, 0), 1, 1, fc='blue', alpha=0.3)
line_legend, = ax2.plot([], [], color='red', linewidth=2)

ax1.legend([area_legend, line_legend], ['Sales (DZD)', 'Growth (%)'], loc='upper right')

# Set tight layout to ensure labels fit
plt.tight_layout()
plt.show()
