# AttendanceSystemProject
An attendance system based on face recognition implemented using Python.

Steps to setup the database:
  1. Open MySQL Workbench
  2. Connect to a server
  3. Create a database schema "student_schema"
  4. Create 3 tables:
                     1. class_table: Add the following attributes: class_id, Total_classes. Make Class-id primary key.
                     2. record_table: Add the following attributes: Student_id, Class_id, Attendance. Make Student_id and Class-id primary key.
                     3. student_table: dd the following attributes:  Dep, Course, Year, Semester, Student_id, Name, Section, Roll, Gender,DOB, Phone,  Email, Address, PhotoSample.                         Make Student_id primary key.
                    
  5. Setup all the tables with necessary data.
  
Steps to setup the project:
  1. Add necessary server credentials wherever needed.
   
Steps to run the system:
  1. Run main.py file.
  2. The Home Page is visible.
  3. To train the dataset: Click on Train Data button: A file named classifier.xml will be created.
  4. To run face recognition and mark attendance:
  
          1. Click on Check In button.
          2. Enter Class ID of the class.
          3. Webcam popups
          4. If the face is recognized attendance will be marked in the databased as well as stored in xml file.
           
  5. To create attendance reports: Click on Create Reports button.
  6. To see daily attendance: Click on View Attendance button.
  7. To view and modify student data: Click on Student Details button.
