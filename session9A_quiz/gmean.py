# Session 9A post-class test problem 5
# http://people.stern.nyu.edu/adamodar/pdfiles/eqnotes/postclass/session9Atest.pdf

from scipy.stats.mstats import gmean

if __name__ == "__main__":
    earnings = [90, 120, 115, 150, 100, 180]
    calc1 = gmean(earnings) / earnings[1] - 1
    print("Method 1 - Using all earnings:", calc1)

    debug1 = earnings[0]
    print("Debugging method 1:")
    for i, e in enumerate(earnings[1:]):
        debug1 = debug1 * (1+calc1)
        print("year {}:".format(
            i+1
        ))
        print(debug1)


    calc2 = (earnings[-1] / earnings[0]) ** (1 / (len(earnings) - 1)) - 1
    print("Method 2 - Using only the first and last earnings:", calc2)

    debug2 = earnings[0]
    print("Debugging method 2:")
    for i, e in enumerate(earnings[1:]):
        debug2 = debug2 * (1+calc2)
        print("year {}:".format(
            i+1
        ))
        print(debug2)

    print("\nConclusion: Method 2 is the correct method since it correctly",
          "calculates the earnings after {} years of growth.".format(len(earnings)-1))
