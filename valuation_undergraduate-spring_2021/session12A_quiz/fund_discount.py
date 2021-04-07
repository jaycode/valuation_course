# Session 12A post-class test problem 2
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session12atest.pdf
def fund_discount(
    past_fund_returns, past_market_returns,
    exp_market_returns):
    return_diff = past_market_returns - past_fund_returns
    exp_fund_return = exp_market_returns - return_diff
    fund_market_value = exp_fund_return / exp_market_returns
    discount = 1.0 - fund_market_value
    return discount

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Calculate fund discount based on past market and fund returns " +
                    "and expected market returns.")
    parser.add_argument("-pf", "--past_fund_returns", help="Past fund returns",
                        type=float, default=0.09)
    parser.add_argument("-pm", "--past_market_returns", help="Past market returns",
                        type=float, default=0.12)
    parser.add_argument("-em", "--exp_market_returns",
                        help="Expected market returns",
                        type=float, default=0.08)

    args = parser.parse_args()

    print(fund_discount(args.past_fund_returns, args.past_market_returns, args.exp_market_returns))
    # 0.375
