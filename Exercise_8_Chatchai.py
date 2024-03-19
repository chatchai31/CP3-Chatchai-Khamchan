usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "chatchai" and passwordInput == "9999":
    print("Welcome to Uspace Resort !")
    print("*******Room Type*******")
    print("1. Superior Garden   Price 2,800.-")
    print("2. Dluxe Oceanphere  Price 3,300.-")
    print("3. Duplex Suite      Price 4,200.-")
    userSelected = int(input("select room type>>"))
    numberRoom = int(input("Number >>"))
    if userSelected == 1:
        sumprice = numberRoom*2800
        print("Superior Garden x",numberRoom)
    elif userSelected == 2:
        sumprice = numberRoom * 3300
        print("Dluxe Oceanphere x", numberRoom)
    elif userSelected == 3:
        sumprice = numberRoom * 4200
        print("Duplex Suite x", numberRoom)
    else:
        print("Not Found Type Room")
    print("Total Price =",sumprice,"Baht")
else:
    print("Please Check Your Username & Password")