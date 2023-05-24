from tkinter import messagebox, ttk
from PIL import ImageTk,Image
import mysql.connector
import pandas as pd
import tkinter as tk

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="myPhone",
    database="ddd"
)

cursor = db.cursor()

# function to open a new window after successful login
def open_new_window():
    root.withdraw()
    def destroy_window():
        new_window.destroy()
        root.deiconify()
    
    new_window = tk.Toplevel(root)
    new_window.title("myPhone")
    new_window.geometry("750x750")
    new_window.maxsize(750, 750)

    btn_logout = tk.Button(new_window, text = "Sign Out", command = destroy_window, bg = '#CED4DA', font = ("Yu Gothic UI SEMIBOLD",15))
    btn_logout.place(x = 225, y = 600, width = 200)

    cursor.execute("SELECT fname, contact_number, position, office, local_line, email_add FROM users")
    result = cursor.fetchall()

    scrollbar = tk.Scrollbar(root)
    scrollbar.place(x=730, y=0, height=750)

    # Create a treeview
    treeview = ttk.Treeview(new_window, yscrollcommand=scrollbar.set, show = 'headings')

    # Define the columns
    treeview["columns"] = ("#1", "#2", "#3", "#4", "#5", "#6")

    # Format column headers
    treeview.heading("#1", text = "Fname")
    treeview.heading("#2", text = "Contact#")
    treeview.heading("#3", text = "Position")
    treeview.heading("#4", text = "Office")
    treeview.heading("#5", text = "Local_line")
    treeview.heading("#6", text = "Email_add")

    # Configure column widths
    treeview.column("#1", width = 100, anchor ='c')
    treeview.column("#2", width = 25, anchor ='c')
    treeview.column("#3", width = 50, anchor ='c')
    treeview.column("#4", width = 50, anchor ='c')
    treeview.column("#5", width = 15, anchor ='c')
    treeview.column("#6", width = 75, anchor ='c')

    # Bind the treeview to the scrollbar
    scrollbar.config(command=treeview.yview)

    # Insert data into the treeview
    for item in result:
        treeview.insert("", tk.END, values=item)

    # Place the treeview widget
    treeview.place(x = 0, y = 0, width = 730, height = 450)

    
    new_window.mainloop()

# function to open a new window for the admin
def open_new_window1(*args):
    root.withdraw()
    def signout():
        new_window1.destroy()
        root.deiconify()
    new_window1 = tk.Toplevel(root)
    new_window1.title("myPhone")
    new_window1.geometry("750x750")
    new_window1.maxsize(750, 750)

    btn_register = tk.Button(new_window1, text = "Register", command = register, bg = '#CED4DA', font = ("Yu Gothic UI SEMIBOLD",15))
    btn_register.place(x = 225, y = 550, width = 200)

    btn_delete = tk.Button(new_window1, text = "Delete", command = delete, bg = '#CED4DA', font = ("Yu Gothic UI SEMIBOLD",15))
    btn_delete.place(x = 225, y = 600, width = 200)

    btn_logout = tk.Button(new_window1, text = "Sign Out", command = signout, bg = '#CED4DA', font = ("Yu Gothic UI SEMIBOLD",15))
    btn_logout.place(x = 225, y = 650, width = 200)
    
    cursor.execute("SELECT fname, contact_number, position, office, local_line, email_add FROM users")
    result = cursor.fetchall()

    scrollbar = tk.Scrollbar(root)
    scrollbar.place(x=730, y=0, height=750)

    # Create a treeview
    treeview = ttk.Treeview(new_window1, yscrollcommand=scrollbar.set, show = 'headings')

    # Define the columns
    treeview["columns"] = ("#1", "#2", "#3", "#4", "#5", "#6")

    # Format column headers
    treeview.heading("#1", text = "Fname")
    treeview.heading("#2", text = "Contact#")
    treeview.heading("#3", text = "Position")
    treeview.heading("#4", text = "Office")
    treeview.heading("#5", text = "Local_line")
    treeview.heading("#6", text = "Email_add")

    # Configure column widths
    treeview.column("#1", width = 100, anchor ='c')
    treeview.column("#2", width = 25, anchor ='c')
    treeview.column("#3", width = 50, anchor ='c')
    treeview.column("#4", width = 50, anchor ='c')
    treeview.column("#5", width = 15, anchor ='c')
    treeview.column("#6", width = 75, anchor ='c')

    # Bind the treeview to the scrollbar
    scrollbar.config(command=treeview.yview)

    # Insert data into the treeview
    for item in result:
        treeview.insert("", tk.END, values=item)

    # Place the treeview widget
    treeview.place(x = 0, y = 0, width = 730, height = 450)

    
    new_window1.mainloop()

