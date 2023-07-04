bill_total = 250
discount1 = 10
discount2 = 20

if bill_total > 100 and bill_total < 200:
    print("Bill is greater than 100")
    bill_total = 114 - 10
elif bill_total > 200:
    print("Bill is greater than 200")
    bill_total -= 20
else:
    print("ill is smaller than 100")

print(f"Total bill: {bill_total}")
