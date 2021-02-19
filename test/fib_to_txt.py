import math
import time

def fib_iterative(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    arr = [0,1]
    for i in range(2, n+1, 1):
        arr.append(arr[i-2] + arr[i-1])
    return arr[len(arr)-1]

def main():
    f = open('fib.txt', 'w')
    for i in range(10000+1):
        print(str(i) + ' ' + str(fib_iterative(i)))
        f.write(str(i) + ' ' + str(fib_iterative(i)) + '\n')
if __name__ == "__main__":
    main()
