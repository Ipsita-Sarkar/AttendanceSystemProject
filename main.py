from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from class_record import Class_Record
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from record import Record

class Face_Recognition_System:
    def __init__(self, root): 
        self.root=root
        self.root.geometry ("1330x700+0+0")
        self.root.title("Face Recogniton System")
        #background image
        img=Image.open(r"ProjectImages\bg2.jpg")
        img=img.resize((1350, 690), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg=Label(self.root, image=self.photoimg)
        bg.place(x=0, y=0,width=1350,height=690)


        title_lbl=Label(bg, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("Montserrat",30,"bold","underline"),bg="#1bc3c6",fg="white") 
        title_lbl.place(x=120, y=80,width=1200,height=50)

        def time():

            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after (1000, time)

        lbl=Label(bg, font = ('times new roman', 14, 'bold'), background = 'white', foreground='black')
        lbl.place(x=0,y=0,width=110, height=50)
        time()

        #student button
        img4=Image.open(r"ProjectImages\student.jpg")
        img4=img4.resize((150,150), Image.ANTIALIAS) 
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button (bg, image=self.photoimg4, cursor="hand2",command=self.student_details)
        b1.place(x=200, y=250,width=150,height=150)
        b1_1=Button (bg, text="Student Details",  cursor="hand2",command=self.student_details, font=("arial", 12, "bold"), bg="#089ae5",fg="white")
        b1_1.place(x=200, y=400,width=150,height=40)

        img7=Image.open(r"ProjectImages\class.png")
        img7=img7.resize((150,150), Image.ANTIALIAS) 
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button (bg, image=self.photoimg7, cursor="hand2",command=self.class_details)
        b1.place(x=550,y=250,width=150,height=150)
        b1_1=Button (bg, text="Class Details",  cursor="hand2",command=self.class_details, font=("arial", 12, "bold"), bg="#089ae5",fg="white")
        b1_1.place(x=550, y=400,width=150,height=40)
       
        img5=Image.open(r"ProjectImages\train.jpg") 
        img5=img5.resize((150,150), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg, image=self.photoimg5, cursor="hand2",command=self.train_data)
        b1.place(x=900,y=250,width=150,height=150)
        b1_1=Button (bg, text="Train Data", cursor="hand2",command=self.train_data,font=("arial", 12, "bold"), bg="#089ae5",fg="white")
        b1_1.place(x=900, y=400,width=150,height=40)

        #attendance button

        

        img8=Image.open(r"ProjectImages\face_r.jpg") 
        img8=img8.resize((150,150), Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button (bg, image=self.photoimg8, cursor="hand2",command=self.face_data)
        b1.place(x=200, y=450,width=150,height=150)
        b1_1=Button (bg, text="Check In", cursor="hand2",command=self.face_data, font=("arial", 12, "bold"), bg="#089ae5",fg="white")
        b1_1.place(x=200, y=600,width=150,height=40)
        #Record button
        img9=Image.open(r"ProjectImages\record.png" )
        img9=img9.resize((150,150), Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button (bg, image=self.photoimg9, cursor="hand2",command=self.show_record) 
        b1.place(x=550, y=450,width=150, height=150)
        b1_1=Button (bg, text="Create Reports", cursor="hand2",command=self.show_record, font=("arial", 12, "bold"), bg="#089ae5",fg="white")
        b1_1.place(x=550, y=600,width=150,height=40)

        img6=Image.open(r"ProjectImages\attendance.jpg") 
        img6=img6.resize((150,150), Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button (bg, image=self.photoimg6, cursor="hand2",command=self.attendance_data) 
        b1.place(x=900, y=450,width=150,height=150) 
        b1_1=Button (bg, text="View Attendance", cursor="hand2",command=self.attendance_data, font=("arial", 12, "bold"), bg="#089ae5",fg="white")
        b1_1.place(x=900, y=600,width=150,height=40)

    def show_record(self):
        self.new_window=Toplevel(self.root)
        self.app=Record(self.new_window)

   

    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

    def class_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Class_Record(self.new_window)

    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)
    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)
    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)

    

    

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()	
    