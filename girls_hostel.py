from tkinter import *
import time
import random
from tkinter import Toplevel,messagebox
from tkinter import ttk

def added_student():
    if rbval.get()=="0":
        add_label=Label(addbase,text="Vehicle type",font=("arial",16,"italic"),bg="lightcyan")
        add_label.place(x=10,y=400)
        add_label2=Label(addbase,text="Vehicle number",font=("arial",16,"italic"),bg="lightcyan")
        add_label2.place(x=10,y=450)
        add_entry=Entry(addbase,width="15",font=("arial",16,"italic"))
        add_entry.place(x=250,y=400)
        add_entry2=Entry(addbase,width="15",font=("arial",16,"italic"))
        add_entry2.place(x=250,y=450)

    else:
        end_label.configure(text="Added Successfully!!!!", fg="blue", font=("arial", 18, "italic bold"))


def new_admission():
    global addbase
    addbase=Toplevel(master=data_entry_frame)
    addbase.grab_set()
    addbase.geometry("600x600+700+180")
    addbase.title("Add new student")
    addbase.config(bg="powderblue")
    addbase.resizable(False,False)
    namelabel=Label(addbase,text="Enter Name",bg="lightcyan",font=("consolas",16,"italic"),anchor='w')
    namelabel.place(x=10,y=10)
    idlabel=Label(addbase,text="Enter id",bg="lightcyan",font=("consolas",16,"italic"),anchor='w')
    idlabel.place(x=10,y=60)
    agelabel=Label(addbase,text="Enter age",bg="lightcyan",font=("consolas",16,"italic"),anchor='w')
    agelabel.place(x=10,y=110)
    moblabel=Label(addbase,text="Enter mob no.",bg="lightcyan",font=("consolas",16,"italic"),anchor='w')
    moblabel.place(x=10,y=160)
    emaillabel=Label(addbase,text="Enter email",bg="lightcyan",font=("consolas",16,"italic"),anchor='w')
    emaillabel.place(x=10,y=210)
    clglabel=Label(addbase,text="Enter clg name",bg="lightcyan",font=("consolas",16,"italic"),anchor='w')
    clglabel.place(x=10,y=260)
    roomlabel=Label(addbase,text="Enter room no.",bg="lightcyan",font=("consolas",16,"italic"),anchor='w')
    roomlabel.place(x=10,y=310)

    entry_name=Entry(addbase,width=20,bd=4,fg="blue",font=20)
    entry_name.place(x=250,y=10)
    entry_id=Entry(addbase,width=20,bd=4,fg="blue",font=20)
    entry_id.place(x=250,y=60)
    entry_age=Entry(addbase,width=20,bd=4,fg="blue",font=20)
    entry_age.place(x=250,y=110)
    entry_mob=Entry(addbase,width=20,bd=4,fg="blue",font=20)
    entry_mob.place(x=250,y=160)
    entry_email=Entry(addbase,width=20,bd=4,fg="blue",font=20)
    entry_email.place(x=250,y=210)
    entry_clg=Entry(addbase,width=20,bd=4,fg="blue",font=20)
    entry_clg.place(x=250,y=260)
    entry_room=Entry(addbase,width=20,bd=4,fg="blue",font=20)
    entry_room.place(x=250,y=310)
    rblabel=Label(addbase,text="Do you have any vehicle?",font=("consolas",16,"italic"),bg="lightcyan")
    rblabel.place(x=10,y=360)

    global rbval
    rbval = StringVar()
    rb1 = Radiobutton(addbase, text="yes", variable=rbval, value=0,font=("consolas",16),fg="black",bg="powderblue")
    rb1.place(x=320, y=360)
    rb2 = Radiobutton(addbase, text="no", variable=rbval, value=1,font=("consolas",16),fg="black",bg="powderblue")
    rb2.place(x=420, y=360)

    submit_button=Button(addbase,text="SUBMIT",width=15,font=("arial",15,"bold"),bd=5,fg="white",bg="teal",activebackground="blue",activeforeground="aliceblue",command=added_student)
    submit_button.place(x=200,y=500)

    global end_label
    end_label=Label(addbase,text="")
    end_label.place(x=200,y=560)
    addbase.mainloop()

def exit():
    res=messagebox.askyesnocancel('Notification','Do you want to exit?')
    if (res==True):
        base.destroy()

