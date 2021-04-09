# Session 15B post-class test problem 4
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session15Btest.pdf

def expected_value(value, failure_rate, failure_value):
    return (failure_value * failure_rate + value * (1 - failure_rate))

if __name__ == "__main__":
    print(expected_value(250, 0.2, 50))
    # 7.058159232072275
