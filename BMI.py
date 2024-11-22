from tkinter import *
# Frame
root = Tk()
root.title("BMI Calculator")
root.configure(bg="#252525")
root.geometry("500x400")
root.resizable(0,0)
# Functions
def clear():
    order1.delete(0,END)
    order2.delete(0,END)
    order3.delete(0,END)

def BMI():
    order3.delete(0,END)
    h = order1.get()
    w = order2.get()
    h = float(h)
    w = float(w)
    result = (w / (h * h))
    result = str(result)
    bmi = float(result)
    if bmi <= 25 and bmi > 18.5:
        order3.insert(0,(result[0:5],"Normal weight"))
    elif bmi > 25:
        order3.insert(0,(result[0:5],"Over weight"))
    elif bmi < 18.5:
        order3.insert(0,(result[0:5],"Under weight"))
# Lable
text = Label(root, text= "BMI Rate", fg="white", bg="#252525", font="corbel 45 bold", width="60")
text.pack()


height = Label(root, text="Enter your height in meters:", fg="white", bg="#252525", font="corbel 13 bold")
height.place(x="62", y="95")

weight = Label(root, text="Enter your weight in Kg:", fg="white", bg="#252525", font="corbel 13 bold")
weight.place(x="62", y="175")

bmi = Label(root, text="Your BMI is:", fg="white", bg="#252525", font="corbel 13 bold")
bmi.place(x="62", y="255")
# User_input
order1 = Entry(root, font="normal 20 bold", width="25")
order1.place(x="62", y="120")

order2 = Entry(root, font="normal 20 bold", width="25")
order2.place(x="62", y="200")

order3 = Entry(root, font="normal 20 bold", width="25")
order3.place(x="62", y="280")
# Buttons
btn1 = Button(root, text="BMI Calculate", fg="white", bg="#1358CC", bd="0", font="corbel 20 bold", command= BMI)
btn1.place(x="62", y="335")

btn2 = Button(root, text="Clear", fg="white", bg="#FF2D2D", bd="0", font="corbel 20 bold", command= clear)
btn2.place(x="361", y="335")


root.mainloop()