# Session 8A post-class test problem 3
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session8Atest.pdf

import sys
sys.path.append("../")
from pv_of_annuity import pv_of_annuity

def roc_after_rnd(invested_capital, operating_income, expenses):
    current_expense = expenses.pop(0)
    unamortized_expenses = 0
    total_amortizations = 0
    for i, e in enumerate(expenses):
        cur_amort = e / len(expenses)
        amortization = e * (i+1) / len(expenses)
        total_amortizations += cur_amort
        unamortized_expenses += e - amortization
        # print("e:", e)
        # print("amort",(i+1),":",cur_amort)
    ebit = operating_income \
           + current_expense \
           - total_amortizations
    rnd_val = current_expense + unamortized_expenses
    capex = invested_capital + rnd_val
    # print("ebit:", ebit)
    # print("opin:", operating_income)
    # print("curex:", current_expense)
    # print("total amort:", total_amortizations)
    # print("unamortized_expenses:", unamortized_expenses)
    # print("value of research asset:", rnd_val)
    # print("capex: {} + {} = {}".format(invested_capital, rnd_val, capex))
    roc = ebit / capex
    return roc

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Calculate Return on Capital after R&D adjustments.")
    parser.add_argument("-c", "--invested_capital",
                        help="Invested capital",
                        type=float, default=40)
    parser.add_argument("-o", "--operating_income",
                        help="Pre-tax operating income",
                        type=float, default=-10)
    parser.add_argument("-e", "--expenses",
                        help="List of past R&D expenses from the earliest (closest to today)",
                        nargs="+", type=float, default=[30, 24, 18, 12])
    args = parser.parse_args()

    print(roc_after_rnd(args.invested_capital, args.operating_income,
                        args.expenses))
