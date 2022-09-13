from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import sys
import subprocess
from playsound import playsound #pip install playsound
from gtts import gTTS #pip install gtts
import cv2
import os
import webbrowser
from googletrans import Translator #pip install google-trans



#voice module
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

l = "eng"

def guihotel():
    root = Tk()
    root.geometry("1366x768")
    root.title("welcome to hotel grand")
    root.configure(background="black")
    img = PhotoImage(file="G:\\Desktop\\project\\all pictures\\hotel.png")
    label = Label(root,image=img)
    label.place(x=183, y=134)
    start = Button(root, text="start", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=wishMe)
    start.pack(side=BOTTOM)
    login = Button(root, text="login", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=loginp)
    login.pack(side=BOTTOM)
    feedback = Button(root, text="feedback", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=sujjestion)
    feedback.pack(side=BOTTOM)
    root.mainloop()
 
def guirec():
    root = Toplevel()
    root.geometry("1366x768")
    root.title("welcome to reception")
    root.configure(background="black")
    img = PhotoImage(file="G:\\Desktop\\project\\all pictures\\rec.png")
    label = Label(root,image=img)
    label.place(x=183, y=134)
    start = Button(root, text="start", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=reception)
    start.pack(side=BOTTOM)
    room = Button(root, text="book room", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=roomb)
    room.pack(side=BOTTOM)
    login = Button(root, text="login", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=loginp)
    login.pack(side=BOTTOM)
    feedback = Button(root, text="feedback", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=sujjestion)
    feedback.pack(side=BOTTOM)

    root.mainloop()

def guiman():
    hotm = Toplevel()
    hotm.geometry("1366x768")
    hotm.title("welcome to manager desk")
    hotm.configure(background="black")
    img = PhotoImage(file="G:\\Desktop\\project\\all pictures\\man.png")
    label = Label(hotm,image=img)
    label.place(x=183, y=134)
    start = Button(hotm, text="start", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=manager)
    start.pack(side=BOTTOM)
    feedback = Button(root, text="feedback", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=sujjestion)
    feedback.pack(side=BOTTOM)
    hotm.mainloop()

def guisec():
    root = Toplevel()
    root.geometry("1366x768")
    root.title("welcome to sequrity desk")
    root.configure(background="black")
    img = PhotoImage(file="G:\\Desktop\\project\\all pictures\\sec.png")
    label = Label(root,image=img)
    label.place(x=183, y=134)
    start = Button(root, text="start", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=sequrity)
    start.pack(side=BOTTOM)
    root.mainloop()

def guichef():
    root = Toplevel()
    root.geometry("1366x768")
    root.title("welcome to chef desk")
    root.configure(background="black")
    img = PhotoImage(file="G:\\Desktop\\project\\all pictures\\chef.png")
    label = Label(root,image=img)
    label.place(x=183, y=134)
    start = Button(root, text="start", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=chef)
    start.pack(side=BOTTOM)
    order = Button(root, text="order", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=orderfood)
    order.pack(side=BOTTOM)
    feedback = Button(root, text="feedback", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=sujjestion)
    feedback.pack(side=BOTTOM)
    root.mainloop()

def guiwait():
    root = Toplevel()
    root.geometry("1366x768")
    root.title("welcome to our waiter desk")
    root.configure(background="black")
    img = PhotoImage(file="G:\\Desktop\\project\\all pictures\\wait.png")
    label = Label(root,image=img)
    label.place(x=183, y=134)
    start = Button(root, text="start", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=waiter)
    start.pack(side=BOTTOM)
    order = Button(root, text="order", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=orderfood)
    order.pack(side=BOTTOM)
    feedback = Button(root, text="feedback", bg="grey", fg="black",
        font="comicsnssms 30 bold", command=sujjestion)
    feedback.pack(side=BOTTOM)
    root.mainloop()

def sujjestion():
    subprocess.Popen("feedback.py", shell = True)

def orderfood():
    subprocess.Popen("bill_food.py", shell = True)
    subprocess.Popen("pay.py", shell = True)

