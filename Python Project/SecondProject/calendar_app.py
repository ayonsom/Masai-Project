import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def get_date():
    selected_date = cal.selection_get()
    label.config(text=f"Selected Date: {selected_date}")

root = tk.Tk()
root.title("Calendar App")

cal = Calendar(root, selectmode="day", year=2023, month=7, day=29)
cal.pack(pady=20)

button = ttk.Button(root, text="Get Date", command=get_date)
button.pack(pady=10)

label = ttk.Label(root, text="Selected Date: ")
label.pack(pady=10)

root.mainloop()
