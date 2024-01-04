from tkinter import *
from tkinter import ttk

import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Welcome_window():
    def __init__(self, window):
        self.window = window
        self.window.title("Login")
        self.window.geometry = ("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(
            file=r"Images\Welcome-message.jpg")
        lbl_bg = Label(self.window, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
class Login_window:
    def __init__(self, window):
        self.window = window
        self.window.title("Login")
        self.window.geometry = ("1550x800+0+0")

        self.var_email=StringVar()
        self.var_pass=StringVar()

        self.bg = ImageTk.PhotoImage(
            file=r"Images\1350991-download-free-cool-windows-10-hd-wallpapers-1920x1080-windows-xp.jpg")
        lbl_bg = Label(self.window, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.window,bg="white")
        frame.place(x=630,y=170,width=340,height=450)

        get_strt=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_strt.place(x=95,y=50)

        # label
        username=ttk.Label(frame,text="Username",font=("times new roman",15,"bold"))
        username.place(x=70,y=120)

        self.txtusr=ttk.Entry(frame,font=("times new roman",15,"normal"))
        self.txtusr.place(x=40,y=155,width=270)

        password=ttk.Label(frame,text="Password",font=("times new roman",15,"bold"))
        password.place(x=70,y=200,bordermode="inside")

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"normal"))
        self.txtpass.place(x=40,y=235,width=270)

        # Icon Images

        img1 = Image.open(r"Images\username_logo.png")
        img1 = img1.resize((27,27),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=670,y=290,width=27,height=27)

        img2 = Image.open(r"Images\password_logo.png")
        img2 = img2.resize((27,27),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lblimg2.place(x=670,y=370,width=27,height=27)

        # Login Button
        login_button=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="steel blue",activeforeground="black",activebackground="steel blue")
        login_button.place(x=110,y=300,width=120,height=35)

        # Register Button
        register_button=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
        register_button.place(x=15,y=350,width=160,)

        # Forgot Password Button
        forgetpass_button=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
        forgetpass_button.place(x=10,y=390,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.window)
        self.app=Register_window(self.new_window)


    def login(self):
        if self.txtusr.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txtusr.get()=="kapu" and self.txtpass.get()=="gappu":
            messagebox.showinfo(title='Welcome',message="Sucessful Login")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="mysql_db")
            cur = conn.cursor()
            # Your SQL query with placeholders
            query = "SELECT * FROM register WHERE email=%s AND password=%s"
            value = (self.var_email.get(), self.var_pass.get())

            # Execute the query with the provided data
            cur.execute(query,value)
            row=cur.fetchone()

            if row!=None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                self.new_window = Toplevel(self.window)
                self.app = Welcome_window(self.new_window)

