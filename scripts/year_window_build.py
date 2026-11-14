import json,re,collections,datetime,openpyxl,html
D='./inputs/'  # folder holding the saved browser exports
def jt(f):
    t=json.load(open(D+f))[0]['text'].split('\n\n(captured at origin')[0]; return json.loads(t)
FX=json.loads(jt('mcp-remote-devices-Claude_Browser__javascript_tool-1794609714901.txt'))
CA=json.loads(jt('mcp-remote-devices-Claude_Browser__javascript_tool-1794609713141.txt')+jt('mcp-remote-devices-Claude_Browser__javascript_tool-1794609713677.txt')+jt('mcp-remote-devices-Claude_Browser__javascript_tool-1794609714327.txt'))
PA=json.loads(json.loads(json.load(open(D+'toolu_01KgFnXejzEWPakbFC2zKTFb.json'))[0]['text'].split('\n\n(captured at origin')[0]).rstrip())
TX=json.load(open('yr/tx.json'))
U=re.compile(r"UNION|WORKERS|LABORERS|LABORS'|TEAMSTERS|FIRE ?FIGHTER|FIREFIGHTER|POLICE|SHERIFF|DEPUTY|PEACE OFFICER|LAW ENFORCEMENT|TEACHERS|AFL-?CIO|LABOR (FED|COUNCIL|UNITED|ACTION|&)|EMPLOYEES|NURSES|FRATERNAL ORDER|FEDERATION OF|\bIBEW\b|I\.B\.E\.W|LIUNA|SEIU|AFSCME|UFCW|CARPENTERS|PLUMBERS|PIPEFITTERS?|PIPE FITTERS|STEAM ?FITTERS|SPRINKLER FITTERS|ELECTRICAL WORKERS|IRON ?WORKERS|OPERATING ENGINEERS|BOILERMAKERS|SHEET METAL|BRICKLAYERS|ROOFERS|INSULATORS|CEMENT MASONS|\bIUEC\b|\bIATSE\b|\bCWA\b|\bCTA\b|\bCSEA\b|PORAC|CCPOA|CLEAT|\bAFT\b|\bTSTA\b|\bPSEA\b|\bLOCAL \d|LOCAL UNION|BUILDING (&|AND) CONSTRUCTION TRADES|BUILDING TRADES|MINE W(OR)?KE?RS|COAL MINERS|IN UNION|WORKING CLASS|BROTHERHOOD|\bCOPE\b|\bDRIVE\b|32BJ",re.I)
X=re.compile(r"EMPLOYEES? (PAC|POLITICAL|FUND|OF |BETTER)|EMPLOYEE PAC|EMPLOYEES OF|UNION PACIFIC|CREDIT UNION|UNION BANK|SOCIAL WORKERS|AGRICULTURE TEACHERS|WESTERN UNION|UNION SQUARE|EMPLOYER|CIVIL LIBERTIES|PERSONAL INSURANCE|CHARTER SCHOOLS|UNION (ELEMENTARY |HIGH )?SCHOOL|UNIFIED SCHOOL|UNION CITY|FOR UNION|UNION COUNTY|UNION TOWNSHIP|ACTIVE BALLOT CLUB$",re.I)
isU=lambda s:bool(s) and bool(U.search(s)) and not X.search(s)
T=datetime.datetime(2026,11,13)
def dt(s):
    s=str(s or '')
    if len(s)==8 and s.isdigit(): s=s[:4]+'-'+s[4:6]+'-'+s[6:]
    return datetime.datetime.strptime(s[:10],'%Y-%m-%d') if len(s)>=10 else None
sc=lambda p:(p[:1].upper()+p[1:].lower()) if p else ''
TIERV={'Team Civx':'Adjacent','L2 (L2 Political / L2 Data)':'Lead source'}
CATV={'PDI (Political Data Inc.)':'Voter data / advocacy tool','OutreachCircle':'Voter data / advocacy tool','Union Graphics':'Print','Kelly Press':'Print','Mosaic':'Print','Doyle Printing':'Print','Arandell':'Print','911 Media':'Print','Modern Cartographers':'Agency','Team Civx':'Agency','BMA Media Group':'Agency','617 Media Group':'Agency','Union Labor Works':'Agency','Union Up':'Agency','LinkedUnion':'Member platform / database','UnionActive':'Member platform / database','L2 (L2 Political / L2 Data)':'Voter data (partner)'}
def backs(L):
    L=sorted(L,key=lambda r:-r[1]); tot=round(sum(r[1] for r in L),2)
    return tot,'; '.join('%s ($%s)'%(n,format(round(a),',')) for n,a,c,i in L[:5])
