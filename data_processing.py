import pandas as pd

df = pd.read_csv("datasets/clean_companies.csv")

#rename columns
df.rename(columns={"homepage_url":"homepage", "category_list":"category", "funding_total_usd":"funding", "country_code":"country"}, inplace=True)
#drop useless columns
df = df.drop(['permalink', 'state_code', 'region', 'first_funding_at','last_funding_at'], axis = 1)
#replace empty values
df['funding'].fillna(df["funding"].mean(), inplace=True)#mean-imputaiton
df['founded_at'].fillna(method="backfill", inplace=True) #backfill-imputation
df['homepage'].fillna("Not found", inplace=True)
df['country'].fillna("Not found", inplace=True)
df['city'].fillna("Not found", inplace=True)

#create a new .csv file
df.to_csv("datasets/new_companies.csv", index = False)
