from tkinter import*
from PIL import Image, ImageTk, ImageDraw # pip install pillow
from datetime import*
import time
from math import*
import sqlite3
from tkinter import messagebox, ttk
import os

class Login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1350x655+0+0")
        self.root.config(bg="#021e2f")

        #***********Background***********
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        #left_lbl.place(x=0,y=0,relheight=1,width=600)

        #right_lbl=Label(self.root,bg="#031F3C",bd=0)
        #right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        #***********Frames***********
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=80,width=750,height=500)

        #***********Title***********
        title=Label(login_frame,text="LOGIN HERE", font=("times new roman", 20, "bold"),bg="white",fg="green").place(x=250,y=50)

        email=Label(login_frame,text="Enter Email Address", font=("times new roman", 15, "bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350)

        password=Label(login_frame,text="Enter Password", font=("times new roman", 15, "bold"),bg="white",fg="gray",).place(x=250,y=230)
        self.txt_password=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=250,y=260,width=350)

        btn_reg=Button(login_frame,text="Register new Account?", font=("times new roman",14),bg="white",bd=0,fg="green",cursor="hand2", command=self.register_window).place(x=250,y=290)

        btn_forget=Button(login_frame,text="Forget Password?", font=("times new roman",14),bg="white",bd=0,fg="red",cursor="hand2", command=self.forget_password_window).place(x=450,y=290)

        btn_login=Button(login_frame,text="Login", font=("times new roman",18,"bold"),fg="white",bg="green", cursor="hand2", command=self.login).place(x=250,y=350,width=180)
        

        
#==============================================================================
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)

    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root2)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please Select the Correct Security Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?",(self.txt_new_password.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your password has been reset, Please login with new password", parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}",parent=self.root)


    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error", "Please enter the email address to reset your password",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror("Error", "Please enter the valid email address to reset your password",parent=self.root)
                else:
                    con.close()   
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x410+450+140")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

                    #***********Forget Password***********
                    question=Label(self.root2,text="Security Question", font=("times new roman", 15, "bold"),bg="white",fg="gray").place(x=70,y=100)

                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13), state="readonly", justify=CENTER)
                    self.cmb_quest["values"]=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=70,y=130,width=250)
                    self.cmb_quest.current(0)

                    answer=Label(self.root2,text="Enter Answer", font=("times new roman", 15, "bold"),bg="white",fg="gray").place(x=70,y=180)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_answer.place(x=70,y=210,width=250)

                    new_password=Label(self.root2,text="Enter New Password", font=("times new roman", 15, "bold"),bg="white",fg="gray").place(x=70,y=260)
                    self.txt_new_password=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_new_password.place(x=70,y=290,width=250)

                    btn_change_password=Button(self.root2,text="Reset Password",bg="green",fg="white",cursor="hand2",command=self.forget_password,font=("times new roman",15,"bold")).place(x=110, y=340, width=180)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}",parent=self.root)
    
    def register_window(self):
        self.root.destroy()
        import register,register

    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error", "All Fields Are Required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_password.get(),))
                row=cur.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror("Error", "Invalid Username & Password", parent=self.root) 
                else:
                    messagebox.showinfo("Success", f"Welcome: {self.txt_email.get()}", parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()    
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}",parent=self.root)


root=Tk()
obj=Login_window(root)
root.mainloop()