import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font
import pandas as pd
import os

class ViewUser:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý kho hàng")
        self.label_header = ttk.Label(self.root, text="QUẢN LÝ KHO HÀNG USER", foreground='RED',
                                      font=font.Font(family="Helvetica", size=12, weight="bold"))
        self.label_header.place(relx=0.5, rely=0.5, anchor='center')
        self.label_header.lift()
        

        window_width = 1350
        window_height = 800
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.actual_value = None
        self.root.option_add("*Font", "Arial 12")
        # Hiển thị cửa sổ ở giữa màn hình


        self.label = ttk.Label(root, text="Mã GP:")
        self.label.grid(row=1, column=0, padx=(10, 5), pady=10, sticky="e")  # Đặt tiêu đề ở bên phải và tạo một khoảng cách nhỏ ở bên phải
        self.entry = ttk.Entry(root)
        self.entry.grid(row=1, column=1, padx=(5, 10), pady=10, sticky="w")  # Đặt ô input ở bên trái và tạo một khoảng cách nhỏ ở bên trái


        self.label_selected_item_search = ttk.Label(root, text="Tìm kho:")
        self.label_selected_item_search.grid(row=2, column=0, padx=(10, 5), pady=10, sticky="e")
        self.selected_item_search = ttk.Combobox(root)
        self.selected_item_search.grid(row=2, column=1, padx=10, pady=10)
       


     

        self.search_button = ttk.Button(root, text="Tìm kiếm")
        self.search_button.grid(row=3, column=0, padx=10, pady=10)
        
        self.clear_button = ttk.Button(root, text="Clear dữ liệu")
        self.clear_button.grid(row=3, column=1, padx=10, pady=10)

        self.export_button = ttk.Button(root, text="Xuất Excel", command=self.export_to_excel)
        self.export_button.grid(row=3, column=2, padx=10, pady=10)

        self.tree = ttk.Treeview(root, show='headings', height=40)
        # self.tree.place(x=25, y=350, width=root.winfo_width() - 50)
        self.tree["columns"] = (
            "STT",
            "Ten_Kho",
            "MaGP",
            "Ten_Vat_Tu",
            "Don_Gia",
            "Tien_Te",
            "Vi_Tri",
            "So_Luong",
            "Don_Vi_Vat_Tu",
            "Phan_Loai",
            "He_So_An_Toan",
            "Gia_Tri",
        )
        self.tree.place(x=25, y=450, width=1295, height=320)
        self.tree.column("STT", width=50)
        self.tree.column("Ten_Kho", width=70)
        self.tree.column("MaGP", anchor='c', width=90)
        self.tree.column("Ten_Vat_Tu", anchor='c', width=310)
        self.tree.column("Don_Gia", anchor='c', width=100)
        self.tree.column("Tien_Te", anchor='c', width=100)
        self.tree.column("Vi_Tri", anchor='c', width=100)
        self.tree.column("So_Luong", anchor='c', width=100)
        self.tree.column("Don_Vi_Vat_Tu", anchor='c', width=60)
        self.tree.column("Phan_Loai", anchor='c', width=100)
        self.tree.column("He_So_An_Toan", anchor='c', width=100)
        self.tree.column("Gia_Tri", anchor='c', width=100)
    
        self.tree.heading("STT", text="STT", anchor='c')
        self.tree.heading("Ten_Kho", text="Tên kho", anchor='c')
        self.tree.heading("MaGP", text="Mã Vật Tư", anchor='c')
        self.tree.heading("Ten_Vat_Tu", text="Tên Vật Tư", anchor='c')
        self.tree.heading("Don_Gia", text="Đơn Giá", anchor='c')
        self.tree.heading("Tien_Te", text="Tiền Tệ", anchor='c')
        self.tree.heading("Vi_Tri", text="Vị Trí", anchor='c')
        self.tree.heading("So_Luong", text="Số Lượng", anchor='c')
        self.tree.heading("Don_Vi_Vat_Tu", text="Đơn Vị Vật Tư", anchor='c')
        self.tree.heading("Phan_Loai", text="Phân Loại", anchor='c')
        self.tree.heading("He_So_An_Toan", text="Hệ Số An Toàn", anchor='c')
        self.tree.heading("Gia_Tri", text="Giá Trị", anchor='c')

        # self.tree.grid(row=200, column=0, columnspan=20, padx=10, pady=20)
        # self.tree.bind("<ButtonRelease-1>", self.on_tree_select)
        # self.on_read_button_click()'
        # self.clear_inputs()
        # self.selected_item_combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)
        # self.selected_item_combobox.bind("<<ComboboxSelected>>", self.on_combobox_select_value)
        # self.selected_item_search.bind("<<ComboboxSelected>>", self.on_combobox_value_change)

        self.data_mapping = {} 
        self.data_search = {}
        self.data = [] 
    def export_to_excel(self):
    # Define column headers
        columns = ['STT', 'Tên kho', 'Mã Vật Tư', 'Tên Vật Tư', 'Đơn Giá', 'Tiền Tệ', 'Vị Trí', 'Số Lượng', 
                'Đơn Vị Vật Tư', 'Phân Loại', 'Hệ Số An Toàn', 'Giá Trị']

        # Ensure self.data is properly formatted and not empty
        if not self.data:
            print("No data to export")
            return

        # Convert data to a pandas DataFrame
        df = pd.DataFrame(self.data, columns=columns)

        # Specify the initial file path for the Excel file
        excel_file_path = r'C:\Users\PC\Downloads\PythonTest\file\tree_data.xlsx'

        # If the file already exists, add an index to create a unique file name
        index = 1
        while os.path.exists(excel_file_path):
            excel_file_path = f'C:\\Users\\PC\\Downloads\\PythonTest\\file\\tree_data_{index}.xlsx'
            index += 1

        # Export DataFrame to Excel
        df.to_excel(excel_file_path, index=False)

        print(f"Data has been exported to '{excel_file_path}'")
        messagebox.showinfo('Thành công' ,'Xuất file thành công')


    def get_entry(self):
        return self.entry.get()

    def get_id(self):
        return self.entry_id.get()

    def get_tenVatTu(self):
        return self.entry_tenVatTu.get()

    def get_donGia(self):
        return self.entry_donGia.get()
        # try:
        #     donGia = float(self.entry_donGia.get())
        #     return donGia
        # except ValueError:
        #     messagebox.showerror("Lỗi", "Vui lòng nhập một giá trị số hợp lệ cho Đơn giá.")
        #     return None

    def get_tienTe(self):
        return self.entry_donVi.get()

    def get_viTri(self):
        return self.entry_viTri.get()

    def get_soLuong(self):
        return self.entry_soLuong.get()
        # try:
        #     soLuong = int(self.entry_soLuong.get())
        #     return soLuong
        # except ValueError:
        #     messagebox.showerror("Lỗi", "Vui lòng nhập một giá trị số hợp lệ cho số lượng.")
        #     return None

    def get_donViVatTu(self):
        return self.entry_donViVatTu.get()
    
    
    # Tìm kiếm ID tương ứng của loại vật tư trong dữ liệu
        # loai_vat_tu_id = None
        # for row in self.loai_vat_tu_data:  # Giả sử self.loai_vat_tu_data là danh sách các bản ghi từ cơ sở dữ liệu
        #     if row[1] == selected_loai_vat_tu:  # Giả sử loại vật tư nằm ở cột thứ hai của mỗi bản ghi
        #         loai_vat_tu_id = row[0]  # Giả sử ID loại vật tư nằm ở cột đầu tiên của mỗi bản ghi
        #         break
        
        # return loai_vat_tu_id

    def get_heSo(self):
        return self.entry_heSo.get()
        # try:
        #     heSo = float(self.entry_heSo.get())
        #     return heSo
        # except ValueError:
        #     messagebox.showerror("Lỗi", "Vui lòng nhập một giá trị số hợp lệ cho Đơn giá.")
        #     return None

    def set_text(self, text):
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, text)

    def set_tree_data(self, rows):
        # Xóa các hàng hiện có
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Thêm dữ liệu mới vào Treeview
        # for row in rows:
        #     self.tree.insert('', tk.END, values=row)
        for row in rows:
            # Convert row elements to string to avoid displaying None
            formatted_row = [str(element) if element is not None else '' for element in row]
            don_gia = float(formatted_row[4]) if formatted_row[4] else 0  # Assuming "Đơn Giá" is in the 5th column
            so_luong = float(formatted_row[7]) if formatted_row[7] else 0  # Assuming "Số Lượng" is in the 8th column
            gia_tri = don_gia * so_luong
            print(f"Selected Display Value: {formatted_row}")
            # self.tree.set(self.tree.get_children()[11], "Gia_Tri", gia_tri)

        # Append calculated "Giá Trị" to the row
            # formatted_row.append(gia_tri)
            inserted_row =  self.tree.insert('', tk.END, values=formatted_row)
            self.tree.set(inserted_row, "Gia_Tri", gia_tri)
            self.data.append(formatted_row)

      

    def show_message(self, message):
        messagebox.showinfo("Info", message)

    def show_message_warning(self, message):
        messagebox.showwarning("Warning", message)

    def show_confirm(self, message):
        return messagebox.askyesno("Xác nhận", message)

    def on_tree_select(self, event):
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, 'values')
        if values:  # Ensure values is not empty
            stt = values[0]
            self.entry.delete(0, tk.END)
            self.entry.insert(0, values[2]) 
            # MaGP is the second colum
            tt =self.on_combobox_select_value(values[1]) 
            self.actual_value = tt
            print(f"Selected Display Value: {values[1]}, Actual Value: {self.actual_value}")


      
            self.selected_item_search.set('')

       

   

    def clear_all_inputs(self):
        # Xóa hết nội dung hiện tại trong các ô nhập liệu
        self.entry.delete(0, tk.END)
        self.selected_item_search.set('')
        selected_items = self.tree.selection()
        if selected_items:
           for selected_item in selected_items:
            self.tree.selection_remove(selected_item)
        # self.selected_item_combobox[0]
        # self.selected_item_combobox.set('')
        self.actual_value = None
        self.value_id = None

    def on_combobox_select(self, event):
        selected_display_value = self.selected_item_combobox.get()
        if selected_display_value in self.data_mapping:
            self.actual_value = self.data_mapping[selected_display_value]
            print(f"Selected Display Value: {selected_display_value}, Actual Value: {self.actual_value}")
        else:
            print("Selected value not found in mapping.")   

    def on_combobox_select_value(self, value):
        if value in self.data_mapping:
            actual_value = self.data_mapping[value]
            print(f"Selected Display Value: {value}, Actual Value: {actual_value}")
        else:
            print("Selected value not found in mapping.") 
        return actual_value                
          

    def get_loaiVatTuId(self):
        return self.actual_value
 
    def get_vauleId(self):
        return self.value_id
    
    def render_kho_vat_tu(self, kho_vat_tu_data):
        for item in kho_vat_tu_data:
            self.tree.insert('', 'end', values=item)