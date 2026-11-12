# Sheet formulas and reference values

Exported from the live Google Sheet on Nov. 11, 2026. Each entry is `cell: content`.

## Executive brief

```
A1: NEP Union Intelligence: Executive brief
A2: ="Every union that files with the U.S. Department of Labor, matched to the NEP master list. Data refreshed "&TEXT(MAX('Prospect index'!Z2:Z),"mmmm d, yyyy")&". Dollar figures come from each union's latest filing and count only payments of $5,000 or more, so they are minimums."
A4: The headline numbers
D4: Where the money is (consolidation targets)
A5: Unions with full DOL financial reports (LM-2)
B5: =COUNTA('Prospect index'!A2:A)
D5: Service line
E5: Yearly spend
A6: Consolidation targets (buying 3+ NEP services from 3+ vendors)
B6: =COUNTIF('Prospect index'!W2:W,"Tier*")
D6: Website
E6: =SUMIFS('Prospect index'!AA2:AA,'Prospect index'!W2:W,"Tier*")
A7: Tier 1 targets (4+ services, $150K+)
B7: =COUNTIF('Prospect index'!W2:W,"Tier 1")
D7: Member comms
E7: =SUMIFS('Prospect index'!AB2:AB,'Prospect index'!W2:W,"Tier*")
A8: Yearly spend NEP could win from all targets
B8: =SUMIFS('Prospect index'!AF2:AF,'Prospect index'!W2:W,"Tier*")
D8: Advocacy & political
E8: =SUMIFS('Prospect index'!AC2:AC,'Prospect index'!W2:W,"Tier*")
A9: Existing NEP clients found in the data
B9: =COUNTIF('Prospect index'!AO2:AO,"Yes")
D9: Social, digital & ads
E9: =SUMIFS('Prospect index'!AD2:AD,'Prospect index'!W2:W,"Tier*")
A10: Targets already in NEP's pipeline
B10: =COUNTIFS('Prospect index'!W2:W,"Tier*",'Prospect index'!AH2:AH,"<>Not in master list")
D10: Print & magazine
E10: =SUMIFS('Prospect index'!AE2:AE,'Prospect index'!W2:W,"Tier*")
A11: Targets NOT yet in our master list (net new)
B11: =COUNTIFS('Prospect index'!W2:W,"Tier*",'Prospect index'!AH2:AH,"Not in master list")
A12: Paid by unions to competitors (2025 filings)
B12: =SUMIFS('Competitor watch'!H2:H,'Competitor watch'!A2:A,2025,'Competitor watch'!D2:D,"<>NEP Services")
A13: Unions on a competitor website platform (LM-2 filers)
B13: =COUNTIF('Prospect index'!AR2:AR,"Yes")
A15: Top 10 local and council opportunities (Tier 1, not yet NEP clients)
A16: =QUERY('Prospect index'!A1:AR,"select B, D, G, AF, AH, U where W = 'Tier 1' and AO <> 'Yes' and C <> 'International' order by AF desc limit 10 label B 'Union', D 'Sector', G 'State', AF 'Yearly spend NEP could win', AH 'NEP pipeline stage', U 'Who they pay today'",1)
A28: Top 10 international targets (national headquarters)
A29: =QUERY('Prospect index'!A1:AR,"select B, D, G, AF, AH, U where W starts with 'Tier' and AO <> 'Yes' and C = 'International' order by AF desc limit 10 label B 'Union', D 'Sector', G 'State', AF 'Yearly spend NEP could win', AH 'NEP pipeline stage', U 'Who they pay today'",1)
A41: Top competitors by what unions pay them (2025 filings)
A42: =QUERY('Competitor watch'!A1:K,"select D, count(E), sum(H) where A = 2025 and D <> 'NEP Services' group by D order by sum(H) desc limit 8 label D 'Competitor', count(E) 'Union clients', sum(H) 'Paid by unions'",1)
```

## Advocacy & political

```
A7: =IFERROR(QUERY('Prospect index'!A1:BQ,"select BC,B,AT,H,AZ,BB,BA,BD,AV,AW,AX,BE,Y where P > 0"&IF($A$5="All",""," and G = '"&$A$5&"'")&IF($B$5="All",""," and BC contains '"&$B$5&"'")&IF($C$5="Yes"," and AO <> 'Yes'","")&IF($D$5="All","",IF($D$5="Internationals only"," and C = 'International'"," and C <> 'International'"))&IF($E$5="All",""," and AH = '"&$E$5&"'")&" order by BC, AZ desc, P desc label BC 'Priority', B 'Union', AT 'City, State', H 'Members', AZ 'Advocacy spend (last filing)', BB 'Suggested starting price (yr)', BA 'Who they use now', BD 'The pitch', AV 'Timing', AW 'Our status (rep)', AX 'Contact', BE 'Confidence', Y 'Filing year'",1),"No unions match these filters.")
```

## Sales: websites & Connect Plus+

```
A7: =IFERROR(QUERY('Prospect index'!A1:BQ,"select BI,B,AT,H,BF,BH,BG,BJ,AV,AW,AX,BK,Y where A is not null"&IF($A$5="All",""," and G = '"&$A$5&"'")&IF($B$5="All",""," and BI contains '"&$B$5&"'")&IF($C$5="Yes"," and AO <> 'Yes'","")&IF($D$5="All","",IF($D$5="Internationals only"," and C = 'International'"," and C <> 'International'"))&IF($E$5="All","",IF($E$5="Any competitor platform"," and AR = 'Yes'",IF($E$5="No provider listed"," and AJ = ''"," and AJ = '"&$E$5&"'")))&" order by BI, BF desc, H desc label BI 'Priority', B 'Union', AT 'City, State', H 'Members', BF 'Website + member tools spend (last filing)', BH 'Suggested starting price (yr)', BG 'Who they use now', BJ 'The pitch', AV 'Timing', AW 'Our status (rep)', AX 'Contact', BK 'Confidence', Y 'Filing year'",1),"No unions match these filters.")
```

## Print & magazine

```
A7: =IFERROR(QUERY('Prospect index'!A1:BQ,"select BO,B,AT,H,BL,BN,BM,BP,AV,AW,AX,BQ,Y where BL > 0"&IF($A$5="All",""," and G = '"&$A$5&"'")&IF($B$5="All",""," and BO contains '"&$B$5&"'")&IF($C$5="Yes"," and AO <> 'Yes'","")&IF($D$5="All","",IF($D$5="Internationals only"," and C = 'International'"," and C <> 'International'"))&IF($E$5="All",""," and AH = '"&$E$5&"'")&" order by BO, BL desc label BO 'Priority', B 'Union', AT 'City, State', H 'Members', BL 'Print spend (last filing)', BN 'Suggested starting price (yr)', BM 'Who they use now', BP 'The pitch', AV 'Timing', AW 'Our status (rep)', AX 'Contact', BQ 'Confidence', Y 'Filing year'",1),"No unions match these filters.")
```

