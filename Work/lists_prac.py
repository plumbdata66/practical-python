# lists_prac.py
# practice Lists Lesson-1.5 : David Beazley

print("Hello Lists")

## [List from Strings]
line = "GooG, 100, 490.10"
row = line.split(",")
print(row)

## [Replication]

s = [1, 2, 3]
print(s * 3)

## [Find Index]
names = ["Elwood", "Jake", "Curtis"]
print(names.index("Jake"))

## [List Removal]
#names.remove("Jake")
#print(names)

del names[0]
print(names)


## [Sorting]

s = [10, 1, 7, 3]
s.sort()
print(s)

## [Exercises]

symbols = "HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG"
symlist = symbols.split(",")
print(symlist)

## [Exercise: 1.19]

print(symlist[0], symlist[1], symlist[2], symlist[-1], symlist[-2])

# Reassign value
symlist[2] = "AIG"
print(symlist)

# Slicing
print(symlist[0:3])

print(symlist[-2:])

mysyms = []
mysyms.append("GOOG")
print("mysyms: ", mysyms)

print("Old symlist: ", symlist)
symlist[-2:] = mysyms
print("New symlist: ", symlist)

## [Exercise 1.20]
for s in symlist:
    print("s= ", s)


## [Exercise 1.21]

print("AIG" in symlist)
print("AA" in symlist)
print("CAT" not in symlist)

## [Exercise 1.22]
symlist.append("RHT")
print(symlist)




