from tkinter import *
from tkinter import messagebox

root = Tk()
f1=('arial',32)

root.title("Calculator")
root.geometry("215x285")
root.configure(bg='#e6f9ff')
root.resizable(False,False)

e1=Entry(root,width=8,font=f1,bg="#e6ffff")
e1.place(x=10,y=10)

def click(text):
    e1.insert(END,text)
    return

def add():
    try:
        ex=e1.get()
        ans=eval(ex)
        e1.delete(0,END)
        e1.insert(0,ans)
    except Exception as e:
        messagebox.showerror("error",e)
    return

def clearAll():
    e1.delete(0,END)
    return

def clr():
    ex=e1.get()
    ex=ex[0:len(ex)-1]
    e1.delete(0,END)
    e1.insert(0,ex)
    return

#buttons
b1=Button(root,text="<-",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:clr()).place(x=10,y=80)
b2=Button(root,text="%",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click("%")).place(x=110,y=80)
b3=Button(root,text="C",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:clearAll()).place(x=60,y=80)
b4=Button(root,text="=",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:add()).place(x=160,y=80)

b5=Button(root,text="7",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click(7)).place(x=10,y=120)
b6=Button(root,text="8",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click(8)).place(x=60,y=120)
b7=Button(root,text="9",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click(9)).place(x=110,y=120)
b8=Button(root,text="/",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click("/")).place(x=160,y=120)

b9=Button(root,text="4",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click(4)).place(x=10,y=160)
b10=Button(root,text="5",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click(5)).place(x=60,y=160)
b11=Button(root,text="6",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click(6)).place(x=110,y=160)
b12=Button(root,text="*",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click("*")).place(x=160,y=160)

b13=Button(root,text="1",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click(1)).place(x=10,y=200)
b14=Button(root,text="2",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click(2)).place(x=60,y=200)
b15=Button(root,text="3",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click(3)).place(x=110,y=200)
b16=Button(root,text="-",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click("-")).place(x=160,y=200)

b17=Button(root,text="0",bg="#e6f9ff",width=12,activebackground="#ffdf4f",command=lambda:click(0)).place(x=10,y=240)
b18=Button(root,text=".",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click(".")).place(x=110,y=240)
b19=Button(root,text="+",bg="#e6f9ff",width=5,activebackground="#ffdf4f",command=lambda:click("+")).place(x=160,y=240)

root.mainloop()












