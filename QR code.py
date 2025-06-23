import pyqrcode
import png
from tkinter import *
from PIL import Image, ImageTk
import cv2

def generate_qr():
    message = entry.get()
    if not message:
        return
    qr = pyqrcode.create(message)
    filename = "message_qr.png"
    qr.png(filename, scale=10)
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img

root = Tk()
root.title("QR Code Generator")
root.geometry("400x500")

label = Label(root, text="Enter your message:")
label.pack(pady=10)

entry = Entry(root, width=40)
entry.pack(pady=10)

generate_button = Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

qr_label = Label(root)
qr_label.pack(pady=20)
root.mainloop()