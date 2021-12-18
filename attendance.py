from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogniton System")

         #Variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #first image
        img=Image.open(r"ProjectImages\header.jpeg")
        img=img.resize((1350, 100), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0,width=1350,height=100)

        #bg

        bg=Label(self.root,bg="white")
        bg.place(x=0, y=100,width=1350,height=690)

        title_lbl=Label(bg, text="ATTENDANCE MANAGEMENT SYSTEM ", font=("Montserrat",25,"bold","underline"),bg="white",fg="#010280") 
        title_lbl.place(x=0, y=10,width=1350,height=50)

        main_frame=Frame (bg, bd=2, bg="white")
        main_frame.place(x=0, y=70,width=1350,height=600)

        #left label frame

        Left_frame=LabelFrame (main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details" ,font=("Arial",12,"bold"))
        Left_frame.place(x=10, y=15,width=650,height=400)

        #Labels entry
        #attendance id
        attendanceId_label=Label(Left_frame, text="Student ID: ", font=("times new roman",13,"bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=20, pady=5, sticky=W)
        attendanceID_entry=ttk. Entry(Left_frame,width=22,textvariable=self.var_atten_id, font=("times new roman",13, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=20, pady=5, sticky=W)


        #name
        namelabel=Label(Left_frame, text="Name: ",bg="white", font=("times new roman",13, "bold"))
        namelabel.grid(row=1,column=0, padx=20)

        atten_name=ttk.Entry(Left_frame, width=22,textvariable=self.var_atten_name, font=("times new roman",13, "bold"))
        atten_name.grid(row=1,column=1, padx=20, pady=8)

        #time
        timelabel=Label(Left_frame, text="Time: ", bg="white", font=("times new roman",13, "bold"))
        timelabel.grid (row=2, column=0, padx=20)

        atten_time=ttk.Entry(Left_frame, width=22,textvariable=self.var_atten_time, font=("times new roman",13, "bold")) 
        atten_time.grid(row=2, column=1, padx=20, pady=8)

        #Date
        datelabel=Label(Left_frame, text="Date: ", bg="white", font=("times new roman",13, "bold"))
        datelabel.grid(row=3, column=0, padx=20)

        atten_date=ttk.Entry(Left_frame,width=22,textvariable=self.var_atten_date, font=("times new roman",13, "bold"))
        atten_date.grid(row=3, column=1, padx=20, pady=8)

        #attendance
        attendanceLabel=Label(Left_frame,text= "Attendance Status", bg="white", font=("times new roman",13, "bold")) 
        attendanceLabel.grid (row=4, column=0, padx=20)

        self.atten_status=ttk.Combobox(Left_frame,width=20,textvariable=self.var_atten_attendance, font=("times new roman",13, "bold"),state="readonly") 
        self.atten_status["values"]=("Status", "Present", "Absent") 
        self.atten_status.grid(row=4, column=1, padx=20, pady=8)
        self.atten_status.current (0)

        #buttons frame
        btn_frame=Frame(Left_frame, bd=2, relief=RIDGE, bg="white") 
        btn_frame.place(x=65, y=250,width=540,height=35)

        save_btn=Button(btn_frame, text="Import csv",command=self.importCsv,width=17, font=("arial",13, "bold"), bg="#010280",fg="white")
        save_btn.grid(row=0, column=0)

        export_btn=Button (btn_frame, text="Export csv",width=17,command=self.exportCsv, font=("arial", 13, "bold"), bg="#010280", fg="white")
        export_btn.grid(row=0,column=1)

        reset_btn=Button(btn_frame, text="Reset",width=17,command=self.reset_data, font=("arial",13, "bold"),bg="#010280", fg="white") 
        reset_btn.grid(row=0,column=2)

        #right label frame
        right_frame=LabelFrame (main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=(" Times new roman",12,"bold"))
        right_frame.place(x=670, y=15,width=660,height=400)

        table_frame=Frame (right_frame, bd=2, relief=RIDGE, bg="white") 
        table_frame.place(x=5, y=5,width=640,height=370)

        #scroll bar table
        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable=ttk. Treeview (table_frame, column=("id", "name", "time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack (side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview) 
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Student ID")
        self.AttendanceReportTable.heading("name", text="Name") 
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
            self.AttendanceReportTable.update(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)

    def exportCsv(self):
            try:
                if len(mydata)<1:
                    messagebox.showerror("No data","No Data Found", parent=self.root)
                    return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                    exp_write=csv.writer(myfile,delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)

    def get_cursor(self, event=""):
            cursor_row=self.AttendanceReportTable.focus()
            content=self.AttendanceReportTable.item(cursor_row)
            rows=content['values']
            self.var_atten_id.set(rows[0])
            self.var_atten_name.set(rows[1])
            self.var_atten_time.set(rows[2])
            self.var_atten_date.set(rows[3])
            self.var_atten_attendance.set(rows[4])

    def reset_data(self):
            self.var_atten_id.set("")
            self.var_atten_name.set("")
            self.var_atten_time.set("")
            self.var_atten_date.set("")
            self.var_atten_attendance.set("")

if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()