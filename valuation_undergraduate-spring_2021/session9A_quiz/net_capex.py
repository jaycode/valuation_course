# Session 9A post-class test problem 1
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session9Atest.pdf

def net_capex(previous_capex, depam, acquisitions):
    return previous_capex - depam + acquisitions[0]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Calculate Net Capital Expenditure for FCFF calculation.")
    parser.add_argument("-p", "--previous_capex",
                        help="Last Capital Expenditure",
                        type=float, default=80)
    parser.add_argument("-da", "--depam",
                        help="Depreciation & Amortization",
                        type=float, default=60)
    parser.add_argument("-a", "--acquisitions",
                        help="Acquisitions (cash, stock)",
                        nargs="+", type=float, default=[40, 60])

    args = parser.parse_args()

    print(net_capex(args.previous_capex, args.depam,
                    args.acquisitions))

# Default output:

# 60
