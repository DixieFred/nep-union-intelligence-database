import json,re,sys,collections
from openpyxl import Workbook
OUT,IL2,ISM=sys.argv[1],sys.argv[2],sys.argv[3];TABF=sys.argv[4:]
def jl(p):
    j=json.load(open(p))
    return j.get('content',j) if isinstance(j,dict) else j
T={}
for f in TABF:
    for s in jl(f)['sheets']:
        rows=[[(v.get('formattedValue') or '').strip() for v in rd.get('values',[])] for rd in (s.get('data') or [{}])[0].get('rowData',[])]
        T[s['properties']['title']]=rows
SKIP={'Sunday Event ATTENDEES','HSR Conference','DEMS','VENDORS','PRICING Calculator'}
STAGES={'SIGNED':'Signed (NEP client)','QUOTES DELIVERED':'Quote delivered','PROSPECTS':'Prospect (in contact)','READY TO CALL':'Ready to call','NOT READY TO CALL':'Not ready to call','NEEDS MORE INFO':'Needs more info','DEFUNCT':'Defunct'}
TABAFF={'IBEW':'IBEW','UA':'UA','SMART':'SMART','Teamsters':'IBT','Bricklayers':'BAC','IUOE':'IUOE','Ironworkers':'BSOIW','IUPAT':'PAT','CARPENTERS':'CJA','LIUNA':'LIUNA','Cement Masons':'OPCM','IUEC':'IUEC','CWA':'CWA','SMART TD':'SMART','IATSE':'IATSE','IBEW/NABTU 26':'IBEW','TWU':'TWU','ROOF':'RWAW','NTEU':'NTEU','MUSICIANS':'AFM','NPMHU':'NPMHU','UFCW':'UFCW','UNITE HERE':'UNITHE','BOIL':'BBF','IFPTE':'IFPTE','ATU':'ATU','APWU':'APWU','AFSCME':'AFSCME','RWDSU':'RWDSU','CSEA':'AFSCME','NALC':'NALC','Longshoremen':'ILA','TEAMSTER RAIL':'IBT','SEIU':'SEIU','Rural Letter Carriers':'RLCA','Postal Supervisors':'NAPS','AFSA':'AFSA','AFGE':'AFGE','NFFE':'NFFE','UAW':'UAW','IAFF':'IAFF','OPEIU':'OPEIU','UWUA':'UWUA','NATCA':'NATCA','ILWU':'ILWU','STEEL':'USW','INSUL':'HFIA','IAMAW':'IAM','BRS Rail':'BRS','BCTGM':'BCTGMI','BWME Rail':'BMWE','NWSEO':'NWSEO','MINE WORKERS':'UMW','IBEW CLIENTS':'IBEW','TEACHERS':'AFT'}
SYN=[(r'^IBEW\b','IBEW'),(r'^(UA|U\.A\.|PLUMBERS|PIPEFITTERS|STEAMFITTERS)\b','UA'),(r'^SMART\b|^SHEET METAL','SMART'),(r'^(TEAMSTERS|IBT)\b','IBT'),(r'^(BAC|BRICKLAYERS)\b','BAC'),(r'^(IUOE|OPERATING ENGINEERS)\b','IUOE'),(r'^(IRONWORKERS|IRON WORKERS|BSOIW)\b','BSOIW'),(r'^(IUPAT|PAINTERS|DC \d|DISTRICT COUNCIL \d)','PAT'),(r'^(CARPENTERS|UBC|MILLWRIGHTS)\b','CJA'),(r'^(LIUNA|LABORERS)\b','LIUNA'),(r'^(OPCMIA|OPCM|CEMENT MASONS|PLASTERERS)\b','OPCM'),(r'^IUEC\b|^ELEVATOR','IUEC'),(r'^CWA\b','CWA'),(r'^IATSE\b','IATSE'),(r'^TWU\b','TWU'),(r'^(ROOFERS|RWAW)\b','RWAW'),(r'^NTEU\b','NTEU'),(r'^(AFM|MUSICIANS)\b','AFM'),(r'^NPMHU\b','NPMHU'),(r'^UFCW\b','UFCW'),(r'^UNITE HERE\b','UNITHE'),(r'^(BOILERMAKERS|IBB)\b','BBF'),(r'^IFPTE\b','IFPTE'),(r'^ATU\b','ATU'),(r'^APWU\b','APWU'),(r'^AFSCME\b','AFSCME'),(r'^RWDSU\b','RWDSU'),(r'^NALC\b','NALC'),(r'^ILA\b','ILA'),(r'^SEIU\b','SEIU'),(r'^AFGE\b','AFGE'),(r'^NFFE\b','NFFE'),(r'^UAW\b','UAW'),(r'^IAFF\b','IAFF'),(r'^OPEIU\b','OPEIU'),(r'^UWUA\b','UWUA'),(r'^NATCA\b','NATCA'),(r'^ILWU\b','ILWU'),(r'^(USW|STEELWORKERS)\b','USW'),(r'^(HFIA|INSULATORS)\b','HFIA'),(r'^(IAM|IAMAW|MACHINISTS)\b','IAM'),(r'^BRS\b','BRS'),(r'^BCTGM\b','BCTGMI'),(r'^(BMWE|BMWED)\b','BMWE'),(r'^NWSEO\b','NWSEO'),(r'^(UMWA|UMW)\b','UMW'),(r'^(BLET|BLE)\b','BLE'),(r'^AFT\b','AFT'),(r'^NEA\b','NEA'),(r'^(SAG|SAG-AFTRA)','SAGAFTRA'),(r'^AFA\b','AFA'),(r'^MEBA\b','MEBA'),(r'^(BCTC|.*BUILDING (AND|&) CONSTRUCTION TRADES|.*BUILDING TRADES)','BCTD'),(r'\bFOP\b|FRATERNAL ORDER OF POLICE','NFOP')]
def affof(n,tab):
    N=n.upper().strip()
    for rx,c in SYN:
        if re.search(rx,N): return c
    return TABAFF.get(tab,'')