def tick():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d:%m:%Y")
    clock.config(text="Date:"+date_string+"\n"+"Time:"+time_string)
    clock.after(200,tick)
##########
colors=['blue','pink','gold2','red']
def intro_label_color_tick():
    fg=random.choice(colors)
    slider_label.config(fg=fg)
    slider_label.after(5,intro_label_color_tick)

def intro_label_tick():
    global count,text
    if count>=len(ss):
        count=-1
        text=""
        slider_label.configure(text=text)
    else:
        text=text+ss[count]
        slider_label.configure(text=text)
        count+=1
    slider_label.after(200,intro_label_tick)

##########################################################################
base=Tk()
base.title("Hostel Management System")
base.configure(bg="powderblue")
#in below statement + is used to fix screen on proper location
base.geometry("1200x800+200+40")
base.resizable(False,False)
#############################################################################
data_entry_frame= Frame(base,bg="lightcyan",relief=GROOVE,borderwidth=3)
data_entry_frame.place(x=20,y=80,width=400,height=700)
#::::::::::::::
front_label=Label(data_entry_frame,text="---------SELECT----------",width=30,font=("chiller",22,"italic bold"),bg="powderblue")
front_label.pack(side=TOP,expand=True)
addbtn=Button(data_entry_frame,text="New Admission",width=18,font=("arial",18,"italic"),bg="white",bd=6,activebackground="blue",relief=RIDGE,activeforeground="white",command=new_admission)
addbtn.pack(side=TOP,expand=True)
addbtn2=Button(data_entry_frame,text="Intime/Outtime",width=18,font=("arial",18,"italic"),bg="white",bd=6,activebackground="blue",relief=RIDGE,activeforeground="white")
addbtn2.pack(side=TOP,expand=True)
addbtn4=Button(data_entry_frame,text="Visitor",width=18,font=("arial",18,"italic"),bg="white",bd=6,activebackground="blue",relief=RIDGE,activeforeground="white")
addbtn4.pack(side=TOP,expand=True)
addbtn5=Button(data_entry_frame,text="Guest",width=18,font=("arial",18,"italic"),bg="white",bd=6,activebackground="blue",relief=RIDGE,activeforeground="white")
addbtn5.pack(side=TOP,expand=True)
addbtn6=Button(data_entry_frame,text="Leave",width=18,font=("arial",18,"italic"),bg="white",bd=6,activebackground="blue",relief=RIDGE,activeforeground="white")
addbtn6.pack(side=TOP,expand=True)
addbtn7=Button(data_entry_frame,text="View info",width=18,font=("arial",18,"italic"),bg="white",bd=6,activebackground="blue",relief=RIDGE,activeforeground="white")
addbtn7.pack(side=TOP,expand=True)
addbtn8=Button(data_entry_frame,text="View/Change Room",width=18,font=("arial",18,"italic"),bg="white",bd=6,activebackground="blue",relief=RIDGE,activeforeground="white")
addbtn8.pack(side=TOP,expand=True)
addbtn9=Button(data_entry_frame,text="Fees",width=18,font=("arial",18,"italic"),bg="white",bd=6,activebackground="blue",relief=RIDGE,activeforeground="white")
addbtn9.pack(side=TOP,expand=True)
addbtn10=Button(data_entry_frame,text="Quit Hostel",width=18,font=("arial",18,"italic"),bg="white",bd=6,activebackground="blue",relief=RIDGE,activeforeground="white")
addbtn10.pack(side=TOP,expand=True)
addbtn11=Button(data_entry_frame,text="Exit",width=18,font=("arial",18,"italic"),bg="white",bd=6,activebackground="blue",relief=RIDGE,activeforeground="white",command=exit)
addbtn11.pack(side=TOP,expand=True)



##################################################################################3
show_data_frame=Frame(base,bg="lightcyan",relief=GROOVE,borderwidth=3)
show_data_frame.place(x=450,y=80,width=700,height=700)

#############################################################################
ss="GIRLS HOSTEL MANAGEMENT "
count=0
text=""
slider_label=Label(base,text=ss,font=("chiller",30,"italic bold"),relief=RIDGE,borderwidth=5,width=35,bg="white")
slider_label.place(x=300,y=20)
intro_label_tick()
intro_label_color_tick()
#####
clock=Label(base,font=("chiller",14,"bold"),relief=RIDGE,borderwidth=5,bg="white")
clock.place(x=0,y=0)
tick()

base.mainloop()

