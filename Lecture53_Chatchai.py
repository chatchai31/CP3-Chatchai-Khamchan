def vatCalculate(Price):
    result = Price + (Price*7/100)
    return result
Price = int(input("Price :"))
print("Total Price (vat) = ",vatCalculate(Price))