import pandas as pd
f = pd.read_csv('titanic.csv')
print(len(f[(f['Sex'] == 'female') & (f['Pclass'] == 1) & (f['Survived'] == 1)]))  
print(len(f[(f['Age'] < 18) & (f['Parch'] == 0)]))