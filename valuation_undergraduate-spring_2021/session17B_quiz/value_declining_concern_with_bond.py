# Session 17D post-class test problem 3
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session17Dtest.pdf

"""
Now assume that you were told that the debt in GenStore is publicly traded and
takes the form of one zero coupon bond with ten years to maturity and a face
value of $400 million. Estimate the probability of failure that the bond market is
attaching to the firm, and your equity value, if it is worth nothing in the event of
failure. (The riskfree rate is 3%)
"""

import sys
sys.path.append("../../")
from modules.valuation.terminal_value import terminal_value

def pv(fv, num_periods, interest):
    pv = fv / (1 + interest)**num_periods
    return pv

if __name__ == "__main__":
    atax_opin = 50
    gr = -0.02
    roc = 0.1
    coc = 0.08
    debt = 250 # Market value of debt

    print("Reinvestment rate:", gr/roc)
    tv = terminal_value(atax_opin, roc, coc, gr)
    print("Terminal Value:", tv)
    fcff = tv-debt
    print("FCFF:", fcff)

    debt_face_value = 400
    debt_maturity_num_years = 10
    rfr = 0.03
    debt_pv = pv(debt_face_value, debt_maturity_num_years, rfr)
    print("Value of bond with riskfree rate:", debt_pv)

    failure_prob = 1 - debt / debt_pv
    print("Probability of failure:", failure_prob)

    exp_value = fcff * (1 - failure_prob) + 0 * failure_prob
    print("Expected Value:", exp_value)
    # Output:
    #
    # Reinvestment rate: -0.19999999999999998
    # Terminal Value: 600.0
    # FCFF: 350.0
    # Value of bond with riskfree rate: 297.63756595869
    # Probability of failure: 0.1600522629099237
    # Expected Value: 293.9817079815267
