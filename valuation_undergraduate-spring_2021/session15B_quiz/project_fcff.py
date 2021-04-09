# Session 15B post-class test problem 2
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session15Btest.pdf

def project_fcff(input):
    i = input
    print("Expected operating loss next year: {} million".format(i['opin_ny']))
    rev_chg = i['rev'] * i['rev_g'] - i['rev']
    print("Expected change in revenue nect year: {} million".format(rev_chg))
    reinvestment = rev_chg / i['rev_on_capital']
    print("Reinvestment next year: {}".format(reinvestment))
    fcff = i['opin_ny'] - reinvestment
    return fcff

if __name__ == "__main__":
    input = {
        'rev': 100,
        'rev_g': 2.0,
        'rev_on_capital': 4.0,
        'opin': -50,
        'opin_ny': -25,
    }

    print("Expected FCFF next year: {}".format(project_fcff(input)))

    # Output:
    # 
    # Expected operating loss next year: -25 million
    # Expected change in revenue nect year: 100.0 million
    # Reinvestment next year: 25.0
    # Expected FCFF next year: -50.0
