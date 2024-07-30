import tkinter

def sayHello():
    print("Hello World")
mainWindow = tkinter.Tk()
button = tkinter.Button(mainWindow,text="Click Me!!",command=sayHello).grid(row=1,column=0)
button2 = tkinter.Button(mainWindow,text="Click Me!!",command=sayHello).grid(row=2,column=0)
button3 = tkinter.Button(mainWindow,text="Click Me!!",command=sayHello).grid(row=0,column=1)
label = tkinter.Label(mainWindow,text="Hello world",width=20,foreground='red',bg='black',font=("TH SarabunPSK",20),anchor=tkinter.W).grid(row=0,column=0)
# wigth กำหนดความกล้างของ Button
# grid เลือกตำแหน่ง row/column ใส่ลงใน mainWindow
# Label ฟังชั่นป้ายประกาศข้อความเปล่าๆ
# foreground หรือย่อ fg ใส่สี text
# anchor กำหนดข้อมความให้อยู่ W = ซ้าย E = ขวา
mainWindow.mainloop()