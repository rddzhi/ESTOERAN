import tkinter as tk
from tkinter import messagebox
import main_app  # Import the main app after successful login
import create_account  # Import the create account module


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")
        self.root.configure(bg="#FFDDFF")  # Cute pink background

        tk.Label(root, text="Welcome!", font=("Comic Sans MS", 16, "bold"), bg="#FFDDFF").pack(pady=10)
        tk.Label(root, text="Username:", font=("Arial", 12), bg="#FFDDFF").pack()

        self.username_entry = tk.Entry(root, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Password:", font=("Arial", 12), bg="#FFDDFF").pack()

        self.password_entry = tk.Entry(root, font=("Arial", 12), show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(root, text="Login", font=("Arial", 12, "bold"), bg="#FFC0CB",
                                      command=self.check_login)
        self.login_button.pack(pady=10)

        self.create_account_button = tk.Button(root, text="Create Account", font=("Arial", 10), bg="#FFB6C1",
                                               command=self.open_create_account)
        self.create_account_button.pack(pady=5)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            with open("users.txt", "r") as f:
                users = [line.strip().split(":") for line in f.readlines()]

            for user, passw in users:
                if username == user and password == passw:
                    messagebox.showinfo("Success", "Login Successful!")
                    self.root.destroy()
                    main_app.start_main_app()  # Start the main app
                    return

            messagebox.showerror("Login Failed", "Incorrect Username or Password!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No accounts found. Please create an account.")

    def open_create_account(self):
        self.root.destroy()
        create_account.start_create_account()  # Navigate to Create Account page


def start_login():
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()


if __name__ == "__main__":
    start_login()
