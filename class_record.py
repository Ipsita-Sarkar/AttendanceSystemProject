from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Class_Record:
    def __init__(self, root):
        self.root=root
        self.root.geometry ("1350x690+0+0")
        self.root.title("Attendance Management System")
        # ‒‒‒‒‒‒‒‒‒‒==variables=====

        self.var_std_id=StringVar()
        self.var_class_id=StringVar()
        

        #first image
        img=Image.open(r"ProjectImages\header.jpeg")
        img=img.resize((1350, 100), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0,width=1350,height=100)

        
        #bg

        bg=Label(self.root,bg="white")
        bg.place(x=0, y=100,width=1350,height=560)

        title_lbl=Label(bg, text="ATTENDANCE MANAGEMENT SYSTEM ", font=("Montserrat",25,"bold","underline"),bg="white",fg="#010280") 
        title_lbl.place(x=0, y=15,width=1350,height=80)
        main_frame=Frame (bg, bd=2, bg="white")
        main_frame.place(x=0, y=80,width=1350,height=600)



        #Class Student information

        class_Student_frame=LabelFrame (main_frame, bd=2, bg="white", relief=RIDGE,text="Class Information",font=("times new roman", 13, "bold"))
        class_Student_frame.place(x=350, y=100,width=620,height=200)

        #student id

        studentId_label=Label(class_Student_frame, text="Enter Student ID: ", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=2, padx=80, pady=20, sticky=W)
        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id, width=20, font=("times new roman", 13, "bold")) 
        studentID_entry.grid(row=0,column=3, padx=0, pady=20, sticky=W)
        


        #class_id name

        class_id_label=Label(class_Student_frame, text="Enter Class ID:", font=("times new roman", 13, "bold"), bg="white")
        class_id_label.grid(row=1, column=2, padx=80, pady=5, sticky=W)
        class_id_entry=ttk.Entry(class_Student_frame,textvariable=self.var_class_id, width=20, font=("times new roman",13, "bold"))
        class_id_entry.grid(row=1, column=3, padx=0, pady=5, sticky=W)
       

        #bbuttons frame

        btn_frame=Frame(class_Student_frame, bd=2,relief=RIDGE, bg="white")
        btn_frame.place(x=200, y=120,width=180, height=35)

        save_btn=Button(btn_frame, text="Save",width=17,command=self.add_data, font=("arial",13,"bold"), bg="#010280", fg= "white")
        save_btn.grid (row=0, column=0)

        

    #Function declaration

    def add_data(self):
            a=0
            if  self.var_std_id.get()=="" or self.var_class_id.get()=="":
                messagebox.showerror("Error", "All Fields are required", parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="",username="", password="",database="student_schema")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into record_table values (%s,%s,%s)",(self.var_std_id.get(),self.var_class_id.get(),str(0)))

                    conn.commit()
                    messagebox.showinfo("Done", "Data added!")
                    conn.close()

                except Exception as es:
                    messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)

  
    
         

           

    
        

if __name__=="__main__":
    root=Tk()
    obj=Class_Record(root)
    root.mainloop()	
