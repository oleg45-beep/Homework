import pandas as pd
f = pd.read_csv('titanic.csv')
print(f"{f[f['Pclass'] == 1]['Fare'].mean():.2f}")
print(f"{(f[f['Pclass'] == 3]['Survived'].sum() / f[f['Pclass'] == 3].shape[0] * 100):.2f}")