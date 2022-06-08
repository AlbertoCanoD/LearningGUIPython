from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from matplotlib import image
import numpy as np

try:
    import tkinter
except ImportError:
    raise ImportError("Se requiere el modulo tkinter")


def openImage():

    global panelA, panelB

    path = filedialog.askopenfilename()

    if len(path) > 0:

        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 100)

        # Conversion BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # convert the images to PIL format...
        image = Image.fromarray(image)
        edged = Image.fromarray(edged)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)

        # if the panels are None, initialize them
    if panelA is None or panelB is None:
        # the first panel will store our original image
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side="left", padx=10, pady=10)
        # while the second panel will store the edge map
        panelB = Label(image=edged)
        panelB.image = edged
        panelB.pack(side="right", padx=10, pady=10)
        # otherwise, update the image panels
    else:
        # update the pannels
        panelA.configure(image=image)
        panelB.configure(image=edged)
        panelA.image = image
        panelB.image = edged


class UI(Frame):
    """Docstring."""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.image = None
        self.init_ui()

    def init_ui(self):
        btn = Button(ROOT, text="Select an image", command=openImage)
        btn.pack(side="bottom", fill="both",
                 expand="yes", padx="10", pady="10")
        self.parent.title("Media")


if __name__ == "__main__":
    ROOT = Tk()
    panelA = None
    panelB = None
    ROOT.geometry("800x600")
    APP = UI(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()
