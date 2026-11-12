# Architecture

## Data flow

```
DOL OLMS yearly export (LM-2, LM-3, LM-4, payees)
        │  scripts/olms_build_all.js (runs in the browser on the scheduled task)
        ▼
Union profiles / International profiles / Consolidation targets /
International consolidation targets / Competitor watch / Small locals
        │
NEP MASTER Union Database (Josh's Google Sheet, read only)
        │  scripts/master_import.py (Fridays)
        ▼
Contacts & pipeline
        │
        ▼
Prospect index (formula-driven join + scoring)
        │
        ▼
Executive brief · Lead card · Advocacy & political · Sales: websites & Connect Plus+ ·
Print & magazine · Competitor takeaway
```

## Tabs (in order)

| # | Tab | Sheet ID | Role |
|---|---|---|---|
| 1 | Executive brief | 4006 | KPIs, spend by service line, top 10 locals and internationals, top competitors |
| 2 | Lead card | 4009 | Pick any union in B3 for a one-screen brief and bundle price |
| 3 | Advocacy & political | 4002 | Call list for advocacy, political and social media |
| 4 | Sales: websites & Connect Plus+ | 4003 | Call list for web and member communications |
| 5 | Print & magazine | 4004 | Call list for print and magazine work |
| 6 | Competitor takeaway | 4005 | Unions paying named competitors |
| 7 | Pricing guide | 4008 | Editable floors and per-member rates |
| 8 | Wish list | 4010 | Future enhancements and status |
| 9 | Sector summary | 714225318 | Rollups by sector |
| 10 | Prospect index | 4001 | One row per LM-2 union; every view reads from it |
| 11 | Contacts & pipeline | 62730694 | Normalized master list (never rename or delete) |
| 12 | Consolidation targets | 2086830485 | Locals and councils with addressable spend |
| 13 | International consolidation targets | 3001 | Same, for internationals |
| 14 | Union profiles | 1992334929 | Full DOL profile per local or council |
| 15 | International profiles | 3002 | Full DOL profile per international |
| 16 | Competitor watch | 535828913 | Payments to competitor vendors |
| 17 | Small locals (LM-3, LM-4) | 1201932970 | Smaller filers |
| 18 | Affiliate map | 2107548225 | Affiliate to sector mapping |
| 19 | Method & caveats | 2114443140 | Plain-language method notes |
| 20 | Lists (hidden) | 4007 | Dropdown values, provider cleanup, competitor platforms |

## Design principles

- **Views are formulas, not copies.** Call lists, Lead card and Executive brief are QUERY/XLOOKUP formulas over Prospect index, so a refresh updates everything.
- **Filters are dropdowns.** Yellow cells on rows 4 and 5 of each call list build the QUERY where clause.
- **Master list is read only.** The database copies it in; it never writes back.
