# Session 9A post-class test problem 4
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session9Atest.pdf

"""
Roomba Inc. is a manufacturer of vacuum cleaners and you have estimated a
FCFF of $50 million for firm for the most recent year. Roomba’s total debt
decreased from $100 to $85 million during the course of the year and it reported
interest expense of $10 million for the year. If Roomba’s tax rate is 30%,
estimate the FCFE for the most recent year.
a. $ 25 million
b. $ 58 million
c. $ 28 million
d. $ 55 million
e. None of the above
"""

if __name__ == "__main__":
    fcff = 50
    prev_debt = 100
    debt = 85
    interest_expense = 10
    tax_rate = 0.3

    debt_repayment = prev_debt - debt
    print("Debt repayment:", debt_repayment)

    fcfe = (fcff - debt_repayment - interest_expense*(1-tax_rate))
    print("Free CashFlow to Equity:", fcfe)

# Output

"""
Debt repayment: 15
Free CashFlow to Equity: 28.0
"""
