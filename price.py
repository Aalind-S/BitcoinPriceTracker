from tkinter import *
from tkinter import ttk
import PIL
from PIL import ImageTk, Image
from turtle import width
import requests
import json


col1 = "white"
col2 = "#333333"
col3 = "#000000"

window = Tk()
window.title(' ')
window.geometry('320x350')
window.configure(bg=col1)


def info():
    api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CINR%2CCAD"
    r = requests.get(api_link)
    dic = r.json()
    usd_value = float(dic["USD"])
    usd_formatted = "${:,.3f}".format(usd_value)
    usd["text"] = usd_formatted


frame_head = Frame(window, width=320, height=50, bg=col1)
frame_head.grid(row=1, column=0)

frame_body = Frame(window, width=320, height=300, bg=col2)
frame_body.grid(row=2, column=0)

image_1 = Image.open('images/logobit.png')
image_1 = image_1.resize((30, 30))
image_1 = ImageTk.PhotoImage(image_1)

icon_1 = Label(frame_head, image=image_1, bg=col1)
icon_1.place(x=10, y=10)

name = Label(frame_head, text="Bitcoin Price Tracker", bg=col1, padx=0,
             fg=col3, anchor="center", height=1, width=18, font=('Poppins 15'))
name.place(x=50, y=10)

usd = Label(frame_body, text="$0000", height=1, font=(
    'Arial 30 bold'), width=14, bg=col2, fg=col1, anchor="center")
usd.place(x=0, y=28)

euros = Label(frame_body, text="$0000", height=1, font=(
    'Arial 15 bold'), bg=col2, fg=col1, anchor="center")
euros.place(x=10, y=130)
cad = Label(frame_body, text="$0000", height=1, font=(
    'Arial 15 bold'), bg=col2, fg=col1, anchor="center")
cad.place(x=10, y=170)
inr = Label(frame_body, text="$0000", height=1, font=(
    'Arial 15 bold'), bg=col2, fg=col1, anchor="center")
inr.place(x=10, y=210)

info()

window.mainloop()
