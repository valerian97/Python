from Tkinter import *
myGui = Tk()
myGui.title("Hello World")
myGui.geometry("500x500")
myLabel = Label(myGui, text = "Hello there!",fg = 'white',bg = 'black')
myButton = Button(myGui, text = "Click here!")
myLabel.place(x=100,y=100)
myButton.pack()
myGui.mainloop()
