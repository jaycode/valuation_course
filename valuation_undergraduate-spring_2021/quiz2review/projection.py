# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/valquiz2review.pdf
# Example: Problem 1a, Fall 2010

"""
Maple Telecom is in significant financial trouble. It reported operaHng
losses of $ 20 million in the most recent year on revenues of $ 100
million. The total book value of capital invested in the firm today is $ 190
million. Assuming that the firm will revert back to health in 3 years, you
have forecast revenues, after-tax operaHng income and reinvestment, as
well as the cost of capital:

                  Year 1  Year 2  Year 3
Revenues           $150    $160    $180
Ebit               -$15     $15     $25
+ Depreciation      $15     $20     $25
- CapEx              $5     $25     $40
FCFF                -$5     $10     $10
Cost of Capital     14%     12%     10%
"""

import pandas as pd

def project_pv(projection):
    p = projection
    for y in p.columns:

        if y > 1:
            p.loc['cum_coc', y] = \
                p.loc['cum_coc', y-1] * (1 + p.loc['coc', y])
        else:
            p.loc['cum_coc', y] = 1 + p.loc['coc', y]
        p.loc['cf', y] = p.loc['fcff', y]
        p.loc['pv', y] = p.loc['cf', y] / p.loc['cum_coc', y]
    p.loc['op_assets_pv', 1] = p.loc['pv',:].sum()
    return p

if __name__ == "__main__":
    projection = pd.DataFrame(
        columns = ['name', 1, 2, 3],
        data=[
            ('revenues', 150, 160, 180),
            ('ebit', -15, 15, 25),
            ('depreciation', 15, 20, 25),
            ('capex', 5, 25, 40),
            ('fcff', -5, 10, 10),
            ('coc', 0.14, 0.12, 0.10)
        ]
    )

    projection.set_index('name', inplace=True)

    p = project_pv(projection)
    p = p.rename(mapper={
        'revenues': 'Revenues',
        'ebit': 'EBIT',
        'depreciation': 'Depreciation',
        'capex': 'Cap Ex',
        'fcff': 'FCFF',
        'coc': 'Cost of Capital',
        'cum_coc': 'Cumulated Cost of Capital',
        'cf': 'Cash Flow',
        'pv': 'Present Value',
        'op_assets_pv': 'Value of Operating Assets'
    })
    print(p.round(2))
    
    # Output:
    #
    #                                 1       2       3
    # name
    # Revenues                   150.00  160.00  180.00
    # EBIT                       -15.00   15.00   25.00
    # Depreciation                15.00   20.00   25.00
    # Cap Ex                       5.00   25.00   40.00
    # FCFF                        -5.00   10.00   10.00
    # Cost of Capital              0.14    0.12    0.10
    # Cumulated Cost of Capital    1.14    1.28    1.40
    # Cash Flow                   -5.00   10.00   10.00
    # Present Value               -4.39    7.83    7.12
    # Value of Operating Assets   10.57     NaN     NaN
