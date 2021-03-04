# Class course: https://youtu.be/80rduPdIsWw?t=3360

def pv_of_annuity(cashflow, num_periods, interest):
    pv = cashflow * (1 - (1 + interest)**(-num_periods)) / interest
    return pv

if __name__ == "__main__":
    print(pv_of_annuity(125 * 0.08, 10, 0.04))
    # 81.10895779355035
