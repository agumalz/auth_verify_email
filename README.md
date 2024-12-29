# Authentication API  

API ini menyediakan sistem autentikasi yang aman menggunakan **Simple JWT** untuk pengelolaan token autentikasi, serta verifikasi email untuk mengaktifkan akun pengguna. API ini dirancang untuk digunakan pada berbagai aplikasi web atau mobile.  

---

## ✨ Fitur Utama  
- **Autentikasi dengan JWT**  
  - Login menggunakan token akses (access token) dan token refresh (refresh token).  
  - Mendukung endpoint untuk pembaruan token menggunakan token refresh.  

- **Registrasi dan Verifikasi Email untuk Aktivasi Akun**  
  - Pengguna dapat mendaftar dengan email dan menerima tautan aktivasi akun.  
  - Akun hanya dapat digunakan setelah diverifikasi melalui email.  

- **Manajemen Akun Pengguna**  
  - Edit profil pengguna (nama, email, password).  
  - Lupa password dengan mekanisme reset via email.  

---

## 🛠️ Teknologi  
- **Framework**: Django REST Framework (DRF).  
- **Library Autentikasi**: Simple JWT.  
- **Pengiriman Email**: SMTP manual untuk pengiriman email aktivasi dan reset password.  

---
