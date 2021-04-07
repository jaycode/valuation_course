# Session 11A post-class test problem 2
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session11atest.pdf

"""
Avalon Inc. is a high growth publicly traded firm that is expected to become a
stable growth firm after 5 years. You have estimated an expected after-tax
operating income of $60 million in year 6 and believe that the firm will generate
a return on capital of 12% in perpetuity. If the cost of capital is 10% and the
expected growth rate in perpetuity after year 5 is 3%, what will the terminal
value be at the end of year 5?
a. $857.14 million
b. $666.67 million
c. $642.86 million
d. $450 million
e. None of the above
"""

import sys
sys.path.append("../../")
from modules.valuation import terminal_value

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Terminal value after some number of years")
    parser.add_argument("-oi", "--exp_atax_opin", help="Expected after-tax operating income",
                        type=float, default=60)
    parser.add_argument("-troc", "--terminal_roc",
                        help="Return on Capital after achieving terminal value",
                        type=float, default=0.12)
    parser.add_argument("-tcoc", "--terminal_coc",
                        help="Cost of Capital after achieving terminal value",
                        type=float, default=0.10)
    parser.add_argument("-g", "--terminal_growth_rate",
                        help="Growth rate in perpetuity after achieving terminal value",
                        type=float, default=0.03)

    args = parser.parse_args()

    print(terminal_value(args.exp_atax_opin, args.terminal_roc,
                         args.terminal_coc, args.terminal_growth_rate))
    # 642.8571428571428
