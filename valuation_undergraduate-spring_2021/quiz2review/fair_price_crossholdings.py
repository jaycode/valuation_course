# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/valquiz2review.pdf
# Example: Quiz from Spring 2007

"""
You have been asked to analyze Smithtown Works, a company with a 60%
holding in Kroger Appliances (which is fully consolidated into Smithtown
Works) and 10% of Haverford Steel (which is reported as a minority
passive investment). All three companies are in stable growth (2%
forever), have a return on capital of 10% and share a cost of capital of 8%.

- Smithtown Works has 500 million shares outstanding, trading at $30 a share, and
  the consolidated balance sheet reports debt outstanding of $ 6 billion, a cash
  balance of $ 2 billion and $ 1 billion in minority interests.
  The consolidated aftertax operating income reported by the company the most recent
  year was $ 1.5 billion.
- Kroger Appliances is not publicly traded and there little information on its after-tax
  operating income, debt or cash balance, but appliance companies typically trade at
  3 times book value.
- Haverford Steel reported after-tax operating income of $ 800 million in the most
  recent year.

Evaluate whether the stock in Smithtown Works is fairly priced.

- reinvestment_rate = growth_rate / roe
- fcff = exp_net_income * (1 - reinvestment_rate) / (coe - growth_rate)
- Since the value was coming from the last year, the formula for fcff becomes:
  fcff = exp_net_income * (1 - reinvestment_rate) * (1 + growth_rate) / (coe - growth_rate)
"""

import sys
sys.path.append("../../")
from modules.valuation import terminal_value

def value_crossholdings(inputs, log=False):
    """ Get FCFF of parent and terminal value of each minority holding
    """
    ownerships = inputs['ownerships']
    tv_list = [None] * (len(ownerships))

    # TV of parent + all consolidated holdings
    # ----
    # If data is from last year, then extrapolate the tv result
    # by setting the next year growth rate with the value of
    # last year's growth rate.
    next_year_growth_rate = 0
    if inputs['parent']['is_last_year']:
        next_year_growth_rate = inputs['parent']['growth_rate']

    consolidated_tv = terminal_value(inputs['parent']['atax_opin'],
                                     inputs['parent']['roc'],
                                     inputs['parent']['coc'],
                                     inputs['parent']['growth_rate'],
                                     next_year_growth_rate=next_year_growth_rate,
                                     log=log)
    parent_fcff = consolidated_tv
    # ----

    for i, o in enumerate(ownerships):
        if o['own_size'] < 0.5:
        # Minority interests
            # TV calculation
            tv_parameters = ['atax_opin', 'growth_rate', 'roc', 'coc']
            if all(item in o for item in tv_parameters):
                # If data is from last year, then extrapolate the fcff result
                # by setting the next year growth rate with the value of
                # last year's growth rate.
                next_year_growth_rate = 0
                if o['is_last_year']:
                    next_year_growth_rate = o['growth_rate']
                o_tv = terminal_value(o['atax_opin'],
                                      o['roc'],
                                      o['coc'],
                                      o['growth_rate'],
                                      next_year_growth_rate=
                                        next_year_growth_rate) \
                                      * o['own_size']
                tv_list[i] = o_tv
                o['terminal_value'] = o_tv

            # Add to parent's FCFF
            parent_fcff += o['terminal_value']
        else:
        # Consolidated subsidiaries
            # Parameters to calculate minority interests
            # via PB and market value
            mi_parameters = ['industry_avg_pb', 'minority_interest']
            if all(item in o for item in mi_parameters):
                # Calculate market value minority interests
                mi_market = o['industry_avg_pb'] * o['minority_interest']
                o['mi_market'] = mi_market

            # Reduce parent's FCFF by market value minority interests
            parent_fcff -= o['mi_market']


    parent_fcff += inputs['parent']['cash']
    parent_fcff -= inputs['parent']['debt']

    return {'parent_fcff': parent_fcff,
            'consolidated_tv': consolidated_tv,
            'minority_tv_list': tv_list}

if __name__ == "__main__":
    ownerships = [
        {
            # Kroger
            'own_size': 0.6,
            'industry_avg_pb': 3.0,
            'minority_interest': 1000
        },
        {
            # Haverford
            'own_size': 0.1,
            'atax_opin': 800,
            'growth_rate': 0.02,
            'roc': 0.1,
            'coc': 0.08,
            'is_last_year': True
        }
    ]
    inputs = {
        'parent': {
            'growth_rate': 0.02,
            'roc': 0.1,
            'coc': 0.08,
            'debt': 6000,
            'cash': 2000,
            'atax_opin': 1500,
            'is_last_year': True
        },
        'ownerships': ownerships
    }

    result = value_crossholdings(inputs, log=True)
    consolidated_tv = result['consolidated_tv']
    tv = result['minority_tv_list']
    p_fcff = result['parent_fcff']
    print("Smithtown Works + Kroger Terminal Value:", consolidated_tv)
    print("Value of Haverford Steel:", tv[1])
    print("Value of equity in Smithtown:", p_fcff)

    shares_outstanding = 500
    share_price = 30
    market_cap = shares_outstanding * share_price
    print("Market Value of Equity in Smithtown:", market_cap)
    if market_cap > p_fcff:
        print("Stock is overvalued by", (market_cap - p_fcff), "million")
    elif market_cap < p_fcff:
        print("Stock is undervalued by", (p_fcff - market_cap), "million")
    else:
        print("Stock price is valued the same with the market (impossibru!)")

    # parent_fcff = fcff(adjusted_opin, roc, coc, growth_rate)
    # print("Smithtown Works + Kroger FCFF:", parent_fcff)
    # vps = parent_fcff / shares_outstanding
    # print("Smithtown Works value per share:", vps)