# forgot function
def forgot(*args):
    root.withdraw()
    def forgot_password():
        username = entry_username.get()
        pw = entry_password.get()
        confirm_pw = confirm_entry.get()

        if username == "" or pw == "":
            messagebox.showerror("Error", "Please enter a username and password.")
            return

        # insert data
        if pw == confirm_pw:
            cursor.execute("UPDATE users SET pw = %s WHERE username = %s", (pw, username))
            db.commit()
            messagebox.showinfo("Success", "Reset successful!")
            forgot_window.destroy()
            root.deiconify()

    # registration window
    forgot_window = tk.Toplevel(root)
    forgot_window.geometry("750x750")
    forgot_window.maxsize(750, 750)
    forgot_window.title("Forgot Password")

    label_username = tk.Label(forgot_window, text="Username:", bg = '#CED4DA', font = ("Yu Gothic UI",15))
    label_username.pack()
    entry_username = tk.Entry(forgot_window, font = ("Yu Gothic UI",15))
    entry_username.pack()

    label_password = tk.Label(forgot_window, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(forgot_window, show="*")
    entry_password.pack()

    label_confirm = tk.Label(forgot_window, text="Password:")
    label_confirm.pack()
    confirm_entry = tk.Entry(forgot_window, show="*")
    confirm_entry.pack()


    forgot_window.bind('<Return>', forgot_password)
    btn_reset = tk.Button(forgot_window, text="reset", command=forgot_password, bg = '#CED4DA', font = ("Yu Gothic UI",15))
    btn_reset.pack()

# register function
def register(*args):
    def register_user():
        email_add = entry_email_add.get()
        username = entry_username.get()
        pw = entry_password.get()
        fname = entry_fname.get()
        position = entry_position.get()
        contact_number = entry_contact_number.get()
        office = entry_office.get()
        local_line = entry_local_line.get()

        if  email_add == "" or username == "" or pw == "" or fname == "" or position == "" or contact_number == "" or office == "" or local_line == "":
            messagebox.showerror("Error", "Please enter fields you want to update!")
            return

        # checker if inputted user exists
        cursor.execute("SELECT * FROM users WHERE email_add = %s or username = %s", (username, email_add))
        result = cursor.fetchone()

        if result:
            messagebox.showerror("Error", "User or Email Address is the same.")
            return

        # register data
        cursor.execute("INSERT INTO users (email_add, username, pw, fname, position, contact_number, office, local_line) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (email_add, username, pw, fname, position, contact_number, office, local_line)) 
        db.commit()
        messagebox.showinfo("Success", "Registration successful!")
        register_window.destroy()

    # registration window
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("750x750")

    label_email = tk.Label(register_window, text = "Email Address:")
    label_email.pack()
    entry_email_add = tk.Entry(register_window)
    entry_email_add.pack()

    label_username = tk.Label(register_window, text = "Username:")
    label_username.pack()
    entry_username = tk.Entry(register_window)
    entry_username.pack()

    label_password = tk.Label(register_window, text = "Password:")
    label_password.pack()
    entry_password = tk.Entry(register_window, show = "*")
    entry_password.pack()

    label_fname = tk.Label(register_window, text = "Full Name:")
    label_fname.pack()
    entry_fname = tk.Entry(register_window)
    entry_fname.pack()

    label_position = tk.Label(register_window, text = "Position:")
    label_position.pack()
    entry_position = tk.Entry(register_window)
    entry_position.pack()

    label_contact_number = tk.Label(register_window, text = "Contact#:")
    label_contact_number.pack()
    entry_contact_number = tk.Entry(register_window)
    entry_contact_number.pack()

    label_office = tk.Label(register_window, text = "Office:")
    label_office.pack()
    entry_office = tk.Entry(register_window)
    entry_office.pack()
    
    label_local_line = tk.Label(register_window, text = "Local Line:")
    label_local_line.pack()
    entry_local_line = tk.Entry(register_window)
    entry_local_line.pack()

    btn_register = tk.Button(register_window, text = "Register", command = register_user)
    btn_register.pack()

    register_window.bind('<Return>',register_user)

# login function
def login(*args):
    username = entry_username.get()
    pw = entry_password.get()

    if username == "" or pw == "":
        messagebox.showerror("Error", "Please enter a username and password.")
        return
    # admin
    if username == "controller" and pw == "1234":
        messagebox.showinfo("Success", "Login successful!")
        open_new_window1()

    # if user and pw == sql user and pw
    cursor.execute("SELECT * FROM users WHERE username = %s AND pw = %s", (username, pw))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Login successful!")
        open_new_window()
    else:
        messagebox.showerror("Error", "Invalid username or password.")
  
# delete function
def delete():
    def delete_user(*args):
        email_add = entry_email_add1.get()
        username = entry_username.get()

        if username == "" or email_add == "":
                messagebox.showerror("Error", "Please enter a username and password.")
                return

        # delete data   
        cursor.execute("DELETE FROM users WHERE email_add = %s or username = %s", (email_add, username))
        db.commit()
        messagebox.showinfo("Success", "Delete successful!")
        delete_window.destroy()

    delete_window=tk.Toplevel(root)
    delete_window.title("Delete")

    label_email = tk.Label(delete_window, text = "Email Address:")
    label_email.pack()
    entry_email_add1 = tk.Entry(delete_window)
    entry_email_add1.pack()

    label_username = tk.Label(delete_window, text = "Username:")
    label_username.pack()
    entry_username = tk.Entry(delete_window)
    entry_username.pack()

    btn_delete = tk.Button(delete_window, text = "Delete", command = delete_user)
    btn_delete.pack()
    delete_window.bind('<Return>',delete_user)
    
# privacy window
def privacy(*args):
    def destroy_privacywindow():
        privacy_window.destroy()
    privacy_window = tk.Toplevel(root)
    privacy_window.title("myPhone")
    privacy_window.geometry("250x250")
    privacy_window.maxsize(250, 250)
    
    lblheader = tk.Label(privacy_window, font = ("Yu Gothic UI SEMIBOLD",9), text = "PRIVACY, COOKIES AND TERMS OF USE")
    lblheader.place(x=5,y=10)

    lblcontent = tk.Label(privacy_window,font = ("Yu Gothic UI",10), text = "myCorphone will collect, use, and store")
    lblcontent.place(x=5,y=30)
    lblcontent = tk.Label(privacy_window,font = ("Yu Gothic UI",10), text = "your personal information that is")
    lblcontent.place(x=5,y=50)
    lblcontent = tk.Label(privacy_window,font = ("Yu Gothic UI",10), text = "necessary to use this application and")
    lblcontent.place(x=5,y=70)
    lblcontent = tk.Label(privacy_window,font = ("Yu Gothic UI",10), text = "the related functionalities.")
    lblcontent.place(x=5,y=90)
    lblcontent = tk.Label(privacy_window,font = ("Yu Gothic UI",10), text = "myCorphone handles this information")
    lblcontent.place(x=5,y=120)
    lblcontent = tk.Label(privacy_window,font = ("Yu Gothic UI",10), text = "on behalf of your institution.")
    lblcontent.place(x=5,y=140)

    btn_ok = tk.Button(privacy_window,text = "OK", command = destroy_privacywindow,bg = 'black',font = ("Yu Gothic UI",10), fg = 'white' )
    btn_ok.place(x = 210,y = 200)

# create the main application window
root = tk.Tk()
root.geometry("750x750")
root.title("Login")
root.configure(bg='gainsboro')
root.maxsize(750, 750)

left_frame = tk.Frame(root,  width = 250,  height = 700,  bg = '#6C757D')
left_frame.place(x = 100, y = 50)

right_frame = tk.Frame(root,  width = 300, height = 700,  bg = 'white')
right_frame.place(x = 350, y = 50)

logo_image=Image.open(r"C:\Users\raben\Downloads\myCorphone.PNG")
resize_image=logo_image.resize((200,200))
image1=ImageTk.PhotoImage(resize_image)
logo= tk.Label(root,image = image1)
logo.place(x = 125, y = 250)

label_corp = tk.Label(root, text = "VIRDAN", font = ("Segoe UI",25), fg = 'white', bg = '#6C757D')
label_corp.place(x = 160,y = 100) 

label_welcome = tk.Label(root, text = "WELCOME", font = ("Yu Gothic UI SEMIBOLD",25), bg = '#CED4DA')
label_welcome.place(x = 415,y = 100) 

# create labels, entry fields, and buttons for login
label_username = tk.Label(root, text = "Username:", font = ("Yu Gothic UI",14), fg = 'black', bg = 'white')
label_username.place(x = 396, y = 225)
entry_username = tk.Entry(root, font = (14), bg = 'gainsboro', width = 20)
entry_username.place(x = 400, y = 275)

label_password = tk.Label(root, text = "Password:",font = ("Yu Gothic UI",14), fg = 'black', bg = 'white')
label_password.place(x = 396, y = 325)
entry_password = tk.Entry(root, show = "*", font=(14), bg = 'gainsboro', width = 20)
entry_password.place(x = 400, y = 375)

root.bind('<Return>',login)
btn_login = tk.Button(root, text="Sign in",font=("Yu Gothic UI",10), command = login, bg = '#CED4DA')
btn_login.place(x = 400, y = 425, width = 185)


# create a button to open the registration window
label_forgot = tk.Label(root, text = "Forgot password?",font = ("Yu Gothic UI",10),fg= 'blue',  bg='white')
label_forgot.bind("<Button-1>",forgot)
label_forgot.place(x = 400, y = 465, width = 185)

label_privacy = tk.Label(root, text = "Privacy and Terms of Use",font = ("Yu Gothic UI",10),fg = 'gray',  bg = 'white')
label_privacy.bind("<Button-1>",privacy)
label_privacy.place(x = 400, y = 500, width = 185)

# run the application
root.mainloop()

# close the database connection
db.close()
