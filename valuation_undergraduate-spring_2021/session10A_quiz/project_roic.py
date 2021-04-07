# Session 10A post-class test problem 5
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session10Atest.pdf

import pandas as pd

def project_roic(projection, invested_capital, sales_to_capital_ratio):
    p = projection
    # Prepare new measures
    p.loc['reinvestment', :] = None
    p.loc['invested_capital', :] = None
    p.loc['return_on_capital', :] = None

    p.loc['invested_capital', 0] = invested_capital

    for y in p.columns:

        if y > 0:
            rev_diff = p.loc['revenues', y] - p.loc['revenues', y-1]
            p.loc['reinvestment', y] = rev_diff / sales_to_capital_ratio
            p.loc['invested_capital', y] = \
                p.loc['invested_capital', y-1] + p.loc['reinvestment', y]

        p.loc['return_on_capital', y] = \
            p.loc['operating_income', y] / p.loc['invested_capital', y]
    return projection

if __name__ == "__main__":
    projection = pd.DataFrame(
        columns = ['name', 0, 1, 2, 3, 4],
        data=[
            ('revenues', 100, 200, 320, 450, 600),
            ('operating_margin', -0.1, -0.05, 0, 0.05, 0.1),
            ('operating_income', -10, -10, 0, 22.5, 60),
        ]
    )
    projection.set_index('name', inplace=True)

    invested_capital = 50
    sales_to_capital_ratio = 2.0

    print(projection)
    print("Invested capital:", invested_capital)
    print("Sales-to-capital ratio:", sales_to_capital_ratio)

    # Output:
    """
                          0       1    2       3      4
    name
    revenues          100.0  200.00  320  450.00  600.0
    operating_margin   -0.1   -0.05    0    0.05    0.1
    operating_income  -10.0  -10.00    0   22.50   60.0
    Invested capital: 50
    Sales-to-capital ratio: 2.0
    """

    print(project_roic(projection, invested_capital, sales_to_capital_ratio))

    # Output:
    """
                           0       1      2       3      4
    name
    revenues           100.0  200.00  320.0  450.00  600.0
    operating_margin    -0.1   -0.05    0.0    0.05    0.1
    operating_income   -10.0  -10.00    0.0   22.50   60.0
    reinvestment         NaN   50.00   60.0   65.00   75.0
    invested_capital    50.0  100.00  160.0  225.00  300.0
    return_on_capital   -0.2   -0.10    0.0    0.10    0.2
    """
