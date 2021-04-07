# Session 13A post-class test problem 5
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session11atest.pdf

"""
The main formula to use here is:

growth_rate = (1 - payout_ratio) * roe

We will use Sympy to help us solve the equations.
"""

from sympy.solvers import solve
from sympy import Symbol


def growth_rate_ddm(roe, hg_payout_ratio, t_growth_rate):
    hg_retained_earnings_ratio = (1 - hg_payout_ratio)
    print("Retained earnings ratio during the high-growth phase:", hg_retained_earnings_ratio)
    hg_growth_rate = hg_retained_earnings_ratio * roe
    print("Growth rate during the high-growth phase: {}".format(hg_growth_rate))

    x = Symbol('t_payout_ratio')
    t_payout_ratio = solve((1 - x) * roe - t_growth_rate)[0]
    print("Payout ratio after achieving terminal value: {}".format(t_payout_ratio))

    return (hg_growth_rate, t_payout_ratio)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Growth rate during high-growth phase and terminal payout ratio " +
                    "using dividend discount model (usually for banks)")
    parser.add_argument("-roe", "--roe",
                        help="Return on Equity in perpetuity",
                        type=float, default=0.12)
    parser.add_argument("-hgpr", "--hg_payout_ratio",
                        help="Payout ratio during high-growth phase",
                        type=float, default=0.20)
    parser.add_argument("-tgr", "--t_growth_rate",
                        help="Growth rate after achieving terminal value",
                        type=float, default=0.03)

    args = parser.parse_args()

    growth_rate_ddm(args.roe, args.hg_payout_ratio, args.t_growth_rate)

    # Output:
    #
    # Retained earnings ratio during the high-growth phase: 0.8
    # Growth rate during the high-growth phase: 0.096
    # Payout ratio after achieving terminal value: 0.750000000000000
