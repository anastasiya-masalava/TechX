import pandas as pd

df = pd.read_csv("datasets/new_df.csv")
new_dic={}
for cat in df["category"]:
    if cat not in new_dic:
        new_dic[cat]=1
    else:
        new_dic[cat]+=1
dic2 = {v: k for k, v in new_dic.items()}
new_list=list(dic2.keys())
new_list.sort()
new_list.reverse()
columns=[]
for i in range(2):
    columns.append(dic2[new_list[i]])
    print(new_dic[dic2[new_list[i]]])
print(columns)
new_df=pd.DataFrame(columns=["category", "funding", "country"])
index=0
country_list=["USA", "GBR", "CAN"]
for category in df["category"]:
    count = df["country"][index]
    if (category in columns) and (count in country_list):
        fund = df["funding"][index]
        new_df = new_df.append({'category': category, "funding": fund, "country": count}, ignore_index=True)
    index+=1
new_df = pd.concat([new_df, pd.get_dummies(new_df['country'])], axis = 1).drop(columns = ['country'])
new_df.to_csv("datasets/MLfile2.csv", index = False)