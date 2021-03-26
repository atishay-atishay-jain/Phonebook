from Tkinter import*
import sqlite3
from tkMessageBox import *
root=Tk()
root.geometry("500x400")
root.configure(bg='gray11')
con=sqlite3.Connection('PhoneBook_bb059')
cur=con.cursor()
#1st screen start#

Label(root,text="Project Title :PhoneBook",font="Arial 13 bold ",fg="spring green",bg='gray11').grid(row=0,column=0)
Label(root,text="Project of Python and Database ",font="Arial 13 bold ",fg="olivedrab1",bg='gray11').grid(row=1,column=2)
Label(root,text="DevelopedBy :Atishay Jain ",font="Arial 13 bold" ,fg="turquoise1",bg='gray11').grid(row=2,column=2)
Label(root,text="EnrollmentNo :181B059 ",font="Arial 13 bold ",fg="lawn green",bg='gray11').grid(row=3,column=2)
Label(root,text="--------------------------",font="Arial 13 bold",fg="gold",bg='gray11').grid(row=4,column=2)

def close(e=1):
    root.destroy()#1st screen done#
    root1=Tk()
    root1.configure(bg="gray100")
    root1.geometry("550x575")
    #b=PhotoImage(file='C:\\Users\\welcome\\Desktop\\pyth+dbms+final\\bookkk-fin.gif')
    #b=PhotoImage(file='phnbok.gif')
    #a=PhotoImage(file='C:\Users\welcome\Desktop\personal\sem 3\adv  prog lab\pyth+dbms+final\pyth+dbms.gif')
    #Label(root1,image=b).grid(row=0,column=2)
    Label(root1,text="Phone Book",font="Arial 15 underline bold ",fg="deeppink2",bg="gray100").grid(row=1,column=2)


    
    Label(root1,text="First Name ",font="Arial 10 bold",fg="green",bg="gray100").grid(row=3,column=1)
    Label(root1,text="Middle Name ",font="Arial 10 bold",fg="dodgerblue",bg="gray100").grid(row=4,column=1)
    Label(root1,text="Last Name ",font="Arial 10 bold",fg="darkorange1",bg="gray100").grid(row=5,column=1)
    Label(root1,text="Company Name ",font="Arial 10 bold",fg="orangered2",bg="gray100").grid(row=6,column=1)
    Label(root1,text="Adress ",font="Arial 10 bold",fg="darkorchid3",bg="gray100").grid(row=7,column=1)
    Label(root1,text="City ",font="Arial 10 bold",fg="slateblue2",bg="gray100").grid(row=8,column=1)
    Label(root1,text="Pincode ",font="Arial 10 bold",fg="cyan2",bg="gray100").grid(row=9,column=1)
    Label(root1,text="Website URL ",font="Arial 10 bold",fg="purple",bg="gray100").grid(row=10,column=1)
    Label(root1,text="Date Of Birth ",font="Arial 10 bold",fg="deep pink",bg="gray100").grid(row=11,column=1)
    Label(root1,text="Select Phone Type  ",font="Arial 12 bold",fg="yellow2",bg="gray100").grid(row=12,column=1)
    Label(root1,text="Phone Number",font="Arial 10 bold",fg="green3",bg="gray100").grid(row=13,column=1)
    Label(root1,text="Select Email Type ",font="Arial 12 bold",fg="dark turquoise",bg="gray100").grid(row=14,column=1)
    Label(root1,text="Email-ID",font="Arial 10 bold",fg="orangered",bg="gray100").grid(row=15,column=1)
    
    e1=Entry(root1)
    e2=Entry(root1)
    e3=Entry(root1)
    e4=Entry(root1)
    e5=Entry(root1)
    e6=Entry(root1)
    e7=Entry(root1)
    e8=Entry(root1)
    e9=Entry(root1)
    e10=Entry(root1)
    e11=Entry(root1) 
    e1.grid(row=3,column=2)
    e2.grid(row=4,column=2)
    e3.grid(row=5,column=2)
    e4.grid(row=6,column=2)
    e5.grid(row=7,column=2)
    e6.grid(row=8,column=2)
    e7.grid(row=9,column=2)
    e8.grid(row=10,column=2)
    e9.grid(row=11,column=2)
    e10.grid(row=13,column=2)
    e11.grid(row=15,column=2)

    v1=IntVar()
    

    Radiobutton(root1,text="Office",variable=v1,value=1).grid(row=12,column=2)
    Radiobutton(root1,text="Home",variable=v1,value=2).grid(row=12,column=3)   
    Radiobutton(root1,text="Phone",variable=v1,value=3).grid(row=12,column=4)

    r1=IntVar()
    Radiobutton(root1,text="office",variable=r1,value=1).grid(row=14,column=2)
    Radiobutton(root1,text="personal",variable=r1,value=2).grid(row=14,column=3)

    def show():
        ###########################
        
        cur.execute('create table if not exists details_1_b059(contact_id integer PRIMARY KEY AUTOINCREMENT,fname varchar2(50),mname varchar2(50),lname varchar2(50),company varchar2(70),adress varchar2(100),city varchar2(50),pin integer(6),website_url varchar2(100),dob date)')
        cur.execute('create table if not exists details_2_b059(contact_id integer ,phonetype varchar2(20),phone_no number(10),foreign key(contact_id) references details_1_b059(contact_id) on delete cascade)')          
        cur.execute('create table if not exists details_3_b059(contact_id integer ,emailtype varchar2(20),email_id varchar2(50),foreign key(contact_id) references details_1_b059(contact_id) on delete cascade)')          
        con.commit()
        


        ##################################################################
        ##check if names are same or not##
        if (e1.get()==e2.get()==e3.get()):
            showerror('error',' invalid First Name,Middle Name,Last Name same')
        elif(e1.get()==''and e2.get()=='' and e3.get()==''):
            showerror('error','invalid first name /middle name/last name')
        
        else:
            if(len(e10.get())<10 or len(e10.get())>10):
                showerror('Error',' Please enter a valid phone number' )
            else:
                ##checking if phone numb is digit or not##
                if(e10.get().isdigit()):
                    ##checking pincode is valid or not##
                    if(e7.get().isdigit()and len(e7.get())==6):
                        #city contraint
                        if(e6.get().isdigit() ):
                            showerror('city error','enter a valid city name')
                        else:
                            if v1.get()==1 and r1.get()==1:
                                A=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())
                                cur.execute('insert into details_1_b059(fname,mname,lname,company,adress,city,pin,website_url,dob) values(?,?,?,?,?,?,?,?,?)',A)
                                cur.execute('insert into details_2_b059 values((select max(contact_id)from details_1_b059),?,?)',('office',e10.get()))
                                cur.execute('insert into details_3_b059 values((select max(contact_id)from details_1_b059),?,?)',('office',e11.get()))
                                showinfo('Save','your details are saved')

                            elif v1.get()==1 and r1.get()==2:
                                A=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())
                                
                                    
                                cur.execute('insert into details_1_b059(fname,mname,lname,company,adress,city,pin,website_url,dob) values(?,?,?,?,?,?,?,?,?)',A)
                                cur.execute('insert into details_2_b059 values((select max(contact_id)from details_1_b059),?,?)',('office',e10.get()))
                                cur.execute('insert into details_3_b059 values((select max(contact_id)from details_1_b059),?,?)',('personal',e11.get()))
                                showinfo('Save','your details are saved')
                    
                            elif v1.get()==2 and r1.get()==1:
                                A=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())
                                
                                
                                cur.execute('insert into details_1_b059(fname,mname,lname,company,adress,city,pin,website_url,dob) values(?,?,?,?,?,?,?,?,?)',A)
                                cur.execute('insert into details_2_b059 values((select max(contact_id)from details_1_b059),?,?)',('home',e10.get()))
                                cur.execute('insert into details_3_b059 values((select max(contact_id)from details_1_b059),?,?)',('office',e11.get()))
                                showinfo('Save','your details are saved')
                            elif v1.get()==2 and r1.get()==2:
                                A=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())
                                
                                
                                cur.execute('insert into details_1_b059(fname,mname,lname,company,adress,city,pin,website_url,dob) values(?,?,?,?,?,?,?,?,?)',A)
                                cur.execute('insert into details_2_b059 values((select max(contact_id)from details_1_b059),?,?)',('home',e10.get()))
                                cur.execute('insert into details_3_b059 values((select max(contact_id)from details_1_b059),?,?)',('personal',e11.get()))
                                showinfo('Save','your details are saved')
                            elif v1.get()==3 and r1.get()==1:
                                A=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())
                                
                                
                                cur.execute('insert into details_1_b059(fname,mname,lname,company,adress,city,pin,website_url,dob) values(?,?,?,?,?,?,?,?,?)',A)
                                cur.execute('insert into details_2_b059 values((select max(contact_id)from details_1_b059),?,?)',('phone',e10.get()))
                                cur.execute('insert into details_3_b059 values((select max(contact_id)from details_1_b059),?,?)',('office',e11.get()))
                                showinfo('Save','your details are saved')
                            elif v1.get()==3 and r1.get()==2:
                                A=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())
                                
                                
                                cur.execute('insert into details_1_b059(fname,mname,lname,company,adress,city,pin,website_url,dob) values(?,?,?,?,?,?,?,?,?)',A)
                                cur.execute('insert into details_2_b059 values((select max(contact_id)from details_1_b059),?,?)',('phone',e10.get()))
                                cur.execute('insert into details_3_b059 values((select max(contact_id)from details_1_b059),?,?)',('personal',e11.get()))
                                showinfo('Save','your details are saved')
                                
                    
                            elif(e1.get()=='' and e2.get()=='' and e3.get()=='' and e4.get()=='' and e5.get()=='' and e6.get()=='' and e7.get()=='' and e8.get()=='' and e9.get()=='' and e10.get()=='' and e11.get()==''):
                                showerror('Error','no entries found')
                            else:
                                A=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())
                    
                    
                                cur.execute('insert into details_1_b059(fname,mname,lname,company,adress,city,pin,website_url,dob) values(?,?,?,?,?,?,?,?,?)',A)
                                cur.execute('insert into details_2_b059 values((select max(contact_id)from details_1_b059),?,?)',('',e10.get()))
                                cur.execute('insert into details_3_b059 values((select max(contact_id)from details_1_b059),?,?)',('',e11.get()))
                                showinfo('Save','your details are saved')
                   

                            cur.execute('select * from details_1_b059')
                            print cur.fetchall()
                            cur.execute('select * from details_2_b059')
                            print cur.fetchall()
                            cur.execute('select * from details_3_b059')
                            con.commit()
                            print cur.fetchall()
                            
                            e1.delete(0,END)
                            e2.delete(0,END)
                            e3.delete(0,END)
                            e4.delete(0,END)
                            e4.delete(0,END)
                            e5.delete(0,END)
                            e6.delete(0,END)
                            e7.delete(0,END)
                            e8.delete(0,END)
                            e9.delete(0,END)
                            e10.delete(0,END)
                            e11.delete(0,END)
                    else:
                        showerror('pincode error','enter a valid pincode')
                else:
                    showerror('phone number','please enter a valid number')
                
        
            

        
        ####################################################################
        
    def search():
        def on_sel(event):
            A=lb.curselection()
            if(A==()):
                return 
            else:
                def delete_details():
                    cur.execute('delete from details_1_b059 where fname=? and mname=? and lname=?',retrive)
                    showinfo("Delete","Record successfully deleted")
                    root2.destroy()
                    root5.destroy()
                    con.commit()
                root2=Tk()
                root2.configure()
                root2.geometry('450x550')
                print"fuckkk ahhhh"
                retrive=lb.get(A[0])
                cur.execute('select contact_id from details_1_b059 where fname =? and mname=? and lname =?',retrive)
                fetch_0=cur.fetchall()
                cur.execute('select fname,mname,lname,company,adress,city,pin,website_url,dob from details_1_b059 where contact_id=?',fetch_0[0])
                fetch_1=cur.fetchall()
                fetch_1=fetch_1[0]
                cur.execute('select phonetype,phone_no from details_2_b059 where contact_id=?',fetch_0[0])
                fetch_2=cur.fetchall()
                fetch_2=fetch_2[0]
                cur.execute('select emailtype,email_id from details_3_b059 where contact_id=?',fetch_0[0])
                fetch_3=cur.fetchall()
                fetch_3=fetch_3[0]
                lib1=Listbox(root2,width=400,height=20)#grid(row=2,column=0,columnspan=35,rowspan=10)
                lib1.pack()
                lib1.insert(0,"First Name: "+  fetch_1[0])
                lib1.insert(1,"Middle Name: "+ fetch_1[1])
                lib1.insert(2,"Last Name:"+    fetch_1[2])
                lib1.insert(3,"Company Name:"+ fetch_1[3])
                lib1.insert(4,"Address:"+      fetch_1[4])
                lib1.insert(5,"City:"+         fetch_1[5])
                lib1.insert(6,"Pin:"+str(fetch_1[6]))
                lib1.insert(7,"Website:"+fetch_1[7])
                lib1.insert(8,"DOB: "+fetch_1[8])
                lib1.insert(9,"Contact Type:"+fetch_2[0])
                lib1.insert(10,"Phone no.:"+str(fetch_2[1]))
                lib1.insert(11,"Email Type:"+fetch_3[0])
                lib1.insert(12,"Email id:"+fetch_3[1])
                def on_close():
                    a12=askokcancel('close','are you sure to exist')
                    if a12==1:
                        
                        root2.destroy()
                        root5.destroy()
                Button(root2,text="Close",command=on_close).pack()#grid(row=11,column=1)                
                Button(root2,text="Delete",command=delete_details).pack()#grid(row=11,column=2)
                root2.mainloop()
               
        def get_text(event1):
            lb.delete(0, END)
            print m1.get()
            cur.execute('select fname,mname,lname from details_1_b059 where fname like "%'+m1.get()+'%" or mname like " %'+m1.get()+'%" or lname like " %'+m1.get()+'%" ')
            retrive3=cur.fetchall()
            for j in range(len(retrive3)):
                lb.insert(j,retrive3[j])
            

        root5=Tk()
        root5.configure(bg='darkolivegreen1')
        root5.geometry('650x600')
        root5.bind('<Button-1>', on_sel)
        Label(root5,text="Searching Phone Book",font="Arial  16 bold",bg="darkolivegreen1",fg='dodgerblue2').pack()#grid(row=0,column=2)
        Label(root5,text="Enter Name ",font="Arial 12 bold ",bg='darkolivegreen1',fg='dodgerblue').pack()#grid(row=1,column=1)
        m1=Entry(root5)#grid(row=1,column=2)
        m1.pack()
        m1.bind('<KeyRelease>',get_text)
        lb=Listbox(root5,height=25,width=85,font="Arial 10 bold",fg="dodgerblue2",bg="darkolivegreen2",selectmode=SINGLE)#grid(row=2,column=0,columnspan=35,rowspan=10)
        lb.pack()
        Button(root5,text="Close",command=root5.destroy).pack()#grid(row=11,column=2)
        root5.mainloop()
        

    
     
    def edit():
        def on_sel_edit(event_edit):
            A_edit=lb_edit.curselection()
            if(A_edit==()):
                return 
            else:
                def edit_details():
                   # print"update"
                    root9=Tk()
                    root9.configure(bg='lavender')
                    root9.geometry('450x550')
                    Label(root9,text="update details",font="Arial 13 underline bold ",fg="deep pink",bg='lavender').grid(row=1,column=2)
                    Label(root9,text="First Name ",font="Arial 10 bold",bg='lavender').grid(row=3,column=1)
                    Label(root9,text="Middle Name ",font="Arial 10 bold",bg='lavender').grid(row=4,column=1)
                    Label(root9,text="Last Name ",font="Arial 10 bold",bg='lavender').grid(row=5,column=1)
                    Label(root9,text="Company Name ",font="Arial 10 bold",bg='lavender').grid(row=6,column=1)
                    Label(root9,text="Adress ",font="Arial 10 bold",bg='lavender').grid(row=7,column=1)
                    Label(root9,text="City ",font="Arial 10 bold",bg='lavender').grid(row=8,column=1)
                    Label(root9,text="Pincode ",font="Arial 10 bold",bg='lavender').grid(row=9,column=1)
                    Label(root9,text="Website URL ",font="Arial 10 bold",bg='lavender').grid(row=10,column=1)
                    Label(root9,text="Date Of Birth ",font="Arial 10 bold",bg='lavender').grid(row=11,column=1)
                    Label(root9,text="Select Phone Type  ",font="Arial 12 bold",fg='deep pink',bg='lavender').grid(row=12,column=1)
                    Label(root9,text="Select phone_no ",font="Arial 12 bold",bg='lavender').grid(row=13,column=1)
                    Label(root9,text="Select Email Type ",font="Arial 12 bold",fg='blue',bg='lavender').grid(row=14,column=1)
                    Label(root9,text="Email-ID",font="Arial 10 bold",bg='lavender').grid(row=15,column=1)
    
                    r1_edit=StringVar()
                    r1_edit1=Radiobutton(root9,text="office",variable=r1_edit,value='office').grid(row=12,column=2)
                    r1_edit2=Radiobutton(root9,text="home",variable=r1_edit,value='home').grid(row=12,column=3)
                    r1_edit3=Radiobutton(root9,text="phone",variable=r1_edit,value='phone').grid(row=12,column=4)

                    r2_edit=StringVar()
                    r2_edit1=Radiobutton(root9,text="office",variable=r2_edit,value='office').grid(row=14,column=2)
                    r2_edit2=Radiobutton(root9,text="personal",variable=r2_edit,value='personal').grid(row=14,column=3)
                    
