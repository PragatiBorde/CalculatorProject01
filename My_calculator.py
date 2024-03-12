from tkinter import *

def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnClear():
    global val
    val=""
    data.set("")

def btnEquals():
    global val
    results=str(eval(val)) 
    data.set(results)       

root=Tk()
root.geometry("600x490")
root.title("My Calculator")
val=""
data= StringVar()
display = Entry(root,bd=29, justify='right',textvariable=data,bg='powder blue',font=("ariel",22))
display.grid(row=0,columnspan=4)
btn7=Button(text='7',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(7))
btn7.grid(row=1,column=0)
btn8=Button(text='8',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(8))
btn8.grid(row=1,column=1)
btn9=Button(text='9',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(9))
btn9.grid(row=1,column=2)
btnplus=Button(text='+',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('+'))
btnplus.grid(row=1,column=3)

btn4=Button(text='4',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(4))
btn4.grid(row=2,column=0)
btn5=Button(text='5',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(5))
btn5.grid(row=2,column=1)
btn6=Button(text='6',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(6))
btn6.grid(row=2,column=2)
btnminus=Button(text='-',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('-'))
btnminus.grid(row=2,column=3)

btn1=Button(text='1',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(1))
btn1.grid(row=3,column=0)
btn2=Button(text='2',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(2))
btn2.grid(row=3,column=1)
btn3=Button(text='3',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(3))
btn3.grid(row=3,column=2)
btnmul=Button(text='*',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('*'))
btnmul.grid(row=3,column=3)

btnc=Button(text='Clear',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnClear)
btnc.grid(row=4,column=0)
btn0=Button(text='0',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(0))
btn0.grid(row=4,column=1)
btndiv=Button(text='/',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('/'))
btndiv.grid(row=4,column=2)
btnequal=Button(text='=',font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnEquals)
btnequal.grid(row=4,column=3)












root.mainloop()