## Competitor takeaway

```
A7: =IFERROR(QUERY('Competitor watch'!A1:K,"select D, C, count(E), sum(H) where A = "&$B$4&" and D <> 'NEP Services' group by D, C order by sum(H) desc label D 'Competitor', C 'Category', count(E) 'Unions paying them', sum(H) 'Total paid'",1),"No data for this year yet.")
F7: =IFERROR(QUERY('Competitor watch'!A1:K,"select E, G, B, H, I, J where A = "&$B$4&" and D = '"&$G$4&"' order by H desc label E 'Union', G 'State', B 'Sector', H 'Paid to competitor', I 'What for', J 'OLMS file #'",1),"No clients found for this competitor and year.")
L7: NEP pipeline stage
M7: Contact
N7: Email
L8: =ARRAYFORMULA(IF(K8:K="",,IFERROR(XLOOKUP(K8:K,'Prospect index'!A2:A,'Prospect index'!AH2:AH),IFERROR(XLOOKUP(K8:K,'Contacts & pipeline'!O2:O,'Contacts & pipeline'!L2:L),"Not in master list"))))
M8: =ARRAYFORMULA(IF(K8:K="",,IFERROR(XLOOKUP(K8:K,'Contacts & pipeline'!O2:O,'Contacts & pipeline'!F2:F),"")))
N8: =ARRAYFORMULA(IF(K8:K="",,IFERROR(XLOOKUP(K8:K,'Contacts & pipeline'!O2:O,'Contacts & pipeline'!H2:H),"")))
A61: =QUERY({ARRAYFORMULA(IFERROR(VLOOKUP('Contacts & pipeline'!J2:J,Lists!H2:I40,2,FALSE),"")),'Contacts & pipeline'!A2:A},"select Col1, count(Col2) where Col1 <> '' group by Col1 order by count(Col2) desc label Col1 'Website provider', count(Col2) 'Unions listed'",0)
```

## Pricing guide

```
A1: Pricing guide: suggested starting prices
A2: These are starting points for planning a call, not approved NEP pricing. Leadership should replace the yellow cells with NEP's current rate card; every suggested price in the prospect tabs updates automatically.
A4: How a suggested price is set: the HIGHER of (1) what the union already paid outside vendors for that service on its latest DOL filing, or (2) the floor below plus the per-member rate times its membership. Rounded to the nearest $500.
A5: Service line
B5: Annual floor ($)
C5: Per member per year ($)
D5: Basis for the starting numbers (estimates)
A6: Website (build spread over year one, plus monthly care)
B6: 9000
C6: 0.1
D6: Union website builds commonly run about $6,000 to $20,000, plus $250 to $1,000 a month for hosting, updates and support.
A7: Member comms platform (Connect Plus+)
B7: 3000
C7: 1
D7: Union member platforms are commonly priced around $1 to $4 per member per year with an annual minimum. Replace with the Connect Plus+ rate card.
A8: Advocacy & political (management plus minimum media)
B8: 18000
C8: 0.5
D8: NEP's standard $500 a month management fee (SMART 2026 proposal) plus about $1,000 a month minimum media, scaled by membership. Large campaigns are scoped separately.
A9: Print & magazine (printing, postage, design)
B9: 6000
C9: 2
D9: A quarterly member magazine or newsletter commonly costs about $0.40 to $1.00 per copy printed and mailed, roughly $1.60 to $4 per member per year.
A11: Rules for the call
A12: 1. Never quote below what the union already pays. That money is already in their budget; going lower only leaves revenue on the table.
A13: 2. Win on consolidation, not discount: one team, one invoice, one strategy across website, member comms, advocacy and print.
A14: 3. Spend figures are minimums. DOL filings only itemize payments of $5,000 or more to a single vendor, so true spend is usually higher.
A15: 4. Advocacy prices include management and a minimum media budget. Paid media above that is billed at cost, scoped per campaign.
A16: 5. Prices are annual. Divide by 12 for a monthly figure; one-time builds (websites) can be quoted separately from monthly care.
A17: 6. Any price in a proposal still needs approval under NEP's normal review (Scott Welkley handles term and billing).
```

## Wish list

```
A1: Wish list: ideas to add to the database
A2: Add a row for any feature, data source or view you want. Set Status as it moves. Josh reviews and prioritizes.
A3: #
B3: Idea
C3: What it does / how it helps us win
D3: Team(s)
E3: Priority
F3: Effort
G3: Status
H3: Requested by
I3: Date added
J3: Notes / decision
A4: 1
B4: Weekly Hot list of buying signals
C4: Flags unions with an officer election in the next 6 months, a comms staffer who left, a jump in spend, a dropped competitor, or new Tier 1/2 status. Tells reps who to call this week.
D4: All
E4: High
F4: Small
G4: Idea
H4: Josh
I4: 46337
J4: Recommended next build; uses data already in the sheet.
A5: 2
B5: Website and digital audit
C5: Checks each prospect's site: real platform, last update, copyright year, mobile, security certificate, active social pages. Verifies the provider column and gives reps an opening line.
D5: Sales
E5: High
F5: Medium
G5: Idea
H5: Josh
I5: 46337
A6: 3
B6: Meta Ad Library scan
C6: Shows which unions run paid ads and who places them. Intelligence on competitors' advocacy clients.
D6: Advocacy, Exec
E6: Medium
F6: Medium
G6: Idea
H6: Josh
I6: 46337
A7: 4
B7: FEC and state campaign finance vendor data
C7: Union PAC payments show which agencies run political mail and digital. A second view of the competitive landscape.
D7: Advocacy
E7: Medium
F7: Large
G7: Idea
H7: Josh
I7: 46337
J7: State rules and data formats vary; start with FEC.
A8: 5
B8: Lookalike scoring
C8: Profiles current NEP clients and scores every union on similarity. Shows where we already win.
D8: Exec, Sales
E8: Medium
F8: Medium
G8: Idea
H8: Josh
I8: 46337
A9: 6
B9: Client upsell gaps
C9: For each current client, lists the services they still buy elsewhere. Cheapest new revenue.
D9: Exec, Sales
E9: High
F9: Small
G9: Idea
H9: Josh
I9: 46337
A10: 7
B10: Council and local hierarchy
C10: Shows which locals sit under each council or international, to support a win-the-council, expand-to-locals strategy.
D10: Exec, Sales
E10: Medium
F10: Medium
G10: Idea
H10: Josh
I10: 46337
A11: 8
B11: News watch tie-in
C11: Flags strikes, contract fights and ballot measures involving a union in the database as an advocacy opportunity.
D11: Advocacy
E11: Medium
F11: Medium
G11: Idea
H11: Josh
I11: 46337
J11: Builds on the existing client news watch.
A12: 9
B12: Master list cleanup report
C12: Lists records that conflict with the federal filings on state (about 1,100) or match nothing (about 4,200), so the team can fix them.
D12: Sales
E12: Medium
F12: Small
G12: Idea
H12: Josh
I12: 46337
A13: 10
B13: Replace Pricing guide estimates with NEP rate card
C13: Makes every suggested price reflect real NEP pricing, especially Connect Plus+.
D13: Exec, Sales
E13: High
F13: Small
G13: Idea
H13: Josh
I13: 46337
J13: Needs leadership / Scott Welkley input.
A14: 11
B14: HubSpot integration
C14: Syncs the database with HubSpot once the data is trusted.
D14: Exec
E14: Low
F14: Large
G14: Parked
H14: Josh
I14: 46337
J14: Discuss with Shubi before any HubSpot changes.
A15: 12
B15: Lead card (one-screen pre-call brief)
C15: Pick any union and see spend, suggested prices, vendors, pipeline, contact and pitch by team.
D15: All
E15: High
F15: Small
G15: Done
H15: Josh
I15: 46337
J15: Built Nov. 11, 2026.
A16: 13
B16: Team call lists with pricing and confidence
C16: Advocacy, Sales and Print call lists with priority, suggested starting price and confidence legend.
D16: All
E16: High
F16: Medium
G16: Done
H16: Josh
I16: 46337
J16: Built Nov. 11, 2026.
```

