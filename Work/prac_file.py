# file_prac.py
# practice Files Management Lesson-1.6 : David Beazley

## [Start]
print("hello files")

## [File Input and Output]
f = open("foo.txt", "rt") # open for reading text
g = open("bar.txt", "wt") # open for writing text

## [Reading file data]
with open("foo.txt", "rt") as file:
    data = file.read()
    print(data)
    print(type(data))

with open("foo.txt", "wt") as file:
    file.write("This is line one.")

with open("foo.txt", "at") as file:
    file.write("This is line two.")
    file.write("This is line three")


with open("foo.txt", "rt") as file:
    for line in file:
        print(line)

with open("foo.txt", "wt") as out:
    print("Hello, World", file=out)


## [ Exercise: 1.26]
import os
print(os.getcwd())

with open("Data/portfolio.csv", "rt") as f:
    data = f.read()
    print(data)

with open("Data/portfolio.csv", "rt") as f:
    for line in f:
        print(line, end="")

f = open("Data/portfolio.csv", "rt")
headers = next(f)
print(headers)

for line in f:
    print(line, end="")

print(f.read())
print(headers)

f.close()

f = open("Data/portfolio.csv", "rt")
headers = next(f).split(",")
print(headers)

for line in f:
    row = line.split(",")
    print(row)

f.close()

## [ Exercise: 1.28]
import gzip

with gzip.open("Data/portfolio.csv.gz", "rt") as f:
    for line in f:
        print(line, end="")
        #line = line.split(",")
        #print(line)















