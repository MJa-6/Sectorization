import tkinter as tk
import pandas as pd
from test import classify

def show_url():
    url = entry.get()
    print(url)
    root.destroy() # this line closes the first window
    computed_text = classify(url)
    new_window = tk.Tk()
    new_window.title("URL")
    new_window.configure(bg='#1c1c1c')
    new_window.geometry("300x150")
    new_window.resizable(False, False)
    text = tk.Label(new_window, text=computed_text, font=("Helvetica", 16), fg='white', bg='#1c1c1c')
    text.grid(row=0, column=0, padx=20, pady=20)
    ok_button = tk.Button(new_window, text="OK", command=new_window.destroy, bg='#0099ff', fg='white', font=("Helvetica", 16))
    ok_button.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
    new_window.mainloop()

root = tk.Tk()
root.title("URL Input")
root.geometry("450x150")
root.configure(bg='#1c1c1c')
root.resizable(False, False)

url_label = tk.Label(root, text="Enter URL:", font=("Helvetica", 16), fg='white', bg='#1c1c1c')
url_label.grid(row=0, column=0, padx=20, pady=20)

entry = tk.Entry(root, bg='#333333', fg='white', insertbackground='white', font=("Helvetica", 16))
entry.grid(row=0, column=1, padx=20, pady=20)

submit_button = tk.Button(root, text="Submit", command=show_url, bg='#0099ff', fg='white', font=("Helvetica", 16))
submit_button.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

root.mainloop()
