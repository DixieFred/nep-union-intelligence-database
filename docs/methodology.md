# Methodology

## Sources

- **DOL OLMS** yearly union financial disclosures (LM-2, LM-3, LM-4) and itemized payee schedules.
- **NEP MASTER Union Database** (Google Sheet, official master as of Nov. 11, 2026).

## Spend classification

Itemized LM-2 disbursements are classified by payee and purpose into service lines: website, member communications, advocacy, digital, print and political. Only payments of $5,000 or more are itemized by the DOL, so every spend figure is a floor, not a total. Since Nov. 12, 2026 the build also adds each vendor's non-itemized amount from the payer/payee file, so a vendor paid $5,000+ in the year in smaller installments is counted in full. Those amounts are classified by vendor name and type (and the vendor's first itemized purpose, when there is one).

## Sectors and levels

Affiliates map to sectors through `config/affiliate_map.csv`. SMART transportation units are routed to the Transportation sector by unit name. Internationals are split into their own profile and consolidation tabs.

## Master-list matching

Each master-list record is normalized (affiliate, local number, city, state) and matched to an OLMS file number. Match confidence is High, Medium or Review.

USW note: the DOL drops the district prefix, so "Local 12-591" in the master list is OLMS Local 591. The import handles this, and also parses the Steelworkers tab's stacked layout (name line followed by a "City, ST" line and an "Office:" phone line).

## Priority

Each team column set scores every union as 1 Hot, 2 Warm or 3 Watch based on spend in that service line, timing (months to next election) and relationship status.

## Confidence (shown on every call list)

| Level | Meaning |
|---|---|
| High | Spend on file and a high-confidence match to our master list |
| Medium | Spend on file with a medium or review-level match, or a strong match without spend |
| Spend only | Reliable DOL spend, but not matched to our master list |
| Low | No spend in that line and no strong match |

## Pricing

Suggested starting price (per year) for each service line:

```
ROUNDUP( MAX(current spend in that line, floor + rate x members) / 500 ) x 500
```

| Line | Floor | Per member |
|---|---|---|
| Website | $9,000 | $0.10 |
| Connect Plus+ | $3,000 | $1.00 |
| Advocacy | $18,000 | $0.50 |
| Print | $6,000 | $2.00 |

These are **estimates** pending NEP's approved rate card. Rules: never quote below what the union already pays; term and billing questions go to Scott Welkley. The Lead card bundle price is never below the union's total addressable spend.
