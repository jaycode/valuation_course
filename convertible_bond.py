# Class course: https://youtu.be/80rduPdIsWw?t=3360

from pv_of_annuity import pv_of_annuity

def straight_debt(face_value, maturity_years, debt_interest_rate, bond_interest_rate):
    sd = pv_of_annuity(face_value * debt_interest_rate, maturity_years, bond_interest_rate) + \
         face_value / (1 + bond_interest_rate)**maturity_years

    return sd

def equity_portion(market_value, straight_debt):
    return market_value - straight_debt

if __name__ == "__main__":
    sd = straight_debt(125, 10, 0.04, 0.08)
    print("straight debt:", sd)
    # straight debt: 91.44959300529275
    print("equity portion:", equity_portion(140, sd))
    # equity portion: 48.550406994707245
