from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Mahendra Paudel")
        self.root.geometry('1400x700+0+0')
        title=Label(self.root,text="Student Management System",font=("times new roman",40,"bold"),bg='firebrick',fg="gold",bd=5,relief=GROOVE)
        title.pack(side=TOP,fill=X)
        self.root.config(bg='black')


        #=============================================Frame=======================
        #================DataEnteryFrame=======================
        DataEntryFrame=Frame(self.root,bg='red',bd=5,relief=RIDGE)
        DataEntryFrame.place(x=5,y=80,width=450,height=610)


        lba=Label(DataEntryFrame,text='----Manage Students----',font=('roman',25,'bold'),bg='red',fg='white')
        lba.grid(row=0,column=0,columnspan=2,padx=5,pady=20)


        rolllbl=Label(DataEntryFrame,text='Roll No :',font=('roman',20,'bold'),bg='red',fg='white')
        rolllbl.grid(row=1,column=0,padx=20,pady=14,sticky='w')

        namelbl = Label(DataEntryFrame, text='Name :', font=('roman', 20, 'bold'), bg='red', fg='white')
        namelbl.grid(row=2, column=0, padx=20, pady=14, sticky='w')

        emaillbl = Label(DataEntryFrame, text='Email :', font=('roman', 20, 'bold'), bg='red', fg='white')
        emaillbl.grid(row=3, column=0, padx=20, pady=14, sticky='w')

        genderlbl = Label(DataEntryFrame, text='Gender :', font=('roman', 20, 'bold'), bg='red', fg='white')
        genderlbl.grid(row=4, column=0, padx=20, pady=14, sticky='w')

        contactlbl = Label(DataEntryFrame, text='Contact :', font=('roman', 20, 'bold'), bg='red', fg='white')
        contactlbl.grid(row=5, column=0, padx=20, pady=14, sticky='w')

        doblbl = Label(DataEntryFrame, text='D.O.B :', font=('roman', 20, 'bold'), bg='red', fg='white')
        doblbl.grid(row=6, column=0, padx=20, pady=14, sticky='w')

        addresslbl = Label(DataEntryFrame, text='Address :', font=('roman', 20, 'bold'), bg='red', fg='white')
        addresslbl.grid(row=7, column=0, padx=20, pady=14, sticky='w')


        #================all variable===============================
        self.roll_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()
        self.gender_var=StringVar()
        self.dob_var=StringVar()





        #==========================entrybox==================================

        rollentry=Entry(DataEntryFrame,font=('times',15,'bold'),width=15,borderwidth=4,relief=RIDGE,bd=5,textvariable=self.roll_var)
        rollentry.grid(row=1,column=1,sticky='w')

        nameentry = Entry(DataEntryFrame, font=('times', 15, 'bold'), width=15, borderwidth=4, relief=RIDGE, bd=5,
                          textvariable=self.name_var)
        nameentry.grid(row=2, column=1,sticky='w')

        emailentry = Entry(DataEntryFrame, font=('times', 15, 'bold'), width=15, borderwidth=4, relief=RIDGE, bd=5,
                          textvariable=self.email_var)
        emailentry.grid(row=3, column=1,sticky='w')

        genderentry = ttk.Combobox(DataEntryFrame, font=('times', 15, 'bold'), width=14,
                          textvariable=self.gender_var,state='readonly')
        genderentry['values']=('Male','Female','Other')
        genderentry.grid(row=4, column=1,sticky='w')
        genderentry.current('0')

        contactentry = Entry(DataEntryFrame, font=('times', 15, 'bold'), width=15, borderwidth=4, relief=RIDGE, bd=5,
                          textvariable=self.contact_var)
        contactentry.grid(row=5, column=1,sticky='w')

        dobentry = Entry(DataEntryFrame, font=('times', 15, 'bold'), width=15, borderwidth=4, relief=RIDGE, bd=5,
                          textvariable=self.dob_var)
        dobentry.grid(row=6, column=1,sticky='w')

        self.addressentry = Text(DataEntryFrame, font=('times', 15, 'bold'), width=16,height=2
                          )
        self.addressentry.grid(row=7, column=1,sticky='w')


        #=================Button Frame==================================================
        self.search_by = StringVar()
        self.search_text = StringVar()

        btnframe=Frame(DataEntryFrame,bd=4,relief=RIDGE,bg='red')
        btnframe.place(x=10,y=540,width=415,height=50)

        dltbtn=Button(btnframe,text="Delete",width=10,command=self.Delete)
        dltbtn.grid(row=0,column=1,padx=10,pady=7)

        updatebtn = Button(btnframe, text="Update", width=10,command=self.Update)
        updatebtn.grid(row=0, column=2, padx=10, pady=7)

        clearbtn = Button(btnframe, text="Clear", width=10,command=self.clear)
        clearbtn.grid(row=0, column=3, padx=10, pady=7)

        addbtn = Button(btnframe, text="Add", width=10,command=self.Add_student)
        addbtn.grid(row=0, column=0, padx=10, pady=7)

        #==============DataShowFrame===========================

        DataShowFrame=Frame(self.root,bd=5,relief=RIDGE,bg='pink3')
        DataShowFrame.place(x=460,y=80,width=890,height=610)



        searchlbl=Label(DataShowFrame,text='Search By',font=('roman',20,'bold'),bg='pink3',fg='white')
        searchlbl.grid(row=0,column=0,padx=20,pady=10,sticky='w')


        search_combox=ttk.Combobox(DataShowFrame,width=10,state='readonly',font=('times',15,'bold '),textvariable=self.search_by)
        search_combox['values']=('Roll No','Name',"Contact")
        search_combox.grid(row=0,column=1,padx=20,pady=10,sticky='w')
        search_combox.current(0)


        entry_box=Entry(DataShowFrame,width=15,bd=4,relief=GROOVE,font=('times',15,'bold'),textvariable=self.search_text)
        entry_box.grid(row=0,column=2,padx=20,pady=10,sticky='w')

        searchbtn = Button(DataShowFrame, text="Search", width=13,bd=4,relief=RIDGE,command=self.Search)
        searchbtn.grid(row=0, column=3, padx=20, pady=10)

        showallbtn = Button(DataShowFrame, text="Show All", width=13,bd=4,relief=RIDGE,command=self.fetch)
        showallbtn.grid(row=0, column=4, padx=20, pady=10)



        #======================================================Table Frame=================


        Table_Frame=Frame(DataShowFrame,bd=4,relief=RIDGE,bg='pink3')
        Table_Frame.place(x=5,y=70,width=863,height=523)
        scroll_X=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_Frame,columns=("roll",'name','email','gender','contact','dob','address'),xscrollcommand=scroll_X.set,yscrollcommand=scroll_y.set)
        scroll_X.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_X.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('roll',text='Roll No:')
        self.student_table.heading('name',text='Name:')
        self.student_table.heading('email',text='Email:')
        self.student_table.heading('gender',text='Gender:')
        self.student_table.heading('contact',text='Contact:')
        self.student_table.heading('dob',text='D.O.B:')
        self.student_table.heading('address',text='Address:')
        self.student_table['show']='headings'
        self.student_table.column('roll',width=80)
        self.student_table.column('name',width=160)
        self.student_table.column('email',width=160)
        self.student_table.column('contact',width=110)
        self.student_table.column('dob',width=110)
        self.student_table.column('address',width=110)
        self.student_table.column('gender',width=80)







        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch()


    def fetch(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="studentmanagementsystem")
        cur = con.cursor()
        cur.execute('select * from student')
        rr=cur.fetchall()
        if len(rr)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rr:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()


    def get_cursor(self,ev):
        cc=self.student_table.focus()
        content=self.student_table.item(cc)
        row=content['values']
        if len(row)!=0:
            self.roll_var.set(row[0])
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.contact_var.set(row[4])
            self.gender_var.set(row[3])
            self.dob_var.set(row[5])
            self.addressentry.delete('1.0',END)
            self.addressentry.insert(END,row[6])







    def clear(self):
        self.roll_var.set(" ")
        self.name_var.set(" ")
        self.email_var.set(" ")
        self.contact_var.set(" ")
        self.gender_var.set(" ")
        self.dob_var.set(" ")
        self.addressentry.delete('1.0', END)

    def Delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="studentmanagementsystem")
        cur = con.cursor()
        strr='delete from student where roll=%s'
        cur.execute(strr,self.roll_var.get())
        con.commit()
        con.close()
        self.fetch()
        self.clear()
        messagebox.showinfo("Notification","Data is Sucessfully Deleted")
    def Update(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="studentmanagementsystem")
        cur = con.cursor()
        strr='update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll=%s '
        cur.execute(strr,(self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.addressentry.get('1.0',END),self.roll_var.get()))
        con.commit()
        self.fetch()
        self.clear()
        messagebox.showinfo("Notification","Data is Sucessfully Updated")
        con.close()

    def Add_student(self):
        roll = self.roll_var.get()
        name = self.name_var.get()
        email = self.email_var.get()
        contact = self.contact_var.get()
        gender = self.gender_var.get()
        dob = self.dob_var.get()
        address = self.addressentry.get("1.0", END)
        if roll == '' or name == '':
            messagebox.showerror('Error', "All Field Are Required")

        else:
            con = pymysql.connect(host="localhost",user="root",password="",database="studentmanagementsystem")
            cur=con.cursor()
            strr="insert into  student value(%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(strr,(roll,name,email,gender,contact,dob,address))
            con.commit()
            self.fetch()
            self.clear()
            messagebox.showinfo('Notification','Data is inserted Sucessfully......')
            con.close()
    def Search(self):
        if (self.search_by.get()=='Roll No'):
            con = pymysql.connect(host="localhost", user="root", password="", database="studentmanagementsystem")
            cur = con.cursor()
            strr='select * from student where roll=%s'
            cur.execute(strr,self.search_text.get())
            rr=cur.fetchall()
            if len(rr) !=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rr:
                    self.student_table.insert("",END,values=row)
                con.commit()
            con.close()


        elif (self.search_by.get()=='Name'):
            con=pymysql.connect(host='localhost',user='root',password='',database='studentmanagementsystem')
            cur=con.cursor()
            strr='select * from student where name=%s'
            cur.execute(strr,self.search_text.get())
            rr=cur.fetchall()
            if len(rr)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rr:
                    self.student_table.insert('',END,values=row)
                con.commit()
            con.close()


        elif(self.search_by.get()=='Contact'):
            con=pymysql.connect(host='localhost',user='root',password='',database='studentmanagementsystem')
            cur=con.cursor()
            strr='select * from student where contact=%s'
            cur.execute(strr,self.search_text.get())
            rr=cur.fetchall()
            if (len(rr)!=0):
                self.student_table.delete(*self.student_table.get_children())
                for row in rr:
                    self.student_table.insert("",END,values=row)
                con.commit()
            con.close()










root=Tk()
obj=Student(root)
root.mainloop()