# Session 9A post-class test problem 3
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session9Atest.pdf

"""
Tymba Inc. generated $20 million in after-tax operating income on revenues of
$100 million during the course of the most recent year. You expect revenues to
grow 10% a year next year and margins to stay stable. The firm’s non-cash
current assets are $40 million and its non-debt current liabilities are $50 million,
and non-cash working capital as a percent of revenues is expected to remain
unchanged next year. If the net cap ex is expected to be $10 million next year,
what is your estimate of the FCFF for the next year?
a. $13 million
b. $11 million
c. $8 million
d. $23 million
e. None of the above
"""

if __name__ == "__main__":
    net_income = 20
    revenue = 100
    next_year_rev_growth = 0.1
    non_cash_cur_assets = 40
    non_debt_cur_liabilities = 50
    expected_capex = 10

    next_year_rev = revenue + revenue * next_year_rev_growth
    print("Next year revenue:", next_year_rev)

    ncwc = non_cash_cur_assets - non_debt_cur_liabilities
    print("Non-Cash Working Capital:", ncwc)

    ncwc_rev_ratio = ncwc / revenue
    print("% of Revenue:", ncwc_rev_ratio)

    next_year_ncwc = ncwc_rev_ratio * next_year_rev
    print("Next year estimated Non-Cash Working Capital:", next_year_ncwc)

    ncwc_diff = next_year_ncwc - ncwc
    print("Changes in Non-Cash Working Capital:")
    print("{} - {} = {}".format(next_year_ncwc, ncwc, ncwc_diff))

    fcff = net_income * (1+next_year_rev_growth) - expected_capex \
           - ncwc_diff
    print("Next year estimated Free CashFlow to Firm:")
    print("{} * {} - {} - {} = {}".format(net_income, (1+next_year_rev_growth),
                                    expected_capex, ncwc_diff, fcff))

# Output

"""
Next year revenue: 110.0
Non-Cash Working Capital: -10
% of Revenue: -0.1
Next year estimated Non-Cash Working Capital: -11.0
Changes in Non-Cash Working Capital:
-11.0 - -10 = -1.0
Next year estimated Free CashFlow to Firm:
20 * 1.1 - 10 - -1.0 = 13.0
"""
