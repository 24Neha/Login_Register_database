from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


class Forget_password:
    def __init__(self, window):

        self.root = window
        self.root.title("Forget Password")
        self.root.geometry("340x450+530+170")

        label = Label(self.root, text="Forget Password ", font=("times new roman", 25, "bold"), fg="red")
        label.place(x=8, y=40, relwidth=1)

        security_q = Label(self.root, text="Select Security Question", font=("times new roman", 15, "bold"),
                           fg="black")
        security_q.place(x=35, y=90)

        self.security_q_entry = ttk.Combobox(self.root, font=("times new roman", 15))
        self.security_q_entry["values"] = (
            "Select", "Your Birth Place", "You Pet Name", "Your Primary School")
        self.security_q_entry.place(x=35, y=130, width=250)
        self.security_q_entry.current(0)

        security_a = Label(self.root, text="Security Answer", font=("times new roman", 15, "bold"),
                           fg="black")
        security_a.place(x=35, y=180)

        self.security_a_entry = ttk.Entry(self.root, font=("times new roman", 15))
        self.security_a_entry.place(x=35, y=210, width=250)

        reset_pass = Label(self.root, text="New Password", font=("times new roman", 15, "bold"), fg="black")
        reset_pass.place(x=35, y=260)

        self.reset_pass_entry = ttk.Entry(self.root, font=("times new roman", 15))
        self.reset_pass_entry.place(x=35, y=290, width=250)

        pass_button = Button(self.root, text="Reset", command=self.reset_pass,
                             font=("times new roman", 15, "bold"), fg='white', bg='green',
                             activebackground='green')
        pass_button.place(x=120, y=350)

    def reset_pass(self):
        if self.security_q_entry.get() == "Select":
            messagebox.showerror("Error", "Select security question", parent=self.root)
        elif self.security_a_entry == "":
            messagebox.showerror("Error", "Please enter answer", parent=self.root)
        elif self.reset_pass_entry == "":
            messagebox.showerror("Error", "Please enter new password", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="mysql_db")
            cur = conn.cursor()

            # Your SQL query with placeholders
            query = ("SELECT * FROM register WHERE securityQ=%s and securityA=%s")
            value = (self.security_q_entry.get(),self.security_a_entry.get())

            # Execute the query with the provided data
            cur.execute(query, value)
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Please enter correct answer", parent=self.root)
            else:
                update_query = "UPDATE register SET password=%s WHERE email=%s"
                update_values = (self.reset_pass_entry.get(), self.login.txtusr.get())
                cur.execute(update_query, update_values)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset, Please login with new password", parent=self.root)

                self.root.destroy()


    def forgot_password(self):
        if self.login.txtusr.get() == "":
            messagebox.showerror("Error", "Please enter email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="mysql_db")
            cur = conn.cursor()

            query = ("select * from register where email=%s")
            value = (self.login.txtusr.get(),)

            cur.execute(query, value)
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("My Error", "Please enter valid email address")
            else:
                conn.close()
                self.root = Toplevel()
                self.root.title("Forget Password")
                self.root.geometry("340x450+530+170")

                label = Label(self.root, text="Forget Password ", font=("times new roman", 25, "bold"), fg="red")
                label.place(x=8, y=40, relwidth=1)

                security_q = Label(self.root, text="Select Security Question", font=("times new roman", 15, "bold"),
                                   fg="black")
                security_q.place(x=35, y=90)

                self.security_q_entry = ttk.Combobox(self.root, font=("times new roman", 15))
                self.security_q_entry["values"] = (
                "Select", "Your Birth Place", "You Pet Name", "Your Primary School")
                self.security_q_entry.place(x=35, y=130, width=250)
                self.security_q_entry.current(0)

                security_a = Label(self.root, text="Security Answer", font=("times new roman", 15, "bold"),
                                   fg="black")
                security_a.place(x=35, y=180)

                self.security_a_entry = ttk.Entry(self.root, font=("times new roman", 15))
                self.security_a_entry.place(x=35, y=210, width=250)

                reset_pass = Label(self.root, text="New Password", font=("times new roman", 15, "bold"), fg="black")
                reset_pass.place(x=35, y=260)

                self.reset_pass_entry = ttk.Entry(self.root, font=("times new roman", 15))
                self.reset_pass_entry.place(x=35, y=290, width=250)

                pass_button = Button(self.root, text="Reset", command=self.reset_pass,
                                     font=("times new roman", 15, "bold"), fg='white', bg='green',
                                     activebackground='green')
                pass_button.place(x=120, y=350)


if __name__ == "__main__":
    window = Tk()
    app=Forget_password(window)
    window.mainloop()