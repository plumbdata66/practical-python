import sys
import csv

def portfolio_cost(filename):

    total_cost = 0.0
    row_number = 1

    f = open(filename, "rt")
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        row_number += 1
        try:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price

        except ValueError:
            print("Bad Row: ", row_number, row)

    return total_cost

try:
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Enter a filename: ")

    cost = portfolio_cost(filename)
    print("Total Cost: ", cost)

except FileNotFoundError:
    print("File Not Found. No such file or directory. Please Check!")
