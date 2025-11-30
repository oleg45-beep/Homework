import pandas as pd
f = pd.read_csv('titanic.csv')
print(f['Age'].median())