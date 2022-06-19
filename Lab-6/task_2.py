from tkinter import *
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import gspread

gc = gspread.service_account(filename="./python-college-project-406804075937.json")
sh = gc.open("Task 2").sheet1

app_title = sh.get('A1')[0][0]

first_desc  = sh.get('C4')[0][0]
second_desc = sh.get('C5')[0][0]

def App():
    root = Tk()
    root.title(app_title)
    root.geometry("500x200")
    root.resizable(width=False, height=False)

    frame = Frame(root, bg="#171717")
    frame.place(relwidth=1, relheight=1)

    Label(frame, text=first_desc, bg="#171717").place(x=100, y=20) 
    first_entry = Entry(frame, width=5)
    first_entry.place(x=40, y=20)

    Label(frame, text=second_desc, bg="#171717").place(x=100, y=70) 
    second_entry = Entry(frame, width=5)
    second_entry.place(x=40, y=70)

    Label(frame, text="PDF Filename", bg="#171717").place(x=200, y=120) 
    filename_entry = Entry(frame, width=16)
    filename_entry.place(x=40, y=120)

    def save_click():
        flag = False
        sh.update('B4', int(first_entry.get()))
        sh.update('B5', int(second_entry.get()))
        sh.update('C1', date.today().strftime("%Y-%m-%d"))
        flag = True

        if flag:
            data_frame = pd.DataFrame(sh.get_all_records())
            filename = date.today().strftime("%Y-%m-%d") + " - " + filename_entry.get()

            fig, axs = plt.subplots()
            axs.axis("off")
            axs.table(cellText=data_frame.values, colLabels=data_frame.columns, loc="center")
            fig.tight_layout()
            plt.savefig(f"{filename}.pdf")

    Button(frame, text="Save", bg="#171717", borderwidth=0, command=save_click).place(x=40, y=170)

    root.mainloop()

if __name__ == "__main__":
    App()