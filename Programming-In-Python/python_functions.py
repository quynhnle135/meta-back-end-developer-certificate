bill = 175.00
tax_rate = 15
total_tax = (bill * tax_rate) / 100.00
print('Total tax', total_tax)


def calculate_tax(bill, tax_rate):
    return (bill * tax_rate) / 100.00


print(calculate_tax(200, 15))
print("Total tax", calculate_tax(bill, tax_rate))
