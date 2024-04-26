import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

from LoginService import LoginService


class TopModule:
    def __init__(self, root):
        self.login_service = LoginService()
        self.root = root
        self.root.geometry("850x600")
        self.root.title("Energy Management")

        # Setting background color
        self.root.configure(bg="#f0f0f0")

        self.currentDir = os.path.dirname(os.path.realpath(__file__))
        self.energy_file_path = os.path.join(self.currentDir, "resources/energy_photo.png")
        self.energy_image = Image.open(self.energy_file_path)
        self.energy_image = self.energy_image.resize((200, 150))
        self.energy_photo = ImageTk.PhotoImage(self.energy_image)

        # Create label for the image
        self.label_image = tk.Label(self.root, image=self.energy_photo)

        # Creating labels with font and background color
        self.label_username = tk.Label(self.root, text="Username:", bg="#f0f0f0", font=("Helvetica", 12))
        self.label_password = tk.Label(self.root, text="Password:", bg="#f0f0f0", font=("Helvetica", 12))

        # Creating entry widgets with font
        self.entry_username = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_password = tk.Entry(self.root, show="*", font=("Helvetica", 12))  # Show '*' for password

        # Creating login button with font and background color
        self.button_login = tk.Button(self.root, text="Login", bg="#4CAF50", fg="white",
                                      font=("Helvetica", 12), command= lambda: self.verify_login(self.entry_username.get(),self.entry_password.get()) )

        self.create_login_page()

    def create_login_page(self):
        # Placing widgets using grid layout
        self.label_image.place(x=340, y=80)
        self.label_username.place(x=250, y=250)
        self.label_password.place(x=250, y=300)
        self.entry_username.place(x=350, y=250)
        self.entry_password.place(x=350, y=300)
        self.button_login.place(x=415, y=375)

    def verify_login(self, username, password):
        success = self.login_service.verify_password(username,password)
        if success:
            print("success")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

