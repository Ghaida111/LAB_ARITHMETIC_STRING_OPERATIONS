price= 2.99
quantity=3
tax_rate=7.5
subtotal=price*quantity
tax=subtotal *tax_rate/100
total= subtotal+tax

print("Price of item: $",price)
print("Quantity:",quantity)
print("Tax rate:" ,tax_rate)
print("Subtotal: $",subtotal)
print("Tax: $",round(tax,2))
print("Total: $",round(total,2))

