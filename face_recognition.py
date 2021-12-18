from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.var_class_id=StringVar()

        img=Image.open(r"ProjectImages\header.jpeg")
        img=img.resize((1350, 100), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0,width=1350,height=100)

        title_lbl=Label(self.root, text="FACE RECOGNITION",font=("Monserrat",25,"bold","underline"),bg="white",fg="#010280")
        title_lbl.place(x=0,y=100,width=1350,height=145)

        main_lbl=Label(self.root,bg="white")
        main_lbl.place(x=0,y=190,width=1350,height=600)
        

        main_frame=LabelFrame (main_lbl, bd=2, bg="white", relief=RIDGE,font=("times new roman", 13, "bold"))
        main_frame.place(x=400, y=100,width=500,height=175)

        class_id_label=Label(main_frame, text="Enter Class ID:", font=("times new roman", 13, "bold"), bg="white")
        class_id_label.grid(row=1, column=0,padx=60,pady=30, sticky=W)
       
        class_id_entry=ttk.Entry(main_frame,textvariable=self.var_class_id,width=20, font=("times new roman",13, "bold"))
        class_id_entry.grid(row=1, column=1,padx=0,pady=30, sticky=W)
     

        b1_2=Button(main_frame,text="Face Recognition", cursor="hand2",command=self.face_recog,font=("arial",12,"bold"),bg="#010280",fg="white")
        b1_2.place(x=160,y=100,width=160,height=30)
    
    def store_attendance (self,i,n):
            with open("daily_record.csv","r+", newline="\n") as f:
                myDataList=f.readlines()
                name_list=[]
                for line in myDataList:
                    entry=line.split((","))
                    name_list.append(entry [0])
                if((i not in name_list) and (n not in name_list)):
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines (f"{i},{n},{dtString},{d1},Present")
    
    def mark_attendance (self,i,n):
        conn=mysql.connector.connect(host="",username="", password="",database="student_schema")
        my_cursor=conn.cursor()
        my_cursor.execute("select Class_id,Attendance from record_table where Student_id="+str(i))
        data=my_cursor.fetchall()
        for row in data:
            if(row[0]==self.var_class_id.get()):
                att=str(int(row[1])+1)
                my_cursor.execute("update record_table set Attendance=%s where Student_id=%s and Class_id=%s",(att,str(i),str(self.var_class_id.get())))
        
        
        conn.commit()
    

    

    def face_recog(self):

            def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
                gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
                coord=[]
                for (x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0), 3)
                    id, predict=clf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))
                    conn=mysql.connector.connect(host="",username="", password="",database="student_schema")
                    my_cursor=conn.cursor()

                    my_cursor.execute("select Name from student_table where Student_id="+str(id))
                    n=my_cursor.fetchone()
                    n="+".join(n)

                    my_cursor.execute("select Student_id from student_table where Student_id="+str(id))
                    i=my_cursor.fetchone()
                    i=i[0]

                    if confidence>70:
                       
                       cv2.putText(img, f"ID: {i}", (x,y-75), cv2. FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)                       
                       cv2.putText(img, f"Name: {n}", (x,y-55), cv2. FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                     
                       if cv2.waitKey(1)==13:
                        self.store_attendance(i,n)
                        self.mark_attendance(i,n)
                
                        return 1

                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 3)
                        cv2.putText(img, "Face Not Recognised", (x,y-5), cv2. FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                        return 0

                    coord=[x,y,w,h]

                return coord
            def recognize(img, clf, faceCascade):
                f=draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face",clf)
                return f
            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")
            video_cap=cv2.VideoCapture(0)
            while True:
                ret,img=video_cap.read()
                f=recognize(img, clf, faceCascade)
                cv2.imshow("Welcome To Face Recognition", img)
                if f==1:
                     messagebox.showinfo("Attendance taken", "You are marked present",parent=self.root)
                     break;
                if cv2.waitKey(1)==13:
                    break
            video_cap.release()
            cv2.destroyAllWindows()


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()