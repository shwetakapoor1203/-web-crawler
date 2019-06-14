from tkinter import *
import requests
#import tkHyperlinkManager
from bs4 import BeautifulSoup

answer_val =[]


def crawl(url):
    ans=[]
    if url!=None:
        r = requests.get("https://"+url)
        data = r.text
        soup = BeautifulSoup(data,"lxml")
        for link in soup.find_all('a'):
            print(link.get('href'))
            if link.get('href')!=None:
                ans.append(link.get('href')+"\r\n\r")
    return ans


def get_me():
    url=entry.get()
    answer_val=crawl(url)
    answer_url.delete(0.1,END)
    answer_url.insert(INSERT,answer_val)

root=Tk()                     

root.title("chihiro")
label1=Label(root, text='"chihiro"', anchor=CENTER, font=("Maiandra GD", 30),foreground="Green")
label1.pack()               
label2=Label(root, text="crawl the web", anchor=CENTER, font=("Algerian", 20), foreground="Red")
label2.pack()                   


topframe=Frame(root)

entry=Entry(topframe, bd=5, width=40)
entry.bind('<Return>', lambda _: get_me())
entry.pack()                       
button=Button(topframe, text="Crawl", width=15, height=1, font=("Algerian",10), command=get_me)
button.pack()

topframe.pack(side=TOP)


bottomframe=Frame(root)

scroll=Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)

answer_url=Text(bottomframe, width=100, height=30, yscrollcommand=scroll.set, wrap=WORD, state=NORMAL)
scroll.config(command=answer_url.yview)
answer_url.pack()

bottomframe.pack(side=BOTTOM)

root.mainloop()                      