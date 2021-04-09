# Session 15B post-class test problem 3
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session15Btest.pdf
def cf_pv(cur_cf, cf_growths = []):
    pv = cur_cf
    for g in cf_growths:
        pv /= 1 + g
    return pv

if __name__ == "__main__":
    print(cf_pv(10, (0.15, 0.12, 0.1)))
    # 7.058159232072275
