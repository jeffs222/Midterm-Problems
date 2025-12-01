from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
import os

# -------------------------
# Window setup
# -------------------------
root = Tk()
root.title('CCSU Mobile App')          # updated title per spec
root.geometry("500x500")
root.configure(bg='light blue')

# -------------------------
# Find logo1 or logo2 in the local folder (keep behavior close to original)
# -------------------------
def find_logo_path():
    candidates = [
        "logo2.jpg", # fallback to your original name if present
    ]
    for name in candidates:
        if os.path.exists(name):
            return name
    return None

logo_path = find_logo_path()
if logo_path is None:
    # Minimal fallback: a tiny text label if no logo is found
    logoLabel = Label(root, text="(logo1/logo2 not found)", bg='light blue')
    logoLabel.place(x=1, y=1)
else:
    # -------------------------
    # Make white in logo transparent and show it (same approach as your original)
    # -------------------------
    img = Image.open(logo_path)
    # Pillow>=10 changed ANTIALIAS; this keeps it compatible
    try:
        img = img.resize((100, 100), Image.Resampling.LANCZOS)
    except AttributeError:
        img = img.resize((100, 100), Image.ANTIALIAS)

    img = img.convert("RGBA")
    data = img.getdata()

    newData = []
    for item in data:
        # if pixel is white make it transparent; else keep it
        if item[:3] == (255, 255, 255):
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("transparent.png")

    logo = Image.open("transparent.png")
    logo = ImageTk.PhotoImage(logo)
    logoLabel = Label(root, image=logo, bg='light blue')
    logoLabel.place(x=1, y=1)

# -------------------------
# Read the CSV required by the assignment
# -------------------------
data = pd.read_csv("midterm_exam.csv")

# Label used to display results (single output area to avoid overlap)
lb = Label(root, justify="left", bg="light blue", anchor="w", wraplength=340)
lb.place(x=130, y=150)

# -------------------------
# button 1: calendar
def calendar():
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected_rows = df[~df['CalendarDate'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=150)

# button 2: buildings
def building():
    df = pd.DataFrame(data, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=150)

# button 3: faculty
def faculty():
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=150)

# -------------------------
# Buttons (light green, horizontal)
button1 = Button(root, text='Calendar', command=calendar, bg="light green")  # fixed spelling
button1.place(x=50, y=110)

button2 = Button(root, text='Buildings', command=building, bg="light green")
button2.place(x=150, y=110)

button3 = Button(root, text='Faculty', command=faculty, bg="light green")
button3.place(x=250, y=110)

mainloop()