# Scheduled refresh

- **Name:** Weekday OLMS union prospect refresh
- **Schedule:** Weekdays, 1:43 p.m. Central
- **Runs on:** Josh's Mac mini through the Claude desktop app's built-in browser (OLMS downloads require a real browser session)
- **Full instructions:** `scheduled-task/weekday-refresh-prompt.txt`

## What it does

1. Downloads the latest OLMS yearly data.
2. Runs the builder (`scripts/olms_build_all.js`) to rebuild profile, consolidation, competitor and small-locals rows.
3. Writes those tabs; formula views update automatically.
4. Fridays: re-imports the master list into Contacts & pipeline (`scripts/master_import.py`).

## Safeguards

- Skips the master-list replace if the new record count is below 80 percent of the current count.
- Never edits the master list and never renames or deletes Contacts & pipeline.
- Changes to the task's instructions must be re-approved on the Mac mini before they take effect.
