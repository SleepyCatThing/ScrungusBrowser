import tkinter as tk
from tkinter import ttk

window = tk.Tk()

output = tk.StringVar()
headline = tk.Label(window, text = "Scrungus Browser version 1").grid(row=0, columnspan=2)

search_bar = tk.Entry(window, text = "Search Here:").grid(row=1, column=0)

search_button=tk.Button(window, text="Search", command=lambda: output.set("Scrungus")).grid(row=1, column=1)

output_text = tk.Label(window, textvariable=output).grid(row=2, column=0, columnspan=2)

window.mainloop()