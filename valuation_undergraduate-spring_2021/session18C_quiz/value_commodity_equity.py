# Session 18C post-class test problem 3
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session18Ctest.pdf

"""
Selma Oil is an oil services company that reported after-tax operating profits last
year of $150 million on revenues of $ 1 billion. However, the firm benefited from
high oil prices (averaging $100/barrel) during the course of the year. Oil prices
have now dropped to $ 60/barrel and your assessment of Selma Oil’s history
suggests that every $ 1/barrel drop in the stock price costs them $1.25 million in
after-tax operating profits. If the firm is in stable growth, with production
growing 2% a year in perpetuity and the business is a competitive one (where
firms earn their cost of capital of 8% over time), estimate the value of Selma Oil
today.
"""

# Answer: Use the oil price difference for calculating normalized income.
#         "firms earn their cost of capital of 8% over time" means that
#         Return on Capital and Cost of Capital are the same 8%.
#         Revenue is not used for calculation.

import sys
sys.path.append("../../")
from modules.valuation.terminal_value import terminal_value

def value_commodity_equity(inputs, log=False):
    i = inputs
    norm_atax_opin = i['atax_opin'] + i['com_price_beta'] * (i['com_price'] - i['avg_com_price'])
    if log:
        print("Normalized After-Tax Operational Income:", norm_atax_opin)
    # norm_roic = i['atax_opin'] / i['rev']
    # if log:
    #     print("Return on Capital:", norm_roic)
    tv = terminal_value(norm_atax_opin, i['roc'], i['coc'], i['prod_gr'])
    return tv

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Value a company that produces a commodity")
    parser.add_argument("-oi", "--atax_opin", help="After-tax operating income",
                        type=float, default=150)
    parser.add_argument("-r", "--rev", help="Revenues",
                        type=float, default=1000)
    parser.add_argument("-acp", "--avg_com_price",
                        help="Average Commodity Price during the accounting period",
                        type=float, default=100)
    parser.add_argument("-cp", "--com_price", help="Current Commodity Price",
                        type=float, default=60)
    parser.add_argument("-cpv", "--com_price_beta", help="Commodity Price Beta",
                        type=float, default=1.25)
    parser.add_argument("-pgr", "--prod_gr", help="Production Growth Rate",
                        type=float, default=0.02)
    parser.add_argument("-coc", "--coc", help="Cost of Capital",
                        type=float, default=0.08)
    parser.add_argument("-roc", "--roc", help="Return on Capital",
                        type=float, default=0.08)
    args = parser.parse_args()

    tv = value_commodity_equity({
        'atax_opin': args.atax_opin,
        'rev': args.rev,
        'avg_com_price': args.avg_com_price,
        'com_price': args.com_price,
        'com_price_beta': args.com_price_beta,
        'prod_gr': args.prod_gr,
        'coc': args.coc,
        'roc': args.roc},
        log=True)
    print(tv)
    # 1333.3333333333335
