
from tkinter import *
import os
root = Tk()

def getvals():
    print("Form Submited!")
    print(f"{namev.get(),addressv.get(),timev.get(),phonev.get(),paymentv.get(),foodservicev.get()}")
    
    with open("booking details.txt","a") as f:
        f.write(f"{namev.get(),addressv.get(),timev.get(),phonev.get(),paymentv.get(),foodservicev.get()}\n")
        

root.geometry("1000x500")
root.title("hotel_booking_portal")
#heading
Label(root, text="hotel_booking_portal", font="comicsansms 20 bold",bg="black",fg="white",pady=15).grid(row=0,column=3)
#text for our form
name = Label(root, text="Name:",pady=10,padx=10, font="comicsansms 8 bold")
address = Label(root, text="Pick Up Address:",pady=10,padx=10, font="comicsansms 8 bold")
time = Label(root, text="Prefered Time:",pady=10,padx=10, font="comicsansms 8 bold")
days = Label(root, text="Number of Days:",pady=10,padx=10, font="comicsansms 8 bold")
phone = Label(root, text="Emergency Contact:",pady=10,padx=10, font="comicsansms 8 bold")
payment = Label(root, text="Payment Mode:",pady=10,padx=10, font="comicsansms 8 bold")
#pack text for our form
name.grid(row=1,column=2)
address.grid(row=2,column=2)
time.grid(row=3,column=2)
days.grid(row=4,column=2)
phone.grid(row=5,column=2)
payment.grid(row=6,column=2)
#tkinter variable for storing entries
namev = StringVar()
addressv = StringVar()
timev = StringVar()
daysv = StringVar()
phonev = StringVar()
paymentv = StringVar()
foodservicev = IntVar()
#entries for our form
nameentry = Entry(root,textvariable=namev)
addressentry = Entry(root,textvariable=addressv)
timeentry = Entry(root,textvariable=timev)
daysentry = Entry(root,textvariable=daysv)
phoneentry = Entry(root,textvariable=phonev)
paymententry = Entry(root,textvariable=paymentv)
#packing entries
nameentry.grid(row=1,column=3)
addressentry.grid(row=2,column=3)
timeentry.grid(row=3,column=3)
daysentry.grid(row=4,column=3)
phoneentry.grid(row=5,column=3)
paymententry.grid(row=6,column=3)
#check box
foodservice = Checkbutton(text="Want to prebook your meals!",pady=10, font="comicsansms 10 bold", variable=foodservicev)
#check box packing
foodservice.grid(row=9,column=3)
#button $ packing it and assing it a commend
Button(text="Submit ",command=getvals,fg="red",pady=10, font="comicsansms 15 bold", ).grid(row=10,column=3)

root.mainloop()