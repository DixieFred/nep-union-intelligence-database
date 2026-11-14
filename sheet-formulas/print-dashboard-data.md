# Print Dashboard Data: formulas

Google Sheet "Print Dashboard Data (Looker Studio source)" (1YbbN4bNcnJuqEwywOqzUAkykOvl4kSHvyOPOXetIKG4). Exported Nov. 13, 2026. IMPORTRANGE needs a one-time Allow access click by the owner.

Validation: Assignments!A2:A dropdown from _lists!A1:A3000; Assignments!D2:D dropdown from _lists!B1:B50; Assignments!E2:E valid date. Protected: Assignments, Reps, Union leads, Telemarketing leads, Who has the work.

## _raw_union!A1

```
=IMPORTRANGE("1c3j7reNvBeBTLUC9B_N2lUugvR1ZQnfju_DXv1QT1sk","'Print & magazine'!A8:M3000")
```

## _raw_fund!A1

```
=IMPORTRANGE("1c3j7reNvBeBTLUC9B_N2lUugvR1ZQnfju_DXv1QT1sk","'Fundraising watch'!A1:AA1000")
```

## _raw_comp!A1

```
=IMPORTRANGE("1c3j7reNvBeBTLUC9B_N2lUugvR1ZQnfju_DXv1QT1sk","'Competitor list'!A3:D200")
```

## _lists!A1 (all lead IDs)

```
=IFERROR(SORT(VSTACK(FILTER('Union leads'!A2:A,'Union leads'!A2:A<>""),UNIQUE(FILTER('Telemarketing leads'!A2:A,'Telemarketing leads'!A2:A<>"")))),"")
```

## _lists!B1 (rep names)

```
=IFERROR(FILTER(Reps!A2:A,Reps!A2:A<>""),"")
```

## _lists!C1 (Print competitor pattern)

```
=IFERROR(TEXTJOIN("|",TRUE,ARRAYFORMULA(UPPER(FILTER('_raw_comp'!A2:A,'_raw_comp'!D2:D="Print")))),"KELLY PRESS|UNION GRAPHICS|MOSAIC|ARANDELL|DOYLE PRINTING|911 MEDIA")
```

## Union leads!A1

```
=LET(r,FILTER('_raw_union'!A2:M,'_raw_union'!B2:B<>""),c,LAMBDA(i,INDEX(r,0,i)),num,LAMBDA(x,ARRAYFORMULA(IFERROR(VALUE(REGEXREPLACE(TO_TEXT(x),"[^0-9.]","")),0))),lid,ARRAYFORMULA("U-"&c(2)),stc,ARRAYFORMULA(IFERROR(REGEXEXTRACT(c(3),", ([A-Z]{2})$"),"")),comp,ARRAYFORMULA(IFERROR(PROPER(REGEXEXTRACT(UPPER(c(7)),"("&'_lists'!C1&")")),"")),repraw,ARRAYFORMULA(XLOOKUP(lid,Assignments!A2:A,IF(Assignments!D2:D="","",Assignments!D2:D),"")),rep,ARRAYFORMULA(IF(repraw="","Unassigned",repraw)),eml,ARRAYFORMULA(XLOOKUP(rep,Reps!A2:A,IF(Reps!B2:B="","",LOWER(Reps!B2:B)),"")),dte,ARRAYFORMULA(XLOOKUP(lid,Assignments!A2:A,IF(Assignments!E2:E="","",TEXT(Assignments!E2:E,"yyyy-mm-dd")),"")),VSTACK({"Lead ID","Lead type","Priority","Union","City, State","State","Members","Print spend","Suggested starting price","Who has the work now","Competitor on our list","The pitch","Timing","Status","Contact on file","Contact","Confidence","Filing year","Assigned rep","Rep email","Date assigned"},HSTACK(lid,ARRAYFORMULA(IF(LEN(lid),"Union print","")),c(1),c(2),c(3),stc,num(c(4)),num(c(5)),num(c(6)),c(7),comp,c(8),c(9),c(10),ARRAYFORMULA(IF(c(11)<>"","Yes","No")),c(11),c(12),c(13),rep,eml,dte)))
```

## Telemarketing leads!A1

```
=LET(r,FILTER('_raw_fund'!A2:AA,REGEXMATCH('_raw_fund'!L2:L&"","Phone")),c,LAMBDA(i,INDEX(r,0,i)),num,LAMBDA(x,ARRAYFORMULA(IFERROR(VALUE(x),0))),lid,ARRAYFORMULA("T-"&c(5)&" ("&c(7)&")"),repraw,ARRAYFORMULA(XLOOKUP(lid,Assignments!A2:A,IF(Assignments!D2:D="","",Assignments!D2:D),"")),rep,ARRAYFORMULA(IF(repraw="","Unassigned",repraw)),eml,ARRAYFORMULA(XLOOKUP(rep,Reps!A2:A,IF(Reps!B2:B="","",LOWER(Reps!B2:B)),"")),dte,ARRAYFORMULA(XLOOKUP(lid,Assignments!A2:A,IF(Assignments!E2:E="","",TEXT(Assignments!E2:E,"yyyy-mm-dd")),"")),VSTACK({"Lead ID","Lead type","Priority","Filed year","Fiscal year end","Organization","Org type","State","City","Telemarketer","Telemarketer location","Raised","Kept by telemarketer","Net to organization","Share to organization","Signing officer","Officer title","Org phone","Website","990 link","Assigned rep","Rep email","Date assigned"},HSTACK(lid,ARRAYFORMULA(IF(LEN(lid),"Telemarketing","")),c(3),c(1),c(2),c(5),c(6),c(7),c(8),c(10),c(11),num(c(15)),num(c(16)),num(c(17)),c(18),c(22),c(23),c(24),c(21),c(26),rep,eml,dte)))
```

## Who has the work!A1

```
=LET(w,FILTER('Union leads'!J2:J,'Union leads'!J2:J<>""),p,TOCOL(ARRAYFORMULA(SPLIT(REGEXREPLACE(w,"\)\s*[,;]\s*",")|"),"|",FALSE,TRUE)),1),q,FILTER(p,REGEXMATCH(p,"\(\$[0-9.]+[KM]\)$")),nm,ARRAYFORMULA(PROPER(TRIM(REGEXREPLACE(REGEXREPLACE(UPPER(REGEXEXTRACT(q,"^(.*)\s\(\$")),"[.,]",""),"\s+(INC|LLC|CO|CORP|COMPANY|LTD)$","")))),amt,ARRAYFORMULA(VALUE(REGEXEXTRACT(q,"\$([0-9.]+)"))*IF(RIGHT(q,2)="M)",1000000,1000)),cp,ARRAYFORMULA(IF(REGEXMATCH(UPPER(nm),'_lists'!C1),"Yes","No")),VSTACK({"Vendor","Amount paid","Competitor on our list"},HSTACK(nm,amt,cp)))
```

## Assignments!B2 (lead type)

```
=ARRAYFORMULA(IF(A2:A="","",IF(LEFT(A2:A,2)="U-","Union print","Telemarketing")))
```

## Assignments!C2 (lead name)

```
=ARRAYFORMULA(IF(A2:A="","",IFERROR(XLOOKUP(A2:A,'Union leads'!A2:A,'Union leads'!D2:D),IFERROR(XLOOKUP(A2:A,'Telemarketing leads'!A2:A,'Telemarketing leads'!F2:F),"Not found: check the ID"))))
```

