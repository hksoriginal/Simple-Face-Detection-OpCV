
import sys
from tkinter import *
import numpy as np
from PIL import Image, ImageTk
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


class face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600+0+0")
        self.root.title("Face Detection")
        self.root.iconbitmap("face.ico")


# __________________________

        def face():
            import cv2
           

            face_cascade = cv2.CascadeClassifier(
                'haarcascade_frontalface_default.xml')

            cap = cv2.VideoCapture(0)

            while cap.isOpened():

                _, img = cap.read()

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                cv2.putText(img,"Press 'Q' to quite Detection",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,120,255),2)

                cv2.imshow('Image', img)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                 break

            cap.release()
            
# __________________________

        # background
        img_background = Image.open("3.png")
        img_background = img_background.resize((600, 600), Image.ANTIALIAS)
        self.photoimage_background = ImageTk.PhotoImage(img_background)
        label1 = Label(self.root, image=self.photoimage_background)
        label1.place(x=0, y=0, width=600, height=600)

        label_title = Label(label1, text="Simple Face Detection", font=(
            "Helvetica", 15, "bold"), bg="#333333", fg="White")
        label_title.place(x=-1, y=0, width=650, height=50)

        # Scan Button
        img_scan_button = Image.open("scan.png")
        img_scan_button = img_scan_button.resize((200, 200), Image.ANTIALIAS)
        self.photoimg_scan_button = ImageTk.PhotoImage(img_scan_button)
        b_scan = Button(label1, image=self.photoimg_scan_button,
                        cursor="hand2", border="5", command=face)
        b_scan.place(x=200, y=150, width=200, height=200)

        # Exit button
        b_exit = Button(label1, text="Exit", cursor="hand2", font=(
            "Comic Sans", 25, "bold"), bg="#C1272D", fg="White", command=sys.exit)
        b_exit.place(x=200, y=500, width=200, height=50)


if __name__ == "__main__":
    root = Tk()
    obj = face_recognition(root)
    root.mainloop()
