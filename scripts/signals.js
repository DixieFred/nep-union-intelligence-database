function(A,B,empA,empB,lmA,lmB,today){
const out=[];const tc=s=>s.toLowerCase().replace(/\b\w/g,c=>c.toUpperCase());
const latest=lm=>{const b={};lm.filter(r=>r.FORM_TYPE=='LM-2'&&r.TERMINATE!='T').forEach(r=>{const x=b[r.F_NUM];if(!x||r.RECEIVE_DATE>x.RECEIVE_DATE)b[r.F_NUM]=r});const o={};for(const [f,r] of Object.entries(b))o[r.RPT_ID]=f;return o};
const cls=t=>/^(BUSINESS MANAGER|BUSINESS MGR|BUS\.? MGR)/.test(t)?'business manager':/^EXECUTIVE DIRECTOR/.test(t)?'executive director':/^PRESIDENT/.test(t)?'president':null;
const offs=(emp,R)=>{const m={};for(const e of emp){const f=R[e.RPT_ID];if(!f)continue;const c=cls((e.TITLE||'').toUpperCase().trim());if(!c)continue;const nm=tc(((e.FIRST_NAME||'')+' '+(e.LAST_NAME||'')).trim());if(!nm)continue;m[f]=m[f]||{};(m[f][c]=m[f][c]||new Set()).add(nm)}return m};
const OA=offs(empA,latest(lmA)),OB=offs(empB,latest(lmB));
const last=n=>n.toUpperCase().split(' ').pop();
const money=v=>'$'+(v>=1e6?(v/1e6).toFixed(1)+'M':Math.round(v/1000)+'K');
const compOf=(R)=>{const m={};for(const c of R.comp){if(c[3]=='NEP Services'||/partner/i.test(c[2]))continue;(m[c[9]]=m[c[9]]||{})[c[3]]=c[2]}return m};
const CA=compOf(A),CB=compOf(B);
const teamOfCat=c=>/Member platform/.test(c)?'Sales':/Advocacy|Voter|Agency/.test(c)?'Advocacy':/Print/.test(c)?'Print':'All';
const push=(f,p,type,detail,pts,team,subj)=>out.push([today,p[3],+f,type,detail,pts,team,p[27],f+'|'+type+'|'+subj+'|'+p[27]]);
for(const [f,pb] of Object.entries(B.profiles)){const pa=A.profiles[f];if(!pa)continue;
 const oa=OA[f]||{},ob=OB[f]||{};
 for(const c of Object.keys(ob)){if(!oa[c]||ob[c].size>3)continue;const nw=[...ob[c]].filter(n=>![...oa[c]].some(o=>last(o)==last(n)));if(nw.length)push(f,pb,'New leadership','New '+c+': '+nw.join(', '),5,'All',c+':'+nw.join(','))}
 const nms=s=>new Set([...(s||'').matchAll(/\(([^)]+)\)/g)].map(m=>m[1].trim().toUpperCase()));
 const sa=nms(pa[12]),sb=nms(pb[12]);
 const add=[...sb].filter(n=>!sa.has(n)),gone=[...sa].filter(n=>!sb.has(n));
 if(add.length)push(f,pb,'Comms hire','Added comms staff: '+add.map(tc).join(', '),4,'All','hire:'+add.join(','));
 if(gone.length&&sb.size<sa.size)push(f,pb,'Comms staff left','Comms staff no longer listed: '+gone.map(tc).join(', '),4,'All','left:'+gone.join(','));
 const ca=A.cons[f],cb=B.cons[f];
 if(ca&&cb){[['Website',9,'Sales'],['Member comms',10,'Sales'],['Advocacy/political',11,'Advocacy'],['Social/digital/ads',12,'Advocacy'],['Print/magazine',13,'Print']].forEach(([lab,i,tm])=>{const a=+ca[i]||0,b=+cb[i]||0;if(b>=10000&&b-a>=10000&&(a==0||b>=a*1.25))push(f,pb,'Spend up',lab+' spend up to '+money(b)+(a?' from '+money(a):' (new)'),3,tm,lab)})}
 else{const a=+pa[17]||0,b=+pb[17]||0;if(b>=10000&&b-a>=10000&&(a==0||b>=a*1.25))push(f,pb,'Spend up','Ad and print spend up to '+money(b)+(a?' from '+money(a):' (new)'),3,'All','adpr')}
 const xa=CA[f]||{},xb=CB[f]||{};
 for(const [v,c] of Object.entries(xa))if(!xb[v])push(f,pb,'Dropped competitor','No longer paying '+v,5,teamOfCat(c),'drop:'+v);
 for(const [v,c] of Object.entries(xb))if(!xa[v])push(f,pb,'Started competitor','Started paying '+v,1,teamOfCat(c),'start:'+v);
 const ta=pa[25],tb=pb[25];if((tb=='Tier 1'||tb=='Tier 2')&&(!ta||ta=='Tier 3'||(ta=='Tier 2'&&tb=='Tier 1')))push(f,pb,'New target tier','Now '+tb+' (was '+(ta||'not a target')+')',4,'All','tier:'+tb);
 const ma=+pa[7]||0,mb=+pb[7]||0;if(ma>=100&&Math.abs(mb-ma)/ma>=0.10)push(f,pb,'Membership change','Membership '+(mb>ma?'up ':'down ')+Math.round(Math.abs(mb-ma)/ma*100)+'% to '+mb.toLocaleString(),2,'All',mb>ma?'up':'down');
}
const now=new Date(today+'T12:00:00');const mo=now.getFullYear()*12+now.getMonth();
const seen=new Set();
for(const R of [B,A])for(const [f,p] of Object.entries(R.profiles)){if(seen.has(f))continue;seen.add(f);const m=(p[10]||'').match(/^(\d{4})-(\d{2})$/);if(!m)continue;const d=(+m[1])*12+(+m[2]-1)-mo;if(d>=0&&d<=6)out.push([today,p[3],+f,'Election soon','Officer election '+p[10]+(d==0?' (this month)':' (in '+d+' mo)'),3,'All',p[27],f+'|Election soon|'+p[10]])}
return out}
