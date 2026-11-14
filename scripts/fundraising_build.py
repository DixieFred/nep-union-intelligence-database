import json,re,datetime
from openpyxl import Workbook
rows=json.load(open('rows.json'))
# dedupe amended: keep latest obj per ein+tp+fundraiser
best={}
for r in rows:
    k=(r[0],r[1],r[17].upper().strip(),r[20])
    if k not in best or r[4]>best[k][4]: best[k]=r
# also if same ein+tp appears with different obj (amended), keep only rows from latest obj
latest={}
for r in best.values():
    k=(r[0],r[1]); latest[k]=max(latest.get(k,''),r[4])
rows=[r for r in best.values() if r[4]==latest[(r[0],r[1])]]
def num(x):
    try: return float(x)
    except: return None
def method(a):
    a=a.upper(); m=[]
    if re.search(r'TELE|PHONE|CALL|TLMKT|TELMKT',a): m.append('Phone')
    if re.search(r'MAIL',a): m.append('Mail')
    if re.search(r'MAGAZINE|AD ?BOOK|SPONSOR|PUBLISH|DIRECTORY|YEARBOOK|JOURNAL|ADVERTIS',a): m.append('Ad book / magazine / sponsors')
    if re.search(r'EVENT|SHOW|SHPW|CIRCUS|CONCERT|MUSIC|GOLF|NIGHT|DINNER|RAFFLE|GIVEAWAY|TICKET',a): m.append('Events / shows')
    if re.search(r'HONORARY|MEMBERSHIP',a): m.append('Honorary membership')
    if re.search(r'DIGITAL|ONLINE|INTERNET|EMAIL|WEB',a): m.append('Digital')
    if not m: m.append('General fundraising' if re.search(r'FUND|SOLICI|SOLIT|DONAT|CAMPAIGN|PROFESSION|CONSULT',a) else 'Not specified')
    return ', '.join(m)
def orgtype(n):
    n=n.upper()
    if re.search(r'FIRE|FIREMEN',n): return 'Fire'
    if re.search(r'SHERIFF|DEPUT',n): return 'Sheriff'
    if re.search(r'\bEMS\b|\bEMT|PARAMEDIC',n): return 'EMS'
    if re.search(r'POLICE|F\.?O\.?P|FRATERNAL ORDER|P\.?B\.?A|TROOPER|PATROL|PEACE OFFICER|LAW ENFORCEMENT|DETECTIVE|CONSTABLE|CORRECTION',n): return 'Police / law enforcement'
    return 'Public safety (other)'
def title(s):
    s=(s or '').strip()
    if s.isupper() or s.islower():
        s=' '.join(w if re.fullmatch(r'(FOP|PBA|EMS|EMT|IAFF|II|III|IV|LLC|INC|USA|[A-Z]{2})',w) and len(w)<=4 and w in('FOP','PBA','EMS','EMT','IAFF','II','III','IV','LLC','USA') else w.capitalize() for w in s.split())
    return s
today=datetime.date.today()
out=[]
for r in rows:
    (ein,tp,sub,name,obj,st,city,site,off,offt,ph,totrev,contrib,c501,proffee,phs,mls,fr,act,ctrl,gross,ret,net,fcity,fst,hasf)=r
    if hasf:
        g,k,n=num(gross),num(ret),num(net)
        if n is None and g is not None and k is not None: n=g-k
        pct=(n/g) if (g and n is not None) else None
        frn=title(fr) or '(name not given)'; loc=', '.join(x for x in [title(fcity),fst] if x)
        meth=method(act); act_f=act; ctrl_f='Yes' if ctrl in('1','true','X') else ('No' if ctrl in('0','false') else '')
    else:
        g=None;k=num(proffee);n=None;pct=None;frn='(not itemized on Schedule G)';loc='';meth='Not specified';act_f='Professional fundraising fees reported, fundraiser not itemized';ctrl_f=''
    phone_or_mail=('Phone' in meth) or ('Mail' in meth)
    if pct is not None and pct<0.5 and (g or 0)>=100000: pri='1 High'
    elif (pct is not None and pct<0.5) or ((k or 0)>=50000): pri='2 Medium'
    else: pri='3 Low'
    if not hasf and (k or 0)<25000: pri='3 Low'
    pr='Yes' if ('Mail' in meth or 'Ad book' in meth) else 'No'
    fye=f"{tp[:4]}-{tp[4:]}"
    out.append([int(sub),fye,pri,pr,title(name),orgtype(name),st,title(city),('501(c)('+c501+')') if c501 else '',frn,loc,meth,act_f,ctrl_f,g,k,n,pct,num(totrev),num(contrib),(site or '').lower(),title(off),title(offt),ph,ein,f"https://projects.propublica.org/nonprofits/organizations/{ein}",today])
out.sort(key=lambda x:(x[2],-(x[15] or 0)))
H=['Filed year','Fiscal year end','Help a Hero priority','Print angle','Organization','Org type','State','City','Tax status','Fundraiser','Fundraiser location','Method','Activity (as filed)','Fundraiser handles the money','Gross raised','Kept by fundraiser','Net to organization','% to organization','Org total revenue','Org contributions','Website','Signing officer','Officer title','Org phone','EIN','990 filings link','Last updated']
wb=Workbook();ws=wb.active;ws.title='Fundraising watch';ws.append(H)
for o in out: ws.append(o)
for row in ws.iter_rows(min_row=2):
    for i in (14,15,16,18,19): row[i].number_format='$#,##0'
    row[17].number_format='0%'; row[26].number_format='yyyy-mm-dd'
wb.save('fund.xlsx')
from collections import Counter
ph=[o for o in out if 'Phone' in o[11]]
print('rows',len(out),'priority',dict(Counter(o[2] for o in out)),'phone rows',len(ph),'phone orgs',len(set(o[24] for o in ph)),'phone raised',round(sum(o[14] or 0 for o in ph)),'phone kept',round(sum(o[15] or 0 for o in ph)))
json.dump([[o[24],o[1],o[9],o[4],o[6],o[14],o[15]] for o in out],open('keys.json','w'))
