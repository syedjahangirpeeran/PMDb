from tkinter import *
import random
import time
import tkinter.messagebox
import requests
'''print("\nDo you want to continue(any key) or quit(q)? :")
q=input()
if(q=='q'):
break'''
def btnClick(text):
    global operator
    operator = str(text)
    text_input.set(operator)
    user_input = str(text)
    listbox.delete(0,END)
    listbox.insert(END,'Retrieving results..\n')
    listbox.insert(END,' ')

    def func(user_input):
        url = "http://www.imdb.com/genre/" + user_input
        s = requests.get(url)
        justText = s.text
        f = 1
        for i in range(len(justText)):
            if (justText[i:i + 18] == '<a href="/title/tt' and justText[i + 19:i + 35].find("title") != -1):
                s=""
                j = i + 35
                while (justText[j] != '"'):
                    s+=justText[j]
                    j += 1
                    f = 0
                listbox.insert(END, s)
        if (f):
            print("We're afraid no such Genre exits :(")

    func((user_input).title())

def btnClick1(text):
    global operator
    operator = str(text)
    text_input.set(operator)
    user_input = str(text)
    listbox.delete(0,END)
    listbox.insert(END,'Retrieving results..')

    def topGlobal():
        url = "http://www.imdb.com/chart/top?ref_=nv_mv_250_6"
        s = requests.get(url)
        print(s)
        justText = s.text
        listbox.insert(END,'\nThe Top 250 Rated movies are:\n')
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 70 + "+" + "-" * 15 + "+")
        listbox.insert(END,"|"+ "Rank".center(12)+ "|"+ "Ratings".center(13)+ "|"+ "Movie Names".center(68)+ "|")
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 70 + "+" + "-" * 15 + "+")
        c = 0
        for i in range(len(justText)):
            if (justText[i:i + 18] == '<a href="/title/tt' and justText[i + 180:i + 1000].find("width") == -1):
                # print("|"+(str(c)+". ").center(14),end="|")
                c += 1
                j = i + 10
                while (justText[j] != '>'):
                    j += 1
                j += 1
                name = ""
                while (justText[j:j + 4] != '</a>'):
                    name += justText[j]
                    j += 1
                # print("\t",end="")
                while (j < len(justText) and justText[j:j + 9] != "</strong>"):
                    j += 1
                # print(name.center(46),justText[j-3:j].center(12),"|")
                listbox.insert(END,"|"+ str(c).center(16)+ "|"+ justText[j - 3:j].center(18)+ "|" + name.center(68))
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 70 + "+" + "-" * 15 + "+")

    def topRatedTamil():
        url = "http://www.imdb.com/india/top-rated-tamil-movies"
        s = requests.get(url)
        justText = s.text
        listbox.insert(END,"\nThe Top 50 Tamil movies are:\n")
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 50 + "+" + "-" * 15 + "+")
        listbox.insert(END,"|"+ "Rank".center(12)+ "|"+ "Ratings".center(13)+ "|"+ "Movie Names".center(48)+ "|")
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 50 + "+" + "-" * 15 + "+")
        c = 0
        for i in range(len(justText)):
            if (justText[i:i + 18] == '<a href="/title/tt' and justText[i + 180:i + 1000].find("width") == -1):
                # print("|"+(str(c)+". ").center(14),end="|")
                c += 1
                j = i + 10
                while (justText[j] != '>'):
                    j += 1
                j += 1
                name = ""
                while (justText[j:j + 4] != '</a>'):
                    name += justText[j]
                    j += 1
                # print("\t",end="")
                while (j < len(justText) and justText[j:j + 9] != "</strong>"):
                    j += 1
                # print(name.center(46),justText[j-3:j].center(12),"|")
                listbox.insert(END,"|"+ str(c).center(12)+ "|"+ justText[j - 3:j].center(13)+ "|"+ name.center(48))
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 50 + "+" + "-" * 15 + "+")

    def topRatedTelugu():
        url = "http://www.imdb.com/india/top-rated-telugu-movies"
        s = requests.get(url)
        justText = s.text
        listbox.insert(END,"\nThe Top 50 Telugu movies are:\n")
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 50 + "+" + "-" * 15 + "+")
        listbox.insert(END,"|"+ "Rank".center(12)+"|"+ "Ratings".center(13)+ "|"+ "Movie Names".center(48)+  "|")
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 50 + "+" + "-" * 15 + "+")
        c = 0
        for i in range(len(justText)):
            if (justText[i:i + 18] == '<a href="/title/tt' and justText[i + 180:i + 1000].find("width") == -1):
                # print("|"+(str(c)+". ").center(14),end="|")
                c += 1
                j = i + 10
                while (justText[j] != '>'):
                    j += 1
                j += 1
                name = ""
                while (justText[j:j + 4] != '</a>'):
                    name += justText[j]
                    j += 1
                # print("\t",end="")
                while (j < len(justText) and justText[j:j + 9] != "</strong>"):
                    j += 1
                # print(name.center(46),justText[j-3:j].center(12),"|")
                listbox.insert(END,"|"+ str(c).center(12)+ "|"+ justText[j - 3:j].center(13)+"|"+ name.center(48))
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 50 + "+" + "-" * 15 + "+")

    def topIndian():
        url = "http://www.imdb.com/india/top-rated-indian-movies"
        s = requests.get(url)
        justText = s.text
        listbox.insert(END,"\nThe Top Indian movies are:\n")
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 50 + "+" + "-" * 15 + "+")
        listbox.insert(END,"|"+ "Rank".center(12)+ "|"+ "Ratings".center(13)+ "|"+ "Movie Names".center(48)+ "|")
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 50 + "+" + "-" * 15 + "+")
        c = 0
        for i in range(len(justText)):
            if (justText[i:i + 18] == '<a href="/title/tt' and justText[i + 180:i + 1000].find("width") == -1):
                # print("|"+(str(c)+". ").center(14),end="|")
                c += 1
                j = i + 10
                while (justText[j] != '>'):
                    j += 1
                j += 1
                name = ""
                while (justText[j:j + 4] != '</a>'):
                    name += justText[j]
                    j += 1
                # print("\t",end="")
                while (j < len(justText) and justText[j:j + 9] != "</strong>"):
                    j += 1
                # print(name.center(46),justText[j-3:j].center(12),"|")
                listbox.insert(END,"|"+ str(c).center(12)+ "|" +justText[j - 3:j].center(13)+ "|"+ name.center(48))
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 50 + "+" + "-" * 15 + "+")

    def topTv():
        url = "http://www.imdb.com/chart/toptv/"
        s = requests.get(url)
        justText = s.text
        listbox.insert(END,"\nThe Top Rated TV shows are:\n")
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 60 + "+" + "-" * 15 + "+")
        listbox.insert(END,"|"+ "Rank".center(12)+ "|"+ "Ratings".center(13)+ "|"+ "TV Show Names".center(58)+ "|")
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 60 + "+" + "-" * 15 + "+")
        c = 0
        for i in range(len(justText)):
            if (justText[i:i + 18] == '<a href="/title/tt' and justText[i + 180:i + 1000].find("width") == -1):
                # print("|"+(str(c)+". ").center(14),end="|")
                c += 1
                j = i + 10
                while (justText[j] != '>'):
                    j += 1
                j += 1
                name = ""
                while (justText[j:j + 4] != '</a>'):
                    name += justText[j]
                    j += 1
                # print("\t",end="")
                while (j < len(justText) and justText[j:j + 9] != "</strong>"):
                    j += 1
                # print(name.center(46),justText[j-3:j].center(12),"|")
                listbox.insert(END,"|"+ str(c).center(12)+ "|"+ justText[j - 3:j].center(13)+ "|"+ name.center(58))
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 60 + "+" + "-" * 15 + "+")

    def popularTv():
        url = "http://www.imdb.com/chart/tvmeter"
        s = requests.get(url)
        justText = s.text
        listbox.insert(END,"\nThe Popular TV shows are:\n")
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 60 + "+" + "-" * 15 + "+")
        listbox.insert(END,"|"+ "Rank".center(12)+ "|"+ "Ratings".center(13)+ "|"+ "TV Show Names".center(58)+ "|")
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 60 + "+" + "-" * 15 + "+")
        c = 0
        for i in range(len(justText)):
            if (justText[i:i + 18] == '<a href="/title/tt' and justText[i + 180:i + 1000].find("width") == -1):
                # print("|"+(str(c)+". ").center(14),end="|")
                c += 1
                j = i + 10
                while (justText[j] != '>'):
                    j += 1
                j += 1
                name = ""
                while (justText[j:j + 4] != '</a>'):
                    name += justText[j]
                    j += 1
                # print("\t",end="")
                while (j < len(justText) and justText[j:j + 9] != "</strong>"):
                    j += 1
                # print(name.center(46),justText[j-3:j].center(12),"|")
                listbox.insert(END,"|"+ str(c).center(12)+ "|" + justText[j - 3:j].center(13)+ "|"+ name.center(58))
        listbox.insert(END,"+" + "-" * 14 + "+" + "-" * 60 + "+" + "-" * 15 + "+")

    def boxOffice():
        url = "http://www.imdb.com/chart/boxoffice"
        s = requests.get(url)
        justText = s.text
        # print(justText)
        c = 0
        for i in range(len(justText)):
            if (justText[i:i + 18] == '<a href="/title/tt' and justText[i + 180:i + 1000].find("width") == -1):
                # print("|"+(str(c)+". ").center(14),end="|")
                c += 1
                j = i + 10
                while (justText[j] != '>'):
                    j += 1
                j += 1
                name = ""
                while (justText[j:j + 4] != '</a>'):
                    name += justText[j]
                    j += 1
                listbox.insert(END,name)
    if user_input == "Top Global":
        topGlobal()
    elif user_input == "Top Indian":
        topIndian()
    elif user_input == "Top Telugu":
        topRatedTelugu()
    elif user_input == "Top Tamil":
        topRatedTamil()
    elif user_input == "Top TV":
        topTv()
    elif user_input == "Popular TV":
        popularTv()
    else:
        boxOffice()