## Sector summary

```
A1: NEP Union Prospecting Summary
A2: Source: U.S. DOL OLMS LM filings (2025 and 2026 data years). Most recent update:
B2: =MAX(MAX('Union profiles'!AC2:AC),MAX('International profiles'!AC2:AC))
A4: Sector
B4: LM-2 filers
C4: Small locals (LM-3/LM-4)
D4: Tier 1 targets
E4: Tier 2 targets
F4: Tier 3 targets
G4: Existing NEP clients to expand
H4: Total addressable $ (targets)
I4: LM-2 unions paying a named competitor
J4: Ad + print spend (all LM-2)
K4: Political & lobbying (all LM-2)
L4: Update day
A5: Building trades
B5: =COUNTIF('Union profiles'!$A:$A,$A5)+COUNTIF('International profiles'!$A:$A,$A5)
C5: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A5)
D5: =COUNTIFS('Consolidation targets'!$B:$B,$A5,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A5,'International consolidation targets'!$A:$A,"Tier 1")
E5: =COUNTIFS('Consolidation targets'!$B:$B,$A5,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A5,'International consolidation targets'!$A:$A,"Tier 2")
F5: =COUNTIFS('Consolidation targets'!$B:$B,$A5,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A5,'International consolidation targets'!$A:$A,"Tier 3")
G5: =COUNTIFS('Consolidation targets'!$B:$B,$A5,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A5,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H5: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A5)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A5)
I5: =COUNTIFS('Union profiles'!$A:$A,$A5,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A5,'International profiles'!$X:$X,"<>")
J5: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A5)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A5)
K5: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A5)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A5)
L5: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A5,'Affiliate map'!$C:$C,0)),"")
A6: Federal & postal
B6: =COUNTIF('Union profiles'!$A:$A,$A6)+COUNTIF('International profiles'!$A:$A,$A6)
C6: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A6)
D6: =COUNTIFS('Consolidation targets'!$B:$B,$A6,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A6,'International consolidation targets'!$A:$A,"Tier 1")
E6: =COUNTIFS('Consolidation targets'!$B:$B,$A6,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A6,'International consolidation targets'!$A:$A,"Tier 2")
F6: =COUNTIFS('Consolidation targets'!$B:$B,$A6,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A6,'International consolidation targets'!$A:$A,"Tier 3")
G6: =COUNTIFS('Consolidation targets'!$B:$B,$A6,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A6,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H6: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A6)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A6)
I6: =COUNTIFS('Union profiles'!$A:$A,$A6,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A6,'International profiles'!$X:$X,"<>")
J6: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A6)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A6)
K6: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A6)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A6)
L6: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A6,'Affiliate map'!$C:$C,0)),"")
A7: Public safety & security
B7: =COUNTIF('Union profiles'!$A:$A,$A7)+COUNTIF('International profiles'!$A:$A,$A7)
C7: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A7)
D7: =COUNTIFS('Consolidation targets'!$B:$B,$A7,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A7,'International consolidation targets'!$A:$A,"Tier 1")
E7: =COUNTIFS('Consolidation targets'!$B:$B,$A7,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A7,'International consolidation targets'!$A:$A,"Tier 2")
F7: =COUNTIFS('Consolidation targets'!$B:$B,$A7,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A7,'International consolidation targets'!$A:$A,"Tier 3")
G7: =COUNTIFS('Consolidation targets'!$B:$B,$A7,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A7,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H7: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A7)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A7)
I7: =COUNTIFS('Union profiles'!$A:$A,$A7,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A7,'International profiles'!$X:$X,"<>")
J7: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A7)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A7)
K7: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A7)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A7)
L7: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A7,'Affiliate map'!$C:$C,0)),"")
A8: Public sector (state & local)
B8: =COUNTIF('Union profiles'!$A:$A,$A8)+COUNTIF('International profiles'!$A:$A,$A8)
C8: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A8)
D8: =COUNTIFS('Consolidation targets'!$B:$B,$A8,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A8,'International consolidation targets'!$A:$A,"Tier 1")
E8: =COUNTIFS('Consolidation targets'!$B:$B,$A8,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A8,'International consolidation targets'!$A:$A,"Tier 2")
F8: =COUNTIFS('Consolidation targets'!$B:$B,$A8,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A8,'International consolidation targets'!$A:$A,"Tier 3")
G8: =COUNTIFS('Consolidation targets'!$B:$B,$A8,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A8,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H8: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A8)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A8)
I8: =COUNTIFS('Union profiles'!$A:$A,$A8,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A8,'International profiles'!$X:$X,"<>")
J8: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A8)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A8)
K8: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A8)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A8)
L8: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A8,'Affiliate map'!$C:$C,0)),"")
A9: Education
B9: =COUNTIF('Union profiles'!$A:$A,$A9)+COUNTIF('International profiles'!$A:$A,$A9)
C9: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A9)
D9: =COUNTIFS('Consolidation targets'!$B:$B,$A9,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A9,'International consolidation targets'!$A:$A,"Tier 1")
E9: =COUNTIFS('Consolidation targets'!$B:$B,$A9,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A9,'International consolidation targets'!$A:$A,"Tier 2")
F9: =COUNTIFS('Consolidation targets'!$B:$B,$A9,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A9,'International consolidation targets'!$A:$A,"Tier 3")
G9: =COUNTIFS('Consolidation targets'!$B:$B,$A9,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A9,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H9: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A9)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A9)
I9: =COUNTIFS('Union profiles'!$A:$A,$A9,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A9,'International profiles'!$X:$X,"<>")
J9: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A9)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A9)
K9: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A9)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A9)
L9: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A9,'Affiliate map'!$C:$C,0)),"")
A10: Transportation
B10: =COUNTIF('Union profiles'!$A:$A,$A10)+COUNTIF('International profiles'!$A:$A,$A10)
C10: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A10)
D10: =COUNTIFS('Consolidation targets'!$B:$B,$A10,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A10,'International consolidation targets'!$A:$A,"Tier 1")
E10: =COUNTIFS('Consolidation targets'!$B:$B,$A10,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A10,'International consolidation targets'!$A:$A,"Tier 2")
F10: =COUNTIFS('Consolidation targets'!$B:$B,$A10,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A10,'International consolidation targets'!$A:$A,"Tier 3")
G10: =COUNTIFS('Consolidation targets'!$B:$B,$A10,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A10,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H10: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A10)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A10)
I10: =COUNTIFS('Union profiles'!$A:$A,$A10,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A10,'International profiles'!$X:$X,"<>")
J10: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A10)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A10)
K10: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A10)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A10)
L10: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A10,'Affiliate map'!$C:$C,0)),"")
A11: Communications & media
B11: =COUNTIF('Union profiles'!$A:$A,$A11)+COUNTIF('International profiles'!$A:$A,$A11)
C11: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A11)
D11: =COUNTIFS('Consolidation targets'!$B:$B,$A11,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A11,'International consolidation targets'!$A:$A,"Tier 1")
E11: =COUNTIFS('Consolidation targets'!$B:$B,$A11,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A11,'International consolidation targets'!$A:$A,"Tier 2")
F11: =COUNTIFS('Consolidation targets'!$B:$B,$A11,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A11,'International consolidation targets'!$A:$A,"Tier 3")
G11: =COUNTIFS('Consolidation targets'!$B:$B,$A11,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A11,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H11: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A11)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A11)
I11: =COUNTIFS('Union profiles'!$A:$A,$A11,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A11,'International profiles'!$X:$X,"<>")
J11: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A11)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A11)
K11: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A11)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A11)
L11: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A11,'Affiliate map'!$C:$C,0)),"")
A12: Entertainment & sports
B12: =COUNTIF('Union profiles'!$A:$A,$A12)+COUNTIF('International profiles'!$A:$A,$A12)
C12: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A12)
D12: =COUNTIFS('Consolidation targets'!$B:$B,$A12,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A12,'International consolidation targets'!$A:$A,"Tier 1")
E12: =COUNTIFS('Consolidation targets'!$B:$B,$A12,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A12,'International consolidation targets'!$A:$A,"Tier 2")
F12: =COUNTIFS('Consolidation targets'!$B:$B,$A12,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A12,'International consolidation targets'!$A:$A,"Tier 3")
G12: =COUNTIFS('Consolidation targets'!$B:$B,$A12,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A12,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H12: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A12)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A12)
I12: =COUNTIFS('Union profiles'!$A:$A,$A12,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A12,'International profiles'!$X:$X,"<>")
J12: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A12)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A12)
K12: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A12)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A12)
L12: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A12,'Affiliate map'!$C:$C,0)),"")
A13: Healthcare
B13: =COUNTIF('Union profiles'!$A:$A,$A13)+COUNTIF('International profiles'!$A:$A,$A13)
C13: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A13)
D13: =COUNTIFS('Consolidation targets'!$B:$B,$A13,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A13,'International consolidation targets'!$A:$A,"Tier 1")
E13: =COUNTIFS('Consolidation targets'!$B:$B,$A13,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A13,'International consolidation targets'!$A:$A,"Tier 2")
F13: =COUNTIFS('Consolidation targets'!$B:$B,$A13,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A13,'International consolidation targets'!$A:$A,"Tier 3")
G13: =COUNTIFS('Consolidation targets'!$B:$B,$A13,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A13,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H13: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A13)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A13)
I13: =COUNTIFS('Union profiles'!$A:$A,$A13,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A13,'International profiles'!$X:$X,"<>")
J13: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A13)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A13)
K13: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A13)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A13)
L13: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A13,'Affiliate map'!$C:$C,0)),"")
A14: Retail, food & agriculture
B14: =COUNTIF('Union profiles'!$A:$A,$A14)+COUNTIF('International profiles'!$A:$A,$A14)
C14: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A14)
D14: =COUNTIFS('Consolidation targets'!$B:$B,$A14,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A14,'International consolidation targets'!$A:$A,"Tier 1")
E14: =COUNTIFS('Consolidation targets'!$B:$B,$A14,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A14,'International consolidation targets'!$A:$A,"Tier 2")
F14: =COUNTIFS('Consolidation targets'!$B:$B,$A14,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A14,'International consolidation targets'!$A:$A,"Tier 3")
G14: =COUNTIFS('Consolidation targets'!$B:$B,$A14,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A14,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H14: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A14)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A14)
I14: =COUNTIFS('Union profiles'!$A:$A,$A14,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A14,'International profiles'!$X:$X,"<>")
J14: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A14)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A14)
K14: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A14)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A14)
L14: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A14,'Affiliate map'!$C:$C,0)),"")
A15: Hospitality & service
B15: =COUNTIF('Union profiles'!$A:$A,$A15)+COUNTIF('International profiles'!$A:$A,$A15)
C15: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A15)
D15: =COUNTIFS('Consolidation targets'!$B:$B,$A15,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A15,'International consolidation targets'!$A:$A,"Tier 1")
E15: =COUNTIFS('Consolidation targets'!$B:$B,$A15,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A15,'International consolidation targets'!$A:$A,"Tier 2")
F15: =COUNTIFS('Consolidation targets'!$B:$B,$A15,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A15,'International consolidation targets'!$A:$A,"Tier 3")
G15: =COUNTIFS('Consolidation targets'!$B:$B,$A15,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A15,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H15: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A15)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A15)
I15: =COUNTIFS('Union profiles'!$A:$A,$A15,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A15,'International profiles'!$X:$X,"<>")
J15: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A15)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A15)
K15: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A15)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A15)
L15: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A15,'Affiliate map'!$C:$C,0)),"")
A16: Manufacturing & industrial
B16: =COUNTIF('Union profiles'!$A:$A,$A16)+COUNTIF('International profiles'!$A:$A,$A16)
C16: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A16)
D16: =COUNTIFS('Consolidation targets'!$B:$B,$A16,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A16,'International consolidation targets'!$A:$A,"Tier 1")
E16: =COUNTIFS('Consolidation targets'!$B:$B,$A16,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A16,'International consolidation targets'!$A:$A,"Tier 2")
F16: =COUNTIFS('Consolidation targets'!$B:$B,$A16,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A16,'International consolidation targets'!$A:$A,"Tier 3")
G16: =COUNTIFS('Consolidation targets'!$B:$B,$A16,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A16,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H16: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A16)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A16)
I16: =COUNTIFS('Union profiles'!$A:$A,$A16,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A16,'International profiles'!$X:$X,"<>")
J16: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A16)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A16)
K16: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A16)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A16)
L16: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A16,'Affiliate map'!$C:$C,0)),"")
A17: Labor federations & departments
B17: =COUNTIF('Union profiles'!$A:$A,$A17)+COUNTIF('International profiles'!$A:$A,$A17)
C17: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A17)
D17: =COUNTIFS('Consolidation targets'!$B:$B,$A17,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A17,'International consolidation targets'!$A:$A,"Tier 1")
E17: =COUNTIFS('Consolidation targets'!$B:$B,$A17,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A17,'International consolidation targets'!$A:$A,"Tier 2")
F17: =COUNTIFS('Consolidation targets'!$B:$B,$A17,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A17,'International consolidation targets'!$A:$A,"Tier 3")
G17: =COUNTIFS('Consolidation targets'!$B:$B,$A17,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A17,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H17: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A17)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A17)
I17: =COUNTIFS('Union profiles'!$A:$A,$A17,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A17,'International profiles'!$X:$X,"<>")
J17: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A17)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A17)
K17: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A17)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A17)
L17: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A17,'Affiliate map'!$C:$C,0)),"")
A18: Independent & other
B18: =COUNTIF('Union profiles'!$A:$A,$A18)+COUNTIF('International profiles'!$A:$A,$A18)
C18: =COUNTIF('Small locals (LM-3, LM-4)'!$A:$A,$A18)
D18: =COUNTIFS('Consolidation targets'!$B:$B,$A18,'Consolidation targets'!$A:$A,"Tier 1")+COUNTIFS('International consolidation targets'!$B:$B,$A18,'International consolidation targets'!$A:$A,"Tier 1")
E18: =COUNTIFS('Consolidation targets'!$B:$B,$A18,'Consolidation targets'!$A:$A,"Tier 2")+COUNTIFS('International consolidation targets'!$B:$B,$A18,'International consolidation targets'!$A:$A,"Tier 2")
F18: =COUNTIFS('Consolidation targets'!$B:$B,$A18,'Consolidation targets'!$A:$A,"Tier 3")+COUNTIFS('International consolidation targets'!$B:$B,$A18,'International consolidation targets'!$A:$A,"Tier 3")
G18: =COUNTIFS('Consolidation targets'!$B:$B,$A18,'Consolidation targets'!$A:$A,"Existing NEP client: expand")+COUNTIFS('International consolidation targets'!$B:$B,$A18,'International consolidation targets'!$A:$A,"Existing NEP client: expand")
H18: =SUMIFS('Consolidation targets'!$O:$O,'Consolidation targets'!$B:$B,$A18)+SUMIFS('International consolidation targets'!$O:$O,'International consolidation targets'!$B:$B,$A18)
I18: =COUNTIFS('Union profiles'!$A:$A,$A18,'Union profiles'!$X:$X,"<>")+COUNTIFS('International profiles'!$A:$A,$A18,'International profiles'!$X:$X,"<>")
J18: =SUMIFS('Union profiles'!$R:$R,'Union profiles'!$A:$A,$A18)+SUMIFS('International profiles'!$R:$R,'International profiles'!$A:$A,$A18)
K18: =SUMIFS('Union profiles'!$T:$T,'Union profiles'!$A:$A,$A18)+SUMIFS('International profiles'!$T:$T,'International profiles'!$A:$A,$A18)
L18: =IFERROR(INDEX('Affiliate map'!$D:$D,MATCH($A18,'Affiliate map'!$C:$C,0)),"")
A19: Total
B19: =SUM(B5:B18)
C19: =SUM(C5:C18)
D19: =SUM(D5:D18)
E19: =SUM(E5:E18)
F19: =SUM(F5:F18)
G19: =SUM(G5:G18)
H19: =SUM(H5:H18)
I19: =SUM(I5:I18)
J19: =SUM(J5:J18)
K19: =SUM(K5:K18)
A21: Activity in the last 7 days
A22: Union profiles added or updated
B22: =COUNTIF('Union profiles'!AC2:AC,">="&(TODAY()-7))+COUNTIF('International profiles'!AC2:AC,">="&(TODAY()-7))
A23: Consolidation targets added or updated
B23: =COUNTIF('Consolidation targets'!Y2:Y,">="&(TODAY()-7))+COUNTIF('International consolidation targets'!Y2:Y,">="&(TODAY()-7))
A24: Competitor relationships added or updated
B24: =COUNTIF('Competitor watch'!K2:K,">="&(TODAY()-7))
A25: Small locals added or updated
B25: =COUNTIF('Small locals (LM-3, LM-4)'!N2:N,">="&(TODAY()-7))
A27: Top 20 Tier 1 targets (excluding internationals), by total addressable spend
A28: =QUERY('Consolidation targets'!A1:Y,"select A,B,D,E,G,O,R,U where A='Tier 1' and C<>'International' order by O desc limit 20",1)
```

