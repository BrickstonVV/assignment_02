"""
main_marketing_report.py — the Marketing department's report.

Marketing does not care about individual transactions. They care about *products*:
which one earns the most money, and which one moves the most units. Those are
frequently not the same product, and the gap between them is the interesting part.

This is the payoff for building a package instead of a script. Marketing needs a
roll-up that Finance never asked for, so `summarize_by_item` and `find_top_entry`
were **added** to `sales_pipeline.transform` — and `main_finance_report.py` did
not change by a single character. That is what modular means: the package grows
by addition, not by editing everyone who already depends on it.

Before running:  pip install -r requirements.txt

    python code/main_marketing_report.py        # the fixed sample data
    python code/main_marketing_report.py 42     # the generated data for seed 42
"""

import sys

# TODO: import the functions you need from the sales_pipeline package.
#       Import the names you need, not the whole module.


# An optional command-line argument picks which dataset to report on. A missing
# argument — or a blank one, which is what VS Code sends when you clear the seed
# prompt — means "use the sample data". See README Reference #7.
# TODO: set `seed` to None, or to int(sys.argv[1]) when a non-blank one was given.


# TODO: print the report header, exactly:  === MARKETING: Revenue by Item ===
#       followed by a blank line.


# 1. Extract — the same source Finance uses, called the same way.
# TODO


# 2. Transform — clean, then roll the rows up to one entry per item, then find the
#    top entry twice: once by "revenue" and once by "units_sold".
# TODO


# 3. Load — the item table, a blank line, then the two headline lines. Line them up
#    so the values start in the same column:
#        Top seller by revenue: Gizmo Pro ($1,200.00)
#        Top seller by units:   Widget C (15 units)
# TODO
