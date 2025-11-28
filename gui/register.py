import customtkinter as ctk
from backend.db.connection import get_connection

class RegisterPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        ctk.CTkLabel(self, text="Create Account", font=("Arial", 26)).pack(pady=20)

        # Username
        self.username = ctk.CTkEntry(self, placeholder_text="Username", width=250)
        self.username.pack(pady=10)

        # Email
        self.email = ctk.CTkEntry(self, placeholder_text="Email", width=250)
        self.email.pack(pady=10)

        # Password
        self.password = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=250)
        self.password.pack(pady=10)

        # Role
        self.role = ctk.CTkEntry(self, placeholder_text="Role (citizen/politician/bot)", width=250)
        self.role.pack(pady=10)

        # Buttons
        ctk.CTkButton(self, text="Register", command=self.register_user).pack(pady=20)
        ctk.CTkButton(self, text="Back to Login",
                      fg_color="gray", command=self.go_login).pack()

        self.message_label = ctk.CTkLabel(self, text="", text_color="red")
        self.message_label.pack(pady=10)

    def register_user(self):
        user = self.username.get()
        email = self.email.get()
        pwd = self.password.get()
        role = self.role.get()

        if not user or not email or not pwd or not role:
            self.message_label.configure(text="All fields are required!")
            return

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)",
                (user, email, pwd, role)
            )
            conn.commit()
            self.message_label.configure(text="Account created successfully!", text_color="green")
        except Exception as e:
            print(e)
            self.message_label.configure(text="Username or email already exists!", text_color="red")
        finally:
            conn.close()

    def go_login(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        from gui.login import LoginPage
        LoginPage(self.master)
