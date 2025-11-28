import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image
from backend.db.connection import get_connection

class LoginPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        # Load original image
        self.original_image = Image.open("assets/login_bg.jpg")

        # Create CTkLabel for background
        self.bg_label = ctk.CTkLabel(self, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Bind resize event
        self.master.bind("<Configure>", self.resize_bg)

        # --- Widgets ---
        self.username = ctk.CTkEntry(self, placeholder_text="Username", width=250)
        self.username.place(relx=0.5, rely=0.4, anchor="center")

        self.password = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=250)
        self.password.place(relx=0.5, rely=0.5, anchor="center")

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login_user)
        self.login_button.place(relx=0.5, rely=0.6, anchor="center")

        self.register_button = ctk.CTkButton(self, text="Create Account",
                                             fg_color="gray", command=self.go_register)
        self.register_button.place(relx=0.5, rely=0.7, anchor="center")

        self.message_label = ctk.CTkLabel(self, text="", text_color="red")
        self.message_label.place(relx=0.5, rely=0.8, anchor="center")

    def resize_bg(self, event):
        # Resize the original image to match window size
        width = event.width
        height = event.height
        resized_image = self.original_image.resize((width, height))
        self.bg_image = CTkImage(light_image=resized_image, dark_image=resized_image, size=(width, height))
        self.bg_label.configure(image=self.bg_image)

    def login_user(self):
        user = self.username.get()
        pwd = self.password.get()

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user, pwd))
        result = cursor.fetchone()
        conn.close()

        if result:
            for widget in self.master.winfo_children():
                widget.destroy()
            from gui.dashboard import DashboardPage
            DashboardPage(self.master, username=user)
        else:
            self.message_label.configure(text="Invalid username or password!")

    def go_register(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        from gui.register import RegisterPage
        RegisterPage(self.master)
