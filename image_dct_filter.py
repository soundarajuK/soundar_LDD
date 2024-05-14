
# from skimage.io import imread
# import numpy as np
# import matplotlib.pylab as plt
from scipy.fftpack import dct, idct
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
import sample_data
def read_first_data():
    lbl2.place(x=400, y=200)
def next_page():
    root.destroy()
    # import image_watershed_segmentation
    import image_sharpening
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')
def dct1(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')
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
# im = (imread(sample_data.student.file_path))
#
# imF = dct2(im)
# im1 = dct1(imF)
# dd=np.allclose(im, im1)
lbl2 = Label(root)
# np.allclose(im, im1)
#
# plt.imsave('data/dct.png', im1, cmap='bone')
im1 = Image.open(r"data/greyscale.png")
im2 = im1.filter(ImageFilter.MedianFilter(size=3))
im2.save('data/dct.png')

root.configure(background=sample_data.student.background)
message = Label(root, text=sample_data.student.titlec,fg=sample_data.student.text_color,bg=sample_data.student.background, width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=20)
message = Label(root, text="Grayscal Image",fg=sample_data.student.text_color,bg=sample_data.student.background,  font=('times', 10, 'italic bold '))
message.place(x=100, y=170)
message = Label(root, text="DCT Image",fg=sample_data.student.text_color,bg=sample_data.student.background, font=('times', 10, 'italic bold '))
message.place(x=400, y=170)
ri2 = Image.open('data/greyscale.png')
ri2 = ri2.resize((200, 200), Image.LANCZOS)
r2 = ImageTk.PhotoImage(ri2)
label2 = Label(root, image=r2, background=sample_data.student.background)
lbl = Label(root, image=r2, background=sample_data.student.background, fg=sample_data.student.text_color, font=('times', 15, ' bold '))
lbl.place(x=100, y=200)
a1 = Image.open('data/dct.png')
a123 = a1.resize((200, 200), Image.LANCZOS)
a12 = ImageTk.PhotoImage(a123)
lbl2.configure(image=a12)
compare_dataset = Button(root, text="NOISE REMOVE",width=16,command=read_first_data  ,height=1,fg="#000",bg=sample_data.student.background, activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=100, y=450)
resust_dataset = Button(root, text="Next",width=16  ,height=1,command=next_page,fg="#000",bg=sample_data.student.background, activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=400, y=450)
root.mainloop()
