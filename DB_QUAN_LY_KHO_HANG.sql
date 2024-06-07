SELECT lvt.ten_kho_vat_tu as Ten_Kho , kh.* FROM Kho_Hang kh 
join Loai_Vat_Tu lvt on lvt.id  = kh.Loai_Vat_Tu_Id 
WHERE lvt.id  = 1


-- QUAN_LY_KHO_HANG.dbo.Kho_Hang definition

-- Drop table

-- DROP TABLE QUAN_LY_KHO_HANG.dbo.Kho_Hang;
---Tạo mới db
CREATE Database QUAN_LY_KHO_HANG
--Sử dụng db
use QUAN_LY_KHO_HANG



CREATE TABLE Kho_Hang (
	STT int IDENTITY(0,1) NOT NULL,
	MaGP varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	Ten_Vat_Tu varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	Don_Gia numeric(38,0) NULL,
	Tien_Te varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	Vi_Tri varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	So_Luong int NULL,
	Don_Vi_Vat_Tu varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	Phan_Loai varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	He_So_An_Toan numeric(38,0) NULL,
	Gia_Tri varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
);

INSERT INTO QUAN_LY_KHO_HANG.dbo.Kho_Hang 
(MaGP, Ten_Vat_Tu, Don_Gia, Tien_Te, Vi_Tri, So_Luong, Don_Vi_Vat_Tu, Phan_Loai, He_So_An_Toan, Loai_Vat_Tu_Id) 
VALUES 
('GP001', N'Ví dụ 1', 10000, 'VND', N'Kệ A1', 50, 'Cái', 'Loại 1', 0.8, 1),
('GP002', N'Ví dụ 2', 15000, 'VND', N'Kệ A2', 30, 'Cái', 'Loại 2', 0.9, 2),
('GP003', N'Ví dụ 3', 20000, 'VND', N'Kệ B1', 40, 'Cái', 'Loại 1', 0.7, 1);

CREATE TABLE Loai_Vat_Tu (
	id int NOT NULL,
	Ten_Kho_Vat_Tu varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);

INSERT INTO QUAN_LY_KHO_HANG.dbo.Loai_Vat_Tu (id ,Ten_Kho_Vat_Tu) VALUES(1,N'Co Khi');
INSERT INTO QUAN_LY_KHO_HANG.dbo.Loai_Vat_Tu (id ,Ten_Kho_Vat_Tu) VALUES(2,N'Hoa Chat');
INSERT INTO QUAN_LY_KHO_HANG.dbo.Loai_Vat_Tu (id ,Ten_Kho_Vat_Tu) VALUES(3,N'Dien');



CREATE TABLE Users_Admin (
	user_type varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	username varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	pass_word varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);

INSERT INTO QUAN_LY_KHO_HANG.dbo.Users_Admin (user_type, username, pass_word) VALUES('Admin', 'admin', '123');


CREATE TABLE Users_User (
	user_type varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	username varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	pass_word varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);

INSERT INTO QUAN_LY_KHO_HANG.dbo.Users_User (user_type, username, pass_word) VALUES('User', 'user', '123');



