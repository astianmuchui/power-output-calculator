import tkinter
from tkinter import *
from tkinter import messagebox
def calculateOutput():
    if volt_value.get() != '' or res_value.get() != '':
        if isinstance(int(volt_value.get()),int) and isinstance(int(res_value.get()),int):
            #Math
            r_sq = int(volt_value.get())**2
            power = str(r_sq/int(res_value.get())) + " Watts"
            val = Label(app,text=power, font=("italic",16),foreground="#e03b09",padx=5,pady=15)
            val.grid(row=9,column=3,sticky=W)
            val.configure(background="#00030a")
            volt_input.delete(0, END)
            res_input.delete(0, END)

        else:
            messagebox.showerror("Invalid values","Values must be numbers")
                 
    else:
        messagebox.showerror("Missing values","Fill in all fields")
    return power
app = Tk()
app.geometry("600x400")
app.resizable(False,False)
app.configure(background="#00030a")
intro = Label(app,text="Welcome:", font=("italic",16),foreground="#2fa4e7",padx=5,pady=15)
intro.grid(row=1,column=1,sticky=W)
volt_value = StringVar()
volts = Label(app, text="Voltage Rating (V)", font=("bold",12),foreground="crimson", padx=5,pady=2)
volts.configure(background="#00030a")
volts.grid(row=2,column=2,sticky=W)
volt_input = Entry(app,textvariable=volt_value,border=1,width=35,background="#d4d4d4",borderwidth=0)
volt_input.grid(row=2,column=3,sticky=W)
volt_input.place(x=247,y=62,height=30)
res_value = StringVar()
res = Label(app, text="Resistance (Ω)", font=("bold",12),foreground="crimson", padx=5,pady=2)
res.configure(background="#00030a")
res.grid(row=3,column=2,sticky=W,pady=10)
res_input = Entry(app,textvariable=res_value,border=1,width=35,background="#d4d4d4",borderwidth=0)
res_input.grid(row=3,column=3,sticky=W)
res_input.place(x=247,y=96,height=30)
button = Button(app,text="Calculate",width=14,command=calculateOutput,background="skyblue",activebackground="skyblue",border=0,height=2)
button.grid(row=4,column=3,sticky=W)
output = Label(app,text="Power Output :", font=("italic",16),foreground="#09e058",padx=5,pady=15)
output.grid(row=7,column=3,sticky=W)
output.configure(background="#00030a")
app.title("Power output calculator")
intro.configure(background="#00030a")
app.mainloop()