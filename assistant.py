from pydoc import text
import requests
import tkinter as tk
from tkinter import *
import os
from turtle import color




rt = Tk()

rt.title("UniProt Assistant")
rt.geometry("445x750+150+50")
rt.configure(bg="#00639a")
rt.resizable(False,False)

#icon
#img_icon = PhotoImage(file="up.png")
#rt.iconphoto(False,img_icon)

#UniProt label
label_DB = Label(rt,width=1000,height=5,text="You can view and download files\n from the UniProt databases using the UniProt ID\n and choosing the file format\n\nPlease choose the database and file format below",font=("arial",10))
label_DB.pack()

#working

db = ""
tp = ""
def click1(key1):
    if key1 == "UniProtKB":
        db = "uniprot"

    elif key1 == "UniParc":   
        db = "uniparc" 

    elif key1 == "UniRef":
        db = "uniref" 
    else:
        v="Error"    
      

def click2(key2):        
    if key2 == "Text":
        tp = "text"

    elif key2 == "Fasta":
        tp = "fasta"

    elif key2 == "XML":
        tp = "xml"    

    else:
        v="Error"  



#Buttons
#Database
Button(rt,text="UniProtKB", width=10, height=1, font=("arial",10,"bold"), bd=1, bg="#f2f2f2",command=lambda: click1(text)).place(x=50,y=100)
Button(rt,text="UniParc", width=10, height=1, font=("arial",10,"bold"), bd=1, bg="#f2f2f2",command=lambda:click1(text)).place(x=175,y=100)
Button(rt,text="UniRef", width=10, height=1, font=("arial",10,"bold"), bd=1, bg="#f2f2f2",command=lambda:click1(text)).place(x=300,y=100)
print(db)  

#Filename
Button(rt,text="Text", width=10, height=1, font=("arial",10,"bold"), bd=0.5, bg="#f2f2f2",command=lambda:click2("Text")).place(x=50,y=130)
Button(rt,text="Fasta", width=10, height=1, font=("arial",10,"bold"), bd=0.5, bg="#f2f2f2",command=lambda:click2("Fasta")).place(x=175,y=130)
Button(rt,text="XML", width=10, height=1, font=("arial",10,"bold"), bd=0.5, bg="#f2f2f2",command=lambda:click2("XML")).place(x=300,y=130)
print(tp) 

#clear
Button(rt,text="Clear", width=10, height=1, font=("arial",10,"bold"), bd=0.5, bg="#f2f2f2").place(x=100,y=670)
Button(rt,text="Download", width=10, height=1, font=("arial",10,"bold"), bd=0.5, bg="#f2f2f2").place(x=260,y=670)

#queryinput
qu=""
def query():
    qu=entry1.get()
    print(qu)
    return None

val = StringVar()
val.set("Enter your UniProt here")

entry1 = Entry(rt,textvar=val, font=("lucida",12), foreground="#737373")
entry1.place(width=300, height=45, x=70,y=170)
Button(rt, text="Search", command=query).place(x=190,y=220)



#Display window
file_frame = tk.LabelFrame(rt, text="Display",font=("arial",10))
file_frame.place(height=350, width=445, rely=0.35, relx=0)



url = "https://rest.uniprot.org/"+db+"/"+qu+"."+tp
print(url)
r = requests.get(url)
f = open("scrap2out.txt","w")
f.write(r.text)
f.close

rt.mainloop()
