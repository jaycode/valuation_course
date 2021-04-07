# Session 13A post-class test problem 2
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session13btest.pdf

def market_value(
    shares):
    total = 0
    for i, s in iter(shares):
        total += s[s][0] * s[][1]
    return vps

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Estimate the value per share using the option value approach.")
    parser.add_argument("-e", "--equity", help="Equity value",
                        type=float, default=500)
    parser.add_argument("-so", "--shares_outstanding",
                        help="Number of shares outstanding",
                        type=int, default=100)
    # parser.add_argument("-sp", "--share_price",
    #                     help="Share price",
    #                     type=float, default=5)
    parser.add_argument("-os", "--options_outstanding",
                        help="Number options outsanding",
                        type=int, default=25)
    parser.add_argument("-oep", "--options_exercise_price",
                        help="Exercise price of the options",
                        type=int, default=1)

    args = parser.parse_args()

    print(vps_options_ov(args.equity, args.shares_outstanding,
                         args.options_outstanding, args.options_exercise_price))
    # 4.75