def loginp():
    subprocess.Popen("login.py", shell = True)

def roomb():
    subprocess.Popen("room.py", shell = True)

def m(audio):
    if l == "hin":
        transl(audio)
    if l == "eng":
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()


def f(audio):
    if l == "hin":
        trans(audio)
    if l == "eng":
        engine.setProperty('voice', voices[3].id)
        engine.say(audio)
        engine.runAndWait()


def trans(a):
    translater = Translator()
    audio = translater.translate(a,src="en",dest="hi")
    print(audio.text)
    engine.setProperty('voice', voices[1].id)
    engine.say(audio.text)
    engine.runAndWait()


def transl(b):
    translater = Translator()
    audio = translater.translate(b,src="en",dest="hi")
    print(audio.text)
    engine.setProperty('voice', voices[2].id)
    engine.say(audio.text)
    engine.runAndWait()


def place():
    f("Sir, where do you wanna go ?")
    root = Toplevel()
    root.geometry("1366x500")
    root.minsize(1000,500)
    root.maxsize(2000,1000)
    root.title("welcome to hotel grand")
    root.configure(background="black")
    Label(root, text=" ",font="comicsansms 18 bold",justify=LEFT,padx=14,bg="black",fg="orange").pack()
    Label(root, text =" ",font="comicsansms 15 bold",justify=LEFT,padx=14,bg="black",fg="#BF4F51").pack()
    Button(root, text="Manager", bg="green",font="arial 15 bold", command=guiman).pack()
    Button(root, text="Chef", bg="green",font="arial 15 bold", command=guichef).pack()
    Button(root, text="Reception", bg="green",font="arial 15 bold", command=guirec).pack()
    Button(root, text="Waiter", bg="green",font="arial 15 bold", command=guiwait).pack()
    Button(root, text="Security", bg="green",font="arial 15 bold", command=guisec).pack()
    root.mainloop()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        f("Good Morning!")
    elif hour>=12 and hour<18:
        f("Good Afternoon!")
    else:
        f("Good Evening!")
    f("Sir, do you want me to speak hindi")
    while True:
        global l
        query = takeCommand().lower()
        if 'yes' in query:
            l = "hin"
        if 'no' in query:
            l = "eng"
        print(l)
        break
    place()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        m("please speak")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=3)
    try:
        m("thank you")
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sequrity():

    m("welcome sir how can i help you")
    while True:
        query = takeCommand().lower()
        if 'reception' in query:
            m("you must go straight and there is reception")
            guirec()
        elif 'exit' in query or 'by' in query or 'sleep' in query or 'jao' in query:
            m("hope i was helpful to u ,sir thank you for using our services")
            sys.exit()
        elif 'food court' in query:
            m("you must go straight and then turn left there is your food court")
        elif 'restaurant' in query or 'khana' in query:
            m("you must go straight and then turn right there is your destination")
        elif 'bar' in query or 'mehfil bnani hai' in query or 'daaru' in query or 'drink' in query:
            m("you must go straight and then turn left walk straight and turn right there is your bar")
        elif 'room' in query or 'kamre ke liye' in query:
            m("you must go straight and there is reception")
        elif 'how are you ' in query or 'kese ho bhai' in query:
            m("i am fine and hope you are also well")
        elif 'map ' in query or 'rasta' in query or 'near' in query:
            m("ok sir here we are")
            webbrowser.open("maps.google.com")
        elif 'park my car' in query or 'gaadi khadi kardo' in query:
            m("ok sir i am calling driver please give your keys. and fill details about your car here")
        elif 'cleaning staff' in query or 'safai karwani' in query:
            m("you must go straight and there is reception there you can get your solution")
        elif 'time' in query or 'samay' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            m(f"Sir, the time is {strTime}")
        elif 'Location' in query or 'kaha se ho' in query:
            m("our location is at google cloud else we also avilable at my master's laptop")
        elif 'medical shop' in query or 'dawai' in query:
            m("sir you can tell us we can get you the prescribed medicines or you can get that at given location")
        elif 'petrol' in query or 'petrol pump' in query or 'tel' in query:
            m("sir you can give us your car's key or you can get that at given location")
        elif 'gas' in query or 'cng' in query:
            m("sir you can give us your car's key or you can get that at given location")
        elif 'cab' in query or 'car rent' in query:
            m("sir you can get can services from our hotel itself for any location")
        elif 'bus' in query or 'bus adda' in query:
            m("sir you can get bus services at this location")
        elif 'railway' in query or 'rail gadi' in query:
            m("sir you can get railway services at this location")
        else:
            m("sorry i am not able to answer this question")


