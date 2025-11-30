import pandas as pd
f = pd.read_csv('titanic.csv')
print(f"{f[f['Survived'] == 1]['Age'].mean():.2f}") 
print(f"{f[f['Survived'] == 0]['Age'].mean():.2f}")