## Prospect index

```
A1: OLMS file #
B1: Organization
C1: Level
D1: Sector
E1: Affiliate
F1: City
G1: State
H1: Members
I1: Membership change
J1: Has comms staff
K1: # comms staff
L1: Comms staff pay
M1: Ad / media / digital spend
N1: Print / publishing spend
O1: Ad + print total
P1: Political & lobbying total
Q1: Ad/print in political schedule
R1: Ad/print tagged organizing or recruitment
S1: Top comms vendors
T1: Top technology vendors
U1: Competitors / platforms in use
V1: Paying NEP (per OLMS)
W1: Consolidation tier
X1: Next officer election
Y1: Data year
Z1: Last updated
AA1: Website $
AB1: Member comms $
AC1: Advocacy/political $
AD1: Social/digital/ads $
AE1: Print/magazine $
AF1: Total addressable $
AG1: Vendors by service
AH1: Pipeline stage
AI1: NEP rep
AJ1: Website provider (master list)
AK1: Contact
AL1: Phone
AM1: Email
AN1: Website
AO1: NEP client (any source)
AP1: Website + member comms $
AQ1: Why they're a fit
AR1: On a competitor platform
AS1: Match confidence (master list)
AT1: City, State
AU1: Months to next election
AV1: Timing
AW1: Our status
AX1: Contact
AY1: Base confidence
AZ1: Advocacy spend (last filing)
BA1: Advocacy vendors
BB1: Advocacy suggested price
BC1: Advocacy priority
BD1: Advocacy pitch
BE1: Advocacy confidence
BF1: Sales spend (last filing)
BG1: Sales vendors / platform
BH1: Sales suggested price
BI1: Sales priority
BJ1: Sales pitch
BK1: Sales confidence
BL1: Print spend (last filing)
BM1: Print vendors
BN1: Print suggested price
BO1: Print priority
BP1: Print pitch
BQ1: Print confidence
A2: =QUERY({'Union profiles'!A2:AC;'International profiles'!A2:AC},"select Col27,Col4,Col2,Col1,Col3,Col5,Col6,Col8,Col9,Col12,Col14,Col15,Col16,Col17,Col18,Col20,Col21,Col19,Col22,Col23,Col24,Col25,Col26,Col11,Col7,Col29 where Col27 is not null",0)
AA2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,{'Consolidation targets'!X2:X;'International consolidation targets'!X2:X},{'Consolidation targets'!J2:J;'International consolidation targets'!J2:J}),0)))
AB2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,{'Consolidation targets'!X2:X;'International consolidation targets'!X2:X},{'Consolidation targets'!K2:K;'International consolidation targets'!K2:K}),0)))
AC2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,{'Consolidation targets'!X2:X;'International consolidation targets'!X2:X},{'Consolidation targets'!L2:L;'International consolidation targets'!L2:L}),0)))
AD2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,{'Consolidation targets'!X2:X;'International consolidation targets'!X2:X},{'Consolidation targets'!M2:M;'International consolidation targets'!M2:M}),0)))
AE2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,{'Consolidation targets'!X2:X;'International consolidation targets'!X2:X},{'Consolidation targets'!N2:N;'International consolidation targets'!N2:N}),0)))
AF2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,{'Consolidation targets'!X2:X;'International consolidation targets'!X2:X},{'Consolidation targets'!O2:O;'International consolidation targets'!O2:O}),0)))
AG2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,{'Consolidation targets'!X2:X;'International consolidation targets'!X2:X},{'Consolidation targets'!Q2:Q;'International consolidation targets'!Q2:Q}),"")))
AH2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,'Contacts & pipeline'!O2:O,'Contacts & pipeline'!L2:L),"Not in master list")))
AI2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,'Contacts & pipeline'!O2:O,'Contacts & pipeline'!K2:K),"")))
AJ2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(VLOOKUP(XLOOKUP(A2:A,'Contacts & pipeline'!O2:O,'Contacts & pipeline'!J2:J),Lists!H2:I40,2,FALSE),"")))
AK2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,'Contacts & pipeline'!O2:O,'Contacts & pipeline'!F2:F),"")))
AL2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,'Contacts & pipeline'!O2:O,'Contacts & pipeline'!G2:G),"")))
AM2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,'Contacts & pipeline'!O2:O,'Contacts & pipeline'!H2:H),"")))
AN2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,'Contacts & pipeline'!O2:O,'Contacts & pipeline'!I2:I),"")))
AO2: =ARRAYFORMULA(IF(A2:A="",,IF((V2:V="Yes")+(AH2:AH="Signed (NEP client)"),"Yes","No")))
AP2: =ARRAYFORMULA(IF(A2:A="",,N(AA2:AA)+N(AB2:AB)))
AQ2: =ARRAYFORMULA(IF(A2:A="",,TRIM(IF(N(AF2:AF)>0,"Spends "&TEXT(AF2:AF,"$#,##0")&" a year on services NEP sells. ",IF(N(O2:O)>0,"Spends "&TEXT(O2:O,"$#,##0")&" on ads and print. ",""))&IF(U2:U<>"","Pays "&U2:U&". ","")&IF(J2:J="Yes",K2:K&" comms staff on payroll. ","No comms staff on payroll. ")&IF(N(P2:P)>0,"Political and lobbying: "&TEXT(P2:P,"$#,##0")&". ","")&IF(AO2:AO="Yes","Existing NEP client.",""))))
AR2: =ARRAYFORMULA(IF(A2:A="",,IF(AJ2:AJ="","No",IFERROR(VLOOKUP(AJ2:AJ,Lists!I2:J40,2,FALSE),"No"))))
AS2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(XLOOKUP(A2:A,'Contacts & pipeline'!O2:O,'Contacts & pipeline'!P2:P),"Not in master list")))
AT2: =ARRAYFORMULA(IF(A2:A="",,F2:F&", "&G2:G))
AU2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(ROUND((DATEVALUE(X2:X&"-01")-TODAY())/30.44,0),"")))
AV2: =ARRAYFORMULA(IF(A2:A="",,TRIM(IF((AU2:AU<>"")*(AU2:AU>=0)*(AU2:AU<=12),"Election "&IFERROR(TEXT(DATEVALUE(X2:X&"-01"),"mmm yyyy"),"")&". ","")&IF(I2:I>0,"Members up "&TEXT(I2:I,"#,##0")&". ",IF(I2:I<0,"Members down "&TEXT(-I2:I,"#,##0")&". ","")))))
AW2: =ARRAYFORMULA(IF(A2:A="",,AH2:AH&IF(AI2:AI<>""," ("&AI2:AI&")","")))
AX2: =ARRAYFORMULA(IF(A2:A="",,TRIM(AK2:AK&IF(AM2:AM<>"",CHAR(10)&AM2:AM,"")&IF(AL2:AL<>"",CHAR(10)&AL2:AL,""))))
AY2: =ARRAYFORMULA(IF(A2:A="",,IF(AS2:AS="High","High",IF((AS2:AS="Medium")+(AS2:AS="Review"),"Medium","Low"))))
AZ2: =ARRAYFORMULA(IF(A2:A="",,IF(N(AC2:AC)>=N(Q2:Q),N(AC2:AC),N(Q2:Q))))
BA2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(TRIM(REGEXEXTRACT(AG2:AG,"Advocacy/political: ([^|]+)")),IF(REGEXMATCH(U2:U&"","Hustle|EveryAction|Action Network|Quorum|FiscalNote|Phone2Action|Upland|CallHub|Peerly|Scale to Win|Catalist|Twilio|PDI|OutreachCircle|Berlin Rosen|617 Media|GMMB|SKDK|Blue State|Vantage"),U2:U,""))))
BB2: =ARRAYFORMULA(IF(A2:A="",,ROUNDUP(IF(AZ2:AZ>='Pricing guide'!$B$8+'Pricing guide'!$C$8*N(H2:H),AZ2:AZ,'Pricing guide'!$B$8+'Pricing guide'!$C$8*N(H2:H))/500,0)*500))
BC2: =ARRAYFORMULA(IF(A2:A="",,IF((AZ2:AZ>=50000)+(AZ2:AZ>=10000)*((AU2:AU<>"")*(AU2:AU>=0)*(AU2:AU<=6)+(AH2:AH="Prospect (in contact)")+(AH2:AH="Quote delivered")),"1 Hot",IF((AZ2:AZ>=10000)+(N(P2:P)>=100000),"2 Warm","3 Watch"))))
BD2: =ARRAYFORMULA(IF(A2:A="",,IF(AZ2:AZ>0,"Paid "&TEXT(AZ2:AZ,"$#,##0")&" to political and advocacy vendors on its last filing"&IF(BA2:BA<>""," ("&BA2:BA&")","")&". ","No itemized advocacy vendor spend. ")&IF(N(P2:P)>0,"Political and lobbying total: "&TEXT(P2:P,"$#,##0")&". ","")&"Lead with an issue or member-mobilization campaign that runs digital ads, texting and email through one team."))
BE2: =ARRAYFORMULA(IF(A2:A="",,IF(AZ2:AZ>0,IF(AS2:AS="High","High",IF((AS2:AS="Medium")+(AS2:AS="Review"),"Medium","Spend only")),IF(AS2:AS="High","Medium","Low"))))
BF2: =ARRAYFORMULA(IF(A2:A="",,N(AP2:AP)))
BG2: =ARRAYFORMULA(IF(A2:A="",,TRIM(IF(AJ2:AJ<>"","Site: "&AJ2:AJ&". ","")&IFERROR("Web vendors: "&TRIM(REGEXEXTRACT(AG2:AG,"Website: ([^|]+)"))&". ","")&IFERROR("Member tools: "&TRIM(REGEXEXTRACT(AG2:AG,"Member comms: ([^|]+)"))&". ",IF(REGEXMATCH(U2:U&"","UnionWare|UnionTrack|Union Impact|LinkedUnion|UnionActive|MemberTrak|Broadstripes|NationBuilder|Salesforce|Hustle|Mailchimp|Constant Contact|One Call Now"),"Platforms: "&U2:U&".","")))))
BH2: =ARRAYFORMULA(IF(A2:A="",,ROUNDUP(IF(BF2:BF>='Pricing guide'!$B$6+'Pricing guide'!$B$7+('Pricing guide'!$C$6+'Pricing guide'!$C$7)*N(H2:H),BF2:BF,'Pricing guide'!$B$6+'Pricing guide'!$B$7+('Pricing guide'!$C$6+'Pricing guide'!$C$7)*N(H2:H))/500,0)*500))
BI2: =ARRAYFORMULA(IF(A2:A="",,IF((BF2:BF>=25000)+(AR2:AR="Yes")*(J2:J="No")*(N(H2:H)>=1000)+(BF2:BF>=5000)*((AH2:AH="Prospect (in contact)")+(AH2:AH="Quote delivered")),"1 Hot",IF((BF2:BF>=5000)+(AR2:AR="Yes")+(N(H2:H)>=3000),"2 Warm","3 Watch"))))
BJ2: =ARRAYFORMULA(IF(A2:A="",,IF(BF2:BF>0,"Pays "&TEXT(BF2:BF,"$#,##0")&" a year for website and member tools. ","")&IF(AJ2:AJ<>"","Website runs on "&AJ2:AJ&". ","")&IF(J2:J="No","No comms staff on payroll: lead with Connect Plus+ and a fully managed website.","Has "&K2:K&" comms staff: position NEP as their platform and production team.")))
BK2: =ARRAYFORMULA(IF(A2:A="",,IF(BF2:BF>0,IF(AS2:AS="High","High",IF((AS2:AS="Medium")+(AS2:AS="Review"),"Medium","Spend only")),IF(AS2:AS="High","Medium","Low"))))
BL2: =ARRAYFORMULA(IF(A2:A="",,IF(N(N2:N)>=N(AE2:AE),N(N2:N),N(AE2:AE))))
BM2: =ARRAYFORMULA(IF(A2:A="",,IFERROR(TRIM(REGEXEXTRACT(AG2:AG,"Print/magazine: ([^|]+)")),IF(REGEXMATCH(S2:S&"","(?i)press|print|publish|graphic|mail|litho"),S2:S,""))))
BN2: =ARRAYFORMULA(IF(A2:A="",,ROUNDUP(IF(BL2:BL>='Pricing guide'!$B$9+'Pricing guide'!$C$9*N(H2:H),BL2:BL,'Pricing guide'!$B$9+'Pricing guide'!$C$9*N(H2:H))/500,0)*500))
BO2: =ARRAYFORMULA(IF(A2:A="",,IF((BL2:BL>=50000)+(BL2:BL>=10000)*((AH2:AH="Prospect (in contact)")+(AH2:AH="Quote delivered")),"1 Hot",IF((BL2:BL>=10000)+(N(H2:H)>=10000),"2 Warm","3 Watch"))))
BP2: =ARRAYFORMULA(IF(A2:A="",,"Paid "&TEXT(BL2:BL,"$#,##0")&" for printing, publications and mail on its last filing"&IF(BM2:BM<>""," ("&BM2:BM&")","")&". About "&TEXT(N(H2:H),"#,##0")&" members to reach. Lead with a member magazine or mail program printed in a CWA union shop under the union label."))
BQ2: =ARRAYFORMULA(IF(A2:A="",,IF(BL2:BL>0,IF(AS2:AS="High","High",IF((AS2:AS="Medium")+(AS2:AS="Review"),"Medium","Spend only")),IF(AS2:AS="High","Medium","Low"))))
```

