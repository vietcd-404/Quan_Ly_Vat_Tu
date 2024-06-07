import pyodbc

class Model:
    def __init__(self):
        try:
            self.conn = pyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=localhost,1433;'
                'DATABASE=QUAN_LY_KHO_HANG;'
                'UID=sa;'
                'PWD=1234;'
            )
            self.cursor = self.conn.cursor()
            print("Connected to the database successfully")
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")

    def get_user_list(self):
        # Lấy danh sách người dùng tương tác với giao diện để phân loại Admin hay User
        self.cursor.execute('Select * from Users_Admin UNION Select * from Users_User')
        user_list = self.cursor.fetchall()
        return user_list