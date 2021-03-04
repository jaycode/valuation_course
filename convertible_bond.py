# Class course: https://youtu.be/80rduPdIsWw?t=3360

from pv_of_annuity import pv_of_annuity

def straight_debt(face_value, maturity_years, debt_interest_rate, bond_interest_rate):
    sd = pv_of_annuity(face_value * debt_interest_rate, maturity_years, bond_interest_rate) + \
         face_value / (1 + bond_interest_rate)**maturity_years

    return sd

if __name__ == "__main__":
    print(straight_debt(125, 10, 0.04, 0.08))
