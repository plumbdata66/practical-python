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


























