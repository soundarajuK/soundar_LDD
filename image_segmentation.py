from skimage.io import imread
import numpy as np
from tkinter import *
import cv2
from PIL import ImageTk,Image
import sample_data
def read_first_data():
    lbl2.place(x=400, y=200)
def next_page():
    root.destroy()
    import image_morphological
root = Tk()
w=750
h=550
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title(sample_data.student.title)
root.resizable(False, False)
image = (imread(sample_data.student.file_path))
dd=sample_data.student.file_path
lbl2 = Label(root)
file_name = image
src = cv2.imread("data\\dct.png", 1)
img = src
s = 128
img = cv2.resize(img, (s, s), 0, 0, cv2.INTER_AREA)
def apply_watershed_segment(input_img, brightness=0, contrast=0):
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()
    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)
        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)
    return buf
font = cv2.FONT_HERSHEY_SIMPLEX
fcolor = (0, 0, 0)
blist = [ 0]
clist = [ 64]
out = np.zeros((s * 2, s * 3, 3), dtype=np.uint8)
for i, b in enumerate(blist):
    c = clist[i]
    out = apply_watershed_segment(img, b, c)
cv2.imwrite('data/watershed.png', out)
root.configure(background=sample_data.student.background)
message = Label(root, text=sample_data.student.titlec,fg=sample_data.student.text_color,bg=sample_data.student.background, width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=20)
message = Label(root, text="Sharpening Image",fg=sample_data.student.text_color,bg=sample_data.student.background,  font=('times', 10, 'italic bold '))
message.place(x=100, y=170)
message = Label(root, text="Segmentation Image",fg=sample_data.student.text_color,bg=sample_data.student.background, font=('times', 10, 'italic bold '))
message.place(x=400, y=170)
ri2 = Image.open('data/sharpened.png')
ri2 = ri2.resize((200, 200), Image.LANCZOS)
r2 = ImageTk.PhotoImage(ri2)
label2 = Label(root, image=r2, background=sample_data.student.background)
lbl = Label(root, image=r2, background=sample_data.student.background, fg=sample_data.student.text_color, font=('times', 15, ' bold '))
lbl.place(x=100, y=200)
a1 = Image.open('data/watershed.png')
a123 = a1.resize((200, 200), Image.LANCZOS)
a12 = ImageTk.PhotoImage(a123)
lbl2.configure(image=a12)
compare_dataset = Button(root, text="segmentation",width=16,command=read_first_data  ,height=1,fg="#000",bg=sample_data.student.background, activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=100, y=450)
resust_dataset = Button(root, text="Next",width=16  ,height=1,command=next_page,fg="#000",bg=sample_data.student.background, activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=400, y=450)
root.mainloop()
