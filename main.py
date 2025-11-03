import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

Timezone = pytz.timezone("America/Chicago")
current_time = datetime.now(Timezone)
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S %Z")


Timezone2 = pytz.timezone("Australia/Sydney")
current_time2 = datetime.now(Timezone2)
formatted_time2 = current_time2.strftime("%Y-%m-%d %H:%M:%S %Z")

window = tk.Tk()
window.title("Timezones syd - chi")
window.geometry("300x300")  

window.configure(background="#f0f0f5")
title_font = ("Helvetica", 16, "bold")
text_font = ("Helvetica", 12)

def center_window(win, width=400, height=250):
    screen_w = win.winfo_screenwidth()
    screen_h = win.winfo_screenheight()
    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")
center_window(window)

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#f0f0f5", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 11), padding=6)
main_frame = ttk.Frame(window, padding=20, style="TFrame")
main_frame.pack(fill="both", expand=True)

title_label = ttk.Label(main_frame, text="🌎 Timezones: Chicago → Sydney", font=("Segoe UI", 16, "bold"))
title_label.pack(pady=(0, 15))
label1 = tk.Label(window, text=f"Chicago Time: {formatted_time}")
label1.pack(pady=25)

label2 = tk.Label(window, text=f"Sydney Time: {formatted_time2}")
label2.pack(pady=25)

button = tk.Button(window, text="Close", command=window.destroy)
button.pack()


window.mainloop()
