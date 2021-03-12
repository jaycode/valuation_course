# Session 9A post-class test problem 3
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session9Atest.pdf

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
