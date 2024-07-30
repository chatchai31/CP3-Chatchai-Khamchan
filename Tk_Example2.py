from tkinter import *
# การใช้ from จะเป็นการเรียกใช้ module นั่นโดยตรงตั้งแต่แรก

def leftClickButton(event):
    print("Left Click")
def DoubleClickButton(event):
    print("Double Click")
main = Tk()
button = Button(main, text = "My Button!!")
button.pack() # pack เป็นฟังชั่นใส่ค่าลงไป main
# bind เป็นการผูกเชื่อมโยก เหตุการณ์ เข้าด้วยกันกับ Function
# Button -1ปุ่มซ้าย -2ปุ่มตรงกลาง -3ปุ่มขวา
button.bind('<Button-1>',leftClickButton)
button.bind('<Double-1>',DoubleClickButton)
main.mainloop()