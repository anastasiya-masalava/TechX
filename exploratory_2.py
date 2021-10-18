import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("companies.csv")
df.head()
data_pie=df["country_code"].value_counts().rename_axis("country_code").reset_index(name="country_count")
plt.figure(figsize=(12,12))
plt.pie(data_pie.country_count, labels=data_pie.country_code, startangle=90, autopct='%.1f%%', textprops={'fontsize': 6})
plt.axis('equal')
plt.title("Companies by country")
plt.show()