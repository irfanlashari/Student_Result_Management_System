from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from course import courseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
import sqlite3
import threading
class RMS:
    def __init__(self, root):  # Constructor with root (Tkinter object)
        self.root = root
        self.root.title("QUEST Student Result Management System")
        self.root.geometry("1350x655+0+0")  # Setting window size
        self.root.config(bg="white")

        # Load images first
        self.load_images()

        # Title Section (now that self.logo_dash is defined)
        title = Label(self.root, text="QUEST Student Result Management System", padx=10, compound=LEFT, image=self.logo_dash, 
                      font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)

        # Menu Section
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1260, height=80)

        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x=10, y=5, width=200, height=40)
        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=220, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result).place(x=430, y=5, width=200, height=40)
        btn_view = Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x=640, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.logout).place(x=850, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.exit_).place(x=1060, y=5, width=180, height=40)

        # Background Image
        self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize((1280,530))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=0, y=150, width=1280, height=530)

        #   Side image
        #self.side_img = Image.open("images/side_image.jpg")  # Replace with your side image path
        #self.side_img = self.side_img.resize((920, 350))  # Resize image to fit the side of the window
        #self.side_img = ImageTk.PhotoImage(self.side_img)
        #self.lbl_side = Label(self.root, image=self.side_img).place(x=0, y=0, height=350, width=400)  # Adjust the position as needed

        # Update Labels
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=330, y=530, width=300, height=90)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=640, y=530, width=300, height=90)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=950, y=530, width=300, height=90)

        # Footer
        footer = Label(self.root, text="QUEST - Student Result Management System ", font=("goudy old style", 10), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        self.update_details()

    def load_images(self):
        # Load logo image
        if os.path.exists("images/logo_p.jpg"):
            self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.jpg")
        else:
            messagebox.showerror("Error", "Logo image not found!")
            self.logo_dash = None  # Ensure logo_dash exists even if image is not found
        
        # Load background image
        if os.path.exists("images/bg.png"):
            self.bg_img = Image.open("images/bg.png")
            self.bg_img = self.bg_img.resize((920, 350))
            self.bg_img = ImageTk.PhotoImage(self.bg_img)
        else:
            messagebox.showerror("Error", "Background image not found!")

    def update_details(self):
        # Use threading to prevent freezing UI
        def fetch_data():
            try:
                with sqlite3.connect(database="rms.db") as con:
                    cur = con.cursor()

                    cur.execute("SELECT * FROM course")
                    courses = cur.fetchall()
                    self.lbl_course.config(text=f"Total Courses\n[{len(courses)}]")

                    cur.execute("SELECT * FROM student")
                    students = cur.fetchall()
                    self.lbl_student.config(text=f"Total Students\n[{len(students)}]")

                    cur.execute("SELECT * FROM result")
                    results = cur.fetchall()
                    self.lbl_result.config(text=f"Total Results\n[{len(results)}]")
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")

        # Start fetching data in a separate thread
        threading.Thread(target=fetch_data).start()
        
        # Refresh every 1 second
        self.lbl_course.after(1000, self.update_details)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = courseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)
        
    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python login.py")  # You can replace this with subprocess.Popen for better handling

    def exit_(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op == True:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