def numof(n,aff=''):
    if aff=='USW':
        m=re.search(r'\b\d{1,2}-0*(\d+)\b',n)
        if m: return int(m.group(1))
    m=re.search(r'(?:LOCAL|LU|LODGE|BRANCH|DIVISION|DIV\.?|CHAPTER|COUNCIL|DC|NO\.?|#)\s*-?\s*(\d+)',n,re.I)
    if m: return int(m.group(1))
    m=re.search(r'\b(\d{1,5})\b',n); return int(m.group(1)) if m else None
KEYS={'name':['LOCAL','UNION','PBA LOCAL','ORGANIZATION'],'city':['CITY','CITY/TWP/BOROUGH'],'state':['STATE'],'zip':['ZIP'],'phone':['PHONE'],'email':['E-MAIL','EMAIL'],'web':['WEBSITE'],'prov':['PROVIDER','PROVIDER? MAIL?'],'notes':['NOTES'],'rep':['REP','FOLLOW UP BY']}
CK=['CONTACT','BUSINESS MGR','PRESIDENT'];FN=['BM FIRST','CONTACT FIRST','FIRST'];LN=['BM LAST','CONTACT LAST','LAST']
REPS={'SCOTT','CHRISTINE','STAN','KEVIN','NIKKI','STACEY','MARK','MAHER','JULIAN','SEAN','KWH'}
PROV=[('UNIONACTIVE','UnionActive'),('LINKEDUNION','LinkedUnion'),('UNIONLABORWORKS','Union Labor Works'),('ULW','Union Labor Works'),('NEP','NEP'),('SELF','Self-managed'),('WEBRAND','WeBrand Digital'),('HARBORSIDE','Harborside'),('BMA','BMA Media Group'),('WORDPRESS','WordPress'),('WIX','Wix'),('SQUARESPACE','Squarespace'),('GODADDY','GoDaddy'),('UNIONTRACK','UnionTrack'),('UNIONWARE','UnionWare'),('UNIONCENTRIC','UnionCentrics'),('WEBCONNECTIVITY','Web Connectivity')]
def prov(p,rep):
    if not p or p.strip().upper() in ('PRESIDENT','N/A','NA','0','LOCAL','SMART','NONE','-','?','TBD'): return '',rep
    if p.upper().strip() in REPS: return '',(rep or p.strip().title())
    P=p.upper().replace(' ','')
    for k,v in PROV:
        if k in P: return v,rep
    if re.search(r'https?://|www\.',p): return '',rep
    return p.strip(),rep
