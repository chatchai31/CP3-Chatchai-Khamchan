import tkinter

def sayHello():
    print("Hello World")
mainWindow = tkinter.Tk()
button = tkinter.Button(mainWindow,text="Click Me!!",command=sayHello)
button.place(x=50,y=50) # place เป็นการวางตำแหน่ง button ใน mainWindow
button2 = tkinter.Button(mainWindow,text="Click Me!!",command=sayHello)
button2.place(x=150,y=50)
mainWindow.mainloop()