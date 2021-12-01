import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("datasets/clean_companies.csv")
df = df[["category_list", "funding_total_usd", "country_code"]]
df.rename(columns={"category_list":"category", "funding_total_usd":"funding", "country_code":"country"}, inplace=True)
#df = df.dropna(axis=0, how = 'any')


newdf=pd.DataFrame(columns=["category", "funding", "country"])
index=0

for category in df["category"]:
    try:
        catList=category.split("|")
        if len(catList) == 1:
            fund = df["funding"][index]
            count=df["country"][index]
            newdf = newdf.append({'category':category, "funding":fund, "country":count}, ignore_index=True)
        else:
            fund = df["funding"][index]
            count = df["country"][index]
            for i in catList:
                newdf = newdf.append({'category': i, "funding": fund, "country":count}, ignore_index=True)

    except:
        pass
    index += 1
newdf = newdf.dropna(axis=0, how = 'any')
newdf.to_csv("datasets/new_df.csv", index = False)

