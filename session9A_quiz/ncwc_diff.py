# Session 9A post-class test problem 2
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session9Atest.pdf

if __name__ == "__main__":
    cash_last_year = 30
    debt_last_year = 15
    cash_this_year = 20
    debt_this_year = 25
    wc_last_year = 100
    wc_this_year = 120

    ncwc_last_year = wc_last_year - (cash_last_year - debt_last_year)
    print("Non-Cash Working Capital last year:", ncwc_last_year)

    ncwc_this_year = wc_this_year - (cash_this_year - debt_this_year)
    print("Non-Cash Working Capital this year:", ncwc_this_year)

    ncwc_diff = ncwc_last_year - ncwc_this_year
    print("Non-Cash Working Capital difference:", ncwc_diff)