def reception():
    f("welcome sir how can i help you")
    while True:
        query = takeCommand().lower()
        if 'waiter' in query:
            f("you must go straight and there is waiter")
            guiwait()
        elif 'chef' in query:
            f("you must go straight and there is chef")
            guichef()
        elif 'manager' in query:
            f("you must go straight and there is manager")
            guiman()
        elif 'security' in query:
            f("you must go straight and there is security")
            guisec()
        elif 'exit' in query or 'by' in query or 'sleep' in query or 'jao' in query:
            f("hope i was helpful to u ,sir thank you for using our services")
            sys.exit()
        elif 'map ' in query or 'rasta' in query or 'near' in query:
            f("ok sir here we are")
            webbrowser.open("maps.google.com")
        elif 'location' in query or 'tum kaha se ho' in query:
            f("our location is at google cloud else we also avilable at my master's laptop")
        elif 'medical shop' in query or 'dawaiya' in query or 'dawai ki dukan' in query:
            f("sir you can tell us we can get you the prescribed medicines or you can get that at given location")
        elif 'petrol' in query:
            f("sir you can give us your car's key or you can get that at given location")
        elif 'gas' in query or 'cng' in query:
            f("sir you can give us your car's key or you can get that at given location")
        elif 'cab' in query or 'gaadi' in query:
            f("sir you can get can services from our hotel itself for any location")
        elif 'bus' in query or 'bus adda' in query:
            f("sir you can get bus services at this location")
        elif 'railway' in query or 'railway' in query or 'rail gadi' in query:
            f("sir you can get railway services at this location")
        elif 'room' in query or 'kamra' in query:
            f("sir we have a huge variety of rooms avilable here")
            subprocess.Popen("room.pdf", shell = True)
        elif 'food court' in query or 'khane ki jagah' in query or 'khana' in query:
            f("yes we have one but you have to go left and straight to get the food ")
        elif 'food timings' in query or 'khane ka samay' in query:
            f("sir you can have lunch at 12 am . breakfast form 7 am . snacks anytime between 8 am to 11 pm . and dinner from 7 pm to 11 pm")
        elif 'facilities' in query or 'suvidhaye' in query:
            f("sir we have a huge variety of things to do here like . swimming, food arena, bar, gym, restorant")
        elif 'wi-fi' in query or 'internet' in query:
            f("yes sir we have fully wifi hotel and you can access it with password mai kyu batatau")
        elif 'nearby' in query or 'aas pas' in query or 'ghumne' in query:
            f("sir we have a lot to visit nearby our hotel like taj mahal and burj khalifa")
        elif 'call manager' in query or 'manager ko bulao' in query or 'manager' in query:
            f("ok sir now you can talk to manager")
            guiman()
        elif 'clothes washing' in query or 'kapde dhulwane' in query or 'kapde dhona' in query:
            f("we have our own laundry services you can enquire at this number or at reception itself")
        elif 'reading' in query or 'padhne k liye' in query:
            f("yes sir we have a good bunch of some latest magzines and a good collection of books too")
        else:
            f("sorry i am not able to answer this question")


