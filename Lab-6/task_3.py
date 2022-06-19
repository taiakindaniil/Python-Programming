import os, glob
from tkinter import *

def App():
    root = Tk()
    root.title("Открыватель PDF")
    root.geometry("300x140")
    root.resizable(width=False, height=False)

    frame = Frame(root, bg="#171717")
    frame.place(relwidth=1, relheight=1)

    Label(frame, text="Select PDF file that you want to open.", bg="#171717").pack()

    def option_menu(data: list, default_value) -> StringVar:
        variable = StringVar(frame)
        variable.set(default_value)
        OptionMenu(frame, variable, *data).pack()
        return variable

    file_variable = option_menu(files, "Select file")
    
    def open_click():
        value = file_variable.get()
        filename = glob.glob(f"*{value}.pdf")[0].replace(" ", "\\ ")
        os.system(f"open {filename}")

    open_btn = Button(frame, text="Open", bg="#171717", borderwidth=0, command=open_click)
    open_btn.pack()

    root.mainloop()

if __name__ == "__main__":
    files = [f[13:-4] for f in glob.glob("*.pdf")]
    App()