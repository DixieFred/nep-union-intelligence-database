import json,re,collections,datetime,openpyxl,html
D='./inputs/'  # folder holding the saved browser exports
def jt(f):
    t=json.load(open(D+f))[0]['text'].split('\n\n(captured at origin')[0]; return json.loads(t)
# FEC tier data
fx=json.loads(jt('mcp-remote-devices-Claude_Browser__javascript_tool-1794608733219.txt'))
ORG=fx['org']; FDON=fx['don']   # [cyc,rid,bid,bname,amt,n,rank,nb,tot]
CA=json.loads(jt('mcp-remote-devices-Claude_Browser__javascript_tool-1794608726244.txt')+jt('mcp-remote-devices-Claude_Browser__javascript_tool-1794608726923.txt'))  # [cyc,fid,fn,nm,amt,n,rank,nb,tot]
PA=[[a,b,c,html.unescape(d),e,f] for a,b,c,d,e,f in json.loads(jt('mcp-remote-devices-Claude_Browser__javascript_tool-1794608789802.txt'))]  # [cyc,fid,fn,nm,amt,n]
TX=json.load(open('tier/tx_backers.json'))
U=re.compile(r"UNION|WORKERS|LABORERS|TEAMSTERS|FIRE ?FIGHTER|FIREFIGHTER|POLICE|SHERIFF|DEPUTY|PEACE OFFICER|LAW ENFORCEMENT|TEACHERS|AFL-?CIO|LABOR (FED|COUNCIL|UNITED|&)|EMPLOYEES|NURSES|FRATERNAL ORDER|FEDERATION OF|\bIBEW\b|LIUNA|SEIU|AFSCME|UFCW|CARPENTERS|PLUMBERS|PIPEFITTERS|PIPE FITTERS|STEAMFITTERS|ELECTRICAL WORKERS|IRONWORKERS|OPERATING ENGINEERS|BOILERMAKERS|SHEET METAL|BRICKLAYERS|ROOFERS|\bCWA\b|\bCTA\b|\bCSEA\b|PORAC|CCPOA|CLEAT|\bAFT\b|\bTSTA\b|\bLOCAL \d|LOCAL UNION|BUILDING (&|AND) CONSTRUCTION TRADES|BUILDING TRADES|MINE W(OR)?KE?RS|COAL MINERS|IN UNION|WORKING CLASS|BROTHERHOOD|\bCOPE\b|ACTIVE BALLOT|\bDRIVE\b",re.I)
X=re.compile(r"EMPLOYEES? (PAC|POLITICAL|FUND|OF )|EMPLOYEE PAC|EMPLOYEES OF|UNION PACIFIC|CREDIT UNION|UNION BANK|SOCIAL WORKERS|AGRICULTURE TEACHERS|WESTERN UNION|UNION SQUARE|EMPLOYER|CIVIL LIBERTIES|PERSONAL INSURANCE|CHARTER SCHOOLS|UNION (ELEMENTARY |HIGH )?SCHOOL|UNIFIED SCHOOL|UNION CITY|FOR UNION|UNION COUNTY|UNION TOWNSHIP",re.I)
isU=lambda s:bool(s) and bool(U.search(s)) and not X.search(s)
def fix(b):  # filter backers
    return [r for r in b if isU(r[3])]
T=datetime.datetime(2026,11,13)
D2=lambda s:datetime.datetime.strptime(s[:10],'%Y-%m-%d') if s and len(s)>=10 and s[4]=='-' else (s or None)
# ---------- FEC
fec=json.load(open('fec/rows.json'))
fb=collections.defaultdict(list)
for r in FDON: fb[(r[0],r[1])].append(r)
def backsum(L):
    L=sorted(L,key=lambda r:-r[4]); tot=sum(r[4] for r in L)
    return round(tot,2), '; '.join('%s ($%s)'%(r[3].strip(),format(round(r[4]),',')) for r in L[:5])
fecrows=[];t2=[]
for r in fec:
    cyc,v,tier,cat,nm,typ,des,st,party,uc,tot,n,d0,d1,p,cid,link=r
    org=ORG.get(cid,[None,None,'',0])
    L=fix(fb.get((cyc,cid),[]))
    if org[0]=='L' or isU(nm): pt='Tier 1: union or union PAC'
    elif L: pt='Tier 2: union-backed'
    else: pt='Tier 3: other'
    bt,bs=backsum(L) if L else ('','')
    fecrows.append([pt,cyc,v,tier,cat,nm,typ,des,st,party,'Yes' if pt.startswith('Tier 1') else uc,tot,n,D2(d0),D2(d1),p,cid,link,bt,bs,T])
    if pt.startswith('Tier 2'):
        for b in sorted(L,key=lambda r:-r[4]): t2.append(['FEC',cyc,nm,typ,st,cid,v,b[3].strip(),b[2],b[4],b[5],bt])