## Method & caveats

```
A1: METHOD & CAVEATS (rebuilt Nov. 11, 2026 for all unions)
A2: Source: U.S. DOL Office of Labor-Management Standards (OLMS) yearly LM data downloads from the Online Public Disclosure Room. Each union appears once, using its most recent report: the 2026 data year when filed, otherwise 2025. Terminated unions are excluded.
A3: Scope: every union that files with OLMS. Unions representing only state or local government employees (most fire, police, teacher and municipal locals) do not file with OLMS and are not included. Federal and postal unions do file and are included.
A4: Union profiles: every LM-2 filer (unions with $250,000+ in annual receipts). LM-2 reports itemize staff titles and vendor payments.
A5: Small locals (LM-3, LM-4): smaller unions. These reports do not list vendors or staff titles, so only size, location, finances and election timing are available.
A6: Sectors and update days come from the Affiliate map tab. Edit a sector or update day there and the weekly tasks follow it. SMART rail and transportation units are classified as Transportation.
A7: Comms staff: officers and employees whose reported title matches communications, media, marketing, digital, social media, video, editor, publications, public affairs, press, or outreach terms. In the trades, 'Marketing Representative' is often an organizing or contractor-relations role.
A8: Spend figures: itemized disbursements only (payments of $5,000+ to a single vendor in a year), classified by keywords in the purpose, vendor type and vendor name. Figures are floors, not totals. Player licensing, royalties and residuals are excluded from ad and print spend.
A9: Political & lobbying total: Schedule 16 total, which includes staff time allocated to political work.
A10: Top technology vendors: software, IT, computers, cloud, telecom and union membership platforms. A vendor in a union's top four comms vendors stays in the comms column and is left out of the technology column.
A11: Competitor watch: payments to a defined list of agencies, member platforms, advocacy, texting and voter data tools (including PDI and OutreachCircle, added Nov. 12, 2026), print, sports sponsorship and media monitoring vendors, matched by vendor name. Both 2025 and 2026 data years are kept.
A12: Consolidation targets: LM-2 unions paying at least three different vendors across at least three NEP service lines (website, member comms, advocacy/political, social/digital/ads, print/magazine). Merchandise, events, donations, other unions, PACs, campaign committees, and payments to airlines are excluded. Tier 1 = 4+ services and $150K+ addressable spend; Tier 2 = 3+ services and $50K+; Tier 3 = smaller; unions already paying NEP are 'Existing NEP client: expand'.
A13: Membership change compares reported membership with the union's prior-year report. Next officer election is as reported by the union.
A14: Weekly updates: Monday through Thursday each refresh one group of sectors (see Affiliate map). Friday refreshes Small locals and the Summary and sends the weekly digest. Rows are added or updated in place with a Last updated date; nothing is deleted. Consolidation targets that drop below the threshold are marked 'No longer qualifies'.
A15: All classification is keyword-based. Review vendor detail before outreach.
A16: International unions: national and international headquarters (OLMS designation NHQ) are kept in their own tabs, International profiles and International consolidation targets, with the same columns as Union profiles and Consolidation targets. Summary totals include both.
A17: Team views (Executive brief, Advocacy & political, Sales: websites & Connect Plus+, Print & magazine, Competitor takeaway) are formulas. They update automatically when the weekly refresh adds filings. Change the yellow dropdown cells to filter; do not type over the results.
A18: Prospect index: one row per LM-2 union (locals and internationals) combining DOL data, consolidation dollars, and the best matching record from Contacts & pipeline. All team views read from it. Do not edit it by hand.
A19: Contacts & pipeline: every union record from the NEP MASTER Union Database (the Google Sheet owned by Mark Treglio, ID 1J-bzg1r3DrMxpv-QgZPVeKkzOyilSKZzlUtAL4pMMTw, the official master list as of Nov. 12, 2026), normalized into one table with pipeline stage (from the SIGNED / QUOTES DELIVERED / PROSPECTS / READY TO CALL sections), website provider, NEP rep and notes. Re-imported automatically every weekday afternoon, so edits made in the master list show up here the same day. Matched to DOL filings on affiliate + local number + state: 'High' = all three matched; 'Medium' = only one DOL union with that affiliate and number, state missing; 'Review' = several possible matches.
A20: Pipeline stage 'Competitor client list' marks records from the master list's ULW Clients and LinkedUnion Clients tabs. 'Signed (NEP client)' comes from the master list's SIGNED sections and client tabs.
A21: NEP client (any source) = the union paid NEP Services in its DOL filing OR is marked Signed in the master list.
A22: Call lists (Advocacy & political, Sales, Print & magazine): Priority is Hot, Warm or Watch, scored from spend in that service line, election timing, membership and pipeline stage. Confidence is High, Medium, Spend only or Low (legend on each tab).
A23: Suggested starting price = the higher of the union's current spend in that service line or the Pricing guide floor plus per-member rate, rounded up to the nearest $500, so it never falls below what the union already pays. Pricing guide inputs are estimates until leadership replaces them with NEP's rate card.
A24: Lead card: pick any union for a one-screen brief combining spend, suggested prices, vendors, pipeline, contact and pitch by team.
```

