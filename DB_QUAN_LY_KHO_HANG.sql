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


CREATE TABLE Loai_Vat_Tu (
	id int IDENTITY(0,1) NOT NULL,
	Ten_Kho_Vat_Tu varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);


CREATE TABLE Users_Admin (
	user_type varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	username varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	pass_word varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);


CREATE TABLE Users_User (
	user_type varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	username varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	pass_word varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);

