python
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the dataset
dataset_path = "Daily Bulletins FEB 28.xlsx"
df = pd.read_excel(dataset_path)

# Data Cleaning and Preprocessing
df.columns = df.columns.str.strip()  # Remove leading/trailing whitespace
df['Last Close'] = pd.to_numeric(df['Last Close'], errors='coerce')
df['52 Week High'] = pd.to_numeric(df['52 Week High'], errors='coerce')
df['52 Week Low'] = pd.to_numeric(df['52 Week Low'], errors='coerce')

# Function to filter data by company and visualize 52-week high/low
def visualize_stock_performance(company_name):
    company_data = df[df['Company'] == company_name]
    if company_data.empty:
        print(f"No data found for company: {company_name}")
        return
    
    plt.figure(figsize=(10, 6))
    plt.bar(['52 Week Low', 'Last Close', '52 Week High'], [
        company_data['52 Week Low'].values[0],
        company_data['Last Close'].values[0],
        company_data['52 Week High'].values[0]
    ], color=['red', 'blue', 'green'])
    
    plt.title(f"Stock Performance of {company_name}")
    plt.xlabel("Metrics")
    plt.ylabel("Value")
    plt.show()

# Example use of the function
company_to_analyze = "Abu Dhabi Commercial Bank (ADCB)"
visualize_stock_performance(company_to_analyze)