## Lists

```
A1: State
B1: Sector
C1: Website provider
D1: Pipeline stage
E1: Competitor
F1: Data year
H1: Provider as listed
I1: Clean provider name
J1: Competitor platform?
A2: ={"All";SORT(UNIQUE(FILTER('Prospect index'!G2:G,REGEXMATCH('Prospect index'!G2:G&"","^[A-Z]{2}$"))))}
B2: ={"All";SORT(UNIQUE(FILTER('Prospect index'!D2:D,'Prospect index'!D2:D<>"")))}
C2: All
D2: ={"All";"Not in master list";SORT(UNIQUE(FILTER('Contacts & pipeline'!L2:L,'Contacts & pipeline'!L2:L<>"")))}
E2: =SORT(UNIQUE(FILTER('Competitor watch'!D2:D,'Competitor watch'!D2:D<>"")))
F2: =SORT(UNIQUE(FILTER('Competitor watch'!A2:A,'Competitor watch'!A2:A<>"")),1,FALSE)
H2: Self-managed
I2: Self-managed
J2: No
C3: Any competitor platform
H3: UnionActive
I3: UnionActive
J3: Yes
C4: UnionActive
H4: Union Labor Works
I4: Union Labor Works
J4: Yes
C5: LinkedUnion
H5: LinkedUnion
I5: LinkedUnion
J5: Yes
C6: Union Labor Works
H6: UnionCentrics
I6: UnionCentrics
J6: Yes
C7: UnionCentrics
H7: Web Connectivity
I7: Web Connectivity
J7: Yes
C8: Web Connectivity
H8: BMA Media Group
I8: BMA Media Group
J8: Yes
C9: BMA Media Group
H9: NEP
I9: NEP
J9: No
C10: Union Web Services
H10: Union Web Services
I10: Union Web Services
J10: Yes
C11: Harborside
H11: UnionWebServices
I11: Union Web Services
J11: Yes
C12: Prometheus
H12: Prometheus
I12: Prometheus
J12: Yes
C13: Union Up
H13: Harborside
I13: Harborside
J13: Yes
C14: MemberTrak
H14: Data Research Group
I14: Data Research Group
J14: Yes
C15: Self-managed
H15: UnionUp
I15: Union Up
J15: Yes
C16: NEP
H16: Union Up
I16: Union Up
J16: Yes
C17: No provider listed
H17: MOPRO
I17: MoPro
J17: Yes
H18: Mopro
I18: MoPro
J18: Yes
H19: Membertrak
I19: MemberTrak
J19: Yes
H20: MemberTrak
I20: MemberTrak
J20: Yes
H21: Intelligent Design
I21: Intelligent Design
J21: Yes
H22: Mosaic
I22: Mosaic
J22: Yes
H23: Your First Due
I23: Your First Due
J23: Yes
H24: YouTech
I24: YouTech
J24: Yes
H25: Velarium
I25: Velarium
J25: Yes
H26: Slytek Designs
I26: Slytek Designs
J26: Yes
H27: WeBrand Digital
I27: WeBrand Digital
J27: Yes
H28: J. Arthur & Associates
I28: J. Arthur & Associates
J28: Yes
H29: Wix
I29: Wix
J29: No
H30: WordPress
I30: WordPress
J30: No
H31: Squarespace
I31: Squarespace
J31: No
H32: GoDaddy
I32: GoDaddy
J32: No
```