root = Tk()

#Size
root.geometry('1200x650+0+0')
root.title('Python based Movie Database')

#Background
Tops= Frame(root, width = 1200,height=40, bg="purple", relief=SUNKEN)
Tops.pack(side=TOP)

f1= Frame(root, width = 1000,height = 700, relief=SUNKEN)
f1.pack(side=LEFT)

f2= Frame(root, width = 600,height=700, bg="purple", relief=SUNKEN)
f2.pack(side=RIGHT)

#Image
photo = PhotoImage(file="iiits-logo.png")
label = Label(Tops, image = photo)
label.pack(side=LEFT)

#TIME
localtime = time.asctime(time.localtime(time.time()))

#Title
lblInfo = Label(Tops, font=('arial',50),text="Python based Movie Database", fg="Steel Blue",bd=10, anchor='w' )
lblInfo.pack(side=LEFT)
lblInfo = Label(Tops, font=('arial',9),text="            V Tejkiran             ", fg="Steel Blue",bd=9, anchor='w' )
lblInfo.pack()
lblInfo = Label(Tops, font=('arial',9),text=localtime, fg="Steel Blue",bd=8, anchor='w' )
lblInfo.pack()
lblInfo = Label(Tops, font=('arial',9),text="       Syed Jahangir          ", fg="Steel Blue",bd=8, anchor='w' )
lblInfo.pack()

