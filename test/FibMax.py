import math
import os

OUTPUT_FOLDER_NAME = 'output'
OUTPUT_FILE_NAME = 'fib_max.txt'

def make_output_folder():
    if not os.path.exists(OUTPUT_FOLDER_NAME):
        os.mkdir(OUTPUT_FOLDER_NAME)

def main():
    make_output_folder()
    outfile = open(OUTPUT_FOLDER_NAME + '\\' + OUTPUT_FILE_NAME, 'w')

    arr = [0,1]
    n = 10000000
    for i in range(2, n+1):
        arr.append(arr[i-2] + arr[i-1])
        outfile.write(str(i) + ', ' + str(arr[i]) + '\n')

if __name__ == "__main__":
    main()
