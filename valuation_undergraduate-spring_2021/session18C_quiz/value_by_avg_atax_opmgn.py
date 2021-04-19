# Session 18C post-class test problem 2
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session18Ctest.pdf

"""
Lycra Motors is a small automobile firm. The firm is a mature firm, with $2
billion in revenues growing 2% a year in perpetuity; it currently has capital
invested of $ 1 billion. However, it reported an operating loss of $50 million last
year, primarily because the economy was in a recession. If the average after-tax
operating margin for the company across the economic life cycle is 5% and the
cost of capital for the firm is 8%, what is the value of Lycra Motors?
"""

# Answer: Since the operating loss was mainly due to a recession and not some weakness
#         in the company, we can omit the latest operating loss and use the
#         average operating income from the latest economic life cycle.

import sys
sys.path.append("../../")
from modules.valuation.terminal_value import terminal_value

def value_by_avg_atax_opmgn(rev, rev_gr, ic, avg_atax_opmgn, coc):
    norm_atax_opin = avg_atax_opmgn * rev
    norm_roic = norm_atax_opin / ic
    tv = terminal_value(norm_atax_opin, norm_roic, coc, rev_gr)
    return tv

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Value a company using average After-tax Operating Margin across the economic life cycle")
    parser.add_argument("-r", "--rev", help="Revenues",
                        type=float, default=2000)
    parser.add_argument("-rgr", "--rev_gr",
                        help="Revenues growth rate",
                        type=int, default=0.02)
    parser.add_argument("-ic", "--ic",
                        help="Invested Capital",
                        type=int, default=1000)
    parser.add_argument("-oi", "--opin",
                        help="Operating Income",
                        type=int, default=-50)
    parser.add_argument("-a", "--avg_atax_opmgn",
                        help="Average After-tax Operating Margin",
                        type=int, default=0.05)
    parser.add_argument("-coc", "--coc",
                        help="Cost of Capital",
                        type=int, default=0.08)

    args = parser.parse_args()

    if args.opin < 0:
        tv = value_by_avg_atax_opmgn(args.rev, args.rev_gr, args.ic,
                                     args.avg_atax_opmgn, args.coc)
    else:
        tv = terminal_value(args.opin, args.opin/args.ic, args.coc, args.rev_gr)
    print(tv)
    # 1333.3333333333335