##                    Label(root9,text="Phone Number",font="Arial 10 bold").grid(row=13,column=1)
##                    Label(root9,text="Select Email Type ",font="Arial 12 bold",fg='blue').grid(row=14,column=1)
##                    Label(root9,text="Email-ID",font="Arial 10 bold").grid(row=15,column=1)
                    e20=Entry(root9)
                    e21=Entry(root9)
                    e22=Entry(root9)
                    e23=Entry(root9)
                    e24=Entry(root9)
                    e25=Entry(root9)
                    e26=Entry(root9)
                    e27=Entry(root9)
                    e28=Entry(root9)
                    
                    e30=Entry(root9)
                
                    e32=Entry(root9)
                    e20.insert(9,fetch_11[0])
                    e21.insert(9,fetch_11[1])
                    e22.insert(9,fetch_11[2])
                    e23.insert(9,fetch_11[3])
                    e24.insert(9,fetch_11[4])
                    e25.insert(9,fetch_11[5])
                    e26.insert(9,fetch_11[6])
                    e27.insert(9,fetch_11[7])
                    e28.insert(9,fetch_11[8])
                    
                    e30.insert(9,fetch_22[1])
                    
                    e32.insert(9,fetch_33[1])
                    
                    e20.grid(row=3,column=2)
                    e21.grid(row=4,column=2)
                    e22.grid(row=5,column=2)
                    e23.grid(row=6,column=2)
                    e24.grid(row=7,column=2)
                    e25.grid(row=8,column=2)
                    e26.grid(row=9,column=2)
                    e27.grid(row=10,column=2)
                    e28.grid(row=11,column=2)
                    #e29.grid(row=12,column=2)
                    e30.grid(row=13,column=2)
                    #e31.grid(row=14,column=2)
                    e32.grid(row=15,column=2)
                    cur.execute("select contact_id from details_1_b059 where fname=? and mname=? and lname=?",retrive_edit)
                    retrive_4_edit=cur.fetchall()
                    retrive_4_edit=retrive_4_edit[0][0]


                    
                    def insert_edit():
                        if (e20.get()==e21.get()==e22.get()):
                            showerror('error',' invalid First Name,Middle Name,Last Name same')
                        elif(e20.get()==''and e21.get()=='' and e22.get()==''):
                            showerror('error','invalid first name /middle name/last name')
                
                        else:
                            if(len(e30.get())<10 or len(e30.get())>10):
                                showerror('Error',' Please enter a valid phone number' )
                            else:
                                ##checking if phone numb is digit or not##
                                if(e30.get().isdigit()):
                                    ##checking pincode is valid or not##
                                    if((e26.get().isdigit())and len(e26.get())==6):
                                        #city constraint
                                        if(e27.get().isdigit() ):
                                            showerror('city error','enter a valid city name')
                                        else:
                                            cur.execute("update details_1_b059 set fname=?,mname=?,lname=?,company=?,adress=?,city=?,pin=?,website_url=?,dob=? where contact_id=?",(e20.get(),e21.get(),e22.get(),e23.get(),e24.get(),e25.get(),e26.get(),e27.get(),e28.get(),retrive_4_edit))
                                            cur.execute("update details_2_b059 set phone_no=? where contact_id=?",(e30.get(),retrive_4_edit))
                                            cur.execute("update details_3_b059 set email_id=? where contact_id=?",(e32.get(),retrive_4_edit))
                                            con.commit()
                                            showinfo('update','details updated')
                                    else:
                                        showerror('pincode','invalid pin')
                                else:
                                    showerror('Error',' Please enter a valid phone number')
                                    
                                            
                                
                                           
                    def close_edit():
                        abc=askokcancel('close','are you sure you want to exit')
                        if abc==1:
                            root9.destroy()
                            
                                            
                    Button(root9,text='update',command=insert_edit).grid(row=17,column=1)
                    Button(root9,text='close',command=close_edit).grid(row=17,column=2)
                    root9.mainloop()
                    
                    
                    
                   

                root21=Tk()
                root21.geometry('600x600')
                retrive_edit=lb_edit.get(A_edit[0])
               # cur.execute('select fname,mname,lname,company,adress,city,pin,website_url,dob,phonetype,phone_no,emailtype,email_id from details_1_b059,details_2_b059,details_3_b059 where fname=? and mname=? and lname=?',retrive_ed
                cur.execute('select contact_id from details_1_b059 where fname =? and mname=? and lname =?',retrive_edit)
                fetch_00=cur.fetchall()
                cur.execute('select fname,mname,lname,company,adress,city,pin,website_url,dob from details_1_b059 where contact_id=?',fetch_00[0])
                fetch_11=cur.fetchall()
                fetch_11=fetch_11[0]
                cur.execute('select phonetype,phone_no from details_2_b059 where contact_id=?',fetch_00[0])
                fetch_22=cur.fetchall()
                fetch_22=fetch_22[0]
                cur.execute('select emailtype,email_id from details_3_b059 where contact_id=?',fetch_00[0])
                fetch_33=cur.fetchall()
                fetch_33=fetch_33[0]



                #retrive1_edit=cur.fetchall()
                #retrive1_edit=retrive1_edit[0] 
                lib1_edit=Listbox(root21,width=400,height=20)#grid(row=2,column=0,columnspan=35,rowspan=10)
                lib1_edit.pack()
                lib1_edit.insert(0,"First Name: "+fetch_11[0])
                lib1_edit.insert(1,"Middle Name: "+fetch_11[1])
                lib1_edit.insert(2,"Last Name:"+fetch_11[2])
                lib1_edit.insert(3,"Company Name:"+fetch_11[3])
                lib1_edit.insert(4,"Address:"+fetch_11[4])
                lib1_edit.insert(5,"City:"+fetch_11[5])
                lib1_edit.insert(6,"Pin:"+str(fetch_11[6]))
                lib1_edit.insert(7,"Website:"+fetch_11[7])
                lib1_edit.insert(8,"DOB: "+fetch_11[8])
                lib1_edit.insert(9,"Contact Type:"+fetch_22[0])
                lib1_edit.insert(10,"Phone no.:"+str(fetch_22[1]))
                lib1_edit.insert(11,"Email Type:"+fetch_33[0])
                lib1_edit.insert(12,"Email id:"+fetch_33[1])
                def on_close_edit():
                    abcc=askokcancel('close','are you sure you want to close')
                    if abcc==1:
                        root21.destroy()
                        root51.destroy()
                Button(root21,text="Close",command=on_close_edit).pack()#grid(row=11,column=1)                
                Button(root21,text="update",command=edit_details).pack()#grid(row=11,column=2)
                root21.mainloop()
                   
        def get_text_edit(event1_edit):
            lb_edit.delete(0, END)
            #lb=Listbox(root51,height=30,width=80,fg="black",bg="light pink",selectmode=SINGLE).pack()#grid(row=2,column=0,columnspan=35,rowspan=10)
                
            print m1_edit.get()
            cur.execute('select fname,mname,lname from details_1_b059 where fname like "%'+m1_edit.get()+'%" or mname like " %'+m1_edit.get()+'%" or lname like " %'+m1_edit.get()+'%" ')
            retrive3_edit=cur.fetchall()
            for j in range(len(retrive3_edit)):
                lb_edit.insert(j,retrive3_edit[j])
            

        root51=Tk()
        root51.geometry('600x600')
        root51.configure(bg='lavenderblush')
        root51.bind('<Button-1>', on_sel_edit)
        Label(root51,text="Searching Phone Book",font="Arial 15",fg='deeppink2',bg="lavenderblush").pack()#grid(row=0,column=2)
        Label(root51,text="Enter Name").pack()#grid(row=1,column=1)
        m1_edit=Entry(root51)#grid(row=1,column=2)
        m1_edit.pack()
        m1_edit.bind('<KeyRelease>',get_text_edit)
        lb_edit=Listbox(root51,height=30,width=80,fg="black",bg="misty rose",selectmode=SINGLE)#grid(row=2,column=0,columnspan=35,rowspan=10)
        lb_edit.pack()
        Button(root51,text="Close",command=root51.destroy).pack()#grid(row=11,column=2)
        root51.mainloop()
        
        root41=Tk()
        root41.geometry('600x600')
        root41.mainloop()


    def close1():
        x=askokcancel('close','Do you want to close')
        if x==1:
            root1.destroy()
            
    Button(root1,text='Save',command=show).grid(row=17,column=1)
    Button(root1,text='Search',command=search).grid(row=17,column=2)
    Button(root1,text='Close',command=close1).grid(row=17,column=3)
    Button(root1,text='Edit  ',command=edit).grid(row=17,column=4)  
    root1.mainloop()

    
root.bind("<Motion>",close)
root.mainloop()
