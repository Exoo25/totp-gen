from customtkinter import *
import pyotp as otp
import time

# App appearance settings
set_appearance_mode('dark')
set_default_color_theme('green')

# Main app window
app = CTk()
app.title("TOTP Generator")
app.geometry("300x160")
app.resizable(False, False)

# Global variable to hold current OTP
current_otp = ""

# Heading
CTkLabel(app, text="TOTP GENERATOR", font=("Trebuchet MS", 17, "bold")).pack(pady=(10, 0))

# Secret key input frame
frame = CTkFrame(app, border_color='green', border_width=2)
CTkLabel(frame, text="Secret Key").grid(row=0, column=0, padx=5, pady=5)
prompt = CTkEntry(frame, corner_radius=5, width=160, border_color="green")
prompt.grid(row=0, column=1, padx=5)
frame.pack(pady=5)

# Label to show OTP
label = CTkLabel(app, text="Your TOTP will appear here", cursor="hand2")
label.pack(pady=5)

# Label to show countdown
countdown_label = CTkLabel(app, text="")
countdown_label.pack_forget()  # Hidden at start

# Bind clicking the OTP label to copy to clipboard
def on_label_click(event):
    if current_otp:
        app.clipboard_clear()
        app.clipboard_append(current_otp)
        label.configure(text=f"Copied OTP: {current_otp}", text_color="lime")

label.bind("<Button-1>", on_label_click)

# Flag to track countdown status
countdown_running = False

# Generate OTP function
def ggs():
    global current_otp, countdown_running
    secret = prompt.get().strip()

    if not secret:
        label.configure(text="Enter a secret key first!", text_color="orange")
        countdown_label.pack_forget()
        countdown_running = False
        return

    try:
        totp = otp.TOTP(secret)
        otp_code = totp.now()
        current_otp = otp_code
        label.configure(text=f"Your OTP is: {otp_code}", text_color="white", font=("Arial", 12))
        countdown_label.pack()

        if not countdown_running:
            countdown_running = True
            update_countdown()
    except Exception as e:
        label.configure(text=f"Error: {e}", text_color="red", font=("Arial", 12, "bold"))
        countdown_label.pack_forget()
        countdown_running = False

# Countdown function
def update_countdown():
    global countdown_running, current_otp
    secret = prompt.get().strip()

    if not secret:
        countdown_label.configure(text="Enter a valid secret key!")
        countdown_running = False
        return

    try:
        totp = otp.TOTP(secret)
        seconds_remaining = 30 - (int(time.time()) % 30)
        countdown_label.configure(text=f"Expires in: {seconds_remaining}s")
        app.geometry("300x190")

        # Regenerate OTP on every cycle
        if seconds_remaining == 30:
            otp_code = totp.now()
            current_otp = otp_code
            label.configure(text=f"Your OTP is: {otp_code}", text_color="white", font=("Arial", 12))

        if countdown_running:
            app.after(1000, update_countdown)
    except:
        countdown_label.configure(text="Enter a valid secret key!")
        countdown_running = False

# Button to generate OTP
CTkButton(app, text="Generate Now", command=ggs, corner_radius=5).pack()

# Start the app loop
app.mainloop()
