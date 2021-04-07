# Session 12A post-class test problem 3
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session12atest.pdf

def ownership(holding_size, book_value=0, market_value=0):
    if holding_size < 0.5:
        return holding_size * market_value
    else:
        return book_value

if __name__ == "__main__":
    holding_size = 0.1
    owner_equity_size = 250
    subsidiary_equity_bv = 100
    subsidiary_equity_intrinsic = 200
    subsidiary_owned = ownership(
        holding_size,
        book_value=subsidiary_equity_bv,
        market_value=subsidiary_equity_intrinsic)
    print(owner_equity_size + subsidiary_owned)
    # 270.0
