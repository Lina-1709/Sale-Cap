import pandas as pd
df=pd.read_csv('grade_raw_T8_T10.csv',dtype=str).fillna('')
assert df.shape==(333,10)
df['region']=df.team.map(lambda t:'North' if t.startswith(('HN','North')) else 'South')
G=['A+','A','B+','B','B-','C']
M={'T8':('M2','mobM2'),'T9':('M1','mobM1'),'T10 MTD':('MTD','mobMTD')}
print(df.team.value_counts().sort_index().to_dict())
for k,(g,_) in M.items(): print(k, df[g].value_counts().reindex(G+['-','']).fillna(0).astype(int).to_dict())
def rate(sub,g):
    v=sub[sub[g].isin(G)]; n=len(v); b=(v[g]=='B-').sum(); return b,n
def tbl(by,mob3=False):
    rows=[]
    keys=['Total'] if by is None else sorted(df[by].unique())
    for key in keys:
        s=df if by is None else df[df[by]==key]
        r={'grp':key}
        for k,(g,m) in M.items():
            ss=s[s[m]=='MOB3+'] if mob3 else s
            b,n=rate(ss,g); r[k]=f"{b}/{n} = {b/n*100:.1f}%" if n else '-'
        rows.append(r)
    return pd.DataFrame(rows)
for mob3 in (False,True):
  print('\n==== MOB3+ only' if mob3 else '\n==== All graded')
  for by in [None,'region','seg','team']:
    print(tbl(by,mob3).to_string(index=False))
# transitions
print('\nT8->T9 crosstab'); print(pd.crosstab(df.M2.replace('','(none)'),df.M1.replace('','(none)')).reindex(index=G+['-','(none)'],columns=G+['-','(none)']).fillna(0).astype(int))
print('\nT9->T10 crosstab'); print(pd.crosstab(df.M1.replace('','(none)'),df.MTD.replace('','(none)')).reindex(index=G+['-','(none)'],columns=G+['-','(none)']).fillna(0).astype(int))
# B- in Sep: status oct
s=df[df.M1=='B-']; print('\nB- T9 list:'); print(s[['team','seg','region','mobM1','M2','M1','MTD','stMTD']].to_string())
s=df[df.MTD=='B-']; print('\nB- T10 list:'); print(s[['team','seg','region','mobMTD','M2','M1','MTD','stMTD']].to_string())
s=df[df.M2=='B-']; print('\nB- T8 list:'); print(s[['team','seg','region','mobM2','M2','M1','MTD','stMTD','stM1']].to_string())
