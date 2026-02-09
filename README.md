# fashion-reseller-inventory-ai
Prototype AI decision-support workflow for small fashion resellers’ inventory decisions.

# AI Decision-Support for Fashion Reseller Inventory

Prototype for an AI-powered workflow that helps small fashion resellers decide how much to test into new trends, using their historical sales data plus Google Trends.

## Contents
- `script.py` – main analysis and logic
- `cleaned_resale_data.csv` – sample input data structure
- `ai_prompt_example.md` – example of the AI prompt used

## How it works

1. Historical resale data is cleaned and grouped by trend tag.
2. The script calculates average payout, sell-through time, and item count.
3. Summary statistics are visualized in a trend performance table.
4. An AI prompt combines this data with sourcing constraints to recommend a conservative test-buy plan.

## Design principles

- AI is used for decision support, not prediction.
- Recommendations are intentionally conservative.
- User constraints (budget, time, sourcing method) are treated as first-class inputs.
- The system favors small test buys over inventory scaling.


## Non-goals

- This project does not forecast demand or guarantee sales.
- It does not automate buying or listing decisions.
- It is not intended for large-scale or enterprise resellers.



