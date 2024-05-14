import cv2
import numpy as np
import matplotlib.pylab as plt
from tkinter import *
from PIL import ImageTk,Image
import sample_data
from numpy import asarray
from m_bpnn import BPNNetwork
def rotate_bound(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    return cv2.warpAffine(image, M, (nW, nH))
def roi():
    image = cv2.imread('data\\morphological.png')
    # image = cv2.imread(sample_data.student.file_path)
    original = image.copy()
    blank = np.zeros(image.shape[:2], dtype=np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (127, 127), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=2)
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = max(contours, key=lambda x: cv2.contourArea(x))
    cv2.drawContours(image, [contours], -1, (255, 255, 0), 2)
    ar_read = 0
    ar_x = []
    ar_y = []
    hull = cv2.convexHull(contours, returnPoints=False)
    defects = cv2.convexityDefects(contours, hull)
    flag = not np.any(defects)
    if flag == False:
        for i in range(defects.shape[0]):
            _, _, farthest_point_index, distance = defects[i, 0]
            farthest_point = contours[farthest_point_index][0]
            if distance > 50_000:
                ar_x.append(farthest_point[0])
                ar_y.append(farthest_point[1])
                (x, y), (MA, ma), ellipse_angle = cv2.fitEllipse(contours)
                x1 = int((int(x) + int(MA) * np.sin(ellipse_angle * np.pi / 180.0)))
                y1 = int((int(y) - int(MA) * np.cos(ellipse_angle * np.pi / 180.0)))
                x2 = int((int(x) - int(MA) * np.sin(ellipse_angle * np.pi / 180.0)))
                y2 = int((int(y) + int(MA) * np.cos(ellipse_angle * np.pi / 180.0)))
                color = (255, 0, 0)
            else:
                sample_data.student.bpnn -= 1
    plt.imsave('Detected.png', image)
def read_first_data1():
    lbl2.config(text=str(sample_data.student.bpnn))
    lbl2.place(x=400, y=400)
    lbl2.delete(0, END)
    lbl2.insert(0, str(sample_data.student.bpnn))
    labe_rou.place(x=370, y=200)
def read_first_data():
    img = cv2.imread('data\\morphological.png', 0)
    numpydata = asarray(img)
    z = []
    for x in numpydata:
        for y in x:
            z.append(int(y))
    nn = BPNNetwork([2, 2, 1])
    nn.glcm_extract(z)
    sample_data.student.bpnn=nn.result()
    roi()
def next_page():
    root.destroy()
    import image_classification
read_first_data()
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
root.configure(background=sample_data.student.background)
message = Label(root, text=sample_data.student.titlec,fg=sample_data.student.text_color,bg=sample_data.student.background, width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=20)
message = Label(root, text="Morphological",fg=sample_data.student.text_color,bg=sample_data.student.background,  font=('times', 10, 'italic bold '))
message.place(x=100, y=170)
message = Label(root, text="Feature-Extraction",fg=sample_data.student.text_color,bg=sample_data.student.background, font=('times', 10, 'italic bold '))
message.place(x=400, y=170)
ri2 = Image.open('data/morphological.png')
ri2 = ri2.resize((200, 200), Image.LANCZOS)
r2 = ImageTk.PhotoImage(ri2)
label2 = Label(root, image=r2, background=sample_data.student.background)
lbl = Label(root, image=r2, background=sample_data.student.background, fg=sample_data.student.text_color, font=('times', 15, ' bold '))
lbl.place(x=100, y=200)
lbl2 = Entry(root)
lbl2.configure()
ri2 = Image.open('Detected.png')
ri3 = ri2.resize((200, 200), Image.LANCZOS)
r23 = ImageTk.PhotoImage(ri3)
labe_rou = Label(root, image=r23)
compare_dataset = Button(root, text="extraction",width=16,command=read_first_data1  ,height=1,fg="#000",bg=sample_data.student.background, activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=100, y=450)
resust_dataset = Button(root, text="Next",width=16  ,height=1,command=next_page,fg="#000",bg=sample_data.student.background, activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=400, y=450 )
root.mainloop()
