import pandas as pd
import tkniz as tk
#keep the traning set in the same folder
out = [['a'],['b']]
ind = ['fintech', 'fin tech', 'medicine', 'education', 'edtech','ed tech', 'energy', 'sustainability', 'transportation', 'retial', 'ecommerce', 'entertairnment', 'social','non profit', 'agriculture', 'civil', 'manifacturing', 'engineering']
df = pd.read_excel('TrnSet.xlsx')
# print(df.iloc[0])
for i in range(566):
    for x in df.iloc[i]:
        ar = tk.tknxz(str(x).lower())
        print(ar)