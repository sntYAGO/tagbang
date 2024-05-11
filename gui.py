import tkinter as tk
import main
from tkinter import messagebox

def submit_form():
    url = url_entry.get()
    count = count_entry.get()
    if url and count:
        main.auto_answer(url, int(count))
        messagebox.showinfo("Success", "Form submitted successfully!")
    else:
        messagebox.showerror("Error", "Please enter both URL and count")

root = tk.Tk()
root.title("Google Form Automation")

url_label = tk.Label(root, text="Google Form URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

count_label = tk.Label(root, text="Number of Respondents:")
count_label.pack()

count_entry = tk.Entry(root)
count_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

root.mainloop()