lblReference = Label(f1, font=('arial',20),text="Welcome to PMDb...!", fg="black", bd=10, anchor='w')
lblReference.grid(row=0, columnspan=2)
lblReference = Label(f1, font=('arial',10),text="Click on the button to select an option and proceed.", fg="black", bd=10, anchor='w' )
lblReference.grid(row=1,columnspan=2)

#Text input
text_input=StringVar()
txtReference=Entry(f1, font=('arial',10),textvariable=text_input, fg="black",bd=10, insertwidth=3, bg="light blue" , justify ="right")
txtReference.grid(row=1, column=2)

#Buttons
b1 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Animation"), font=('arial', 13), text="Animation")
b2 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Biography"), font=('arial', 13), text="Biography")
b3 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Comedy"), font=('arial', 13), text="Comedy")
b4 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Crime"), font=('arial', 13), text="Crime")
b5 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Documentary"), font=('arial', 13), text="Documentary")
b6 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Drama"), font=('arial', 13), text="Drama")
b7 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Family"), font=('arial', 13), text="Family")
b8 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Fantasy"), font=('arial', 13), text="Fantasy")
b9 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Film-Noir"), font=('arial', 13), text="Film-Noir")
b10 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("History"), font=('arial', 13), text="History")
b11 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Horror"), font=('arial', 13), text="Horror")
b12 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Music"), font=('arial', 13), text="Music")
b13 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Musical"), font=('arial', 13), text="Musical")
b14 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Mystery"), font=('arial', 13), text="Mystery")
b15 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Romance"), font=('arial', 13), text="Romance")
b16 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Sci-Fi"), font=('arial', 13), text="Sci-Fi")
b17 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Sport"), font=('arial', 13), text="Sport")
b18 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Thriller"), font=('arial', 13), text="Thriller")
b19 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("War"), font=('arial', 13), text="War")
b20 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick("Western"), font=('arial', 13), text="Western")
b21 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick1("Top Global"), font=('arial', 13), text="Top Global")
b22 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick1("Top Indian"), font=('arial', 13), text="Top Indian")
b23 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick1("Top Telugu"), font=('arial', 13), text="Top Telugu")
b24 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick1("Top Tamil"), font=('arial', 13), text="Top Tamil")
b25 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick1("Top TV"), font=('arial', 13), text="Top TV")
b26 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick1("Popular TV"), font=('arial', 13), text="Popular TV")
b27 = Button(f1, width=10, height=1, padx=8, bd=5, fg='black', bg="#3399ff", command=lambda:btnClick1("Now-Playing"), font=('arial', 13), text="Now-Playing")
b27.grid(row=14, column=2)
b25. grid(row=10, column=2)
b26. grid(row=12, column=2)
b23. grid(row=6, column=2)
b24. grid(row=8, column=2)
b22. grid(row=4, column=2)
b1. grid(row=2, column=0)
b2. grid(row=2, column=1)
b3. grid(row=4, column=0)
b4. grid(row=4, column=1)
b5.grid(row=6, column=0)
b6.grid(row=6, column=1)
b7.grid(row=8, column=0)
b8.grid(row=8, column=1)
b9.grid(row=10, column=0)
b10.grid(row=10, column=1)
b11.grid(row=12, column=0)
b12.grid(row=12, column=1)
b13.grid(row=14, column=0)
b14.grid(row=14, column=1)
b15.grid(row=18, column=2)
b16.grid(row=18, column=0)
b17.grid(row=18, column=1)
b18.grid(row=16, column=2)
b19.grid(row=16, column=1)
b20.grid(row=16, column=0)
b21.grid(row=2, column=2)

