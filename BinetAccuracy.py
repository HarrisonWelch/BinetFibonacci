import math
import os

OUTPUT_FOLDER_NAME = 'output'
OUTPUT_FILE_NAME = 'output_binet_accuracy.txt'

def fib_binet(n):
    return ((((1+math.sqrt(5)) / 2)**n) - ((1-math.sqrt(5)) / 2)**n) / math.sqrt(5)

def make_output_folder():
    if not os.path.exists(OUTPUT_FOLDER_NAME):
        os.mkdir(OUTPUT_FOLDER_NAME)

def main():
    make_output_folder()
    outfile = open(OUTPUT_FOLDER_NAME + '\\' + OUTPUT_FILE_NAME, 'w')
    n = 10000
    arr = [
        (0,0,0,0,str(0.0)+'%'),
        (1,1,1,0,str(0.0)+'%')
    ]

    for i in range(2, n+1, 1):
        try:
            arr.append((
                i,
                arr[i-2][1] + arr[i-1][1], 
                int(fib_binet(i)),
                (arr[i-2][1] + arr[i-1][1]) - int(fib_binet(i)),
                str((abs( (arr[i-2][1] + arr[i-1][1]) - int(fib_binet(i)) ) / (arr[i-2][1] + arr[i-1][1])) * 100) + '%' ))
        except OverflowError:
            print('Overflow error reached. i = ' + str(i))
            break

    print("+{:8s}+{:18s}+{:18s}+{:18s}+{:28s}+".format('-'*8,'-'*18,'-'*18,'-'*18,'-'*28))
    print("| {:^6s} | {:^16s} | {:^16s} | {:^16s} | {:^26s} |".format('Index', 'Interative', 'Binet\'s Formula', 'Difference', 'ERROR(%)'))
    print("+{:8s}+{:18s}+{:18s}+{:18s}+{:28s}+".format('-'*8,'-'*18,'-'*18,'-'*18,'-'*28))
    for row in arr:
        print("| {:6d} | {:16e} | {:16e} | {:16e} | {:>26s} |".format(row[0],row[1],row[2],row[3],row[4]))
    print("+{:8s}+{:18s}+{:18s}+{:18s}+{:28s}+".format('-'*8,'-'*18,'-'*18,'-'*18,'-'*28))

    
    outfile.write("+{:8s}+{:18s}+{:18s}+{:18s}+{:28s}+".format('-'*8,'-'*18,'-'*18,'-'*18,'-'*28) + '\n')
    outfile.write("| {:^6s} | {:^16s} | {:^16s} | {:^16s} | {:^26s} |".format('Index', 'Interative', 'Binet\'s Formula', 'Difference', 'ERROR(%)') + '\n')
    outfile.write("+{:8s}+{:18s}+{:18s}+{:18s}+{:28s}+".format('-'*8,'-'*18,'-'*18,'-'*18,'-'*28) + '\n')
    for row in arr:
        outfile.write("| {:6d} | {:16e} | {:16e} | {:16e} | {:>26s} |".format(row[0],row[1],row[2],row[3],row[4]) + '\n')
    outfile.write("+{:8s}+{:18s}+{:18s}+{:18s}+{:28s}+".format('-'*8,'-'*18,'-'*18,'-'*18,'-'*28) + '\n')
if __name__ == "__main__":
    main()
