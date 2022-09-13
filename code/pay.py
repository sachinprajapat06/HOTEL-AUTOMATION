from tkinter import *
import tkinter.messagebox as tmsg
import os

root = Tk()
root.geometry("1000x500")
root.title("payment portal")

def payment():
    os.system("G:\\Desktop\\project\\pdf\\pay.jpg")
    print(f"you have done {s2.get()} rupee payment sucessfully")
    tmsg.showinfo(f"you have done {s2.get()} rupee payment sucessfully", "thank you")

#s = Scale(root, from_=0, to=100)
#s.pack()
Label(root, text="please pay your bill!!! ").pack()

s2 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
s2.pack()
Button(root, text="payment",command=payment).pack()

root.mainloop()