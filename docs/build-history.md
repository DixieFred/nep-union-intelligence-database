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
