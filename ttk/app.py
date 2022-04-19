import tkinter as tk1


def click1():
    str1 = "abc"
    textbox1.delete(0, tk1.END)
    textbox1.insert(0, str1)


frame1 = tk1.Tk()
frame1.title('title')
frame1.geometry("300x100")

textbox1 = tk1.Entry(master=frame1)
textbox1.place(x=10, y=10, width=100)

button1 = tk1.Button(frame1, text='click', command=click1)
button1.place(x=120, y=10, width=100)

frame1.mainloop()
