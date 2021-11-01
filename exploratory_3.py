import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('clean_companies.csv')

minidf = df[['name', 'funding_total_usd']]
minidf = minidf[minidf['funding_total_usd'] < 5000000000]
minidf = minidf.dropna(axis=0, how='any')

print(df[df['funding_total_usd'] > 5000000000].count)

plt.hist(minidf["funding_total_usd"], bins=20)
plt.yscale('log')
plt.title('Distribution of Funding (Less than $5 Billion) Per Company (n>60,000)')
plt.xlabel('Funding (USD), Bin Size: $250 Million')
plt.ylabel('Number of Companies')
plt.show()


