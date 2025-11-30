import pandas as pd
f = pd.read_csv("titanic.csv")
print(f[f["Survived"]==1].shape[0])
print(f"{(f[f["Survived"]==1].shape[0]/len(f["Survived"]))*100:.4}")
print(f"{f[f['Sex']=='male']['Survived'].sum()*100/f[f['Sex']=='male'].shape[0]:.2f}")
print(f"{f[f['Sex']=='female']['Survived'].sum()*100/f[f['Sex'] == 'female'].shape[0]:.2f}")