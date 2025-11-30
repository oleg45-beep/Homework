import pandas as pd
f = pd.read_csv("titanic.csv")
f['FamilySize'] = f['SibSp'] + f['Parch'] + 1
print(f.loc[888, 'FamilySize'])
#В первой программе указал по ошибке 887 вместо 888