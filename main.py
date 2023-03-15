import tkinter as tk

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "12345":
        label_status.config(text="Login successful")
    else:
        label_status.config(text="Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Create the username label and entry field
label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

# Create the password label and entry field
label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Create the login button
button_login = tk.Button(root, text="Login", command=login)
button_login.pack()

# Create the status label
label_status = tk.Label(root, text="")
label_status.pack()

# Start the main event loop
root.mainloop()
