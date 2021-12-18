from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry ("1330x700+0+0")
        self.root.title("Face Recogniton System")
        # ‒‒‒‒‒‒‒‒‒‒==variables=====

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_sec=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_class_id=StringVar()
        self.var_atten=StringVar()

        #first image
        img=Image.open(r"ProjectImages\header.jpeg")
        img=img.resize((1350, 100), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0,width=1350,height=100)

        

        #bg

        bg=Label(self.root,bg="white")
        bg.place(x=0, y=100,width=1350,height=590)

        title_lbl=Label(bg, text="STUDENT MANAGEMENT SYSTEM ", font=("Montserrat",25,"bold","underline"),bg="white",fg="#010280") 
        title_lbl.place(x=0, y=10,width=1350,height=45)
        main_frame=Frame (bg, bd=2, bg="white")
        main_frame.place(x=0, y=60,width=1480,height=520)



        # left label frame

        Left_frame=LabelFrame (main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details" ,font=(" Times new roman",12,"bold"))
        Left_frame.place(x=10, y=0,width=700,height=500)



        #current course info
        current_course_frame=LabelFrame (Left_frame, bd=2, bg="white", relief=RIDGE ,font=(" Times new roman",12,"bold"))
        current_course_frame.place(x=5, y=5, width=680,height=150)

        #department
        dep_label=Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white") 
        dep_label.grid(row=0, column=0, padx=10,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman", 13, "bold"), state="readonly", width=20) 
        dep_combo["values"]=("Select Department", "CSE", "ECE", "EE", "EIE", "ME", "CE", "CHE", "PE", "BE") 
        dep_combo.current (0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #Course
        course_label=Label(current_course_frame, text="Course", font=("times new roman",13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo=ttk.Combobox (current_course_frame,textvariable=self.var_course, font=("times new roman",13, "bold"), state="readonly",width=20)
        course_combo["values"]=("Select Course","Btech","Mtech")
        course_combo.current (0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #Year

        year_label=Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"),bg="white" )
        year_label.grid(row=1,column=0, padx=10, sticky=W)

        year_combo=ttk.Combobox (current_course_frame,textvariable=self.var_year, font=("times new roman",13, "bold"), state="readonly",width=20)
        year_combo["values"]=("Select Year", "2020-21", "2021-22", "2022-23","2023-24")
        year_combo.current (0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #Semester

        semester_label=Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"),bg= "white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo=ttk.Combobox (current_course_frame,textvariable=self.var_semester, font=("times new roman", 13, "bold"), state="readonly",width=20)
        semester_combo["values"]=("Select Semester", "1", "2", "3","4","5","6","7","8")
        semester_combo.current (0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #Class Student information

        class_Student_frame=LabelFrame (Left_frame, bd=2, bg="white", relief=RIDGE,font=("times new roman", 13, "bold"))
        class_Student_frame.place(x=5, y=160,width=680,height=300)

        #student id

        studentId_label=Label(class_Student_frame, text="Student ID: ", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id, width=20, font=("times new roman", 13, "bold")) 
        studentID_entry.grid(row=0,column=1, padx=10, pady=5, sticky=W)
        

        #student name
        studentName_label=Label(class_Student_frame, text="Student Name:", font=("times new roman", 13, "bold"),bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5,sticky=W)
        studentName_entry=ttk. Entry(class_Student_frame,textvariable=self.var_std_name,width=20, font=("times new roman",13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #Class section
        class_sec_label=Label(class_Student_frame, text="Section:", font=("times new roman",13, "bold"),bg="white")
        class_sec_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        sec_combo=ttk.Combobox (class_Student_frame,textvariable=self.var_sec, font=("times new roman",13, "bold"), state="readonly",width=18)
        sec_combo["values"]=("A","B","C","D")
        sec_combo.current (0)
        sec_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        #Roll No:

        roll_no_label=Label(class_Student_frame, text="Roll No: ", font=("times new roman",13, "bold"),bg="white")
        roll_no_label.grid(row=1,column=2, padx=10, pady=5, sticky=W)
        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold")) 
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        #Gender

        gender_label=Label(class_Student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
       

        gender_combo=ttk.Combobox (class_Student_frame,textvariable=self.var_gender, font=("times new roman",13, "bold"), state="readonly",width=18)
        gender_combo["values"]=("Female", "Male", "Other")
        gender_combo.current (0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB:

        dob_label=Label(class_Student_frame, text="DOB: ", font=("times new roman",13, "bold"),bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry=ttk. Entry(class_Student_frame,textvariable=self.var_dob,width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #phone

        phone_label=Label(class_Student_frame, text="Phone No: ", font=("times new roman",13, "bold"),bg="white")
        phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone, width=20, font=("times new roman",13, "bold"))
        phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        #Email

        email_label=Label(class_Student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white" )
        email_label.grid (row=3, column=2, padx=10, pady=5, sticky=W)
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email, width=20, font=("times new roman",13, "bold"))
        email_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        #Address

        address_label=Label(class_Student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20, font=("times new roman",13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

  
        # radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk. Radiobutton (class_Student_frame,variable=self.var_radio1, text="Take Photo", value="Yes")
        radionbtn1.grid(row=6, column=0)
    
        radionbtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="No Photo", value="No")
        radionbtn2.grid(row=6, column=1)

        #bbuttons frame

        btn_frame=Frame(class_Student_frame, bd=2,relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200,width=675, height=75)

        save_btn=Button(btn_frame, text="Save",width=16,command=self.add_data, font=("arial",13,"bold"), bg="#010280", fg= "white")
        save_btn.grid (row=0, column=0)

        update_btn=Button (btn_frame, text="Update",width=16,command=self.update_data, font=("arial",13,"bold"), bg="#010280", fg= "white")
        update_btn.grid(row=0, column=1)

        delete_btn=Button(btn_frame, text="Delete",width=16,command=self.delete_data, font=("arial",13, "bold"), bg="#010280", fg= "white")
        delete_btn.grid (row=0, column=2)

        reset_btn=Button (btn_frame, text="Reset",width=15,command=self.reset_data, font=("arial",13, "bold"), bg="#010280", fg= "white")
        reset_btn.grid(row=0, column=3)

        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=170, y=235,width=344,height=35)

        take_photo_btn=Button (btn_frame1,text="Take Photo",command=self.generate_dataset,width=33, font=("arial",13, "bold"), bg="#010280", fg= "white")
        take_photo_btn.grid(row=0,column=0)



        #right label frame

        right_frame=LabelFrame (main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=(" Times new roman",12,"bold"))
        right_frame.place(x=720, y=0,width=610,height=500)

        #Table frame

        table_frame=Frame (right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5,width=600,height=470)

        scroll_x=ttk.Scrollbar (table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar (table_frame, orient=VERTICAL)


        self.student_table=ttk.Treeview(table_frame, column=("dep", "course", "year","sem","id","name", "roll", "sec", "gender", "dob", "phone",  "email","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack (side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("sec", text="Section")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading ("dob", text="DOB")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading ("email", text="Email")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("sec",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
     
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

    #Function declaration

    def add_data(self):
            a=0
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error", "All Fields are required", parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="",username="", password="",database="student_schema")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student_table values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    self.var_std_id.get(),
                                                                                                                    self.var_std_name.get(),
                                                                                                                    self.var_sec.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_email.get(), 
                                                                                                                    
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_radio1.get()
                                                                                                                   ))
                    messagebox.showinfo("Success", "Student details successfully added",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()

                except Exception as es:
                    messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)
    def fetch_data(self):
            conn=mysql.connector.connect(host="",username="", password="",database="student_schema")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student_table")
            data=my_cursor.fetchall()
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()
    def get_cursor (self,event=""):

        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)

        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_sec.set(data[6]), 
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_email.set (data[11]),
        self.var_address.set(data[12]),
        self.var_radio1.set (data[13])
         

    def update_data(self):
        if self.var_dep.get()=="Select Department or self.var_std_name.get()=="" or self.var_std_id=.get()=":
                messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
                try:
                    Update=messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                    if Update>0:
                        conn=mysql.connector.connect(host="",username="", password="",database="student_schema")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update student_table set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Section=%s, Roll=%s,Gender=%s,DOB=%s, Phone=%s,  Email=%s,Address=%s, PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                                            self.var_sec.get(),
                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_phone.get(), 
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_radio1.get(), 
                                                                                                                                                                                                            self.var_std_id.get()
                                                                                                                                                                                                        ))
                    else:
                            if not Update:
                                return
                    messagebox.showinfo("Success", "Student details successfully update completed",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                except Exception as es:
                            messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root)
    def delete_data(self):
        if self.var_std_id.get()=="":
                messagebox.showerror("Error", "Student id isrequired",parent=self.root)
        else:
                try:
                    delete=messagebox.askyesno("Student Delete Page", "Do you want to delete this student",parent=self.root)
                    if delete>0:
                        conn=mysql.connector.connect(host="",username="", password="",database="student_schema")
                        my_cursor=conn.cursor()
                        sql="delete from student_table where Student_id=%s"
                        val=(self.var_std_id.get(),)
                        my_cursor.execute(sql, val)
                    else:
                        if not delete:
                            return
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", "Successfully deleted student detials", parent=self.root)
                except Exception as es: 
                    messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root)
    def reset_data(self):
            self.var_dep.set("Select Department")
            self.var_course.set("Select Course")
            self.var_year.set("Select Year")
            self.var_semester.set("Select Semester")
            self.var_std_id.set("")
            self.var_std_name.set("")
            self.var_sec.set("Select Section")
            self.var_roll.set("")
            self.var_gender.set("Male")
            self.var_dob.set("")
            self.var_email.set("")
            self.var_phone.set("")
            self.var_address.set("")
            self.var_class_id.set("")
            self.var_radio1.set("")

    def generate_dataset(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error", "All Fields are required",parent=self.root)

            else:
                try:   
                    conn=mysql.connector.connect(host="",username="", password="",database="student_schema")
                    
                    id=self.var_std_id.get()

                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped (img):
                        gray=cv2.cvtColor (img, cv2.COLOR_BGR2GRAY) 
                        faces=face_classifier.detectMultiScale(gray, 1.3,5)
                        #scaling factor=1.3
                        #Minimum Neighbor=5

                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped

                    cap=cv2.VideoCapture(0)
                    img_id=0

                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame), (450,450))
                            face=cv2.cvtColor (face, cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+". "+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1)==13 or int(img_id)==1:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data sets completed!!!!")

                except Exception as es: 
                    messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root)
        

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()	
