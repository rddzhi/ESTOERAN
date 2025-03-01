import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk

class CuteRestaurantUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🍰 Kawaii Cafe Reservation 💖")
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.root.configure(bg="#FFE4E1")

        # Load Background Image
        try:
            self.bg_image = Image.open("yaemiko.png")
            self.bg_image = self.bg_image.resize((self.screen_width, self.screen_height), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = tk.Label(root, image=self.bg_photo)
            self.bg_label.place(relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error loading background image: {e}")
            self.bg_label = tk.Label(root, text="🌸 Background 🌸", bg="#FFE4E1", font=("Comic Sans MS", 14, "bold"))
            self.bg_label.place(relwidth=1, relheight=1)

        # Header with Clickable Buttons and Logo
        self.header_frame = tk.Frame(root, bg="#FFB6C1")
        self.header_frame.pack(fill=tk.X)

        # Restaurant Logo
        self.logo_label = tk.Label(self.header_frame, text="🍽️ Kawaii Cafe", font=("Comic Sans MS", 14, "bold"), bg="#FFB6C1", fg="white")
        self.logo_label.pack(side=tk.LEFT, padx=10, pady=5)

        # Header Buttons
        self.create_header_button("🍰 Menu", self.open_menu)
        self.create_header_button("ℹ️ About Us", self.open_about_us)
        self.create_header_button("💳 Billing", self.open_billing)
        self.create_header_button("☎️ Contact Support", self.open_contact_support)
        self.create_header_button("👤 Account", self.open_account)
        self.create_header_button("🚪 Logout", self.logout)

        # Enlarged & Perfectly Centered Reservation Frame
        self.window = tk.Frame(root, bg="#FFF0F5", bd=4, relief=tk.RIDGE)
        self.window.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        # Title Bar
        self.title_bar = tk.Label(self.window, text="🍡 Table Reservation 🍡", bg="#FFB6C1",
                                  font=("Comic Sans MS", 14, "bold"), fg="white", anchor="center")
        self.title_bar.pack(fill=tk.X)

        # Main Container (Uses Grid Layout)
        self.main_frame = tk.Frame(self.window, bg="#FFF0F5")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Table Selection (Left Side)
        self.table_frame = tk.Frame(self.main_frame, bg="#FFF0F5")
        self.table_frame.grid(row=0, column=0, padx=10, pady=10)

        self.tables = {}
        for row in range(3):
            for col in range(3):
                table_num = row * 3 + col + 1
                btn = tk.Button(self.table_frame, text=f"🍩 Table {table_num} 🍩", font=("Comic Sans MS", 10),
                                width=12, height=2, bg="#FFD1DC", relief=tk.GROOVE,
                                activebackground="#FF69B4",
                                command=lambda num=table_num: self.select_table(num))
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.tables[table_num] = btn

        # Customer Details & Calendar (Center)
        self.details_frame = tk.Frame(self.main_frame, bg="#FFF0F5")
        self.details_frame.grid(row=0, column=1, padx=10, pady=10)

        self.name_label = tk.Label(self.details_frame, text="💖 Name:", font=("Comic Sans MS", 12), bg="#FFF0F5")
        self.name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = tk.Entry(self.details_frame, font=("Comic Sans MS", 12), bd=2, relief=tk.GROOVE)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.contact_label = tk.Label(self.details_frame, text="📞 Contact:", font=("Comic Sans MS", 12), bg="#FFF0F5")
        self.contact_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.contact_entry = tk.Entry(self.details_frame, font=("Comic Sans MS", 12), bd=2, relief=tk.GROOVE)
        self.contact_entry.grid(row=1, column=1, padx=5, pady=5)

        self.date_label = tk.Label(self.details_frame, text="📅 Select Date:", font=("Comic Sans MS", 12), bg="#FFF0F5")
        self.date_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.calendar = Calendar(self.details_frame, selectmode="day", date_pattern="yyyy-mm-dd")
        self.calendar.grid(row=2, column=1, padx=5, pady=5)

        # Confirm Button
        self.confirm_button = tk.Button(self.window, text="💌 Confirm Reservation 💌", font=("Comic Sans MS", 12, "bold"),
                                        bg="#FF69B4", fg="white", relief=tk.RAISED,
                                        activebackground="#FF1493", command=self.confirm_reservation)
        self.confirm_button.pack(pady=15)

        self.selected_table = None  # Store selected table

    def create_header_button(self, name, command):
        btn = tk.Button(self.header_frame, text=name, font=("Comic Sans MS", 10), bg="#FFB6C1", fg="white",
                        relief=tk.FLAT, activebackground="#FF69B4", command=command)
        btn.pack(side=tk.LEFT, padx=10, pady=5)

    def select_table(self, table_num):
        if self.selected_table:
            self.tables[self.selected_table].configure(bg="#FFD1DC")
        self.selected_table = table_num
        self.tables[table_num].configure(bg="#FF69B4")

    def confirm_reservation(self):
        messagebox.showinfo("🎀 Reservation Confirmed 🎀", "Reservation successful!")

    def open_window(self, title):
        window = tk.Toplevel(self.root)
        window.title(title)
        window.geometry("400x300")
        window.configure(bg="#FFD1DC")
        label = tk.Label(window, text=f"{title} Window", font=("Comic Sans MS", 14), bg="#FFD1DC")
        label.pack(pady=10)

    def open_menu(self):
        self.open_window("🍰 Menu")

    def open_about_us(self):
        self.open_window("ℹ️ About Us")

    def open_billing(self):
        self.open_window("💰 Billing")

    def open_contact_support(self):
        self.open_window("☎️ Contact Support")

    def open_account(self):
        self.open_window("👤 Account")

    def logout(self):
        if messagebox.askyesno("Logout Confirmation", "Do you really want to log out? 💖"):
            self.root.destroy()

# Function to start the main app
if __name__ == "__main__":
    root = tk.Tk()
    app = CuteRestaurantUI(root)
    root.mainloop()
