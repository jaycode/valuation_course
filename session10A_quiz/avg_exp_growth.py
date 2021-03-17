# Session 10A post-class test problem 4
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session10Atest.pdf
def avg_exp_growth(roic, reinvestment_rate, exp_roic, exp_years):
    exp_growth_from_new_investments = reinvestment_rate * exp_roic
    exp_efficiency_growth_total = (exp_roic - roic) / roic
    exp_efficiency_growth_annual = (1 + exp_efficiency_growth_total)**(1/exp_years) - 1
    return exp_growth_from_new_investments + exp_efficiency_growth_annual

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Net income")
    parser.add_argument("-r", "--roic", help="Return on Invested Capital",
                        type=float, default=0.15)
    parser.add_argument("-rr", "--reinvestment_rate", help="Reinvestment Rate",
                        type=float, default=0.6)
    parser.add_argument("-er", "--exp_roic", help="Expected ROIC",
                        type=float, default=0.18)
    parser.add_argument("-ey", "--exp_years",
        help="Number of years until reaching the expected ROIC",
        type=int, default=5)
    args = parser.parse_args()

    print(avg_exp_growth(args.roic, args.reinvestment_rate,
                         args.exp_roic, args.exp_years))
    # 0.14513728933664816
