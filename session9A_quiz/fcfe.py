# Session 9A post-class test problem 4
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session9Atest.pdf

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
