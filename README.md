# 🔐 TOTP Generator (Python + CustomTkinter)

A simple, stylish TOTP (Time-based One-Time Password) generator built using [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) and [pyotp](https://github.com/pyauth/pyotp)
This tool lets you generate OTPs using your secret key — perfect for testing 2FA systems or verifying OTP functionality.

---

## 🚀 Features

- Generates 6-digit OTPs using your TOTP secret key
- Countdown timer showing time left until OTP expires
- Dark theme with green accents
- Click on the OTP to copy it to clipboard
- Friendly error handling if input is empty or invalid

---

## 📸 Screenshot

- <img width="377" height="277" alt="image" src="https://github.com/user-attachments/assets/f76687c1-3844-4da7-953c-2ea15d0558d7" /

---

## 📦 Installation
-
```bash
git clone https://github.com/Exoo25/totp-gen/
cd totp-gen
pip install -r requirements.txt
py main.py
```
---

 >⚠️ **Important:**  
 >For the TOTP codes to work correctly, your computer's clock **must be synced** with internet time.  
 >Even a small time difference (like 20–30 seconds) can cause OTP verification to fail.  
 > 
 >🔧 To avoid issues, make sure **automatic time synchronization** is enabled on your device.
 >
