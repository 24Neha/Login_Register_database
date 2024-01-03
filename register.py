from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from login import Login_window
import mysql.connector

class Register_window:
    def __init__(self,window):
        self.window=window
        self.window.title("Register")
        self.window.geometry("1600x900+0+0")

        # ------------- Variables -------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=IntVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()

        # ------------- Background Image -------------
        self.bg = ImageTk.PhotoImage(
            file=r"Images\1350991-download-free-cool-windows-10-hd-wallpapers-1920x1080-windows-xp.jpg")
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
            messagebox.showinfo("Success", "Welcome")

if __name__ == "__main__":
    window = Tk()
    app=Register_window(window)
    window.mainloop()