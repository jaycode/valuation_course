# Cumulative tax of a money-losing company.
# Session 8A post-class test problem 4
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session8Atest.pdf

def cumtax(total_net_losses, future_cashflows, marginal_tax_rate):
    future_tax = 0
    nol = total_net_losses # net_operating_loss
    tax_balances = []
    for i, c in enumerate(future_cashflows):
        curr_tax_balance = 0
        nol -= c
        curr_tax_balance = marginal_tax_rate * -nol
        curr_tax_balance = max(0, curr_tax_balance)
        nol = max(0, nol)
        tax_balances.append(curr_tax_balance)
        print("Year", (i+1))
        print("current year tax to pay:", curr_tax_balance)
        print("Net Operating Loss:", nol)
        print("---")

    return tax_balances

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Calculate cumulative taxes to pay in the future.")
    parser.add_argument("-l", "--total_net_losses",
                        help="Total net operating losses",
                        type=float, default=100)
    parser.add_argument("-c", "--future_cashflows",
                        help="Future cashflows",
                        nargs="+", type=float,
                        default=[-50, 75, 125, 125])
    parser.add_argument("-t", "--marginal_tax_rate",
                        help="Marginal tax rate",
                        type=float,
                        default=0.4)
    parser.add_argument("-n", "--num_years",
                        help="Number of years to pay the tax",
                        type=float,
                        default=0.4)


    args = parser.parse_args()

    print(cumtax(args.total_net_losses, args.future_cashflows,
                 args.marginal_tax_rate))
