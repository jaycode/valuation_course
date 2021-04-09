# https://youtu.be/uj5xrGBFf44?t=4308
# Target price and returns calculation

"""
Assume that you believe that your valuation of Con Ed ($42.30) is a fair
estimate of the value, 7.70% is a reasonable estimate of Con Ed's cost of equity
and that your expected dividends for next year (2.32*1.021) is a fair estimate,
what is the expected stock price a year from now (assuming that the market
corrects its mistake?)
"""

if __name__ == "__main__":
    current_price = 42.3
    coe = 0.077
    exp_dividends = 2.32 * 1.021

    target_vps = current_price * (1+coe)
    target_price =  target_vps - exp_dividends
    print(target_price)
    # 43.188379999999995
