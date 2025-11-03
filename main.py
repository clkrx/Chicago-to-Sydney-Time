import tkinter as tk
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


label1 = tk.Label(window, text=f"Chicago Time: {formatted_time}")
label1.pack(pady=25)

label2 = tk.Label(window, text=f"Sydney Time: {formatted_time2}")
label2.pack(pady=25)

button = tk.Button(window, text="Close", command=window.destroy)
button.pack()


window.mainloop()
