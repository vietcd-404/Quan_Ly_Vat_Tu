import tkinter as tk
from database import Database
from service import CRUD
from view import View
from controller import Controller
from login_view import LoginView


if __name__ == "__main__":
    # Cấu hình kết nối
    root = tk.Tk()
    login_view = LoginView(root)
    root.mainloop()

