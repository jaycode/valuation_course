# Session 15B post-class test problem 5
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session15Btest.pdf
# Note: The method shown in the solution is incorrect but the result is correct.

from sympy.solvers import solve
from sympy import Symbol

def change_probability(intrinsic_price=15, change_price=30, market_price=20):
    x = Symbol('x')

    return solve(change_price * x + intrinsic_price * (1 - x) - market_price, x)[0]

if __name__ == "__main__":
    print(round(change_probability(), 2))
    # 0.33
