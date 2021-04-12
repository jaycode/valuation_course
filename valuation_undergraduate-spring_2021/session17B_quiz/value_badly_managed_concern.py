# Session 17D post-class test problem 4
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session17Dtest.pdf

"""
You are valuing an emerging market company that is family controlled and has a
history of bad management. When you value the company, you assume that it
will continue to be run as it has historically, taking projects that earn a return on
capital of 6% in perpetuity, even though they have a cost of capital of 10%. If the
growth rate in perpetuity is 3% and the firm expects to generate after-tax
operating income of $20 million next year, estimate the value of the operating
assets.
"""

import sys
sys.path.append("../../")
from modules.valuation.terminal_value import terminal_value


if __name__ == "__main__":
    atax_opin = 20
    gr = 0.03
    roc = 0.06
    coc = 0.1

    print("Reinvestment rate:", gr/roc)
    tv = terminal_value(atax_opin, roc, coc, gr)
    print("Terminal Value/Value of Operating Assets:", tv)

    # Output:
    #
    # Reinvestment rate: 0.5
    # Terminal Value/Value of Operating Assets: 142.85714285714283
