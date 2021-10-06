import pandas as pd
df = pd.read_csv('List of SP 500 companies.csv')
print(df[df["Sector"] == "Information Technology"])