from tkinter import Tk, Toplevel, Label
root = Tk()
root.withdraw()
for i in range(200):
    topl1 = Toplevel(root)
    topl1.title("Happy new year")
    topl1.geometry('300x300')
    l1 = Label(topl1, text="Happy new year").grid(column=0, row=0)
for j in range(5):
    for k in range(10, 500, 10):
        topl2 = Toplevel(topl1)
        topl2.title("Happy new year")
        topl2.geometry(str(k) + 'x' + str(k))
root.mainloop()
