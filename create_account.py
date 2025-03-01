import tkinter as tk
from tkinter import messagebox
import login  # Redirect to login after account creation


def start_create_account():
    root = tk.Tk()
    app = CreateAccountUI(root)
    root.mainloop()


class CreateAccountUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account")
        self.root.geometry("400x300")
        self.root.configure(bg="#FFDDFF")

        tk.Label(root, text="Create a New Account", font=("Comic Sans MS", 14, "bold"), bg="#FFDDFF").pack(pady=10)

        tk.Label(root, text="New Username:", bg="#FFDDFF").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        tk.Label(root, text="New Password:", bg="#FFDDFF").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.create_button = tk.Button(root, text="Create Account", font=("Arial", 12, "bold"), bg="#FFC0CB",
                                       command=self.create_account)
        self.create_button.pack(pady=10)

        self.back_button = tk.Button(root, text="Back to Login", font=("Arial", 10), bg="#FFB6C1",
                                     command=self.back_to_login)
        self.back_button.pack()

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            with open("users.txt", "a") as f:
                f.write(f"{username}:{password}\n")
            messagebox.showinfo("Success", "Account Created! Please log in.")
            self.root.destroy()
            login.start_login()
        except Exception as e:
            messagebox.showerror("Error", f"Could not create account: {e}")

    def back_to_login(self):
        self.root.destroy()
        login.start_login()


if __name__ == "__main__":
    start_create_account()