recs=[]
for tab,rows in T.items():
    if tab in SKIP: continue
    hi=None
    for i,r in enumerate(rows[:6]):
        u=[c.upper() for c in r]
        if any(k in u for k in KEYS['name']) and ('STATE' in u or 'ADDRESS 1' in u or 'WEBSITE' in u): hi=i;break
    if hi is None: H={'aff':0,'name':1,'city':4,'state':5,'zip':6,'contact':7};start=0
    else:
        u=[c.upper() for c in rows[hi]];H={}
        for k,opts in KEYS.items():
            for j,c in enumerate(u):
                if c in opts and k not in H: H[k]=j
        if tab=='ULW Clients': H['name']=1;H['rep']=0
        for j,c in enumerate(u):
            if c in CK and 'contact' not in H: H['contact']=j
            if c in FN and 'fn' not in H: H['fn']=j
            if c in LN and 'ln' not in H: H['ln']=j
        start=hi+1
    stage=''
    for ri,r in enumerate(rows):
        if ri<start: continue
        g=lambda k:(r[H[k]] if k in H and H[k]<len(r) else '').strip()
        ne=[c for c in r if c]
        if not ne: continue
        nm=g('name')
        if len(ne)==1:
            if ne[0].upper() in STAGES: stage=STAGES[ne[0].upper()]
            elif re.search(r'\b(LOCAL|LODGE|COUNCIL)\b',ne[0],re.I) and len(ne[0])<80:
                nx=[y for y in rows[ri+1:ri+6] if any(y)]
                cs=[y[0] for y in nx if len([c for c in y if c])==1]
                if cs and re.fullmatch(r"[A-Za-z .'\-]+, ?[A-Z]{2}",cs[0].strip()):
                    city,stt=[t.strip() for t in cs[0].rsplit(',',1)]
                    ph=next((re.sub(r'^(Office|Phone|Tel)[: ]*','',c,flags=re.I).strip() for c in cs[1:3] if re.search(r'\d{3}.?\d{3}.?\d{4}',c)),'')
                    nm2=ne[0].strip().rstrip('*').strip();aff2=affof(nm2,tab)
                    recs.append(dict(tab=tab,stage=stage or 'Listed (no stage)',name=nm2,aff=aff2,num=numof(nm2,aff2),city=city,state=stt,zip='',contact='',phone=ph,email='',web='',prov='',rep='',notes=''))
            continue
        if nm.upper() in STAGES: stage=STAGES[nm.upper()]
        if not nm or nm.upper() in STAGES: continue
        cells=' '.join(r);email=g('email');web=g('web')
        if '@' not in email:
            m=re.search(r'[\w.+\-]+@[\w\-]+\.[\w.\-]+',cells);email=m.group(0) if m else ''
        if not web or not re.search(r'\.\w',web) or '@' in web:
            m=re.search(r'(https?://\S+|www\.\S+|\b[\w\-]+\.(?:org|com|net|us)\b\S*)',' '.join(c for c in r if '@' not in c));web=m.group(0) if m else ''
        notes=g('notes')
        if 'notes' in H:
            ex=[c for c in r[H['notes']+1:] if c]
            if ex: notes=(notes+' | '+' | '.join(ex)).strip(' |')
        ta=g('aff') if hi is None else ''
        aff=(affof(nm,tab) or affof(ta,tab) or ta) if ta else affof(nm,tab)
        st=g('state').upper() if re.fullmatch(r'[A-Za-z]{2}',g('state')) else g('state')
        z=g('zip')
        if re.fullmatch(r'\d{4}',z): z='0'+z
        stg=stage or 'Listed (no stage)';pv=g('prov');rep=g('rep')
        if tab=='ULW Clients': stg='Competitor client list';pv=pv or 'Union Labor Works'
        if tab=='LinkedUnion Clients': stg='Competitor client list';pv='LinkedUnion'
        if tab=='UnionActive Clients' and not pv: pv='UnionActive'
        pv,rep=prov(pv,rep)
        recs.append(dict(tab=tab,stage=stg,name=nm.rstrip('- *').strip(),aff=aff,num=numof(nm,aff),city=g('city'),state=st,zip=z,contact=g('contact') or (g('fn')+' '+g('ln')).strip(),phone=g('phone'),email=email,web=web,prov=pv,rep=rep,notes=notes[:500]))
