import json
from src.dfs import tao_ke,chay_dfs
rows=[]
for n in (5,20,50):
 r=chay_dfs(tao_ke(n,[(i,i+1) for i in range(1,n)]),1)
 rows.append({'n':n,'m':n-1,**r['dem']})
print(json.dumps(rows,ensure_ascii=False,indent=2))
