from Tkinter import *
root = Tk()
myLabel = Label(root, text = "Hello there!")
myButton = Button(root,text = "Click me!")

varCheck = False
varCountry = 
myCheckButton = Checkbutton(root, text = "Remember Me", variable = varCheck, onvalue = True, offvalue = False)
myEntry = Entry(root, width = 30)
myOptionMenu = OptionMenu(root,varCountry, "Select Country", "USA", "UK", "India")
myButton.pack()
myOptionMenu.pack()
myEntry.pack()
myCheckButton.pack()
myLabel.pack()
root.mainloop()
