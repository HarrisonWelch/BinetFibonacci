import math
import time

def fib_binet(n):
    print('(((1+math.sqrt(5)) / 2)**n) ............................... = ' + str((((1+math.sqrt(5)) / 2)**n)))
    print('(((1-math.sqrt(5)) / 2)**n) ............................... = ' + str((((1-math.sqrt(5)) / 2)**n)))
    print('round(((1-math.sqrt(5)) / 2)**n, 5) ....................... = ' + str(round(((1-math.sqrt(5)) / 2)**n, 7)))
    print('((((1+math.sqrt(5)) / 2)**n) - (((1-math.sqrt(5)) / 2)**n)) = ' + str(((((1+math.sqrt(5)) / 2)**n) - (((1-math.sqrt(5)) / 2)**n))))
    return ((((1+math.sqrt(5)) / 2)**n) - round(((1-math.sqrt(5)) / 2)**n, 7)) / math.sqrt(5)

def fib_iterative(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    arr = [0,1]
    for i in range(2, n+1, 1):
        arr.append(arr[i-2] + arr[i-1])
    return arr[len(arr)-1]


def fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n-2) + fib_recursive(n-1)
def main():
    for i in range(0,75):
        # ----
        start = time.time()
        x = fib_binet(i)
        end = time.time()
        time_len = end - start
        print(str(i) + ' Binet:' + str(str(x)) + ' Time: ' + str(time_len))
        # ----
        start = time.time()
        x = fib_iterative(i)
        end = time.time()
        time_len = end - start
        print(str(i) + ' Iterv:' + str(str(x)) + ' Time: ' + str(time_len))
        # ----
        # start = time.time()
        # x = fib_recursive(i)
        # end = time.time()
        # time_len = end - start
        # print(str(i) + ' Recur:' + str(int(x)) + ' Time: ' + str(time_len))
        # ----
        print('-'*20)

if __name__ == "__main__":
    main()
