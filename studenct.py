from tkinter import *
from tkinter import ttk,messagebox


import pymysql

class  Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1500x1000+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("time new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
        #======All Variable========
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_text=StringVar()


        #========= Manage Frame====================
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=440,height=580)
        m_title=Label(Manage_Frame,text="Manage Students", font=("time new roman",30,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)
        lbl_roll=Label(Manage_Frame,text="Roll No:",font=("time new roman",18,"bold"),bg="crimson",fg="white")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        entry_roll=Entry(Manage_Frame,textvariable=self.roll_no_var ,width=15,font=("time new roman",13,"bold"),bd=5,relief=GROOVE)
        entry_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text=" Name:", font=("time new roman", 18, "bold"), bg="crimson", fg="white")
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        entry_name = Entry(Manage_Frame, width=15, textvariable=self.name_var,font=("time new roman", 13, "bold"), bd=5, relief=GROOVE)
        entry_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email:", font=("time new roman", 18, "bold"), bg="crimson", fg="white")
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        entry_Email = Entry(Manage_Frame, width=15, textvariable=self.email_var,font=("time new roman", 13, "bold"), bd=5, relief=GROOVE)
        entry_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender:", font=("time new roman", 18, "bold"), bg="crimson", fg="white")
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("time new roman",9,"bold"),state="readonly",width=18,height=9)
        combo_gender["value"]=("male","female","other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        combo_gender.current("0")



        lbl_contact = Label(Manage_Frame, text="Contact:", font=("time new roman", 18, "bold"), bg="crimson", fg="white")
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        entry_contact = Entry(Manage_Frame, width=15, textvariable=self.contact_var,font=("time new roman", 13, "bold"), bd=5, relief=GROOVE)
        entry_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob= Label(Manage_Frame, text="D.O.B", font=("time new roman", 18, "bold"), bg="crimson", fg="white")
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        entry_dob = Entry(Manage_Frame, width=15,textvariable=self.dob_var, font=("time new roman", 13, "bold"), bd=5, relief=GROOVE)
        entry_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address:", font=("time new roman", 18, "bold"), bg="crimson", fg="white")
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.entry_address = Text(Manage_Frame,width=20,height=4,font=("",10))
        self.entry_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")
        #======Button Frame=======
        btn_frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_frame.place(x=10,y=510,width=420)

        Addbtn=Button(btn_frame,command=self.add_student,text="Add",width=10)
        Addbtn.grid(row=0,column=0,padx=10,pady=10)

        dltbtn = Button(btn_frame,command=self.delete_data, text="Delete", width=10)
        dltbtn.grid(row=0, column=1, padx=10, pady=10)

        updatebtn = Button(btn_frame,command=self.update_data, text="Update", width=10)
        updatebtn.grid(row=0, column=2, padx=10, pady=10)

        clrbtn = Button(btn_frame,command=self.clear, text="Clear", width=10)
        clrbtn.grid(row=0, column=3, padx=10, pady=10)
        # ========= Details  Frame====================


        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=825, height=580)

        searchlbl=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=('time new roman',18,"bold"))
        searchlbl.grid(row=0,column=0,padx=10,pady=10,sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by, font=("time new roman", 10, "bold"), state="readonly", width=10,height=9)
        combo_search["value"] = ("Roll_No", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")
        combo_search.current(0)

        entry_search = Entry(Detail_Frame, width=15,textvariable=self.search_text, font=("time new roman", 12, "bold"), bd=5, relief=GROOVE)
        entry_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame,command=self.search_data, text="Search", width=13)
        searchbtn.grid(row=0, column=3, padx=10, pady=10)

        showbtn = Button(Detail_Frame,command=self.fetch_data, text="Show All", width=13)
        showbtn.grid(row=0, column=4, padx=10, pady=10)

        #=====Table Frame===========

        Table_frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_frame.place(x=10,y=70,width=760,height=500)
        scroll_X=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_X.set,yscrollcommand=scroll_y.set)
        scroll_X.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_X.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll No:")
        self.student_table.heading("name",text="Name:")
        self.student_table.heading("email",text="Email:")
        self.student_table.heading("gender",text="Gender:")
        self.student_table.heading("contact",text="Contact:")
        self.student_table.heading("dob",text="D.O.B:")

        self.student_table.heading("address",text="Address:")
        self.student_table['show']='headings'
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("address",width=150)







        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def add_student(self):
        if self.roll_no_var.get()=='' or self.name_var.get()=='':
            messagebox.showerror('Erorr',"All field are Requied!!!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students value(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),
                                                                       self.name_var.get(),
                                                                       self.email_var.get(),
                                                                       self.gender_var.get(),

                                                                       self.contact_var.get(),
                                                                        self.dob_var.get(),

                                                                        self.entry_address.get("1.0",END)
                                                                        ))
            con.commit()
            self.fetch_data()

            self.clear()
            con.close()
            messagebox.showinfo("Notification",'Record  has been inserted')


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.entry_address.delete("1.0",END)


    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents["values"]
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.entry_address.delete("1.0",END)
        self.entry_address.insert( END,row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,dob=%s,contact=%s,address=%s where roll_no=%s", (
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),

                                                                         self.entry_address.get("1.0", END),
                                                                         self.roll_no_var.get()

                                                                         ))
        con.commit()

        self.fetch_data()
        self.clear()
        con.close()
    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete  from students where roll_no=%s",self.roll_no_var.get())
        con.commit()
        con.close()

        self.fetch_data()

        self.clear()



    def search_data(self):
        if (self.search_by.get()=='Roll_No'):
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("select * from students where roll_no=%s", self.search_text.get())
            rows = cur.fetchall()
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)
                con.commit()
            con.close()


        elif (self.search_by.get() == 'Name'):
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("select * from students where name=%s", self.search_text.get())
            rows = cur.fetchall()
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)
                con.commit()
            con.close()

        elif (self.search_by.get() == 'Contact'):
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("select * from students where contact=%s", self.search_text.get())
            rows = cur.fetchall()
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)
                con.commit()
            con.close()

        #if (id != ''):
         #   strr = 'select *from data where id=%s'
          #  mycursor.execute(strr, id)
           # datas = mycursor.fetchall()
            #studenttable.delete(*studenttable.get_children())
            #for i in datas:
             #   vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
              #  studenttable.insert('', END, values=vv)


root=Tk()
obj=Student(root)
root.mainloop()