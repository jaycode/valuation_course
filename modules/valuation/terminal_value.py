# Free CashFlow to the Firm

def terminal_value(
    atax_opin, roc, coc, growth_rate, next_year_growth_rate=0, log=False):
    """
    The terminal value by default works with future values. If last year's value is
    entered, make sure to set the next_year_growth_rate variable
    to grow the operation income with. This is generally set at the same number
    as `growth_rate`.
    """
    reinvestment_rate = growth_rate / roc
    terminal_value = atax_opin * (1 - reinvestment_rate) * (1 + next_year_growth_rate) \
                     / (coc - growth_rate)

    if log:
        print("{} * (1 - {}) * (1 + {}) / ({} - {}) = {}".format(
            atax_opin, reinvestment_rate, next_year_growth_rate,
            coc, growth_rate, terminal_value
        ))
    return terminal_value
