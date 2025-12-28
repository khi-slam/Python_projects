import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. NUMPY: Generate synthetic data (50 random numbers)
# We use NumPy because it generates these numbers faster than standard Python
dates = pd.date_range("20230101", periods=50)
values = np.random.randn(50).cumsum() # Cumulative sum to show a trend

# 2. PANDAS: Organize into a DataFrame
# We give the data meaning (dates and column name)
df = pd.DataFrame({"Date": dates, "Stock_Value": values})

# Calculate a generic moving average using Pandas
df["Moving_Avg"] = df["Stock_Value"].rolling(window=5).mean()

# 3. MATPLOTLIB: Visualize the result
plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Stock_Value"], label="Raw Data", color="blue", alpha=0.5)
plt.plot(df["Date"], df["Moving_Avg"], label="5-Day Moving Avg", color="red", linewidth=2)

# Formatting the plot
plt.title("Simulated Data Analysis")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.grid(True)

# Display
plt.show()
