# 📦 Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🔄 Load the dataset
df = pd.read_csv("sales.csv")

# 👀 Display the first few rows
print(df.head())

# 🧹 Clean the data (remove nulls)
df = df.dropna()

# 💰 Total Sales
total_sales = df['Sales'].sum()
print("Total Sales: ₹", round(total_sales, 2))

# 📍 Sales by Region
sales_by_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Region:\n", sales_by_region)

# 📦 Best-Selling Product
best_seller = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(1)
print("\nBest Selling Product:\n", best_seller)

# 📅 Monthly Sales Trends (if 'Order Date' column exists)
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Month'] = df['Order Date'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Sales'].sum()

    plt.figure(figsize=(12,6))
    monthly_sales.plot(kind='line', marker='o', color='green')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 📊 Plot Sales by Region
plt.figure(figsize=(8,5))
sales_by_region.plot(kind='bar', color='skyblue')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
