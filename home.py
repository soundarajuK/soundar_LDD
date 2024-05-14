import shutil
from tkinter import *
import os
from tkinter.filedialog import askopenfilename
import sample_data
def read_first_data():
    csv_file_path = askopenfilename()
    fpath= os.path.dirname(os.path.abspath(csv_file_path))
    fname=(os.path.basename(csv_file_path))
    fsize=os.path.getsize(csv_file_path)
    txt.delete(0,END)
    txt.insert(0,fpath)
    txt2.insert(0,fname)
    sample_data.student.file_path=csv_file_path
def next_page():
    root.destroy()
    import image_grayscale
root = Tk()
# root.attributes('-alpha',0.5)

w=750
h=550
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title(sample_data.student.title)
root.resizable(False, False)
root.configure(background=sample_data.student.background)
message = Label(root, text=sample_data.student.titlec,fg=sample_data.student.text_color,bg=sample_data.student.background, width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=20)
lbl = Label(root,justify=CENTER, text="PATH", width=20,bg=sample_data.student.background, height=2, fg=sample_data.student.text_color, font=('times', 15, ' bold '))
lbl.place(x=100, y=150)
lbl2 = Label(root,justify=RIGHT, text="FILE", width=20, fg=sample_data.student.text_color,bg=sample_data.student.background,  height=2, font=('times', 15, ' bold '))
lbl2.place(x=100, y=225)
txt = Entry(root, validate="key", width=20, font=('times', 25, ' bold '))
txt.place(x=300, y=150)
txt2 = Entry(root, width=20, font=('times', 25, '  bold '))
txt2.place(x=300, y=225)
compare_dataset = Button(root, text="Select Image",width=15,command=read_first_data  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=250, y=400)
resust_dataset = Button(root, text="Next",width=15  ,height=1,command=next_page,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=400)
root.mainloop()
