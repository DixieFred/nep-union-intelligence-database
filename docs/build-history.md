# Build history

1. Pulled OLMS LM-2, LM-3 and LM-4 filings and payee detail; classified spend by service line.
2. Built Union profiles, Consolidation targets, Competitor watch and Small locals; then split internationals into their own tabs.
3. Normalized the master list into Contacts & pipeline and matched records to OLMS file numbers.
4. Built Prospect index as the single join, then the Executive brief, team call lists, Competitor takeaway and Sector summary.
5. Added suggested pricing, the confidence legend, Pricing guide, Lead card and Wish list.
6. Set up the weekday scheduled refresh, including the Friday master-list re-import.
7. Fixed Steelworkers coverage.

## Problems found and fixed

| Problem | Fix |
|---|---|
| Rounding produced prices a few dollars below current spend | Switched to ROUNDUP; verified zero undercuts |
| Bundle price could fall below total spend | Added MAX against total addressable spend |
| Junk website-provider values (e.g., member counts) | Whitelist mapping on the hidden Lists tab |
| Apostrophe in a QUERY label broke the call lists | Renamed the label to "Why they are a fit" |
| Solid spend shown as Low confidence when unmatched | Added "Spend only" level |
| USW locals missed (district prefix, stacked rows) | Import script handles both; re-imported |
| Merges failed across frozen columns | Unfroze before merging |

## 2026-11-13: Competitor list drives the vendor scan
- New "Competitor list" tab (70 vendors, tiers Us / Direct / Adjacent / Track only / Lead source). Its Match pattern column is now the only source of vendor regexes; the weekday refresh reads it in Step 1, so adding a row takes effect on the next run.
- Category "Voter data (partner)" (L2) is tracked but excluded from competitor totals, the Executive brief and competitor signals.
- Backfill from 2025 and 2026 DOL filings: 189 new Competitor watch rows (Doyle Printing 50, Mosaic 44, K&R Branding 41, Unions America 14, Velarium 13, Campaign Workshop 7, Arandell 5, Clowder 5, ActBlue 4, M+R 2, 911 Media 2, Hamburger Group 1, Team Civx 1). Updated 82 Union profiles, 39 International profiles, 29 Consolidation targets and 37 International consolidation targets; 14 new competitor signals.
- No DOL matches yet for Unionly, L2 or WinRed. UnionActive is billed as "UNIONS-AMERICA.COM, INC", so it appears under Unions America.
- Competitor takeaway dropdown (Lists!E) now reads from the Competitor list tab.

## 2026-11-13: UA naming
- United Association locals (OLMS code PPF) now display as "UA" (for example "UA Local 9"). Renamed 557 existing organization cells across profiles, targets, Competitor watch, Small locals and Signals log, plus 538 affiliate codes in Contacts & pipeline. The build function and master import now produce UA going forward. The OLMS code PPF stays in the Affiliate map because that is DOL's code.
- K&R Branding moved from Direct to Adjacent (Josh, Nov. 13).
