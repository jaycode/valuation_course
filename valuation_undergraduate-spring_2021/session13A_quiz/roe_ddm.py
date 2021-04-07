# Session 13A post-class test problem 6
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session11atest.pdf

"""
To deduct the formula, we start from the following formulas:

1. fcff = exp_net_income * (1 - reinvestment_rate) / (terminal_coe - terminal_growth_rate)
2. reinvestment_rate = growth_rate / roe

fcff and exp_net_income can be normalized to be per-share values like so:

price_per_share = eps * (1 - growth_rate / roe) / (coe - growth_rate)


We will use Sympy to help us solve the equations.
"""

from sympy.solvers import solve
from sympy import Symbol

def roe_ddm(growth_rate, coe, payout_ratio, eps, vps):
    x = Symbol('roe')
    # vps = eps * (1 - growth_rate / x) / (coe - growth_rate)
    roe = solve(eps * (1 - growth_rate / x) / (coe - growth_rate) - vps)[0]
    return roe

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Calculates ROE assuming the market shares the same assumptions " +
                    "on the growth rate, COE, and EPS.")
    parser.add_argument("-gr", "--growth_rate",
                        help="Expected Growth Rate in perpetuity",
                        type=float, default=0.02)
    parser.add_argument("-coe", "--coe",
                        help="Cost of Equity",
                        type=float, default=0.10)
    parser.add_argument("-pr", "--payout_ratio",
                        help="Payout Ratio",
                        type=float, default=0.90)
    parser.add_argument("-eps", "--exp_eps",
                        help="Expected next year's Earnings per Share",
                        type=float, default=2.0)
    # parser.add_argument("-evps", "--est_vps",
    #                     help="Estimated Value per Share",
    #                     type=float, default=22.5)
    parser.add_argument("-p", "--price",
                        help="Current stock price",
                        type=float, default=18.75)
    args = parser.parse_args()

    # 18.75 = 2 * (1 - 0.2/x) / 0.08
    # 18.75 = (2 - 0.4/x) / 0.08
    # 18.75*0.08 = 2 - 0.4/x
    # 0.4/x = 2 - 18.75*0.08
    # x = 0.4 / (2 - 18.75 * 0.08)
    # x = 0.8

    print(roe_ddm(args.growth_rate, args.coe, args.payout_ratio, args.exp_eps, args.price))

    # Output:
    #
    # 0.0800000000000000
