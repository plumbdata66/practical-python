# prac_functions.py
# practice Functions Lesson-1.7 : David Beazley

## [Custom Functions]
def sumcount(n):
    '''
    Returns the sum of forst n integers
    '''
    total = 0

    while n > 0:
        total += n
        n -= 1

    # print(total)
    return total


a = sumcount(10)
print(a)

## [Library Functions]

import math
x = math.sqrt(10)
print(x)

import urllib.request
u = urllib.request.urlopen("http://www.python.org")
data = u.read()
print(data)

## [Errors and Exceptions]
int("N/A")

raise RuntimeError("what a kerfuffle")

## [Exercise: 1.29]

def greeting(name):
    """
    Issues a greeting
    """
    print("Hello", name)


greeting("Monty")
greeting(21)
greeting(Monty)

help(greeting)

## [Exercise: 1.30]
def portfolio_cost(filename):

    total_cost = 0.0
    
    with open(filename, "rt") as f:
        headers = next(f)

        for line in f:
            row = line.split(",")
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price


    return total_cost
    

cost = portfolio_cost("Data/portfolio.csv")
print("Total Cost: ", cost)

cost2 = portfolio_cost("Data/missing.csv")
print(cost2)

## [Exercise: 1.31]

total_cost = 0.0
row_number = 1

with open("Data/missing.csv", "rt") as f:
    headers = next(f)
    for line in f:
        row_number += 1
        row = line.split(",")

        try:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price

        except ValueError:
                print('Bad row:', row_number, "=>", row)

print("Total Cost: ", total_cost)

## [Exercise: 1.32]
import csv
f = open("Data/portfolio.csv")
rows = csv.reader(f)
headers = next(rows)
print(headers)

for row in rows:
    print(row)

f.close()

## [Exercise 1.32-a]

import csv

total_cost = 0.0
row_number = 1

f = open("Data/missing.csv", "rt")
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

print("Total Cost: ", total_cost)

## [Exercise 1.33]

# Reading from the command line


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

import sys

try: 
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Enter a filename")

    cost = portfolio_cost(filename)
    print("Total Cost: ", cost)

except FileNotFoundError:
    print("File Not Found. No such file or directory")


    


















