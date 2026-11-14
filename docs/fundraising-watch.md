# Fundraising watch (built Nov. 13, 2026)

Police, fire, sheriff and EMS organizations that use professional fundraisers (telemarketing, mail, ad books, events), from IRS Form 990 Schedule G. Tab "Fundraising watch" in the database. Feeds the Help a Hero pitch and the Print Division dashboard.

## Source

- IRS e-file 990 XML, published monthly at apps.irs.gov/pub/epostcard/990/xml/<year>/ as `index_<year>.csv` plus `<year>_TEOS_XML_<MM><A-D>.zip` batches.
- Window: filings the IRS released in the current year and the prior year (2026 and 2025 at build). Fiscal years therefore end in 2024 and 2025.
- Organizations selected by name (fire, police, FOP, sheriff, deputies, troopers, EMS, public safety and similar), Form 990 only (990-EZ has no Schedule G Part I). Excludes Eagles aeries, pension, retirement, relief associations, credit unions, insurance.
- From each filing: Schedule G Part I fundraiser rows (name, activity, gross receipts, retained by fundraiser, net to organization), Part IX line 11e professional fundraising fees when no fundraiser is itemized, plus header contact fields.

## How it runs

- The cloud container cannot reach apps.irs.gov, so the scan runs as JavaScript in Claude's built-in browser on a page at https://apps.irs.gov/app/eos/ (same origin). See `scripts/fundraising_990_scan.js`.
- Zips are read with HTTP range requests (central directory, then each needed entry), not downloaded whole.
- Gotchas found at build:
  - Some batches use Deflate64 (zip method 9), which browsers cannot decompress. The script includes a small Deflate64 inflater. In 2025/2026 this affected the 05A/05B and 2025 11B batches.
  - The index can name a batch (e.g. 05A) while the file sits in a sibling (05B). The script falls back to sibling letters A to G.
- `scripts/fundraising_build.py` dedupes amended returns (latest object per EIN and tax period), classifies method, org type and priority, and writes the xlsx that is pasted into the tab.

## Priority (Help a Hero)

- 1 High: organization received under 50% and gross raised was $100,000 or more.
- 2 Medium: organization received under 50%, or the fundraiser kept $50,000 or more.
- 3 Low: everything else; non-itemized rows under $25,000 in fees.
- Print angle = Yes when the method includes mail or ad book / magazine / sponsor sales.

## At build (Nov. 13, 2026)

- 5,962 filings scanned; 583 rows; 314 organizations.
- Telemarketing (phone): 121 rows, 55 organizations, $23.8M raised, $17.8M kept by fundraisers (median share to organization about 21%).
- About 176 rows report fundraising fees without naming the fundraiser; a few filings show inconsistent amounts (check the 990 before quoting).

## Refresh

Scheduled task "Monthly Fundraising watch refresh", 5th of each month at 2:55 p.m. Central, runs on Josh's Mac mini (built-in browser). Full instructions: `scheduled-task/monthly-fundraising-refresh-prompt.txt`. Writes nothing if the new row count is below 70% of the old.

## Kept out of the Competitor list

Telemarketing and fundraising firms stay in this tab only (Josh, Nov. 13): they rarely appear as payees in union filings, so the Competitor list scans would not find them.
