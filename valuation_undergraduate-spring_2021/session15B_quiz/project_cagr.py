# Session 15B post-class test problem 1
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session15Btest.pdf

def project_cagr(input):
    i = input
    terminal_mkt_cap = i['mkt_cap'] * (1 + i['mkt_cap_gr'])**i['num_years']
    print("Market in year {}: {}".format(i['num_years'], terminal_mkt_cap))
    terminal_rev = terminal_mkt_cap * i['terminal_rev_pct_mkt_cap']
    print("Revenues in year {}: {}".format(i['num_years'], terminal_rev))
    # CAGR = (future rev / current rev)**(1/num_years) - 1
    cagr = (terminal_rev / i['rev'])**(1/i['num_years']) - 1
    return cagr

if __name__ == "__main__":
    input = {
        'rev': 100,
        'opin': -50,
        'mkt_cap': 10000,
        'mkt_cap_gr': 0.1,
        'terminal_rev_pct_mkt_cap': 0.05,
        'num_years': 10
    }

    print("CAGR over the next {} years: {}".format(input['num_years'], project_cagr(input)))

    # Output:
    #
    # Market in year 10: 25937.424601000024
    # Revenues in year 10: 1296.8712300500013
    # CAGR over the next 10 years: 0.2920808373968211