def manager():
    m("welcome sir i am the hotel manager how can i help you")
    while True:
        query = takeCommand().lower()
        if 'reception' in query:
            m("you must go straight and there is reception")
            guirec()
        elif 'eat' in query:
            m("you must go straight and there is chef")
            guichef()
        elif 'waiter' in query:
            m("you must go straight and there is waiter")
            guiwait()
        elif 'security' in query:
            m("you must go straight and there is security")
            guisec()
        elif 'dirty' in query or 'ganda' in query:
            m("sir i am really sorry for our mistake")
        elif 'map ' in query or 'rasta' in query or 'near' in query:
            m("ok sir here we are")
            webbrowser.open("maps.google.com")
        elif 'bad service' in query or 'bekar service' in query or 'bekar vyavastha' in query:
            m("sir i am really sorry for our mistake")
        elif 'clean room' in query or 'ganda kamra' in query or 'kamra ganda' in query:
            m("ok sir we will doing it as soon as possible")
        elif 'how are you ' in query or 'kaise hai' in query:
            m("i am fine and hope you are also well")
        elif 'time' in query or 'samay' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            m(f"Sir, the time is {strTime}")
        elif 'exit' in query or 'by' in query or 'sleep' in query or 'jao' in query:
            m("hope i was helpful to u ,sir thank you for using our services")
            sys.exit()
        elif 'bad food' in query or 'not good' in query or 'bekar khana' in query:
            m("ok sir we will doing it as soon as possible")
        else:
            m("sorry i am not able to answer this question you can ask the same at reception")


def chef():
    m("welcome sir i am the chef how can i help you")
    while True:
        query = takeCommand().lower()
        if 'reception' in query:
            m("you must go straight and there is reception")
            reception()
        elif 'waiter' in query:
            m("you must go straight and there is waiter")
            waiter()
        elif 'manager' in query:
            m("you must go straight and there is manager")
            manager()
        elif 'security' in query:
            m("you must go straight and there is security")
            sequrity()
        elif 'show menu' in query or 'khana' in query or 'list dekhaiye' in query or 'chinese' in query or 'desi' in query or 'indian' in query:
            m("ok sir here we are.")
            subprocess.Popen("menu.pdf", shell = True)
        elif 'map ' in query or 'rasta' in query or 'near' in query:
            m("ok sir here we are")
            webbrowser.open("maps.google.com")
        elif 'time' in query or 'samay' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            m(f"Sir, the time is {strTime}")
        elif 'exit' in query or 'by' in query or 'sleep' in query or 'jao' in query:
            m("hope i was helpful to u ,sir thank you for using our services")
            sys.exit()
        elif 'bad food' in query or 'not good' in query or 'bekar khana' in query:
            m("ok sir we will improve us as soon as possible")
        else:
            m("sorry i am not able to answer this question you can ask the same at reception")


def waiter():
    m("welcome sir i am here to help you ")
    while True:
        query = takeCommand().lower()
        if 'reception' in query:
            m("you must go straight and there is reception")
            guirec()
        elif 'chef' in query:
            m("you must go straight and there is waiter")
            guichef()
        elif 'manager' in query:
            m("you must go straight and there is manager")
            guiman()
        elif 'security' in query:
            m("you must go straight and there is security")
            guisec()
        elif 'show menu' in query or 'khana' in query or 'list dekhaiye' in query or 'chinese' in query or 'desi' in query or 'indian' in query:
            m("ok sir here we are.")
            subprocess.Popen("menu.pdf", shell = True)
        elif 'map ' in query or 'rasta' in query or 'near' in query:
            m("ok sir here we are")
            webbrowser.open("maps.google.com")
        elif 'time' in query or 'samay' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            m(f"Sir, the time is {strTime}")
        elif 'exit' in query or 'by' in query or 'sleep' in query or 'jao' in query:
            m("hope i was helpful to u ,sir thank you for using our services")
            sys.exit()
        elif 'bad food' in query or 'not good' in query or 'bekar khana' in query:
            m("ok sir we will improve us as soon as possible")
        else:
            m("sorry i am not able to answer this question you can ask the same at reception")

if __name__ == "__main__":
    guihotel()
   
#end of code


