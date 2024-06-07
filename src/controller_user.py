class ControllerUser:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.clear_button.config(command=self.clear_inputs)
        self.view.search_button.config(command=self.search_vat_tu)
        self.view.selected_item_search.bind("<<ComboboxSelected>>", self.on_combobox_value_change)
        self.actual_value = None
        self.data_mapping = {} 
    def create_data(self):
        data = self.view.get_entry()
        maPG = self.view.get_entry()
        tenVatTu = self.view.get_tenVatTu()
        donGia = self.view.get_donGia()
        tienTe = self.view.get_tienTe()
        viTri = self.view.get_viTri()
        soLuong = self.view.get_soLuong()
        donViVatTu = self.view.get_donViVatTu()
        heSo = self.view.get_heSo()
        loaiVatTuId = self.view.get_loaiVatTuId()
        if not maPG:
            self.view.show_message("Mã PG không được để trống.")
            return
        if not tenVatTu:
            self.view.show_message("Tên vật tư không được để trống.")
            return
        if not donGia:
            self.view.show_message("Đơn giá không được để trống.")
            return
        if not tienTe:
            self.view.show_message("Tiền tệ không được để trống.")
            return
        if not viTri:
            self.view.show_message("Vị trí không được để trống.")
            return
        if not soLuong:
            self.view.show_message("Số lượng không được để trống.")
            return
        if not donViVatTu:
            self.view.show_message("Đơn vị vật tư không được để trống.")
            return
        if not heSo:
            self.view.show_message("Hệ số không được để trống.")
            return
        # if not loaiVatTuId:
        #     self.view.show_message("Loại vật tư không được để trống.")
        #     return

        if not self.is_number(donGia):
                self.view.show_message_warning("Vui lòng nhập một giá trị số hợp lệ cho đơn giá.")
                return
        elif not self.is_number(heSo):
               self.view.show_message_warning("Vui lòng nhập một giá trị số hợp lệ cho hệ số.")
               return
        elif not self.is_int(soLuong):
               self.view.show_message_warning("Vui lòng nhập một giá trị số hợp lệ cho số lượng.")
               return
        else:
            self.model.create(
                "Kho_Hang",
                {
                    "MaGP": maPG,
                    "Ten_Vat_Tu": tenVatTu,
                    "Don_Gia": donGia,
                    "Tien_Te": tienTe,
                    "Vi_Tri": viTri,
                    "So_Luong": soLuong,
                    "Don_Vi_Vat_Tu": donViVatTu,
                    "He_So_An_Toan": heSo,
                    "Loai_Vat_Tu_Id": loaiVatTuId
                },
            )
            self.view.show_message("Thêm thành công dữ liệu")
            # self.read_data_kho_hang_search()
            self.show_kho_vat_tu()
            self.clear_inputs()

    # def read_data(self):
    #     results = self.model.read("Kho_Hang")
    #     if results is not None:
    #         self.view.set_tree_data(results)
    #     else:
    #         self.view.show_message("Lỗi dữ liệu")
      


    def update_data(self):
        id = self.view.get_id()
        if not id:
            self.view.show_message_warning("Vui lòng chọn dòng cần sửa.")
        else:
            # id = self.view.get_id()
            maPG = self.view.get_entry()
            tenVatTu = self.view.get_tenVatTu()
            donGia = self.view.get_donGia()
            loaiVatTuId = self.view.get_loaiVatTuId()
            tienTe = self.view.get_tienTe()
            viTri = self.view.get_viTri()
            soLuong = self.view.get_soLuong()
            donViVatTu = self.view.get_donViVatTu()
            heSo = self.view.get_heSo()
            if not maPG:
                self.view.show_message("Mã PG không được để trống.")
                return
            if not tenVatTu:
                self.view.show_message("Tên vật tư không được để trống.")
                return
            if not donGia:
                self.view.show_message("Đơn giá không được để trống.")
                return
            if not tienTe:
                self.view.show_message("Tiền tệ không được để trống.")
                return
            if not viTri:
                self.view.show_message("Vị trí không được để trống.")
                return
            if not soLuong:
                self.view.show_message("Số lượng không được để trống.")
                return
            if not donViVatTu:
                self.view.show_message("Đơn vị vật tư không được để trống.")
                return
            if not heSo:
                self.view.show_message("Hệ số không được để trống.")
                return
            # if not loaiVatTuId:
            #     self.view.show_message("Loại vật tư không được để trống.")
            #     return
            if not self.is_number(donGia):
                self.view.show_message_warning("Vui lòng nhập một giá trị số hợp lệ cho đơn giá.")
                return
            elif not self.is_number(heSo):
               self.view.show_message_warning("Vui lòng nhập một giá trị số hợp lệ cho hệ số.")
               return
            elif not self.is_int(soLuong):
               self.view.show_message_warning("Vui lòng nhập một giá trị số hợp lệ cho số lượng.")
               return
            else:
             self.model.update(
                "Kho_Hang",
                {
                    "MaGP": maPG,
                    "Ten_Vat_Tu": tenVatTu,
                    "Don_Gia": donGia,
                    "Tien_Te": tienTe,
                    "Vi_Tri": viTri,
                    "So_Luong": soLuong,
                    "Don_Vi_Vat_Tu": donViVatTu,
                    "He_So_An_Toan": heSo,
                    "Loai_Vat_Tu_Id": loaiVatTuId
                },
                id,
            )
            self.view.show_message("Sửa thành công")
            # self.read_data_kho_hang_search()
            self.show_kho_vat_tu()
            self.clear_inputs()

    def delete_data(self):
        id = self.view.get_id()
        if not id:
            self.view.show_message_warning("Vui lòng chọn dòng cần xóa.")
        else:
            confirm = self.view.show_confirm(
                "Bạn có chắc chắn muốn xóa dòng này không?"
            )
        if confirm:
            self.model.delete("Kho_Hang", id)
            self.view.show_message("Xóa thành công")
            # self.read_data_kho_hang_search()\\
            self.show_kho_vat_tu()
            self.view.clear_all_inputs()

    def clear_inputs(self):
        self.view.clear_all_inputs()
        self.actual_value = None
        self.show_kho_vat_tu()
    
    def on_combobox_value_change(self, event):
        selected_display_value = self.view.selected_item_search.get()
        if selected_display_value == "Tất cả":
            self.actual_value = None  # Set actual value to None or any appropriate value for "Tất cả"
            print("Selected Display Value: Tất cả")
            # Perform any actions needed when "Tất cả" is selected
            # For example, show all items in the list
            
        elif selected_display_value in self.data_mapping:
                self.actual_value = self.data_mapping[selected_display_value]
                print(f"Selected Display Value: {selected_display_value}, Actual Value: {self.actual_value}")
                self.show_kho_vat_tu()
        else:
            print("Selected value not found in mapping.")
               

         

        # try:
        #     # Lấy giá trị đã chọn từ combobox
        #     selected_value = self.view.selected_item_search.get()
            
        
        #     print(f"id là {selected_value}")
        #     self.show_kho_vat_tu(selected_value)
        # except Exception as e:
        #     self.view.show_message(f"Error fetching data: {str(e)}")

    def read_data_kho_hang_search(self):
       results = self.model.read("Loai_Vat_Tu")
       if results is not None:
            self.view.selected_item_search['values'] = ()
            self.data_mapping = {}  # Clear the existing mapping

            # Update the combobox with new values and store the mapping
            display_values = []
            for row in results:
                display_values.append(row[1])  # Display row[1] in the combobox
                self.data_mapping[row[1]] = row[0]  # Map row[1] to row[0]

            self.view.selected_item_search['values'] = display_values
           
                
       else:
            self.view.show_message("Lỗi dữ liệu")   
       
    
    def search_vat_tu(self):
        maPG = self.view.get_entry()
        if not maPG:
            self.view.show_message_warning("Vui lòng nhập mã vật tư để tìm kiếm.")
            return
        else:
            print(f"Mã tìm kiếm: {maPG}")
            self.show_kho_vat_tu()
            self.view.clear_all_inputs()

    def show_kho_vat_tu(self):
       try:
        id = self.actual_value
        ma_gp = self.view.get_entry()
        print(f"Mã tìm kiếm: {ma_gp}")
        kho_vat_tu_data = self.model.get_kho_vat_tu(id, ma_gp)
        if kho_vat_tu_data:
            self.view.set_tree_data(kho_vat_tu_data)
        else:
            self.view.show_message("Không có dữ liệu cho kho hàng này")
       except Exception as e:
        self.view.show_message(f"Lỗi khi truy vấn dữ liệu: {str(e)}")
        # try:
        #     kho_vat_tu_data = self.model.get_kho_vat_tu(id)
        #     self.view.render_kho_vat_tu(kho_vat_tu_data)
        # except Exception as e:
        #     self.view.show_message(f"Error fetching data: {str(e)}")  

    def is_number(self, s):
     try:
        float(s)
        return True
     except ValueError:
        return False
     
    def is_int(self, s):
     try:
        int(s)
        return True
     except ValueError:
        return False

