"""
main_finance_report.py — the Finance department's report.

Finance cares about the audit trail: every transaction, and what the whole day
earned.

This file is an *interface*, not a library. Notice how little it does: it calls
the pipeline in order and arranges the output. Every calculation lives in
`sales_pipeline.transform`, every bit of formatting lives in
`sales_pipeline.display`. If you find yourself doing arithmetic in this file,
that logic belongs in the package instead — where it can be unit tested and where
Marketing can reuse it.

Before running:  pip install -r requirements.txt

    python code/main_finance_report.py        # the fixed sample data
    python code/main_finance_report.py 42     # the generated data for seed 42
"""

import sys

# TODO: import the functions you need from the sales_pipeline package.
#       Import the names you need, not the whole module.


# An optional command-line argument picks which dataset to report on. A missing
# argument — or a blank one, which is what VS Code sends when you clear the seed
# prompt — means "use the sample data". See README Reference #7.
# TODO: set `seed` to None, or to int(sys.argv[1]) when a non-blank one was given.


# TODO: print the report header, exactly:  === FINANCE: Daily Sales Detail ===
#       followed by a blank line.


# 1. Extract — get the raw data out of the source system.
# TODO


# 2. Transform — clean it and total it.
# TODO


# 3. Load — put it in front of a human: the detail table, a blank line, then the
#    total formatted as  Total Pipeline Revenue: $1,528.00
# TODO
