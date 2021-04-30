9
# Session 17D post-class test problem 2
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session17Dtest.pdf

"""
You are valuing GenStore, an aging retail firm, and you expect it to generate $50
million in after-tax operating income next year. You expect these earnings to
decline 2% a year, in perpetuity, and you expect your return on capital to be
10% forever. If your cost of capital is 8%, and you have $250 million in net debt
(based on market value of debt today), estimate the value of equity today.
"""

import sys
sys.path.append("../../")
from modules.valuation.terminal_value import terminal_value

if __name__ == "__main__":
    atax_opin = 50
    gr = -0.02
    roc = 0.1
    coc = 0.08
    debt = 250

    print("Reinvestment rate:", gr/roc)
    tv = terminal_value(atax_opin, roc, coc, gr)
    print("Terminal Value:", tv)
    print("FCFF:", tv-debt)

    # Output:
    #
    # Reinvestment rate: -0.19999999999999998
    # Terminal Value: 600.0
    # FCFF: 350.0
