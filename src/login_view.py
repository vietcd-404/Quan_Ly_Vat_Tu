import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import font
from database import Database
from service import CRUD
from view import View
from view_user import ViewUser
from controller import Controller
from model import Model
from controller_user import ControllerUser

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        
        # Center the window on the screen
        window_width = 400
        window_height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Title Label
        self.label_header = ttk.Label(self.root, text="Đăng nhập", foreground='RED',
                                      font=font.Font(family="Helvetica", size=16, weight="bold"))
        # self.label_header.pack(pady=20)
        
        # Username Label and Entry
        self.label_username = ttk.Label(root, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = ttk.Entry(root)
        self.entry_username.pack(pady=5)
        
        # Password Label and Entry
        self.label_password = ttk.Label(root, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = ttk.Entry(root, show="*")
        self.entry_password.pack(pady=5)

        self.Loai = tk.StringVar(value='User')

# Create the Radiobuttons
        self.rd1 = ttk.Radiobutton(root, text="Admin", variable=self.Loai, value='Admin')
        self.rd1.pack(pady=5)
        self.rd2 = ttk.Radiobutton(root, text="User", variable=self.Loai, value='User')
        self.rd2.pack(pady=5)
        # Login Button
        self.button_login = ttk.Button(root, text="Login", command=self.login)
        self.button_login.pack(pady=40)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        user_type = self.Loai.get()
        self.model = Model()
        # Here you would handle the login logic
        print(f"Username: {username}, Password: {password}")
        found = False
        # self.redirect_to_main_view()

        for item in self.model.get_user_list():
            if item[0] == user_type == 'Admin' and item[1] == username and item[2] == password:
                # Nếu người dùng đăng nhập có trong list Admin sẽ gọi giao diện View dành cho Admin
                app = self.redirect_to_main_view()
                # app.mainloop()
                found = True
                break
            elif item[0] == user_type == 'User' and item[1] == username and item[2] == password:
                # Nếu người dùng đăng nhập có trong list User sẽ gọi giao diện View dành cho User
                app = self.redirect_to_main_view_user()
                # app.mainloop()
                found = True
                break
        # Nếu duyệt không có người dùng trong hệ thống, biến found sẽ là false. Gửi thông báo đăng nhập sai và gợi ý tên đăng nhập
        if not found:
            messagebox.showinfo('Thông báo', 'Thông tin đăng nhập sai. '
                                            )

    def redirect_to_main_view(self):
        self.root.destroy()  # Destroy the login window
        main_root = tk.Tk()  # Create a new main window
        main_view = View(main_root)
        db = Database(server='localhost,1433', database='QUAN_LY_KHO_HANG', username='sa', password='1234')
        db.connect()
        # root = tk.Tk()
        # view = View(root)
        model = CRUD(db)
        controller = Controller(model, main_view)
        controller.read_data_kho_hang()
        controller.read_data_kho_hang_search()
        controller.show_kho_vat_tu()
        main_root.mainloop()
        # root.mainloop()
        db.close()  # Instantiate the main view
        main_root.mainloop() 
     
    def redirect_to_main_view_user(self):
        self.root.destroy()  # Destroy the login window
        main_root = tk.Tk()  # Create a new main window
        main_view = ViewUser(main_root)
        db = Database(server='localhost,1433', database='QUAN_LY_KHO_HANG', username='sa', password='1234')
        db.connect()
        # root = tk.Tk()
        # view = View(root)
        model = CRUD(db)
        controller = ControllerUser(model, main_view)
        controller.read_data_kho_hang_search()
        controller.show_kho_vat_tu()
        main_root.mainloop()
        # root.mainloop()
        db.close()  # Instantiate the main view
        main_root.mainloop()     