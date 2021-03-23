# Session 10A post-class test problem 1
# This is the earnings equity investors make.
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session10Atest.pdf

def eps_growth_perp(net_income, dividend, book_value):
    retained_earnings = net_income - dividend
    reinvestment_rate = retained_earnings / net_income
    roe = net_income / book_value
    eps_growth = reinvestment_rate * roe
    return eps_growth

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Net income")
    parser.add_argument("-i", "--net_income", help="Net Income",
                        type=float, default=100)
    parser.add_argument("-d", "--dividends", help="Dividends",
                        type=float, default=80)
    parser.add_argument("-b", "--book_value", help="Book Value",
                        type=float, default=800)

    args = parser.parse_args()

    print(eps_growth_perp(args.net_income, args.dividends,
                          args.book_value))
    # 0.025
