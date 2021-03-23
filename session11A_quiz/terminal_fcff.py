# Session 11A post-class test problem 2
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session11atest.pdf

def terminal_fcff(
    exp_atax_opin, terminal_roc, terminal_coc, terminal_growth_rate):
    reinvestment_rate = terminal_growth_rate / terminal_roc
    fcff = exp_atax_opin * (1 - reinvestment_rate) / (terminal_coc - terminal_growth_rate)
    return fcff

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Terminal value of FCFF after some number of years")
    parser.add_argument("-oi", "--exp_atax_opin", help="Expected after-tax operating income",
                        type=float, default=60)
    parser.add_argument("-troc", "--terminal_roc",
                        help="Return on Capital after achieving terminal value",
                        type=float, default=0.12)
    parser.add_argument("-tcoc", "--terminal_coc",
                        help="Cost of Capital after achieving terminal value",
                        type=float, default=0.10)
    parser.add_argument("-g", "--terminal_growth_rate",
                        help="Growth rate in perpetuity after achieving terminal value",
                        type=float, default=0.03)

    args = parser.parse_args()

    print(terminal_fcff(args.exp_atax_opin, args.terminal_roc,
                        args.terminal_coc, args.terminal_growth_rate))
    # 642.8571428571428
