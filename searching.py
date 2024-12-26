import mysql.connector as ctor
from tkinter import *
con = ctor.connect(host="localhost",user ="root",password='7488',database="items")
cur = con.cursor()

def delete ():
    entryn.delete(0,END)
    entryqty.delete(0,END)
    entryp.delete(0,END)
    entrya.delete(0,END)

def enter ():
    print("not completed yet")

root = Tk()
root.geometry("700x500+300+100")
#img = PhotoImage(file="")
#root.iconphoto(false,img)
root.title("sails management")
label= Label(root,text= "Sails Management System",bg="cyan",fg="black")
label.pack(side=TOP,fill =X,padx=4,pady=4)

frame = Frame(root,bg="blue")
frame.place(x=15,y=40)
label=Label(frame,text="Details Entry",bg='black',fg='white')
label.grid(row=0,column=0,columnspan=3,ipadx=4,ipady=4,padx=5,pady=5)

labeln=Label(frame,text="Item name")
labeln.grid(row=1,column=1,padx=10,pady=4,ipadx=3,ipady=3)
entryn=Entry(frame,text="",width=20)
entryn.grid(row=1,column=2,padx=4,pady=4,ipadx=3,ipady=3)

labelqty=Label(frame,text="Quantuty")
labelqty.grid(row=2,column=1,padx=4,pady=4,ipadx=3,ipady=3)
entryqty=Entry(frame,text="",width=20)
entryqty.grid(row=2,column=2,padx=4,pady=4,ipadx=3,ipady=3)

labelp=Label(frame,text="Price")
labelp.grid(row=3,column=1,padx=4,pady=4,ipadx=3,ipady=3)     
entryp=Entry(frame,text="",width=20)
entryp.grid(row=3,column=2,padx=10,pady=4,ipadx=3,ipady=3)

labela=Label(frame,text="Amount")
labela.grid(row=4,column=1,padx=4,pady=4,ipadx=3,ipady=3)
entrya=Entry(frame,text="",width=20)
entrya.grid(row=4,column=2,padx=4,pady=4,ipadx=3,ipady=3)

button_d = Button (frame,text="DELETE",command=delete,bg="red",fg="black")
button_d.grid(row=5,column=0,columnspan=2,padx=5,pady=5,ipadx=2,ipady=2)

button_e = Button (frame,text="ENTER",command=enter,bg="orange",fg="black")
button_e.grid(row=5,column=2,columnspan=2,padx=5,pady=5,ipadx=4,ipady=4)

frame2=Frame(root,bg="cyan")
frame2.place(x=270,y=40)

listbox=Listbox(frame2)
listbox.pack(side=TOP,fill=BOTH,padx=4,pady=4,ipad=2,ipady=2)

root.mainloop()