def tier(nm,org,L):
    if org=='L' or isU(nm): return 'Tier 1: union or union PAC'
    if L: return 'Tier 2: union-backed'
    return 'Tier 3: other'
t2=[]
# ---- FEC
fb=collections.defaultdict(list)
for y,rid,bid,bn,amt,n in FX['don']:
    if isU(bn): fb[(y,rid)].append((bn.strip(),amt,n,bid))
fec=[]
for y,v,cat,vt,cid,nm,typ,des,st,party,org,tot,n,d0,d1,p in FX['pay']:
    L=fb.get((y,cid),[]); pt=tier(nm,org,L); bt,bs=backs(L) if L else ('','')
    fec.append([pt,y,v,vt,cat,nm,typ,des,st,'' if party in(None,'UNKNOWN') else party.title(),'Yes' if pt[5]=='1' else ('Yes' if isU(nm) else 'No'),tot,n,dt(d0),dt(d1),sc(p),cid,'https://www.fec.gov/data/committee/%s/'%cid,bt,bs,T])
    if pt[5]=='2':
        for bn,a,c,bid in sorted(L,key=lambda r:-r[1]): t2.append(['FEC',y,nm,typ,st,cid,v,bn,bid,a,c,bt])
# ---- states
def staterows(stt,ex,rcmap,link,src):
    out=[]
    for k,a in ex.items():
        y,v,fid=k; L=[b for b in rcmap.get((y,fid),[]) if isU(b[0]) and b[0].upper()!=a['nm'].upper()]
        pt=tier(a['nm'],'',L); bt,bs=backs(L) if L else ('','')
        out.append([pt,stt,y,v,TIERV.get(v,'Direct'),CATV.get(v,''),a['nm'],a['typ'],a['st'],'Yes' if pt[5]=='1' else 'No',round(a['t'],2),a['n'],dt(a['d0']),dt(a['d1']),sc('; '.join(x for x,_ in a['p'].most_common(3))),fid,a['pay'],link(fid),src,bt,bs,T])
        if pt[5]=='2':
            for bn,am,c,bid in sorted(L,key=lambda r:-r[1])[:10]: t2.append([stt,y,a['nm'],a['typ'],stt,fid,v,bn,bid,am,c,bt])
    return out
def agg(rows):
    E={}
    for y,v,fid,nm,typ,st,amt,d,p,pay in rows:
        a=E.setdefault((y,v,fid),{'nm':nm,'typ':typ,'st':st,'t':0,'n':0,'d0':'9','d1':'0','p':collections.Counter(),'pay':pay})
        a['t']+=amt;a['n']+=1;a['d0']=min(a['d0'],d);a['d1']=max(a['d1'],d)
        if p: a['p'][p.strip().upper()]+=1
    return E
def rcagg(rows):
    R=collections.defaultdict(lambda:collections.defaultdict(lambda:[0,0]))
    for y,fid,nm,amt in rows:
        r=R[(y,fid)][html.unescape(nm).strip()]; r[0]+=amt; r[1]+=1
    return {k:[(n,round(v[0],2),v[1],'') for n,v in d.items()] for k,d in R.items()}
# CA (already aggregated): ex [y,v,nm,fid,typ,st,t,n,d0,d1,p,pay]; rc [y,fid,nm,amt,n]
caE={(r[0],r[1],str(r[3])):{'nm':r[2],'typ':r[4],'st':r[5],'t':r[6],'n':r[7],'d0':r[8],'d1':r[9],'p':collections.Counter({x:1 for x in r[10].split('; ') if x}),'pay':r[11]} for r in CA['ex']}
caR=collections.defaultdict(list)
for y,fid,nm,amt,n in CA['rc']: caR[(y,str(fid))].append((nm.strip(),amt,n,''))
st=staterows('CA',caE,caR,lambda f:'https://cal-access.sos.ca.gov/Campaign/Committees/Detail.aspx?id=%s'%f,'Cal-Access raw data (CA Secretary of State)')
TT={'COH':'Candidate/officeholder','JCOH':'Judicial candidate','GPAC':'General purpose PAC','MPAC':'Monthly general purpose PAC','SPAC':'Specific purpose PAC','CEC':'County executive committee','SCC':'State/county chair candidate','DCE':'Direct campaign expenditure only'}
txr=[]
for v,fid,ft,fn,d,amt,ds,cat,nm,pst in TX['ex']:
    if 'AMERICAN UNION GRAPHICS' in nm.upper(): continue
    if v.startswith('L2') and pst not in('WA','NJ','NY'): continue
    txr.append((int(d[:4]),v,fid,fn,TT.get(ft,ft),'TX',float(amt),d[:4]+'-'+d[4:6]+'-'+d[6:],ds or cat,nm))
