import os
from tkinter import *
import PIL
from PIL import ImageGrab
import brainCNN


class main:
    def __init__(self, master):
        self.master = master
        self.res = ""
        self.pre = [None, None]
        self.bs = 8.5
        self.c = Canvas(self.master,bd=3,relief="ridge", width=300, height=282, bg='white')
        self.c.pack(side=LEFT)
        f1 = Frame(self.master, padx=5, pady=5)
        Label(f1,text="CNN Predicting Hand-Written Digits",fg="green",font=("",15,"bold")).pack(pady=10)
        Label(f1,text="Trained using MNSIT Dataset",fg="green",font=("",15)).pack()
        Label(f1,text="Using Python and Keras, Tensorflow",fg="green",font=("",15)).pack()
        Label(f1,text="Draw On The Canvas Alongside",fg="green",font=("",15)).pack()
        self.pr = Label(f1,text="Prediction: None",fg="blue",font=("",20,"bold"))
        self.pr.pack(pady=20)
        
        Button(f1,font=("",15),fg="white",bg="red", text="Clear Canvas", command=self.clear).pack(side=BOTTOM)

        f1.pack(side=RIGHT,fill=Y)
        self.c.bind("<Button-1>", self.putPoint)
        self.c.bind("<ButtonRelease-1>",self.getResult)
        self.c.bind("<B1-Motion>", self.paint)

    def getResult(self,e):
        x = self.master.winfo_rootx() + self.c.winfo_x()
        y = self.master.winfo_rooty() + self.c.winfo_y()
        x1 = x + self.c.winfo_width()
        y1 = y + self.c.winfo_height()
        img = PIL.ImageGrab.grab()
        img = img.crop((x, y, x1, y1))
        img.save("dist.png")
        self.res = str(brainCNN.predict("dist.png"))
        self.pr['text'] = "Prediction: " + self.res

    def clear(self):
        self.c.delete('all')

    def putPoint(self, e):
        self.c.create_oval(e.x - self.bs, e.y - self.bs, e.x + self.bs, e.y + self.bs, outline='black', fill='black')
        self.pre = [e.x, e.y]

    def paint(self, e):
        self.c.create_line(self.pre[0], self.pre[1], e.x, e.y, width=self.bs * 2, fill='black', capstyle=ROUND,
                           smooth=TRUE)

        self.pre = [e.x, e.y]


if __name__ == "__main__":
    root = Tk()
    main(root)
    root.title('Digit Classifier')
    root.resizable(0, 0)
    root.mainloop()
