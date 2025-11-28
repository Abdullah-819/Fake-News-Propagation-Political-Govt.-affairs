import customtkinter as ctk

class DashboardPage(ctk.CTkFrame):
    def __init__(self, master, username=""):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        ctk.CTkLabel(self, text="Dashboard", font=("Arial", 28)).pack(pady=20)
        ctk.CTkLabel(self, text=f"Welcome, {username}!", font=("Arial", 16)).pack(pady=10)
        ctk.CTkButton(self, text="Add Fake News", width=200).pack(pady=10)
        ctk.CTkButton(self, text="Run Simulation", width=200).pack(pady=10)
        ctk.CTkButton(self, text="View Analytics", width=200).pack(pady=10)