st+=staterows('TX',agg(txr),rcagg([(int(d[:4]),fid,nm,float(a)) for fid,nm,d,a in TX['rc']]),lambda f:'https://www.ethics.state.tx.us/search/cf/','Texas Ethics Commission CSV database')
FT={'1':'Candidate','2':'Political committee','3':'Other filer'}
par=[]
seen=set()
for v,fid,fn,ft,nm,pst,d,amt,ds in PA['ex']:
    par.append((int(d[:4]),v,fid,fn,FT.get(ft,ft),'PA',amt,d[:4]+'-'+d[4:6]+'-'+d[6:],ds,nm))
st+=staterows('PA',agg(par),rcagg([(int(d[:4]),fid,nm,a) for fid,nm,d,a in PA['rc']]),lambda f:'https://www.campaignfinanceonline.pa.gov/','Pennsylvania Department of State full export')
o={'Tier 1: union or union PAC':0,'Tier 2: union-backed':1,'Tier 3: other':2}; vo={'Direct':0,'Adjacent':1,'Lead source':2}
fec.sort(key=lambda r:(o[r[0]],vo.get(r[3],3),r[2],-r[1],-r[11]))
st.sort(key=lambda r:(o[r[0]],r[1],vo.get(r[4],3),r[3],-r[2],-r[10]))
g=collections.OrderedDict()
for r in t2:
    k=(r[0],r[1],str(r[5]),r[7].upper())
    if k in g:
        if r[6] not in g[k][6]: g[k][6]+=', '+r[6]
    else: g[k]=r[:]
t2=sorted(g.values(),key=lambda r:(r[0]!='FEC',r[0],-r[11],r[2],-r[1],-r[9]))
wb=openpyxl.Workbook(); ws=wb.active; ws.title='F'
ws.append(['Prospect tier','Year','Vendor','Vendor tier','Category','Committee (who paid)','Committee type','Designation','State','Party','Union-connected','Total paid','# payments','First payment','Last payment','Top purposes','FEC committee ID','FEC link','Union PAC backing ($)','Top union backers','Last updated'])
for r in fec: ws.append(r)
w2=wb.create_sheet('S'); w2.append(['Prospect tier','State','Year','Vendor','Vendor tier','Category','Committee (who paid)','Committee type','Committee state','Union / public safety connected','Total paid','# payments','First payment','Last payment','Top purposes','State filer ID','Payee as filed','State record link','Source','Union backing ($)','Top union backers','Last updated'])
for r in st: w2.append(r)
w3=wb.create_sheet('T'); w3.append(['Source','Year','Tier 2 committee','Committee type','State','Committee ID','Competitor / vendor used','Union or union PAC backer','Backer ID','Amount from backer','# contributions','Total union backing to committee','Last updated'])
for r in t2: w3.append(r+[T])
for w,cols in [(ws,'LS'),(w2,'KT'),(w3,'JL')]:
    for col in cols:
        for c in w[col][1:]: c.number_format='$#,##0'
for w,cols in [(ws,'NOU'),(w2,'MNV'),(w3,'M')]:
    for col in cols:
        for c in w[col][1:]: c.number_format='yyyy-mm-dd'
for c in w2['P'][1:]: c.number_format='@'
for c in w3['F'][1:]: c.number_format='@'
wb.save('yr/yr.xlsx')
C=collections.Counter
print('FEC',len(fec),C((r[1],r[0][:6]) for r in fec)); print('ST',len(st),C((r[1],r[2]) for r in st),C(r[0][:6] for r in st)); print('T2',len(t2),C(r[0] for r in t2))
s=collections.defaultdict(float)
for r in fec: s[('FEC',r[2],r[1])]+=r[11]
for r in st: s[(r[1],r[3],r[2])]+=r[10]
for k in sorted(s): print(k,round(s[k]))
