from tkinter import *
options = [
    "Hz",
    "KHz",
    "MHz"
]
def calculation():
    f=float(inputF.get())
    if clicked.get() =="Hz":
        F=f
    elif clicked.get() =="KHz":
        F=f*1000
    elif clicked.get() =="MHz":
        F=f*1000000
    c=299792458
    y=c/F
    y_out.insert(0, y)
    halfy_out.insert(0, y/2)
    Quartery_out.insert(0, y/4)
def clear():
    inputF.delete(0,END)
    y_out.delete(0,END)
    halfy_out.delete(0,END)
    Quartery_out.delete(0,END)
    
root=Tk()
root.title("Wavelenght calculator")
f_in=Label(root, text="frequency")
f_in.grid(row=0 ,column=0)

inputF=Entry(root, width=30)
inputF.grid(row=0, column=1)
inputF.get()

clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu( root , clicked , *options )
drop.grid(row=0 ,column=2)


calculatebutton=Button(root, text="Calculate", command=calculation, bg='lime')
calculatebutton.grid(row=1 ,column=0)

clearBTN=Button(root, text="Clear", command=clear, bg='red')
clearBTN.grid(row=1 ,column=2)


yl=Label(root, text="Full Wavelenght")
yl.grid(row=2 ,column=0)

y_out=Entry(root, width=30)
y_out.grid(row=2 ,column=1)

meter1=Label(root, text="Meter")
meter1.grid(row=2 ,column=2)

halfyl=Label(root, text="1/2 Wavelenght")
halfyl.grid(row=3 ,column=0)

halfy_out=Entry(root, width=30)
halfy_out.grid(row=3 ,column=1)

meter2=Label(root, text="Meter")
meter2.grid(row=3 ,column=2)


Quarteryl=Label(root, text="1/4 Wavelength")
Quarteryl.grid(row=4 ,column=0)

Quartery_out=Entry(root, width=30)
Quartery_out.grid(row=4 ,column=1)

meter3=Label(root, text="Meter")
meter3.grid(row=4 ,column=2)

ans=("")
root.mainloop()

meter3=Label(root, text="Meter")
meter3.grid(row=4 ,column=3)