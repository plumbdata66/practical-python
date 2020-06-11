# report.py
#

# Exercise-2.4: List of Tuples

import csv

# list of Tuples

def read_function(filename):
    '''
    Reads in the file
    outputs: tuple (name, shares, price)
    '''
    portfolio_tup = []

    with open(filename, "rt") as f:
        next(f)
        rows = csv.reader(f)
        for row in rows:
            portfolio_tup.append( (row[0], int(row[1]), float(row[2]) ) )

    return portfolio_tup
## [subcode]

portfolio_tup = read_function("Data/portfolio.csv")
print(portfolio_tup)

total_tup = 0.0
for name, shares, price in portfolio_tup:
    total_tup += shares * price

print("Total: ", total_tup)

## [subcode]

# Exercise-2.5: List of Dictionaries

def read_function_dict(filename):
    '''
    Reads in the file
    outputs: dictionary {name, shares, price}
    '''
    
    portfolio_dict = []

    with open(filename, "rt") as f:
        next(f)
        rows = csv.reader(f)
        for row in rows:
            portfolio_dict.append( {"name" : row[0], "shares" : int(row[1]),
                               "price" : float(row[2])} )

    return portfolio_dict

## [subcode]

portfolio_dict = read_function_dict("Data/portfolio.csv")
print(portfolio_dict)

total_dict = 0.0
for s in portfolio_dict:
    total_dict += s["shares"] * s["price"]


print("Total: ", total_dict)

from pprint import pprint
pprint(portfolio_dict)

## [subcode]

# Exercise-2.6: Dictionaries as a Container

def read_prices(filename):

    prices_dict = {}
    
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                prices_dict[row[0]] = float(row[1])

    return prices_dict
            
prices_dict = read_prices("Data/prices.csv")
print(prices_dict)

## [subcode]

# Exercise-2.7: Stocks Valuation

total_value = 0.0
for s in portfolio_dict:
    total_value += s["shares"] * prices_dict[s["name"]]

print("Current Value: ", total_value)

print('Gain', total_value - total_dict)

## [Exercise-2.9]

portfolio = read_function("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")

def make_report(filename1, filename2):



## [subcode]

def read_prices(filename):

    prices_dict = {}
    
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                prices_dict[row[0]] = float(row[1])

    return prices_dict
            
prices_dict = read_prices("Data/prices.csv")
print(prices_dict)
