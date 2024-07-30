from tkinter import *
import math
def Calculate(x):
    BMI = float(textBoxWeigth.get())/math.pow(float(textBoxHight.get())/100,2)
    labelBMI.configure(text=BMI)

    if BMI < 18.5:
        labelResult.configure(text="ผอมเกินไป")
    elif 25 > BMI > 18.5:
        labelResult.configure(text="รูปร่างปกติ")
    elif 30 > BMI > 24:
        labelResult.configure(text="ค่อนข้างอ้วน")
    elif BMI > 29:
        labelResult.configure(text="อ้วนมาก")

MainWindow = Tk()
labelHight = Label(MainWindow,text="ส่วนสูง (cm.)").grid(row=0,column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)

labelWeigth = Label(MainWindow,text="น้ำหนัก (Kg.)").grid(row=1,column=0)
textBoxWeigth = Entry(MainWindow)
textBoxWeigth.grid(row=1,column=1)

calculateButton = Button(MainWindow,text="คำนวณ BMI")
calculateButton.grid(row=2,column=0)
calculateButton.bind('<Button-1>',Calculate)

labelBMI = Label(MainWindow,text="ผลลัพธ์ BMI")
labelBMI.grid(row=2,column=1)

labelResult = Label(MainWindow,width=15,foreground='red',font=("TH SarabunPSK",15))
labelResult.grid(row=3,column=1)

MainWindow.mainloop()