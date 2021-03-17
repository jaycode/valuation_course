# Session 10A post-class test problem 3
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session10Atest.pdf

def opin_growth_prep(
        atax_opin, book_value_equity,
        book_value_debt, cash_balance,
        capital_expenditure, wc_diff,
        depreciation):
    roic = atax_opin / (book_value_equity + book_value_debt - cash_balance)
    reinvestment_rate = \
        (capital_expenditure + wc_diff - depreciation) / \
        atax_opin
    opin_growth = reinvestment_rate * roic
    return opin_growth

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Net income")
    parser.add_argument("-oi", "--atax_opin", help="After-Tax Operating Income",
                        type=float, default=50)
    parser.add_argument("-b", "--book_value_equity", help="Book Value of Equity",
                        type=float, default=400)
    parser.add_argument("-d", "--book_value_debt", help="Book Value of Debt",
                        type=float, default=250)
    parser.add_argument("-cb", "--cash_balance", help="Cash Balance",
                        type=float, default=150)
    parser.add_argument("-ce", "--capital_expenditure", help="Net Capital Expenditure",
                        type=float, default=75)
    parser.add_argument("-wc", "--wc_diff",
                        help="Working Capital difference (positive for increase)",
                        type=float, default=-5)
    parser.add_argument("-dp", "--depreciation", help="Depreciation",
                        type=float, default=30)

    args = parser.parse_args()
    print(opin_growth_prep(
            args.atax_opin, args.book_value_equity,
            args.book_value_debt, args.cash_balance,
            args.capital_expenditure, args.wc_diff,
            args.depreciation))
    # 0.08000000000000002
