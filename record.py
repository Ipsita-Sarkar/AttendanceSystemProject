from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Record:
    def __init__(self, root):
        self.root=root
        self.root.geometry ("1330x700+0+0")
        self.root.title("Attendance Management System")
        self.var_percentage=StringVar()
        self.var_class_id=StringVar()

        img=Image.open(r"ProjectImages\header.jpeg")
        img=img.resize((1350, 100), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0,width=1350,height=100)

        bg=Label(self.root,bg="white")
        bg.place(x=0, y=100,width=1350,height=710)


        title_lbl=Label(bg, text="SHOW RECORDS", font=("Montserrat",25,"bold","underline"),bg="white",fg="#010280") 
        title_lbl.place(x=0, y=10,width=1350,height=50)
        main_frame=Frame (bg, bd=2, bg="white")
        main_frame.place(x=0, y=55,width=1480,height=600)

        class_frame=LabelFrame (main_frame, bd=2, bg="white", relief=RIDGE,font=("times new roman", 13, "bold"))
        class_frame.place(x=15, y=50,width=420,height=400)

        grid_frame=Frame(class_frame, bd=2, bg="white" )
        grid_frame.place(x=0, y=5,width =400, height=100)

        class_id_label=Label(grid_frame, text="Enter Class ID:", font=("times new roman", 13, "bold"), bg="white")
        class_id_label.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        class_id_entry=ttk.Entry(grid_frame,textvariable=self.var_class_id,width=20, font=("times new roman",13, "bold"))
        class_id_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        percentage_label=Label(grid_frame, text="Enter percentage:", font=("times new roman", 13, "bold"), bg="white")
        percentage_label.grid(row=1, column=1, padx=10, pady=30, sticky=W)
        percentage_entry=ttk.Entry(grid_frame,textvariable=self.var_percentage,width=20, font=("times new roman",13, "bold"))
        percentage_entry.grid(row=1, column=2, padx=10, pady=30, sticky=W)

        grid_frame=Frame(class_frame, bd=2, bg="white" )
        grid_frame.place(x=20, y=140,width =350, height=250)

        show_all=Button(grid_frame, text="Show ALL Student Records",width=30,command=self.fetch_data, font=("arial",13,"bold"), bg="#010280", fg= "white")
        show_all.grid (row=1, column=0, pady=15)
        show_below=Button(grid_frame, text="Show Students with Low Percentage",width=30,command=self.fetch_below_data, font=("arial",13,"bold"), bg="#010280", fg= "white")
        show_below.grid (row=2, column=0, pady=15)
        show_above=Button(grid_frame, text="Show Students with Proper Percentage",width=30,command=self.fetch_above_data, font=("arial",13,"bold"), bg="#010280", fg= "white")
        show_above.grid (row=3, column=0, pady=15)

        table_frame=Frame (main_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=500, y=50,width=750,height=400)

        scroll_x=ttk.Scrollbar (table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar (table_frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame, column=("name","student_id","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack (side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("name", text="Name")
        self.student_table.heading("student_id", text="Student_id")
        self.student_table.heading("attendance", text="Attendance")

        self.student_table.column("name",width=100)
        self.student_table.column("student_id",width=100)
        self.student_table.column("attendance",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
    def truncate_file(self):
        f=open("report.csv","w")
        f.truncate()
        f.close()
    def store_data (self,n,i,p,d):
            with open("report.csv","a", newline="\n") as f:

                    f.writelines (f"\n{n}, {i},{p},{d}")

    def fetch_data(self):
            self.truncate_file()
            conn=mysql.connector.connect(host="",username="", password="",database="student_schema")
            my_cursor=conn.cursor()
            my_cursor.execute("select Student_id,Attendance from record_table where Class_id="+str(self.var_class_id.get()))
            data=my_cursor.fetchall()
            my_cursor.execute("select Total_classes from class_table where Class_id="+str(self.var_class_id.get()))
            total=my_cursor.fetchone()[0]
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    my_cursor.execute("select Name from student_table where Student_id="+str(i[0]))
                    j=my_cursor.fetchone()
                    p=(int(i[1])/int(total))*100
                    k=j+i
                    self.student_table.insert("",END,values=k)
                    self.store_data(j[0],i[0],str(p),i[1])
            conn.commit()
            conn.close()
    def fetch_below_data(self):
            self.truncate_file()
            conn=mysql.connector.connect(host="",username="", password="",database="student_schema")
            my_cursor=conn.cursor()
            
            my_cursor.execute("select Student_id,Attendance from record_table where Class_id="+str(self.var_class_id.get()))
            data=my_cursor.fetchall()
            my_cursor.execute("select Total_classes from class_table where Class_id="+str(self.var_class_id.get()))
            total=my_cursor.fetchone()[0]
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    my_cursor.execute("select Name from student_table where Student_id="+str(i[0]))
                    j=my_cursor.fetchone()
                    p=(int(i[1])/int(total))*100
                    k=j+i
                    if p<int(self.var_percentage.get()):
                        self.student_table.insert("",END,values=k)
                        self.store_data(j[0],i[0],str(p),i[1])
            conn.commit()
            conn.close()
        
    def fetch_above_data(self):
            self.truncate_file()
            conn=mysql.connector.connect(host="",username="", password="",database="student_schema")
            my_cursor=conn.cursor()
            
            my_cursor.execute("select Student_id,Attendance from record_table where Class_id="+str(self.var_class_id.get()))
            data=my_cursor.fetchall()
            my_cursor.execute("select Total_classes from class_table where Class_id="+str(self.var_class_id.get()))
            total=my_cursor.fetchone()[0]
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    my_cursor.execute("select Name from student_table where Student_id="+str(i[0]))
                    j=my_cursor.fetchone()
                    p=(int(i[1])/int(total))*100
                    k=j+i
                    if p>=int(self.var_percentage.get()):
                        self.student_table.insert("",END,values=k)
                        self.store_data(j[0],i[0],str(p),i[1])
            conn.commit()
            conn.close()

    


if __name__=="__main__":
    root=Tk()
    obj=Record(root)
    root.mainloop()