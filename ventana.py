import tkinter

ventana = tkinter.Tk()

#Size of window
ventana.geometry("500x500")

etiqueta = tkinter.Label(ventana, text = "Aaaaaaa", bg = "blue")
etiqueta.pack(side = tkinter.BOTTOM, fill=tkinter.X)

ventana.mainloop()