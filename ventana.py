import tkinter as tk

#Object of tkinter
ventana = tk.Tk()

#Size of window
ventana.geometry("500x500")

etiqueta = tk.Label(ventana, text = "Aaaaaaa", bg = "blue")
etiqueta.pack(side = tk.BOTTOM, fill=tk.X)

#Force to keep open the window
ventana.mainloop()