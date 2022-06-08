from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import numpy as np

try:
    import tkinter
except ImportError:
    raise ImportError("Se requiere el modulo tkinter")

path = filedialog.askopenfilename()