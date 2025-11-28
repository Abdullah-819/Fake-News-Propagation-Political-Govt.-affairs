import customtkinter as ctk
from gui.login import LoginPage
from backend.db.connection import create_tables

# Setup GUI theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Fake News Propagation Simulator")
        self.geometry("900x600")

        create_tables()  # optional, creates tables if not exists

        LoginPage(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
