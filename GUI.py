from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from SubtitleFixer import fix_encode

# ==================== Tkinter setup ====================

root = Tk()
root.title("SF Subtitle Fixer")
root.configure(bg="#124559")
root.resizable(width=False, height=False)

# ==================== Frames ====================

main_frame = Frame(root,background="#124559", height=100, width=600)
main_frame.pack(padx=10,pady=10)

# ==================== Functions and Variables ====================

filename =StringVar()

def browse():
    filename = filedialog.askopenfilename(title="select subtitle file", filetypes=(("srt file","*.srt"),))
    path_entry.delete(0, END)
    path_entry.insert(END, filename)

#bitmap image
def fix():
    fix_encode(filename.get())
    messagebox.showinfo("Complete","Your subtitle is now fixed and ready to use")

# ==================== Labels and Entries ====================

choose_label = Label(main_frame, text="Choose your subtitle file", font=("arial", 22), background="#124559", fg="#EFF6E0")
choose_label.grid(row=0, column=0, columnspan=4, rowspan=2)

path_entry = Entry(main_frame, textvariable=filename, highlightbackground="#124559")
path_entry.grid(row=2, column=0, columnspan=3, ipadx=40)

browse_button = Button(main_frame, text="Browse", command=browse, highlightbackground="#124559")
browse_button.grid(row=2, column=3)

fix_button = Button(main_frame, text="FIX NOW", command=fix, highlightbackground="#124559")
fix_button.grid(row=3, column=1, rowspan=2, columnspan=2, ipadx=10, ipady=7)

root.mainloop()