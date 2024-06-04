menulist = []
price = []
def showBill():
    print("---- My Food----")
    total = 0
    for number in range(len(menulist)):
        print(menulist[number], price[number])
        total += int(price[number])
    print("Tatal Price :",total)
while True:
    menuname = input("Enter your menu:")
    if menuname.lower() == "exist":
        break
    else:
        pricemenu = input("Price :")
    menulist.append(menuname)
    price.append(pricemenu)
showBill()