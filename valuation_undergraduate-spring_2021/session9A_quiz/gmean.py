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

## Result from running this code:
"""
Method 1 - Using all earnings: 0.01952914954673024
Debugging method 1:
year 1:
91.75762345920572
year 2:
93.54957180979311
year 3:
95.37651538769914
year 4:
97.23913761995153
year 5:
99.13813528032665
Method 2 - Using only the first and last earnings: 0.1486983549970351
Debugging method 2:
year 1:
103.38285194973317
year 2:
118.75571196956051
year 3:
136.41449098593586
year 4:
156.69910139330239
year 5:
180.00000000000006

Conclusion: Method 2 is the correct method since it correctly calculates the earnings after 5 years of growth.
"""
