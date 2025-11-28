import customtkinter as ctk
from backend.db.connection import get_connection

class LoginPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        ctk.CTkLabel(self, text="Login", font=("Arial", 28)).pack(pady=20)

        self.username = ctk.CTkEntry(self, placeholder_text="Username", width=250)
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=250)
        self.password.pack(pady=10)

        ctk.CTkButton(self, text="Login", command=self.login_user).pack(pady=20)
        ctk.CTkButton(self, text="Create Account",
                      fg_color="gray", command=self.go_register).pack()

        self.message_label = ctk.CTkLabel(self, text="", text_color="red")
        self.message_label.pack(pady=10)

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
            # Lazy import to avoid circular dependency
            from gui.dashboard import DashboardPage
            DashboardPage(self.master, username=user)
        else:
            self.message_label.configure(text="Invalid username or password!")

    def go_register(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        # Lazy import to avoid circular dependency
        from gui.register import RegisterPage
        RegisterPage(self.master)