class Register_window:
    def __init__(self,window):
        self.window=window
        self.window.title("Register")
        self.window.geometry("1600x900+0+0")

        # ------------- Variables -------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()

        # ------------- Background Image -------------
        self.bg = ImageTk.PhotoImage(
            file=r"Images\Windows-10-Wallpaper-HD-Free-download.jpg")
        lbl_bg = Label(self.window, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # ------------- Left Frame -------------
        left_frame = Frame(self.window, bg="grey")
        left_frame.place(x=330, y=170, width=370, height=550)

        self.left_frame_1 = ImageTk.PhotoImage(
            file=r"Images/nature-desktop-wallpaper-hd-free-download.jpg")
        lbl_bg = Label(left_frame, image=self.left_frame_1)
        lbl_bg.place(x=30, y=30, width=310, height=500)

        right_frame = Frame(self.window, bg="steel blue")
        right_frame.place(x=700, y=170, width=550, height=550)

        get_strt=Label(right_frame,text="Registration ", font=("times new roman", 30, "bold"), fg="white", bg="steel blue")
        get_strt.place(x=125, y=50)

        # In Column 1
        # ------------- Row 1 -------------
        f_name=Label(right_frame,text="First Name",font=("times new roman",15,"bold"), fg="white", bg="steel blue")
        f_name.place(x=30,y=120)

        self.f_entry=ttk.Entry(right_frame,textvariable=self.var_fname,font=("times new roman",15,"bold") )
        self.f_entry.place(x=30, y= 150, width=200)

        # ------------- Row 2 -------------
        contact=Label(right_frame,text="Contact Number",font=("times new roman",15,"bold"), fg="white", bg="steel blue")
        contact.place(x=30,y=200)

        self.contact_entry=ttk.Entry(right_frame,textvariable=self.var_contact,font=("times new roman",15,"bold") )
        self.contact_entry.place(x=30, y= 230, width=200)

        # -------------- Row 3 -------------
        security_q=Label(right_frame,text="Select Security Question",font=("times new roman",15,"bold"), fg="white", bg="steel blue")
        security_q.place(x=30,y=280)

        self.security_q_entry=ttk.Combobox(right_frame,textvariable=self.var_securityQ,font=("times new roman",12) )
        self.security_q_entry["values"]=("Select", "Your Birth Place", "You Pet Name", "Your Primary School")
        self.security_q_entry.place(x=30, y=310, width=200)
        self.security_q_entry.current(0)

        # --------------- Row 4 -------------
        password=Label(right_frame,text="Password",font=("times new roman",15,"bold"), fg="white", bg="steel blue")
        password.place(x=30,y=360)

        self.password_entry=ttk.Entry(right_frame,textvariable=self.var_pass,font=("times new roman",15,"bold") )
        self.password_entry.place(x=30, y= 390, width=200)

        # Column 2
        l_name=Label(right_frame,text="Last Name",font=("times new roman",15,"bold"), fg="white", bg="steel blue")
        l_name.place(x=300,y=120)

        self.l_entry=ttk.Entry(right_frame,textvariable=self.var_lname,font=("times new roman",15,"bold") )
        self.l_entry.place(x=300, y= 150, width=200)

        # --------------- Row 2
        email=Label(right_frame,text="Email",font=("times new roman",15,"bold"), fg="white", bg="steel blue")
        email.place(x=300,y=200)

        self.email_entry=ttk.Entry(right_frame,textvariable=self.var_email,font=("times new roman",15,"bold") )
        self.email_entry.place(x=300, y= 230, width=200)

        # --------------- Row 3
        security_a=Label(right_frame,text="Security Answer",font=("times new roman",15,"bold"), fg="white", bg="steel blue")
        security_a.place(x=300,y=280)

        self.security_a_entry=ttk.Entry(right_frame,textvariable=self.var_securityA,font=("times new roman",15,"bold") )
        self.security_a_entry.place(x=300, y= 310, width=200)

        # --------------- Row 4
        confirm_password=Label(right_frame,text="Confirm Password",font=("times new roman",15,"bold"), fg="white", bg="steel blue")
        confirm_password.place(x=300,y=360)

        self.confirm_password_entry=ttk.Entry(right_frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.confirm_password_entry.place(x=300, y= 390, width=200)

        # --------------- Checkout ---------------
        checkbutton=Checkbutton(right_frame,variable=self.var_check, text="I Agree The Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0,bg="steel blue",activebackground='steel blue')
        checkbutton.place(x=30, y=420)

        # --------------- Register Now button ---------------
        register_button=Button(right_frame,command=self.register_data,text="Register Now",font=("times new roman",15,"bold"),bg="red",activebackground='red')
        register_button.place(x=30, y=470, width=150)

        # --------------- Login Now button ---------------
        login_button=Button(right_frame,text="Login Now",font=("times new roman",15,"bold"),bg="grey",activebackground='grey')
        login_button.place(x=300, y=470, width=150)

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm password should be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error",'Please agree our terms and conditions')
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="mysql_db")
            cur=conn.cursor()

            query=("SELECT * FROM REGISTER WHERE email=%s")
            value=(self.var_email.get(),)

            cur.execute(query,value)
            row=cur.fetchone()

            if row != None:
                messagebox.showerror("Error","User already exist")
            else:
                cur.execute("INSERT INTO REGISTER VALUES(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully")

if __name__ == "__main__":
    main()