#Display
scrollbar = Scrollbar(f2, orient=VERTICAL)
listbox = Listbox(f2, yscrollcommand=scrollbar.set, width=100, height=17, bg="#b3b3cc")
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=1)

'''
# Mainmenu
menu1 = Menu(root)
root.config(menu=menu1)
submenu = Menu(menu1)
menu1.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Project...", command=doNothing)
submenu.add_command(label="New", command=doNothing)
submenu.add_separator()
submenu.add_command(label="Exit", command=doNothing)
editMenu = Menu(menu1)
menu1.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=doNothing)

# Toolbar
toolbar = Frame(root, bg="grey")
insertbutton = Button(toolbar, text="Insert Image", command=doNothing)
insertbutton.pack(side=LEFT, padx=2, pady=2)
printButton = Button(toolbar, text="Print Image", command=doNothing)
printButton.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

canvas = Canvas(root, width=1200, height=600)
canvas.pack()
blackline = canvas.create_line(0,0,200,50,fill="green")

# Status Bar
status = Label(root, text="You are using movie Database....", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=Y)
'''
#Messagebox
tkinter.messagebox.showinfo('PMDb', 'Welcome to PMDb....!\n\t -Jahangir & Tejkiran')
'''
answer = tkinter.messagebox.askquestion('Question 1', 'Are you a movie enthusiast?')

if answer == 'yes':
    tkinter.messagebox.showinfo('PMDb', 'Your fun ride starts here.')
else:
    tkinter.messagebox.showinfo('PMDb', 'Then this is not what you are looking for.')

'''
root.mainloop()