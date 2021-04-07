# Session 8A post-class test problem 2
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session8Atest.pdf

import sys
sys.path.append("../")
from pv_of_annuity import pv_of_annuity

def roc_after_leases(invested_capital, operating_income, first_lease,
                     next_lease, lease_periods, cost_of_debt):
    lease_outstanding = pv_of_annuity(next_lease, lease_periods, cost_of_debt)
    print("lease outstanding:", lease_outstanding)
    adjusted_operating_income = operating_income + first_lease - lease_outstanding/lease_periods
    debt = lease_outstanding
    roc = adjusted_operating_income / (debt + invested_capital)
    return roc

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Calculate Return on Capital after lease adjustments.")
    parser.add_argument("-c", "--invested_capital", help="Invested capital",
                        type=float, default=125)
    parser.add_argument("-o", "--operating_income", help="Pre-tax operating income",
                        type=float, default=25)
    parser.add_argument("-l1", "--first_lease", help="Most recent year lease expense",
                        type=float, default=25)
    parser.add_argument("-ln", "--next_lease", help="Lease expense for each of the coming years",
                        type=float, default=20)
    parser.add_argument("-lp", "--lease_periods", help="Number of years of lease periods",
                        type=int, default=8)
    parser.add_argument("-d", "--cost_of_debt", help="Pre-tax cost of debt",
                        type=float, default=0.04)

    args = parser.parse_args()

    print(roc_after_leases(args.invested_capital, args.operating_income,
                           args.first_lease, args.next_lease,
                           args.lease_periods, args.cost_of_debt))

# Default output

"""
lease outstanding: 134.65489749900806
0.1277393114171887
"""
