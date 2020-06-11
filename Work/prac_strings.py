# strings_prac.py
# practice String Lesson-1.4 : David Beazley

print("hello Strings")

a = "\xf1"
print(a)

s = "hello"
t = "e" in s
print(t)

print(s * 5)
print(s.upper())

name = "IBM"
shares = 100
price = 91.1

a = f'{name:>10s} {shares:10d} {price:10.2f}'
print(a)

b = f'Cost = ${shares*price:0.2f}'
print(b)

symbols = "AAPL, IBM, MSFT, YHOO, SCO, "

print(symbols[0])
print(symbols[1])
print(symbols[2])

print(symbols + "Google")

text = "Today is 10/06/2020. Tomorrow is 11/06/2020"

# Find all occurences of date
import re

print(re.findall(r'\d+/\d+/\d+', text))
