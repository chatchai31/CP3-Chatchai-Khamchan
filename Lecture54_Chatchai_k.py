def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        print("User or Password incorrect")
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

if login()==True:
    showMenu()
    menu_number = menuSelect()
    if menu_number == 1:
        price = int(input("Product Price: "))
        print("Price Vat :",vatCalculator(price),"Baht")
    elif menu_number == 2:
        print("Total Price (Vat) :",priceCalculator(),"Baht")
    else:
        print("No have select")
