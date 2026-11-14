# Print Division dashboard (Jordan) (started Nov. 13, 2026)

A dashboard for Jordan (print division) and his reps showing who to call, what they spend on print, and who has the work now.

## Decisions (Josh, Nov. 13, 2026)

- Jordan decides who gets called; reps view the dashboard.
- Print lead: a buyer that pays a competitor on the Competitor list with category Print, or whose purchase is described as printing, publications or mail.
- Fundraising leads on the dashboard are telemarketing (phone) leads from Fundraising watch.
- What reps update after a call: to be decided.
- NEP branding (black wordmark, blue double-bar accent, blue dot, www.NEPServices.com).
- Platform: Looker Studio for the dashboard, Google Sheets as the data source. Josh builds the report from the build guide.
- Status: build on hold until Jordan sends his wish list.

## Data source sheet

"Print Dashboard Data (Looker Studio source)" (Google Sheet ID 1YbbN4bNcnJuqEwywOqzUAkykOvl4kSHvyOPOXetIKG4). Reads the database with IMPORTRANGE and never writes back.

| Tab | Contents | Edited by |
|---|---|---|
| Union leads | Print & magazine rows plus Lead ID, State, competitor flag, assigned rep, rep email, date assigned | Formulas |
| Telemarketing leads | Fundraising watch rows whose method includes Phone, plus assignment fields | Formulas |
| Who has the work | Each union print vendor payment split out, with competitor flag | Formulas |
| Assignments | Lead ID (dropdown), lead type, lead name, assigned rep (dropdown), date, notes | Jordan (protected) |
| Reps | Rep name and exact Google email (drives Looker Studio filter by email) | Josh / Jordan (protected) |
| _raw_union, _raw_fund, _raw_comp, _lists | Hidden imports and dropdown lists | Nobody |

Lead IDs: "U-" + union name; "T-" + organization + " (state)". Formulas: `sheet-formulas/print-dashboard-data.md`.

Gotcha: LET variable names that look like cell references (for example `rep0`) break the formula with #ERROR!; use names like `repraw`.

## Looker Studio design

- Five data sources: Union leads, Telemarketing leads, Who has the work (unfiltered) and My union leads, My telemarketing leads (Filter by email on Rep email).
- Pages: Overview, Union print buyers, Telemarketing leads, Who has the work now, My leads.
- Full step-by-step build: Claude Doc "Looker Studio Build Guide: Print Division Dashboard".
- Visual reference: Design artifact "Print Division Dashboard Mockup"; scope: Claude Doc "Print Division Dashboard: Scope and Starting Point".
