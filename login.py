from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Login_window:
    def __init__(self, window):
        self.window = window
        self.window.title("Login")
        self.window.geometry = ("1550x800+0+0")

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
        img1 = img1.resize((27,27),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=670,y=290,width=27,height=27)

        img2 = Image.open(r"Images\password_logo.png")
        img2 = img2.resize((27,27),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lblimg2.place(x=670,y=370,width=27,height=27)

        # Login Button
        login_button=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="steel blue",activeforeground="black",activebackground="steel blue")
        login_button.place(x=110,y=300,width=120,height=35)

        # Register Button
        register_button=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
        register_button.place(x=15,y=350,width=160,)

        # Forgot Password Button
        forgetpass_button=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
        forgetpass_button.place(x=10,y=390,width=160)

    def login(self):
        if self.txtusr.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txtusr.get()=="kapu" and self.txtpass.get()=="gappu":
            messagebox.showinfo(title='Welcome',message="Sucessful Login")
        else:
            messagebox.showerror("Invalid","Invalid username or password")


if __name__ == "__main__":
    window = Tk()
    app = Login_window(window)
    window.mainloop()
