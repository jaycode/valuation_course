# Session 11A post-class test problem 5
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session11atest.pdf

def terminal_value_ddm(
    dividend, net_income, terminal_roe, terminal_coe, terminal_growth_rate, num_years):
    retained_earnings_ratio = (net_income - dividend) / net_income
    print("Retained earnings ratio:", retained_earnings_ratio)
    exp_growth_rate = retained_earnings_ratio * terminal_roe
    print("Expected growth rate for next {} years: {}".format(num_years, exp_growth_rate))
    exp_net_income = net_income * (1 + exp_growth_rate)**num_years * (1 + terminal_growth_rate)
    print("Net income in year {}: {}".format(num_years + 1, exp_net_income))
    payout_ratio = 1 - (terminal_growth_rate / terminal_roe)
    print("Payout ratio in year {}: {}".format(num_years + 1, payout_ratio))
    reinvestment_rate = 1 - payout_ratio
    terminal_value = exp_net_income * (1 - reinvestment_rate) / (terminal_coe - terminal_growth_rate)
    return terminal_value

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Terminal value after some number of years using " +
                    "dividend discount model (usually for banks)")
    parser.add_argument("-d", "--dividend", help="Most recent year's dividend",
                        type=float, default=40)
    parser.add_argument("-ni", "--net_income", help="Most recent year's net income",
                        type=float, default=100)
    parser.add_argument("-troe", "--terminal_roe",
                        help="Return on Equity after achieving terminal value",
                        type=float, default=0.15)
    parser.add_argument("-tcoe", "--terminal_coe",
                        help="Cost of Equity after achieving terminal value",
                        type=float, default=0.09)
    parser.add_argument("-g", "--terminal_growth_rate",
                        help="Growth rate in perpetuity after achieving terminal value",
                        type=float, default=0.03)
    parser.add_argument("-n", "--num_years",
                        help="Number of years",
                        type=float, default=3)

    args = parser.parse_args()

    print(terminal_value_ddm(args.dividend, args.net_income, args.terminal_roe,
                             args.terminal_coe, args.terminal_growth_rate, args.num_years))
    # 642.8571428571428
