from tkinter import *

gui = Tk(className='Calculator')
gui.geometry("346x370")
gui.iconbitmap("C:/Users/My PC/Desktop/python project/Tkinter/eee.ico")
gui.config(bg='#18191C')
opr = ""
text = StringVar()

def btnclick(numbers):
    global opr
    opr = opr + str(numbers)
    text.set(opr)


def btnequal():
    global opr
    result = str(eval(opr))
    text.set(result)
    opr = ""

def btnclear():
    global opr
    opr=""
    text.set("")


result_label = Entry(gui, textvariable=text,width=20, borderwidth="10",bg='#373A40',fg="white",font=('Helvetica',20))

result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

btn7 = Button(gui, text="7", width=3,  height=1,borderwidth=3, font=('Helvetica',20), command=lambda: btnclick('7')).grid(row=1, column=0,padx=16)
btn8 = Button(gui, text="8", width=3, height=1, borderwidth=3,font=('Helvetica',20), command=lambda: btnclick('8')).grid(row=1, column=1,padx=10)
btn9 = Button(gui, text="9", width=3, height=1, borderwidth=3,font=('Helvetica',20), command=lambda: btnclick('9')).grid(row=1, column=2,padx=10)
btnadd = Button(gui, text="+", width=3, height=1,bg='#26272C',fg="white", font=('Helvetica',20),borderwidth=3, command=lambda: btnclick("+")).grid(row=1,
                                                                                                          column=3,
                                                                                                          pady=6,padx=10)

btn4 = Button(gui, text="4", width=3, height=1, borderwidth='3',font=('Helvetica',20), command=lambda: btnclick(4)).grid(row=2, column=0)
btn5 = Button(gui, text="5", width=3, height=1, borderwidth="3",font=('Helvetica',20), command=lambda: btnclick(5)
              )

btn6 = Button(gui, text="6", width=3, height=1, borderwidth='3',font=('Helvetica',20), command=lambda: btnclick(1))
btnsub = Button(gui, width=3, height=1, text="-", borderwidth='3',font=('Helvetica',20),bg='#26272C',fg="white",
                        command=lambda: btnclick("-"))

btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btnsub.grid(row=2, column=3, pady=6)

btn1 = Button(gui, text="1", width=3, height=1, borderwidth='3', font=('Helvetica',20),command=lambda: btnclick(1))

btn2 = Button(gui, text="2", width=3, height=1, borderwidth='3',font=('Helvetica',20),
              command=lambda: btnclick(2)
              )

btn3 = Button(gui, text="3", width=3, height=1, borderwidth='3',font=('Helvetica',20), command=lambda: btnclick(3))
btnmul = Button(gui, width="3", height="1", text="X",borderwidth='3',font=('Helvetica',20),bg='#26272C',fg="white", command=lambda: btnclick("*")).grid(row=3, column=3,
                                                                                                     )
btn1.grid(row=3, column=0,pady=6)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn0 = Button(gui, text="0", width=3, height=1,borderwidth=3, font=('Helvetica',20),command=lambda: btnclick(0)).grid(row=4, column=0,pady=6)
btnclear = Button(gui, text="C", bg="#931A1F", fg="white", width=3,font=('Helvetica',20), height=1,borderwidth=3, command=btnclear).grid(row=4, column=1)
btnequal = Button(gui, text="=", width=3, height=1, borderwidth="3",bg='#26272C',fg="white",font=('Helvetica',20), command=btnequal).grid(row=4, column=2)
btndivi = Button(gui, command=lambda: btnclick("/"), width="3",font=('Helvetica',20),bg='#26272C',fg="white", height="1",borderwidth=3, text="/").grid(row=4, column=3)

gui.mainloop()
