#CREATED BY ARYAN KARN
#Feel free to implement new stufs on github
#Student of Mnnit Allahabad
import random
from tkinter import *  #Do rebember tkinter is a built in function no need to install
import string

#Creating a function
def generate_password():
    password=[ ]   #Total of 15 characters will be made
    for i in range(5):
        #! @ # $ %--- () all these are ascii_letters
        alpha=random.choice(string.ascii_letters)
        #A b c R  any alphabate no
        symbol=random.choice(string.punctuation)
        #For random no's
        numbers=random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)

    #This is used to take out all the 15 different characters and display them
    y="".join(str(x)for x in password)
    lbl.config(text=y)

root=Tk()
#Colouring the Block
root.title("Booring project")
root.configure(background='purple')


root.geometry("300x200")
btn=Button(root,text="GENERATE PASSWORD", command=generate_password)
btn.grid(row=8,column=2)
lbl=Label(root,font=("times",15,"bold"))
lbl.grid(row=4,column=2)
root.mainloop()
