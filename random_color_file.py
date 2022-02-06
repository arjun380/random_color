from tkinter import *
import random

root=Tk()
root.title("Dictionary")
root.geometry("600x400")

dictionary = {"colour" :["#ff0000","#2a3f49","#7e7e49","#57e9ac","#cd54ac","#6f544f"]}

def bg_change():
    random_no =random.randint(0,5)
    print(dictionary["colour"][random_no])
    root.configure(background = dictionary["colour"][random_no])

btn = Button(root,text = "click me", command = bg_change)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()