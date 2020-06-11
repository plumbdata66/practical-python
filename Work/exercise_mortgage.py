# mortgage.py
# Calculate the total amount to pay over the life of the mortgage
# Exercise 1.7

principal = 5_00_000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 1000.0
extra_payment_start_month = 60
extra_payment_end_month = 108

# Exercise 1.8
''' 
while principal > 0:
    
    if months <= 12:
        principal = principal * (1 + rate/12) - (payment + 1000)
        total_paid += payment + 1000
        months += 1
    else:
        principal = principal * (1 + rate/12) - payment
        total_paid += payment
        months += 1

print("Total Paid: ", round(total_paid, 2), "Months: ", months)
'''

# Exercise 1.9

while principal > 0:
    month += 1
    principal = principal * (1 + rate/12) - payment
    total_paid += payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid += extra_payment
        
    print("Month: ", month, "Total Paid: ", round(total_paid,2), "Balance: ", round(principal, 2))

print("Total Paid: ", round(total_paid, 2))
print("Months: ", month)

# print("Total Paid: ", round(total_paid, 2), "Months: ", months)
