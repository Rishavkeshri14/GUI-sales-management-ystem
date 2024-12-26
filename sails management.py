import mysql.connector as ctor
from tkinter import *

def delete ():
    entryn.delete(0,END)
    entryqty.delete(0,END)
    entryp.delete(0,END)
    entrya.delete(0,END)

def enter ():
    name= entryn.get()
    qty= entryqty.get()
    price= entryp.get()
    amt= entrya.get()

    listbox.insert(1,name,qty,price,amt)
    
    con = ctor.connect(host="localhost",user ="root",password='#Rk74887479So*',database="items")
    cur = con.cursor()
    quary="insert into bill values('{}','{}','{}','{}')"#
    val= (name,qty,price,amt)#
    cur.execute(quary,val)#
    con.commit()
    print("work done")
    
root = Tk()
root.geometry("740x500+280+100")
#img = PhotoImage(file="")
#root.iconphoto(false,img)
root.title("sails management")
label= Label(root,text= "Sails Management System",bg="cyan",fg="black")
label.pack(side=TOP,fill =X,padx=4,pady=4)
#------------------------------------------------------------------------------------------------
frame2=Frame(root,bg="cyan")
frame2.place(x=270,y=40)

label_list= Label(frame2,text="TOTAL DETAILS",bg='black',fg='white')
label_list.pack(side=TOP,ipadx=4,ipady=4,padx=5,pady=2)

scroll=Scrollbar(frame2)
scroll.pack(side=RIGHT,fill=Y)

listbox=Listbox(frame2,width=70,height=18,yscrollcomman=scroll.set)
listbox.pack(side=LEFT,fill=BOTH,padx=7,pady=7)

#------------------------------------------------------------------------------------------------
frame = Frame(root,bg="blue")
frame.place(x=15,y=40)
label=Label(frame,text="Details Entry",bg='black',fg='white')
label.grid(row=0,column=0,columnspan=3,ipadx=4,ipady=4,padx=5,pady=2)

labeln=Label(frame,text="Item name")
labeln.grid(row=1,column=1,padx=10,pady=4,ipadx=3,ipady=3)
entryn=Entry(frame,text="",width=20)
entryn.grid(row=1,column=2,padx=4,pady=4,ipadx=3,ipady=3)

labelqty=Label(frame,text="Quantity")
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
#------------------------------------------------------------------------------------------------





root.mainloop()
