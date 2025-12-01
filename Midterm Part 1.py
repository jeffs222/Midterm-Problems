#import
import tkinter as tk
from tkinter import messagebox

# logic for points for books purchased
def points_for_books(books):
    if books < 2:
        return 0
    if books < 4:
        return 5
    if books < 6:
        return 15
    if books < 8:
        return 30
    return 60


# defining button clicks
def compute_button_click():
    books = int(books_entry.get())
    result_text.set(f"Points: {points_for_books(books)}")


def show_result_button_click():
    messagebox.showinfo("Result", result_text.get())


# gui
root = tk.Tk()
root.title("Book Club Points")

instruction_label = tk.Label(root, text="Enter number of books purchased this month:")
instruction_label.pack(padx=10, pady=(10, 4))

entry_frame = tk.Frame(root)
entry_frame.pack(padx=10, pady=4)

books_entry = tk.Entry(entry_frame, width=20)
books_entry.pack(side="left")
books_entry.focus_set()

compute_button = tk.Button(entry_frame, text="Compute Points", command=compute_button_click)
compute_button.pack(side="left", padx=8)

result_frame = tk.Frame(root)
result_frame.pack(padx=10, pady=4, fill="x")

result_text = tk.StringVar(value="Points: 0")
result_label = tk.Label(result_frame, textvariable=result_text)
result_label.pack(side="left")

result_button = tk.Button(result_frame, text="Show Result", command=show_result_button_click)
result_button.pack(side="right",padx=14)

root.mainloop()