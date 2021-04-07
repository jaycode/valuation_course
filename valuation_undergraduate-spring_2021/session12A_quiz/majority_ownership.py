# Session 12A post-class test problem 4
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session12atest.pdf


if __name__ == "__main__":
    holding_size = 0.6
    combined_equity = 1000
    parent_debt = 200
    parent_cash = 100
    subsidiary_equity_intrinsic = 500
    parent_equity = combined_equity + parent_cash - \
        parent_debt - (1-holding_size) * subsidiary_equity_intrinsic
    print(parent_equity)
