CREATE TABLE `log_book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama_user` varchar(255) DEFAULT NULL,
  `nama_kegiatan` varchar(255) DEFAULT NULL,
  `durasi` int DEFAULT NULL,
  `tanggal_input` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO your_db_name.log_book (nama_user,nama_kegiatan,durasi,tanggal_input) VALUES
	 ('adi','memasak',90,'2025-09-28'),
	 ('budi','menggoreng',90,'2025-09-28'),
	 ('dedi','menggoreng',90,'2025-09-28'),
	 ('adi','memasak',90,'2025-09-27'),
	 ('budi','menggoreng',90,'2025-09-27'),
	 ('ceci','memasak',90,'2025-09-27'),
	 ('dedi','menggoreng',90,'2025-09-27');
