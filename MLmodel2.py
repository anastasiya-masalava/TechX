from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import tree
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("datasets/MLfile2.csv")
df.replace(to_replace="Software", value=0, inplace=True, limit=None, regex=False, method='pad')
df.replace(to_replace="Mobile", value=1, inplace=True, limit=None, regex=False, method='pad')

X = df.drop(columns = ['category'])
y = df['category']

# train test splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle = True)

print('Training set shape: ', X_train.shape)
print('Testing set shape: ', X_test.shape)

# Standard Scale the data such that each column has mean 0 and variance 1
scaler = StandardScaler()
# Don't cheat - fit only on training data
scaler.fit(X_train)
X_train = scaler.transform(X_train)
# apply same transformation to test data
X_test = scaler.transform(X_test)

print(X_train)
print(X_train.shape)

pca = PCA(n_components=2)
pca.fit(X_train)
X_train2D = pca.transform(X_train)
X_test2D = pca.transform(X_test)

f, axarr = plt.subplots(1, 2, sharex='col', sharey='row', figsize=(10, 5))
for i in range(2):
    axarr[0].scatter(X_train2D[y_train == i, 0], X_train2D[y_train == i, 1], label=str(i))

    axarr[0].legend()
    axarr[0].set_title('Training data')

    axarr[1].scatter(X_test2D[y_test == i, 0], X_test2D[y_test == i, 1], label=str(i))

    axarr[1].legend()
    axarr[1].set_title('Testing data')



# decision tree classifier
clf_tree = tree.DecisionTreeClassifier(max_leaf_nodes = 8) #limits amount of leafs nodes
clf_tree.fit(X, y)  #fitting to the data
#clf_tree.fit(X_train, y_train)

plt.figure(figsize = (5, 3))
tree.plot_tree(clf_tree,filled = True,fontsize=10,feature_names = ["funding", "CAN", "GBR", "USA"])
plt.show()