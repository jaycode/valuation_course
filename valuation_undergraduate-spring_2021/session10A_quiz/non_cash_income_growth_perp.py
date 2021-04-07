# Session 10A post-class test problem 2
# This is the growth of income the firm makes from non-cash equity.
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session10Atest.pdf

def non_cash_income_growth_prep(
        net_income, book_value,
        interest_income, cash_balance,
        capital_expenditure, wc_diff,
        total_debt_increase):
    non_cash_income = net_income - interest_income
    non_cash_roe = non_cash_income / (book_value - cash_balance)
    equity_reinvestment_rate = \
        (capital_expenditure + wc_diff - total_debt_increase) / \
        non_cash_income
    non_cash_income_growth = equity_reinvestment_rate * non_cash_roe
    return non_cash_income_growth

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Net income")
    parser.add_argument("-i", "--net_income", help="Net Income",
                        type=float, default=10)
    parser.add_argument("-b", "--book_value", help="Book Value of Equity",
                        type=float, default=110)
    parser.add_argument("-ii", "--interest_income", help="After-tax Interest Income",
                        type=float, default=1)
    parser.add_argument("-cb", "--cash_balance", help="Cash Balance",
                        type=float, default=20)
    parser.add_argument("-ce", "--capital_expenditure", help="Net Capital Expenditure",
                        type=float, default=4)
    parser.add_argument("-wc", "--wc_diff",
                        help="Working Capital difference (positive for increase)",
                        type=float, default=2)
    parser.add_argument("-di", "--total_debt_increase", help="Total Debt increase",
                        type=float, default=3)

    args = parser.parse_args()
    print(non_cash_income_growth_prep(
            args.net_income, args.book_value,
            args.interest_income, args.cash_balance,
            args.capital_expenditure, args.wc_diff,
            args.total_debt_increase))
    # 0.03333333333333333
