from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # ใช้ Pillow สำหรับการจัดการรูปภาพ
from tkinter.messagebox import showinfo
import math

class AppGUI:

    def __init__(self):
        self.MainWindow = Tk()
        self.MainWindow.title("โปรแกรมคำนวณค่าแท็กซี่")
        self.MainWindow.geometry('650x500')

        # โหลดและปรับขนาดรูปภาพ
        self.image = Image.open("Taxi.jpg")  # เปิดไฟล์รูปภาพ
        self.image = self.image.resize((650, 220))  # กำหนดขนาดรูปภาพ
        self.tk_image = ImageTk.PhotoImage(self.image)  # แปลงให้ Tkinter ใช้ได้
        # แสดงรูปภาพ
        self.image_label = Label(self.MainWindow, image=self.tk_image)
        self.image_label.grid(row=0, column=0, columnspan=10)

        self.label_data = Label(self.MainWindow, text="**ใส่ข้อมูล**", width=20, font=("Helvetica", 16, "bold"))
        self.label_data.grid(row=1, column=0)

        self.label_type_car = Label(self.MainWindow, text="ประเภทรถแท็กซี่", font=("Helvetica", 12))
        self.label_type_car.grid(row=3, column=0)
        # dropdown
        self.choice = StringVar(value="Select")
        self.combo_type_car = ttk.Combobox(self.MainWindow, textvariable=self.choice, font=("Helvetica", 9))
        self.combo_type_car["values"] = ("ขนาดปกติ", "ขนาดใหญ่ (สามตอน/แวน)")
        self.combo_type_car.grid(row=3, column=1)

        self.label_distance = Label(self.MainWindow, text="ระยะทาง (กิโลเมตร)", font=("Helvetica", 12))
        self.label_distance.grid(row=4, column=0)
        self.textBoxdistance = Entry(self.MainWindow)
        self.textBoxdistance.grid(row=4, column=1)

        self.label_timelate = Label(self.MainWindow, text="เวลารถติด (นาที)", font=("Helvetica", 12))
        self.label_timelate.grid(row=5, column=0)
        self.textBoxtimelate = Entry(self.MainWindow)
        self.textBoxtimelate.grid(row=5, column=1)

        # ปุ่มล้างข้อมูล
        self.btn_delete = Button(self.MainWindow, text="ล้างข้อมูล", command=self.deletetext, fg="red",
                                 font=("Helvetica", 10), activebackground="red")
        self.btn_delete.grid(row=4, column=2)
        # ปุ่มคำนวณ
        self.btn_confirm = Button(self.MainWindow, text="คำนวณ", command=self.process, width=4,
                                  font=("Helvetica", 12, "bold"), activebackground="green")
        self.btn_confirm.grid(row=6, column=1)
        # แสดงผลลัพธ์
        self.label_result = Label(self.MainWindow, text="**ผลลัพธ์**", width=20, font=("Helvetica", 16, "bold"))
        self.label_result.grid(row=7, column=0)
        self.label_value = Label(self.MainWindow, text="ค่าโดยสาร", font=("Helvetica", 12))
        self.label_value.grid(row=8, column=0)
        self.textBoxResult = Entry(self.MainWindow, fg="green", font=("Helvetica", 14, "bold"))
        self.textBoxResult.grid(row=8, column=1)
        self.textBoxResult.insert(0, "0 บาท")

        self.MainWindow.mainloop()

    def deletetext(self):
        self.textBoxdistance.delete(0, END)
        self.textBoxtimelate.delete(0, END)

    def process(self):
        try:
            select_car_type = self.choice.get()
            distance = int(self.textBoxdistance.get())
            time_late = int(self.textBoxtimelate.get() or 0)

            if select_car_type == "Select":
                showinfo(title='Error', message="กรุณาเลือกประเภทรถโดยสาร")
            else:
                price = self.calculate_price(select_car_type, distance, time_late)
                self.textBoxResult.delete(0, END)
                self.textBoxResult.insert(0, f"{math.ceil(price)} บาท")
        except ValueError:
            showinfo(title='Error', message="กรุณากรองข้อมูลให้ครบ")

    def calculate_price(self, select_car_type, distance, time_late):
        price = 0
        # คำนวณตามประเภทของรถ
        if select_car_type == "ขนาดปกติ":
            price = self.calculate_normal_car_price(distance, time_late)
        elif select_car_type == "ขนาดใหญ่ (สามตอน/แวน)":
            price = self.calculate_large_car_price(distance, time_late)
        return price

    def calculate_normal_car_price(self, distance, time_late):
        price = 35.00  # ค่าโดยสารเริ่มต้น
        distance -= 1  # กิโลเมตรแรก
        # ทำแบบเดียวกันสำหรับระยะทางที่เหลือ
        price += self.calculate_additional_price(distance)
        price += time_late * 3.00  # เพิ่มค่าใช้จ่ายจากเวลารถติด
        return price

    def calculate_large_car_price(self, distance, time_late):
        price = 40.00  # ค่าโดยสารเริ่มต้น
        distance -= 1  # กิโลเมตรแรก
        # ทำแบบเดียวกันสำหรับระยะทางที่เหลือ
        price += self.calculate_additional_price(distance)
        price += time_late * 3.00  # เพิ่มค่าใช้จ่ายจากเวลารถติด
        return price

    def calculate_additional_price(self, distance):
        price = 0
        if distance > 0:
            km = min(distance, 9)
            price += km * 6.50
            distance -= km
        if distance > 0:
            km = min(distance, 10)
            price += km * 7.00
            distance -= km
        if distance > 0:
            km = min(distance, 20)
            price += km * 8.00
            distance -= km
        if distance > 0:
            km = min(distance, 20)
            price += km * 8.50
            distance -= km
        if distance > 0:
            km = min(distance, 20)
            price += km * 9.00
            distance -= km
        if distance > 0:
            price += distance * 10.50
        return price

# เรียกใช้งานโปรแกรม
AppGUI()