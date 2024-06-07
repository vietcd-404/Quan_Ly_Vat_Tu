class CRUD:
    def __init__(self, db):
        self.db = db

    def create(self, table, data):
        columns = ", ".join(data.keys())
        values = ", ".join(f"'{v}'" for v in data.values())
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        self.execute(query)

    def read(self, table, conditions=None):
        query = f"SELECT * FROM {table}"
        if conditions:
            query += f" WHERE {' AND '.join(conditions)}"
        return self.execute(query, fetch=True)

    def update(self, table, data, stt):
        updates = ", ".join(f"{k}='{v}'" for k, v in data.items())
        query = f"UPDATE {table} SET {updates} WHERE STT = {stt}"
        self.execute(query)

    def delete(self, table, conditions):
        query = f"DELETE FROM {table} WHERE STT = {conditions}"
        self.execute(query)

    def join(self, table1, table2, join_condition, columns="*", join_type="INNER", conditions=None):
        query = f"SELECT {columns} FROM {table1} {join_type} JOIN {table2} ON {join_condition}"
        if conditions:
            query += f" WHERE {' AND '.join(conditions)}"
        return self.execute(query, fetch=True)    


    def execute(self, query, fetch=False):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(query)
            if fetch:
                results = cursor.fetchall()
                self.db.connection.commit()
                return results
            self.db.connection.commit()
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
        
    def get_kho_vat_tu(self, loai_vat_tu_id, ma_gp):
        query = f"""
        SELECT  kh.STT , lvt.ten_kho_vat_tu , kh.MaGP  ,  kh.Ten_Vat_Tu , kh.Don_Gia ,kh.Tien_Te , kh.Vi_Tri ,
          kh.So_Luong , kh.Don_Vi_Vat_Tu , kh.Phan_Loai , kh.He_So_An_Toan, kh.Gia_Tri
        FROM Kho_Hang kh 
        JOIN Loai_Vat_Tu lvt ON lvt.id = kh.Loai_Vat_Tu_Id 
        """
        if loai_vat_tu_id:
          query += f" WHERE lvt.id = '{loai_vat_tu_id}'"
        if ma_gp:
          query += f" AND kh.MaGP = '{ma_gp}'"
        return self.execute(query, fetch=True)