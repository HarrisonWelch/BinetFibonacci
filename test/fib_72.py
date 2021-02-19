import math
import numpy as np

def fib_binet(n):
    return ((((1+math.sqrt(5)) / 2)**n) - 0) / math.sqrt(5)

def main():
    ans = 498454011879264
    r5 = np.longdouble(np.sqrt(5))
    gr = np.longdouble((1 + np.sqrt(5)) / 2)
    grn = np.longdouble((1 - np.sqrt(5)) / 2)
    n = 72
    a = int((gr**n - grn**n)*1000000) / int(r5*1000000)
    # a = a / 1000000
    print('gr = ' + str(gr))
    print('grn = ' + str(grn))
    print('n = ' + str(n))
    print('a .. = ' + str(a))
    print('ans  = ' + str(ans))
    print('diff = ' + str(ans - a))
    # print('fib_binet(72) = ' + str(fib_binet(72)))
    # print('ans ......... = ' + str(ans))
    # print('diff ........ = ' + str(ans - fib_binet(72)))

if __name__ == "__main__":
    main()
