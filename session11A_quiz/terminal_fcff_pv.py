# Session 11A post-class test problem 3
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session11atest.pdf

from terminal_fcff import terminal_fcff

def pv(fv, interest_rate, num_periods):
    return fv / (1 + interest_rate)**num_periods

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="PV of Terminal value of FCFF after some number of years")
    parser.add_argument("-oi", "--exp_atax_opin", help="Expected after-tax operating income",
                        type=float, default=80)
    parser.add_argument("-troc", "--terminal_roc",
                        help="Return on Capital after achieving terminal value",
                        type=float, default=0.10)
    parser.add_argument("-tcoc", "--terminal_coc",
                        help="Cost of Capital after achieving terminal value",
                        type=float, default=0.10)
    parser.add_argument("-coc", "--coc",
                        help="Cost of Capital before achieving terminal value",
                        type=float, default=0.12)
    parser.add_argument("-g", "--terminal_growth_rate",
                        help="Growth rate in perpetuity after achieving terminal value",
                        type=float, default=0.03)
    parser.add_argument("-n", "--num_years",
                        help="Number of years",
                        type=float, default=10)

    args = parser.parse_args()

    fcff = terminal_fcff(args.exp_atax_opin, args.terminal_roc,
                         args.terminal_coc, args.terminal_growth_rate)
    print(pv(fcff, args.coc, args.num_years))
    # 257.5785892725567
