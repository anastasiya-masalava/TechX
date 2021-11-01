import pandas as pd

df = pd.read_csv("companies.csv")
df = df.drop(['permalink', 'state_code', 'region', 'first_funding_at','last_funding_at'], axis = 1)

#mini_df['Age'].fillna(mini_df['Age'].mean(), inplace=True)


string_data=str(df)
list_data=string_data.split(",")
print(list_data)