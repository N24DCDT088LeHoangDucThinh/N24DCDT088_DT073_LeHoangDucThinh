import argparse,json,sys
from src.dfs import tao_ke,chay_dfs
p=argparse.ArgumentParser();p.add_argument('--example',type=int,choices=[1,2])
p.add_argument('--input');p.add_argument('--trace',action='store_true');p.add_argument('--case')
a=p.parse_args()
if a.case:
    from test.run_tests import run
    r=run(a.case);sys.exit(0 if r['passed']==r['total'] else 1)
try:
    if a.example==1:d={'n':4,'canh':[[1,2],[1,3],[2,4]],'s':1}
    elif a.example==2:d={'n':3,'canh':[[1,2],[2,3],[1,3]],'s':2}
    elif a.input:
        with open(a.input,encoding='utf-8') as f:d=json.load(f)
    else:
        n=int(input('Nhap n (1..100): '));m=int(input('Nhap so canh: '))
        if not 1<=n<=100 or not 0<=m<=n*(n-1)//2:raise ValueError('n hoặc số cạnh không hợp lệ')
        edges=[list(map(int,input(f'Canh {i+1} (u v): ').split())) for i in range(m)]
        d={'n':n,'canh':edges,'s':int(input('Nhap nguon s: '))}
    print('DT073 | Input:',d)
    ke=tao_ke(d['n'],d['canh']);r=chay_dfs(ke,d['s'],lan_vet=a.trace)
    print('Ke:',ke[1:]);print('DFS:',r['thu_tu'])
    print('Visited:',r['visited']);print('Cha:',r['cha']);print('Bo dem:',r['dem'])
    if a.trace:print('\n'.join(r['vet']))
except (ValueError,KeyError,OSError) as e:print('INPUT KHONG HOP LE:',e);sys.exit(2)
