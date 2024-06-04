systemMenu = {"ไก่ทอด": 35, "ส้มตำ": 45, "ปลาทอด": 40, "ลาบเนื้อ": 60}
menuList = []
def showBill():
    Total = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        Total += int(menuList[number][1])
    print("Total Price:",Total)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    elif menuName in systemMenu:
        menuList.append([menuName, systemMenu[menuName]])
    else:
        print(menuName,"ไม่พบในรายการเมนู!!")
showBill()