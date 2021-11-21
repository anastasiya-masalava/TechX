import pandas as pd

df = pd.read_csv("clean_companies.csv")
df = df.drop(['permalink', 'state_code', 'region', 'first_funding_at','last_funding_at'], axis = 1)

df['funding_total_usd'].fillna(df['funding_total_usd'].mean(), inplace=True)

df.to_csv("new_companies.csv", index = False)

'''
string_data=str(df)
list_data=string_data.split(",")
print(list_data)
'''