"""Run independent named cases; each check is counted separately from case count."""
import argparse, hashlib, json, platform, sys
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
CASES = json.loads((ROOT/'test/cases.json').read_text(encoding='utf-8'))

class Checks:
    def __init__(self): self.count = 0
    def equal(self, actual, expected):
        self.count += 1
        if actual != expected:
            raise AssertionError(f'actual={actual!r}; expected={expected!r}')
    def true(self, value): self.equal(bool(value), True)


from src.dfs import tao_ke, chay_dfs

def reachable_oracle(n, edges, s):
    # Đối chứng điểm cố định trên danh sách cạnh; không gọi DFS đang kiểm.
    reached={s}
    while True:
        before=len(reached)
        for u,v in edges:
            if u in reached or v in reached: reached.update((u,v))
        if len(reached)==before:return reached

def evaluate(c,t):
    def execute():return chay_dfs(tao_ke(c['n'],c['canh']),c['s'])
    if c.get('error'):
        try:execute()
        except ValueError as e:t.true(True);return f'ValueError: {e}'
        raise AssertionError('Không từ chối input sai')
    ke=tao_ke(c['n'],c['canh'])
    if c['op']=='reset':chay_dfs(ke,1)
    r=chay_dfs(ke,c['s']);a=r['thu_tu']
    if c['op']=='parents':t.equal(r['cha'],c['expected'])
    else:t.equal(a,c['expected'])
    reached=reachable_oracle(c['n'],c['canh'],c['s'])
    t.equal(set(a),reached);t.equal(len(a),len(set(a)))
    t.equal(r['visited'],[i in reached for i in range(1,c['n']+1)])
    t.equal(r['dem']['so_dinh_tham'],len(reached))
    t.equal(r['dem']['so_lang_gien_xet'],sum(len(ke[u]) for u in reached))
    for v in reached:
        if v==c['s']:t.equal(r['cha'][v-1],0)
        else:t.true(r['cha'][v-1] in ke[v])
    return {'thu_tu':a,'visited':r['visited'],'cha':r['cha']}


def run(case_id=None):
    selected = [c for c in CASES if case_id is None or c['id'] == case_id]
    if not selected: raise ValueError('Không tìm thấy mã ca')
    rows = []
    for c in selected:
        checks = Checks()
        try:
            actual = evaluate(c, checks)
            row = dict(id=c['id'], goal=c['goal'], actual=actual,
                       status='PASS', assertions=checks.count)
        except Exception as exc:
            row = dict(id=c['id'], goal=c['goal'], actual=str(exc),
                       status='FAIL', assertions=checks.count)
        rows.append(row)
        print(f"{row['id']}: {row['status']} | {row['goal']} | actual={row['actual']}")
    report = {'environment': platform.platform(), 'python':sys.version,
              'time_utc':datetime.now(timezone.utc).isoformat(),
              'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in sorted((ROOT/'src').glob('*.py'))},
              'cases':rows, 'passed':sum(r['status']=='PASS' for r in rows),
              'total':len(rows), 'assertions':sum(r['assertions'] for r in rows)}
    print(f"TONG: {report['passed']}/{report['total']} ca PASS; {report['assertions']} phep kiem")
    return report

if __name__ == '__main__':
    p=argparse.ArgumentParser();p.add_argument('--case');p.add_argument('--out')
    a=p.parse_args();report=run(a.case)
    if a.out:
        dest=Path(a.out);dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    sys.exit(0 if report['passed']==report['total'] else 1)
