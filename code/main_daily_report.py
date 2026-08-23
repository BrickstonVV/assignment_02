"""
main_daily_report.py — the Operations department's report.

Finance asked *what did we sell?* and Marketing asked *which products sell?*
Operations asks a third question: *when do we sell?* Same eleven rows, same
pipeline, grouped down a different column — because staffing a shop floor needs
the calendar, not the catalogue.

**You write this file yourself.** `main_finance_report.py` and
`main_marketing_report.py` are your worked examples: this report has the same
three-step shape and mostly calls functions that already exist. The one new piece
is `summarize_by_day`, which you add to `sales_pipeline.transform` — and once it
exists, `find_top_entry` ranks days exactly as happily as it ranks items, because
it never cared what an entry *was*, only which field to compare.

That is the lesson worth taking away: a third report needed one new function, not
a third script.

Before running:  pip install -r requirements.txt

    python code/main_daily_report.py        # the fixed sample data
    python code/main_daily_report.py 42     # the generated data for seed 42
"""

import sys

# TODO: import the functions you need from the sales_pipeline package.
#       Import the names you need, not the whole module.


# An optional command-line argument picks which dataset to report on. A missing
# argument — or a blank one, which is what VS Code sends when you clear the seed
# prompt — means "use the sample data". See README Reference #7.
# TODO: set `seed` to None, or to int(sys.argv[1]) when a non-blank one was given.


# You are on your own for this one. main_finance_report.py and
# main_marketing_report.py are your worked examples: same three-step shape, same
# rule that no arithmetic or formatting belongs in a report.
#
# README Step 9 shows the exact output your report must produce.
# TODO: write the report.
