from tkinter import *
from PIL import ImageTk, Image
import pandas as pd


# Window setup
root = Tk()
root.title('CCSU Mobile App')
root.geometry("500x630")
BG_COLOR = 'light steel blue'
root.configure(bg=BG_COLOR)

img= Image.open('logo2.jpg')
try:
    img = img.resize((160, 160), Image.Resampling.LANCZOS)
except AttributeError:
        img = img.resize((160, 160), Image.ANTIALIAS)

img = img.convert("RGBA")
data = img.getdata()
newData = []
for item in data:
        if item[:3] == (255, 255, 255):
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
img.putdata(newData)
img.save("transparent.png")

logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)
logoLabel = Label(root, image=logo, bg=BG_COLOR)
logoLabel.place(x=170, y=5)


# Read CSV
data = pd.read_csv("midterm_exam.csv")

# Label used to display results
lb = Label(root, justify="left", bg=BG_COLOR, anchor="w", font=("Segoe UI", 10), wraplength=360)
lb.place(x=100, y=260)


# button 1: calendar
def calendar():
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected_rows = df[~df['CalendarDate'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=55, y=260)

# button 2: buildings
def building():
    df = pd.DataFrame(data, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=180, y=260)

# button 3: faculty
def faculty():
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=200, y=260)

# button 4: School of business
def school_of_business():
    lines = [
        "School of Business Departments:",
        "  • Accounting",
        "  • Finance",
        "  • Management & Organization",
        "  • Marketing",
        "  • Management Information Systems (MIS)",
        "  • Business Analytics"
    ]
    lb.config(text="\n".join(lines))
    lb.place(x=150, y=260)

# MIS Department list
def mis_department():
    lines = [
        "MIS Department Core Courses:",
        "  • Intro to MIS",
        "  • Databases Management",
        "  • Systems Analysis & Design",
        "  • Business Analytics / Data Visualization",
        "  • Network and Information Security",
        "  • Project Management",
        "  • Python for Business Applications"
    ]
    lb.config(text="\n".join(lines))
    lb.place(x=150, y=260)

# Colors for buttons
BTN_BG = '#2e5fa4'
BTN_FG = 'white'

# -------------------------
#
button1 = Button(root, text='Calendar', command=calendar, bg=BTN_BG,fg=BTN_FG)
button1.place(x=105, y=170)

button2 = Button(root, text='Buildings', command=building, bg=BTN_BG,fg=BTN_FG)
button2.place(x=225, y=170)

button3 = Button(root, text='Faculty', command=faculty, bg=BTN_BG,fg=BTN_FG)
button3.place(x=345, y=170)

button4 = Button(root, text='School of Business', command=school_of_business, bg=BTN_BG, fg=BTN_FG)
button4.place(x=90, y=220)

button5 = Button(root, text='MIS Department', command=mis_department, bg=BTN_BG, fg=BTN_FG)
button5.place(x=305, y=220)

mainloop()
