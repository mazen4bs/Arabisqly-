import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk,Window
from Connect_Database import *

cursor , conn = connect_to_database(DRIVER,SERVER,DATABASE)

class LoginPage:
    def __init__(self):
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.content = ttk.Frame(main_window)
        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self.content, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.content , textvariable=self.username_var)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.content, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.content,textvariable=self.password_var, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.content, text="Login", command=self.login)
        self.login_button.pack(pady=5)

    def login(self):
        username = self.username_var.get()
        password = self.password_entry.get()
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            self.hide_frame()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            self.username_entry.delete(0,'end')
            self.password_entry.delete(0,'end')


    def show_frame(self):
        self.content.pack(fill="both",expand=True)

    def hide_frame(self):
        self.content.pack_forget()

main_window = Window(themename='darkly')
main_window.geometry("800x600")
main_window.title("Arabisqly")
login_page = LoginPage()


