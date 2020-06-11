# prac_data.py
# practice Working with Data Lesson-2.0 : David Beazley


## [Datatypes and Data Structures]

# Tuples
s = ("GOOG", 100, 49.1)
name = s[0]
shares = s[1]
price = s[2]
print(name, shares, price)

# s[1] = 75
s2 = (s[0], 75, s[1])
print(s2)


# Exercises
import csv
f = open("Data/portfolio.csv")
rows = csv.reader(f)
headers = next(rows)
print(headers)
row = next(rows)
print(row)
f.close()

# Exercise: 2.1 : Tuples
t = (row[0], int(row[1]), float(row[2]))
print(t)

cost = t[1] * t[2]
print(round(cost, 2))
print(f"{cost:0.2f}")

print(t)
t = (name, 2*shares, price)
print(t)

# Exercise 2.2: Dictionaries as a Data Source
d = {
    "name": row[0],
    "shares": int(row[1]),
    "price" : float(row[2])
    }

print(d)

cost = d["shares"] * d["price"]
print(f"{cost:0.2f}")

d["date"] = (6, 11, 2007)
d["account"] = 12345
print(d)

# Exercise: 2.3 : Additional Dict Operations

list1 = list(d)
print(list1)

#list2 = list(d.values)
#print(list2)

for k in d:
    print("k = ", k)

for k in d:
    print(k, " = ", d[k])

keys = d.keys()
print(keys)

del d["account"]
print(keys)

items = d.items()
print(items)

for k, v in d.items():
    print(k, '=', v)

d1 = dict(items)
print(d1)

## [Containers]

# List Construction
records = []

with open("Data/portfolio.csv", "rt") as f:
    next(f) # skip header
    for line in f:
        row = line.split(",")
        records.append( (row[0], int(row[1]), float(row[2])) )

for i, rec in enumerate(records):
    print(i, ":", rec)

# Dicts as a Container
prices = {"GOOG": 513.25, "CAT": 87.22, "IBM": 93.37, "MSFT": 44.12}
print(prices)

# Dict Construction
import csv

prices = {}
row_number = 0

with open("Data/prices.csv", "rt") as f:
    
##    for line in f:
##        row = line.split(",")
##        try:
##            prices[row[0]] = float(row[1])
##        except IndexError:
##            print("Bad Row", row)
        
    rows = csv.reader(f)
    try:
##        row_number += 1
        for row in rows:
            row_number += 1
            prices[row[0]] = float(row[1])

    except:
        print("bad row: ", row_number)        

print(prices)

# Dictionary Lookups

ibm = prices.get("IBM", 0.0)
print(ibm)

scox = prices.get("SCOX", 0.0)
print(scox)

# Composite Keys
holidays = {(1, 1): "New Years", (3, 14): "Pi Day", (9, 13): "Programmer's Day"}
print(holidays[(3, 14)])

# Sets
tech_stocks = {"AAPL", "IBM", "MSFT"}
print(tech_stocks)

tech_stocks = set(["AAPL", "IBM", "MSFT"])
print(tech_stocks)

print("IBM" in tech_stocks)

tech_stocks.add("CAT")
print(tech_stocks)

tech_stocks.remove("CAT")
print(tech_stocks)

names = ["AA", "BB", "IBM", "IBM", "MSFT"]
unique = set(names)
print(unique)

print(tech_stocks.union(names))
print(tech_stocks.intersection(names))
print(tech_stocks.difference(names))


## [Formatted Output]

# Dictionary Formatting

s = {"name": "IBM", "shares": 100, "price": 91.10}

# f-string formatting
print(f"{name:>10s} {shares:>10d} {price:>10.2f}")

# format() method
print("{name:>10s} {shares:>10d} {price:>10}".format(name="IBM", shares=100, price=91.1))

# C-style Formatting
print("The value is %d" % 3)

print("%5d %-5d %10d" % (3,4,5))

print(b"%s has %d messages" % (b"Dave", 37))

# Exercise-2.8 : how to format numbers
value = 42863.1
print(value)
print(f"{value:0.4f}")
print(f"{value:16.2f}")
print(f"{value:>16.2f}")
print(f"{value:<16.2f}")
print(f"{value:*>16.2f}")
print(f"{value:*<16.2f}")

print("%0.4f" % value)

# Exercise-2.9: Collecting Data










## [ Sequences]




## [Collections Module]




## [ List Comprehensions]




## [Object Model]

