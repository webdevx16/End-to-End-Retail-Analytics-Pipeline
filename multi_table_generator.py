import pandas as pd
import numpy as np

np.random.seed(101)
num_sales = 250

#(Dimensiln Table)
products_data = {
    'ProductID': [101, 102, 103, 104, 105, 106, 107, 108],
    'ProductName': ['Alpha Wireless Laptop', 'Ergo Optical Mouse', '4K UltraWide Monitor', 
                    'Mechanical Backlit Keyboard', 'Noise-Canceling Headphones', 
                    'USB-C Multi-Port Hub', 'HD Stream Webcam', 'Ergonomic Desk Chair'],
    'Category': ['Computers', 'Accessories', 'Displays', 'Accessories', 'Audio', 'Accessories', 'Audio', 'Furniture'],
    'SubCategory': ['Hardware', 'Peripherals', 'Hardware', 'Peripherals', 'Peripherals', 'Connectivity', 'Peripherals', 'Office'],
    'CostPrice': [800, 20, 240, 50, 90, 15, 45, 150],
    'RetailPrice': [1200, 45, 350, 95, 175, 35, 89, 299]
}
df_products = pd.DataFrame(products_data)

#(Dimension Table)
customers_data = {
    'CustomerID': [501, 502, 503, 504, 505, 506, 507, 508],
    'CustomerName': ['Aarav Sharma', 'Diya Patel', 'Kabir Singh', 'Isha Gupta', 'Rohan Das', 'Ananya Reddy', 'Vivaan Kapoor', 'Meera Nair'],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Kolkata', 'Chennai', 'Pune', 'Ahmedabad'],
    'State': ['DL', 'MH', 'KA', 'TG', 'WB', 'TN', 'MH', 'GJ'],
    'CustomerTier': ['Platinum', 'Gold', 'Silver', 'Gold', 'Platinum', 'Silver', 'Silver', 'Gold'],
    'SignupDate': pd.date_range(start='2024-01-15', periods=8, freq='ME').date
}
df_customers = pd.DataFrame(customers_data)

#(Fact Table)
sales_data = {
    'SalesID': [f"TXN-{i:04d}" for i in range(1, num_sales + 1)],
    'ProductID': np.random.choice(products_data['ProductID'], size=num_sales),
    'CustomerID': np.random.choice(customers_data['CustomerID'], size=num_sales),
    'UnitsSold': np.random.choice([1, 2, 3, 5], size=num_sales, p=[0.5, 0.3, 0.15, 0.05]),
    'DiscountRate': np.random.choice([0.0, 0.05, 0.10, 0.15], size=num_sales, p=[0.6, 0.2, 0.1, 0.1]),
    'OrderDate': pd.date_range(start='2026-01-01', periods=num_sales, freq='h').date, # Hourly timestamps simulated across days
    'ShippingStatus': np.random.choice(['Delivered', 'Shipped', 'Processing', 'Cancelled'], size=num_sales, p=[0.75, 0.15, 0.07, 0.03]),
    'PaymentMethod': np.random.choice(['Credit Card', 'UPI', 'NetBanking', 'Cash'], size=num_sales)
}
df_sales = pd.DataFrame(sales_data)

df_sales.loc[np.random.choice(df_sales.index, size=12, replace=False), 'ShippingStatus'] = np.nan

df_products.to_csv('dim_products.csv', index=False)
df_customers.to_csv('dim_customers.csv', index=False)
df_sales.to_csv('fact_sales.csv', index=False)

print(" Mega Relational Architecture generated flawlessly! 250 high-complexity rows created.")