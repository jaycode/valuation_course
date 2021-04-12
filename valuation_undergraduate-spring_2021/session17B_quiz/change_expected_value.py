# Session 17D post-class test problem 1
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session17Dtest.pdf

"""
You are trying to value Lorax Inc., a mature food processing company that is
expected to generate $200 million in after-tax operating income next year. The
company is being targeted by activist investors for change and have come up
with the following information:

                     Growth Rate   ROIC   Cost of capital   Probability
Status Quo                3%        10%         9%              60%
Activist in charge        3%        15%         8%              40%

Estimate the expected value per share today, assuming that net debt is zero, and
there are 100 million shares outstanding
"""

import sys
sys.path.append("../../")
from modules.valuation.terminal_value import terminal_value

if __name__ == "__main__":

    atax_opin = 200
    input1 = {
        'gr': 0.03,
        'roic': 0.1,
        'coc': 0.09,
        'prob': 0.6
    }

    input2 = {
        'gr': 0.03,
        'roic': 0.15,
        'coc': 0.08,
        'prob': 0.4
    }

    shares_outstanding = 100

    print("Reinvestment rate 1:", input1['gr'] / input1['roic'])
    val1 = terminal_value(atax_opin,
                          input1['roic'],
                          input1['coc'],
                          input1['gr'])
    print("value 1:", val1)

    print("Reinvestment rate 2:", input2['gr'] / input2['roic'])
    val2 = terminal_value(atax_opin,
                          input2['roic'],
                          input2['coc'],
                          input2['gr'])
    print("value 2:", val2)

    exp_val = input1['prob'] * val1 + input2['prob'] * val2
    print("Expected value:", exp_val)

    print("Expected value-per-share:", exp_val / shares_outstanding)

    # Output:
    #
    # Reinvestment rate 1: 0.3
    # value1: 2333.3333333333335
    # Reinvestment rate 2: 0.2
    # value2: 3200.0
    # Expected value: 2680.0
    # Expected value-per-share: 26.8
