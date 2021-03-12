# Class course: https://youtu.be/80rduPdIsWw?t=3360

def pv_of_annuity(cashflow, num_periods, interest):
    pv = cashflow * (1 - (1 + interest)**(-num_periods)) / interest
    return pv

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Calculate PV of annuity.")
    parser.add_argument("-c", "--cashflow", help="Cashflow - Amount of next payment", type=float)
    parser.add_argument("-n", "--num_periods", help="Number of periods", type=float)
    parser.add_argument("-i", "--interest", help="Interest", type=float)

    args = parser.parse_args()

    if args.cashflow:
        print(pv_of_annuity(args.cashflow, args.num_periods, args.interest))
    else:
        # Test
        print(pv_of_annuity(125 * 0.08, 10, 0.04))
        # 81.10895779355035