# ---------- State
sv=json.load(open(D+'mcp-Google_Sheets-get_values-1794608840417.txt'))['values']
H=sv[0]; S=[r+['']*(19-len(r)) for r in sv[1:] if r and r[0]]
sb=collections.defaultdict(list)
for r in CA: sb[('CA',r[0],str(r[1]))].append(r)
for r in TX: sb[('TX',r[0],str(r[1]))].append(r)
for r in PA: sb[('PA',r[0],str(r[1]))].append(r)
strows=[]
num=lambda x:float(str(x).replace('$','').replace(',','') or 0)
for r in S:
    stt,cyc,v,tier,cat,nm,typ,cst,uc,tot,n,d0,d1,p,fid,pay,link,src,lu=r[:19]
    cyc=int(cyc); key=(stt,cyc,str(fid).lstrip('0') if stt!='TX' else str(fid))
    L=fix(sb.get((stt,cyc,str(fid)),[]))
    # drop self-funding where backer equals committee
    L=[b for b in L if b[3].strip().upper()!=nm.strip().upper()]
    if isU(nm): pt='Tier 1: union or union PAC'
    elif L: pt='Tier 2: union-backed'
    else: pt='Tier 3: other'
    bt,bs=backsum(L) if L else ('','')
    strows.append([pt,stt,cyc,v,tier,cat,nm,typ,cst,'Yes' if pt.startswith('Tier 1') else 'No',num(tot),int(n),D2(d0),D2(d1),p,fid,pay,link,src,bt,bs,T])
    if pt.startswith('Tier 2'):
        for b in sorted(L,key=lambda r:-r[4]): t2.append([stt,cyc,nm,typ,stt,fid,v,b[3].strip(),'',b[4],b[5],bt])
# merge vendors per committee in T2
g=collections.OrderedDict()
for r in t2:
    k=(r[0],r[1],r[5],r[7].upper())
    if k in g: 
        if r[6] not in g[k][6]: g[k][6]+=', '+r[6]
    else: g[k]=r[:]
t2=list(g.values())
o={'Tier 1: union or union PAC':0,'Tier 2: union-backed':1,'Tier 3: other':2}
vo={'Direct':0,'Adjacent':1,'Lead source':2}
fecrows.sort(key=lambda r:(o[r[0]],vo.get(r[3],3),r[2],-r[1],-r[11]))
strows.sort(key=lambda r:(o[r[0]],r[1],vo.get(r[4],3),r[3],-r[2],-r[10]))
t2.sort(key=lambda r:(r[0]!='FEC',r[0],-r[11],r[2],-r[9]))
wb=openpyxl.Workbook(); ws=wb.active; ws.title='F'
ws.append(['Prospect tier','Cycle','Vendor','Vendor tier','Category','Committee (who paid)','Committee type','Designation','State','Party','Union-connected','Total paid','# payments','First payment','Last payment','Top purposes','FEC committee ID','FEC link','Union PAC backing ($)','Top union backers','Last updated'])
for r in fecrows: ws.append(r)
ws2=wb.create_sheet('S')
ws2.append(['Prospect tier','State','Cycle','Vendor','Vendor tier','Category','Committee (who paid)','Committee type','Committee state','Union / public safety connected','Total paid','# payments','First payment','Last payment','Top purposes','State filer ID','Payee as filed','State record link','Source','Union backing ($)','Top union backers','Last updated'])
for r in strows: ws2.append(r)
ws3=wb.create_sheet('T')
ws3.append(['Source','Cycle','Tier 2 committee','Committee type','State','Committee ID','Competitor / vendor used','Union or union PAC backer','Backer ID','Amount from backer','# contributions','Total union backing to committee','Last updated'])
for r in t2: ws3.append(r+[T])
for w,cols in [(ws,['L','S']),(ws2,['K','T']),(ws3,['J','L'])]:
    for col in cols:
        for c in w[col][1:]: c.number_format='$#,##0'
for w,cols in [(ws,'NOU'),(ws2,'MNV'),(ws3,'M')]:
    for col in cols:
        for c in w[col][1:]: c.number_format='yyyy-mm-dd'
for c in ws2['P'][1:]: c.number_format='@'
wb.save('tier/tier.xlsx')
print('FEC',collections.Counter(r[0] for r in fecrows),'State',collections.Counter((r[1],r[0]) for r in strows),'T2',len(t2))
print(len(fecrows),len(strows))
