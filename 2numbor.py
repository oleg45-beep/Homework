import pandas as pd
f = pd.read_csv("titanic.csv")
print(f.describe())
for i in ['Survived', 'Pclass', 'Sex', 'Embarked']:
    print(f[i].value_counts(), f[i].isnull().sum())
print(f[f["Sex"]=="male"].shape[0])
print(f[f["Pclass"]==1].shape[0])