# NEP Union Intelligence Database

Historical record of how NEP Services built its union prospecting database (November 2026). It documents the sources, logic, formulas, scheduled refresh and decisions so the system can be understood, audited or rebuilt later.

**Owner:** Josh Friedrich, Director of Digital Advocacy, NEP Services
**Built:** Nov. 11, 2026, with Claude (Cowork)
**Status:** Live in Google Sheets; refreshed automatically each weekday
**Last updated:** Nov. 12, 2026

## What it is

A Google Sheet ("NEP Union Intelligence Database") that joins U.S. Department of Labor OLMS union financial filings with NEP's MASTER Union Database to show, for every union that files an LM-2:

- what it spends on websites, member communications, advocacy, political work and print
- which vendors and competitors it pays today
- whether it is already an NEP client or in NEP's pipeline
- a suggested starting price that never undercuts what the union already pays
- a confidence level for the match and the spend data

It is intentionally separate from HubSpot. HubSpot integration is deferred pending a conversation with NEP's CTO.

## Repository contents

| Path | What it holds |
|---|---|
| `docs/architecture.md` | Tab-by-tab structure, data flow, sheet IDs |
| `docs/methodology.md` | Classification, tiers, master-list matching, confidence, pricing |
| `docs/data-dictionary.md` | Prospect index columns and call-list columns |
| `docs/scheduled-refresh.md` | How the weekday refresh runs and its safeguards |
| `docs/decisions-log.md` | Key decisions and the reasoning behind them |
| `docs/build-history.md` | Build sequence, problems found and how they were fixed |
| `docs/wish-list.md` | Snapshot of the Wish list tab |
| `docs/hot-list-design.md` | Hot list of buying signals: design and what was built |
| `scripts/signals.js` | Browser-side function that detects buying signals between two filings |
| `scripts/olms_build_all.js` | Browser-side builder that turns the OLMS export into profile and consolidation rows |
| `scripts/master_import.py` | Normalizes and matches the master list into Contacts & pipeline |
| `scheduled-task/weekday-refresh-prompt.txt` | Full instructions the scheduled task runs |
| `sheet-formulas/formulas.md` | Formulas and reference values exported from the live sheet |
| `config/affiliate_map.csv` | Affiliate abbreviation to name and sector mapping |

## What is deliberately not in this repo

- Contact names, phone numbers and emails from the master list
- Pipeline notes and any client-specific pricing

Those stay in Google Sheets. Keep this repository **private**; it still describes NEP's competitive approach and internal pricing estimates.

## Headline numbers at build (2025 filings)

| Measure | Value |
|---|---|
| Unions filing LM-2 | 4,576 |
| Consolidation targets | 231 (71 Tier 1) |
| Yearly addressable spend | About $288 million |
| Existing NEP clients found | 41 |
| Targets already in pipeline | 87 |
| Targets not in master list | 144 |
| Paid to competitors | About $94.9 million |
| LM-2 unions on a competitor website platform | 751 |

Spend figures are minimums: OLMS only itemizes payments of $5,000 or more.