idx=collections.defaultdict(list)
def addidx(f,org,st,city,form):
    try: f=int(str(f).replace(',',''))
    except: return
    code=org.split(' ')[0];m=re.search(r'\b(\d+)\b',org[len(code):])
    if m: idx[(code,int(m.group(1)))].append(dict(f=f,st=st,city=city,form=form))
for r in jl(IL2)['values']:   # Prospect index A:G  -> file, org, level, sector, aff, city, state
    r=r+['']*7; addidx(r[0],r[1],r[6],r[5],'LM-2')
for r in jl(ISM)['values']:   # Small locals C:M -> org, city, state, form, ... file at index 10
    r=r+['']*11; addidx(r[10],r[0],r[2],r[1],r[3])
st=collections.Counter()
for r in recs:
    r['file']='';r['conf']='';r['form']=''
    if not r['aff'] or r['num'] is None: continue
    c=idx.get((r['aff'],r['num']),[])
    if not c: continue
    same=[x for x in c if x['st']==r['state']]
    if len(same)==1: p,cf=same[0],'High'
    elif len(same)>1:
        cc=[x for x in same if x['city'].lower()==r['city'].lower()]
        p,cf=(cc[0],'High') if len(cc)==1 else (same[0],'Review')
    elif len(c)==1 and not r['state']: p,cf=c[0],'Medium'
    else: continue
    r['file']=p['f'];r['conf']=cf;r['form']=p['form'];st[cf]+=1
PRI={'Signed (NEP client)':0,'Quote delivered':1,'Prospect (in contact)':2,'Ready to call':3,'Listed (no stage)':4,'Needs more info':5,'Not ready to call':6,'Defunct':7,'Competitor client list':8}
recs.sort(key=lambda r:(r['file']=='',str(r['file']),PRI.get(r['stage'],9),r['email']=='',r['contact']==''))
wb=Workbook();ws=wb.active;ws.title='Contacts & pipeline'
ws.append(['Organization','Affiliate','City','State','Zip','Contact','Phone','Email','Website','Website provider (per master list)','NEP rep','Pipeline stage','Notes (from master list)','Source list','OLMS file #','Match confidence','OLMS form'])
for r in recs: ws.append([r['name'],r['aff'],r['city'],r['state'],r['zip'],r['contact'],r['phone'],r['email'],r['web'],r['prov'],r['rep'],r['stage'],r['notes'],r['tab'],r['file'],r['conf'],r['form']])
for c in ws['E']+ws['G']: c.number_format='@'
wb.save(OUT)
print(json.dumps({'records':len(recs),'tabs':len(T),'matched':sum(1 for r in recs if r['file']!=''),'distinct_unions':len({r['file'] for r in recs if r['file']!=''}),'confidence':st,'stages':collections.Counter(r['stage'] for r in recs)}))
