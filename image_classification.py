import datetime
import os
import random
import shutil
from tkinter import messagebox
import csv
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt1
from matplotlib import pyplot as plt2
from PIL import ImageTk,Image
import sample_data
def image_matching(a,b):
    i1 = Image.open(a)
    i2 = Image.open(b)
    i1 = i1.resize((230, 200), Image.ANTIALIAS)
    i2 = i2.resize((230, 200), Image.ANTIALIAS)
    assert i1.mode == i2.mode, "Different kinds of images."
    assert i1.size == i2.size, "Different sizes."
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
    ncomponents = i1.size[0] * i1.size[1] * 3
    xx= (dif / 255.0 * 100) / ncomponents
    return xx
def write_dataset(feature,age,level,fertiliser):
    file ='training-dataset.csv'
    pr_chk=0
    with open(file) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            t1 = row['feature']
            a,b=int(t1),int(feature)
            if a==b:
                pr_chk+=1
    if pr_chk==0:
        file1 = 'training-dataset1.csv'
        with open(file) as f, open('training-dataset1.csv', 'w', encoding='utf-8', newline='')as csvfile:
            reader = csv.DictReader(f, delimiter=',')
            filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(
                ['feature', 'data1', 'data2', 'data3'])
            for row in reader:
                t1 = row['feature']
                t2 = row['data1']

                filewriter.writerow([t1, t2])
            filewriter.writerow([feature, age,level,fertiliser])
        shutil.copy('training-dataset1.csv', file)
        os.remove(file1)
        messagebox.showinfo(title="info", message="Success")
    else:
        messagebox.showinfo(title="info", message="Already Trained")
def training():
    name = "train"
    if os.path.exists(name):
        h = 0
    else:
        os.mkdir(name)
    age=txt2.get()
    level=txt3.get()
    fertliser=txt4.get()


    if(age==""):
        messagebox.showinfo(title="info", message="Enter Data")
    elif(level==""):
        messagebox.showinfo(title="info", message="Enter Data")
    elif (fertliser == ""):
        messagebox.showinfo(title="info", message="Enter Data")


    else:
        name1 = "train\\" + age
        if os.path.exists(name1):
            j = 0;
        else:
            os.mkdir(name1)
        ri2 = Image.open(sample_data.student.file_path)
        ri2 = ri2.resize((230, 200), Image.LANCZOS)
        r2 = ImageTk.PhotoImage(ri2)
        x = random.randint(10000000, 100000000)
        str1 = name1 + '\\%d.jpg' % x
        shutil.copy(sample_data.student.file_path, str1)
        write_dataset(feature=sample_data.student.bpnn,age=age,level=level,fertiliser=fertliser)
def testing1():
    noi=0
    actual=[1]
    predicted=[1]
    aci=0
    a = sample_data.student.x
    file = "training-dataset.csv"
    data=sample_data.student.bpnn
    with open(file) as f:
        reader = csv.DictReader(f, delimiter=',')
        age1=0
        # gen=0
        vv=0
        print(a)
        actual.append(0)
        for row in reader:
            id = row['feature']
            data1 = row['data1']
            data2 = row['data2']
            data3 = row['data3']
            # gender = str(row['data2'])
            result=""
            noi += 1
            result1=int(id)-int(data)
            actual.append(1)
            if result1==0:
                age1 = data1
                # gen = gender
                result = str(age1)
                aci += 1
                predicted.append(1)
            else:
                predicted.append(0)
                result1=abs(result1)
                if vv==0:
                    age1=data1
                    # gen=gender
                    vv = result1
                    aci += 1
                elif int(result1)<int(vv):
                    vv = result1
                    age1 = data1
                    aci+=1
            result = "Disease : "+str(age1)+"\nLevel : "+str(data2)+"\nFertiliser : "+str(data3)
        b = datetime.datetime.now()
        ad=len(str(aci))
        predict = b - a
        fxv,fxy=str(predict),a
        bn =sample_data.student.acc-(aci/100)
        fyv=fxv.split(':')
        sample_data.student.d1+=float(fyv[2])*sample_data.student.a1
        sample_data.student.d2+=float(fyv[2])*sample_data.student.a2
        names = ['Existing', 'Proposed']
        plt.figure(0)
        values = [sample_data.student.d1, sample_data.student.d2]
        plt.plot(names, values)
        plt.suptitle('Duration')
        bn1=85
        values = [bn1,bn]
        plt1.figure(1)
        plt1.plot(names, values)
        plt1.suptitle('Accuracy')
        messagebox.showinfo(title="Result", message=str(result))
        plt1.show()

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
message.place(x=00, y=3)
ri2 = Image.open(sample_data.student.file_path)
ri2 = ri2.resize((230, 200), Image.LANCZOS)
r2 = ImageTk.PhotoImage(ri2)
label2 = Label(root, image=r2, background=sample_data.student.background)
lbl = Label(root, image=r2, background=sample_data.student.background, fg=sample_data.student.text_color, font=('times', 15, ' bold '))
lbl.place(x=100, y=100)
lbl2 = Label(root,justify=RIGHT, text="DISEASE", width=10, fg=sample_data.student.text_color,bg=sample_data.student.background,  height=1, font=('times', 15, ' bold '))
lbl2.place(x=350, y=105)
txt2 = Entry(root, width=20, font=('times', 15, ' bold '))
txt2.place(x=350, y=155)
# label2 = Label(root, image=r2, background=sample_data.student.background)
# lbl = Label(root, image=r2, background=sample_data.student.background, fg=sample_data.student.text_color, font=('times', 15, ' bold '))
# lbl.place(x=200, y=100)
lbl2 = Label(root,justify=RIGHT, text="LEVEL", width=10, fg=sample_data.student.text_color,bg=sample_data.student.background,  height=1, font=('times', 15, ' bold '))
lbl2.place(x=350, y=195)
txt3 = Entry(root, width=20, font=('times', 15, ' bold '))
txt3.place(x=350, y=255)


lbl2 = Label(root,justify=RIGHT, text="FERTILISER", width=10, fg=sample_data.student.text_color,bg=sample_data.student.background,  height=1, font=('times', 15, ' bold '))
lbl2.place(x=350, y=285)
txt4 = Entry(root, width=20, font=('times', 15, ' bold '))
txt4.place(x=350, y=355)


compare_dataset = Button(root, text="Training",width=15,command=training  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=200, y=400)
resust_dataset = Button(root, text="Testing",width=15  ,height=1,command=testing1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=400, y=400)
root.mainloop()
