def login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "chatchai" and passwordInput == "9999":
        return True
    else:
        return False
def showMenu():
    print("Welcome to Uspace Resort !")
    print("*******Room Type*******")
    print("1. Superior Garden   Price 2,800.-")
    print("2. Dluxe Oceanphere  Price 3,300.-")
    print("3. Duplex Suite      Price 4,200.-")
def selectMenu():
    userSelected = int(input("select room type>>"))
    numberRoom = int(input("Number >>"))
    return PriceCalculate(userSelected,numberRoom)
def VatCalculate(TotalPrice):
    result = TotalPrice + (TotalPrice*7/100)
    print("Price Total (VAT) :",result,"Baht")
    return result
def PriceCalculate(userSelected,numberRoom):
    if userSelected == 1:
        sumprice = numberRoom*2800
        print("Superior Garden x",numberRoom)
        return VatCalculate(sumprice)
    elif userSelected == 2:
        sumprice = numberRoom * 3300
        print("Dluxe Oceanphere x", numberRoom)
        return VatCalculate(sumprice)
    elif userSelected == 3:
        sumprice = numberRoom * 4200
        print("Duplex Suite x", numberRoom)
        return VatCalculate(sumprice)
login()
showMenu()
selectMenu()