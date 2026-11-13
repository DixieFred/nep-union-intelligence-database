# Hot list of buying signals

Status: Phase 1 built Nov. 12, 2026 as tabs in the sheet (Hot list, Signals log, Lead status). Slack or email delivery may come later.

## As built

- **Signals log tab:** one row per signal (date, union, file #, signal, detail, points, team, filing period, key, weight now). Seeded with 1,832 signals from the 2025 vs. 2026 filings and upcoming elections. The weekday refresh appends new signals for that day's sectors (scripts/signals.js), deduplicated by key.
- **Hot list tab:** one formula ranks the top 25 unions by decayed points over 60 days, with Team and Show NEP clients filters, top three signals as "why now," suggested price, status, contact and lead status.
- **Lead status tab:** reps log Called / Meeting set / Proposal sent / Not interested / Won. Won and Not interested drop off the hot list.
- Leadership changes come from officer names on the filings (president, business manager, executive director).
- Pipeline-stage signals and quote aging are not built yet (Phase 2).

## Purpose

Rank the unions most likely to buy right now and tell each team who to call this week and why.

## How it works

1. **Signals log tab.** One row per detected signal: date, union, OLMS file #, signal type, detail, points, team, status.
2. **Daily task writes to it.** Before the refresh overwrites a union's row, it compares old and new values and logs any signal.
3. **Hot list tab (formulas).** Sums each union's signal points over the last 14 days, with points losing half their value after two weeks. Shows the top 25 with a one-line "why now," owning team, suggested price and contact. NEP clients go to a separate "expand" section.
4. **Friday digest.** Adds the top 10 hot leads to the weekly digest.
5. **Feedback loop.** Reps mark each lead Called, Meeting set, Not interested or Won; weights are adjusted after a quarter.

## Signals and starting points

| Signal | Points |
|---|---|
| Officer election within 6 months | 3 |
| New president or business manager on the filing | 5 |
| Comms staffer hired or left | 4 |
| Spend in a service line up 25% or more | 3 |
| Dropped a competitor | 5 |
| Started paying a competitor | 1 |
| Newly Tier 1 or Tier 2 | 4 |
| Membership growing fast or falling | 2 |
| Pipeline stage moved up (master list) | 3 |
| Quote unanswered 30+ days | 2 |
| News Watch hit (phase 2) | 4 |
| New Meta ads (phase 3) | 3 |
| Outdated competitor-platform website (phase 3) | 2 |

## Phases

| Phase | Scope |
|---|---|
| 1 | DOL signals, Signals log, Hot list tab, Friday digest |
| 2 | Pipeline signals, News Watch tie-in |
| 3 | Meta Ad Library and website checks |

## Cautions

- DOL filings lag up to 90 days after a union's fiscal year, so election timing and pipeline signals are the freshest.
- A signal is a reason to call, not proof of buying intent.
- Cap the list and decay old points so it stays short enough to act on.
