import tkinter as tk
from tinydb import TinyDB, Query
import gc

db = TinyDB('db.json') #Change if another file needed
Gamedb = Query()

gamedetails = ["Title", "Genre", "Year", "Developer", "Publisher", "Completed"]

rowcount = 0
colcount = 0    #Pointers where to display game frames

class Game:
    def __init__(self, master, gridrow, gridcol, gameinfo, gametitle):
        self.gametitle = gametitle
        self.frame = tk.Frame(master, borderwidth=1, relief=tk.SUNKEN)
        self.frame.grid(row=gridrow, column=gridcol, padx=5, pady=5)
        
        self.gamelabel = tk.Label(self.frame, text=gameinfo)
        self.gamelabel.grid(row=0, column=0)
        self.editbutton = tk.Button(self.frame, text="Edit", command=self.editgame)
        self.editbutton.grid(row=0, column=1, sticky="ne")
        self.delbutton = tk.Button(self.frame, text="Delete", command=self.predelete)
        self.delbutton.grid(row=0, column=2, padx=1, sticky="ne")

    def predelete(self):
        def close():
            predelwindow.destroy()
            self.delete()
            
        predelwindow = tk.Tk()
        predelwindow.title("Delete game")

        space = tk.Label(predelwindow, text="")
        space.pack()
        msg = tk.Label(predelwindow, text="       Are you sure you want to delete " + self.gametitle + "?         ")
        msg.pack()
        space1 = tk.Label(predelwindow, text="")
        space1.pack()

        frame = tk.Frame(predelwindow)

        ybtn = tk.Button(frame, text="Yes", command=close)
        ybtn.pack(side=tk.LEFT, padx=2)

        nbtn = tk.Button(frame, text="No", command=predelwindow.destroy)
        nbtn.pack(side=tk.LEFT)
        frame.pack()

        space2 = tk.Label(predelwindow, text="")
        space2.pack()

    def delete(self):
        global rowcount
        global colcount
        print(db.remove(Gamedb.title == self.gametitle))

        rframe.destroy()
        initgames()
        
##        if colcount == 0:
##            rowcount -= 1
##            colcount = 2
##        else:
##            colcount -= 1

    def editgame(self):
        def savegame():
            print("savegame()")

            if enewtitle.get() == "":
                invalidpopup()

            else:
                db.update({'title': enewtitle.get(), 'genre': enewgenre.get(), 'year': enewyear.get(), 'developer': enewdev.get(), 'publisher': enewpub.get(), 'completed': enewc.get(), }, Gamedb.title == self.gametitle)
                t = enewtitle.get() + "\n" + enewgenre.get() + "\n" + enewyear.get() + "\n" + enewdev.get() + "\n" + enewpub.get() + "\n" + enewc.get()

                self.gametitle = enewtitle.get()
                
                self.gamelabel.destroy()
                self.gamelabel = tk.Label(self.frame, text=t)
                self.gamelabel.grid(row=0, column=0)
                
                print(self.gametitle)
                
                edit_window.destroy()   #Ensures window is closed after save button is clicked

        print("editgame()", self.gametitle)
        q = db.search(Gamedb.title == self.gametitle)
        print(q)
        showgames()

        edit_window = tk.Tk()
        edit_window.title("Edit Game")

        etitlelabel = tk.Label(edit_window, text = gamedetails[0])  #Create title input
        etitlelabel.grid(row=0, column=0)
        enewtitle = tk.Entry(edit_window, width=40)
        enewtitle.insert(0, self.gametitle)
        enewtitle.grid(row=0, column=1, pady=1, padx=2)
        
        egenrelabel = tk.Label(edit_window, text = gamedetails[1])  #Create genre input
        egenrelabel.grid(row=1, column=0)
        enewgenre = tk.Entry(edit_window, width=40)
        enewgenre.insert(0, q[0]['genre'])
        enewgenre.grid(row=1, column=1, pady=1, padx=2)
        
        eyearlabel = tk.Label(edit_window, text = gamedetails[2])   #Create year input
        eyearlabel.grid(row=2, column=0)
        enewyear = tk.Entry(edit_window, width=40)
        enewyear.insert(0, q[0]['year'])
        enewyear.grid(row=2, column=1, pady=1, padx=2)
        
        edevlabel = tk.Label(edit_window, text = gamedetails[3])    #Create developer input
        edevlabel.grid(row=3, column=0)
        enewdev = tk.Entry(edit_window, width=40)
        enewdev.insert(0, q[0]['developer'])
        enewdev.grid(row=3, column=1, pady=1, padx=2)
        
        epublabel = tk.Label(edit_window, text = gamedetails[4])    #Create publisher input
        epublabel.grid(row=4, column=0)
        enewpub = tk.Entry(edit_window, width=40)
        enewpub.insert(0, q[0]['publisher'])
        enewpub.grid(row=4, column=1, pady=1, padx=2)
        
        eclabel = tk.Label(edit_window, text = gamedetails[5])  #Create completed input
        eclabel.grid(row=5, column=0)
        enewc = tk.Entry(edit_window, width=40)
        enewc.insert(0, q[0]['completed'])
        enewc.grid(row=5, column=1, pady=1, padx=2)

        edit_windowbtn = tk.Button(edit_window, text="Save", command=savegame) #Create save button
        edit_windowbtn.grid(row=6, column=1, pady=4, padx=55, sticky="e")

        cancelbtn = tk.Button(edit_window, text="Cancel", command=edit_window.destroy)  #Create cancel button
        cancelbtn.grid(row=6, column=1, pady=4, padx=4, sticky="e")
        
        edit_window.mainloop()

def initgames():
    global rowcount
    global colcount
    rowcount = 0
    colcount = 0

    global rframe
    rframe = tk.Frame(window, relief=tk.RAISED)
    rframe.grid(row=0, column=1)
    
    for x in db:    
        if colcount == 3:
            rowcount += 1
            colcount = 0
        
        t = x['title'] + "\n" + x['genre'] + "\n" + x['year'] + "\n" + x['developer'] + "\n" + x['publisher'] + "\n" + x['completed']
        
        g = Game(rframe, rowcount, colcount, t, x['title'])
    
        colcount += 1

def invalidpopup():
    popupwindow = tk.Tk()
    popupwindow.title("Invalid input")

    space = tk.Label(popupwindow, text="")
    space.pack()
    msg = tk.Label(popupwindow, text="       Invalid input! Please enter a game title.         ")
    msg.pack()
    space1 = tk.Label(popupwindow, text="")
    space1.pack()

    btn = tk.Button(popupwindow, text="Okay", command=popupwindow.destroy)
    btn.pack()

    space2 = tk.Label(popupwindow, text="")
    space2.pack()

def add_game(): 
    def submit():
        print("submit()")

        if newtitle.get() == "":
            invalidpopup()

        else:
            db.insert({'title': newtitle.get(), 'genre': newgenre.get(), 'year': newyear.get(), 'developer': newdev.get(), 'publisher': newpub.get(), 'completed': newc.get()})

            global rowcount
            global colcount
            if colcount == 3:
                rowcount += 1
                colcount = 0
                
            t = newtitle.get() + "\n" + newgenre.get() + "\n" + newyear.get() + "\n" + newdev.get() + "\n" + newpub.get() + "\n" + newc.get()
          
            g = Game(rframe, rowcount, colcount, t, newtitle.get()) #Create the new game
            
            colcount += 1
            
            add_window.destroy()    
    
    print("add_game()")
    add_window = tk.Tk()
    add_window.title("Add Game")

    titlelabel = tk.Label(add_window, text = gamedetails[0]+"*")    #Create title input
    titlelabel.grid(row=0, column=0)
    newtitle = tk.Entry(add_window, width=40)
    newtitle.grid(row=0, column=1, pady=1, padx=2)
    
    genrelabel = tk.Label(add_window, text = gamedetails[1])    #Create genre input
    genrelabel.grid(row=1, column=0)
    newgenre = tk.Entry(add_window, width=40)
    newgenre.grid(row=1, column=1, pady=1, padx=2)

    
    yearlabel = tk.Label(add_window, text = gamedetails[2]) #Create year input
    yearlabel.grid(row=2, column=0)
    newyear = tk.Entry(add_window, width=40)
    newyear.grid(row=2, column=1, pady=1, padx=2)
    
    devlabel = tk.Label(add_window, text = gamedetails[3])  #Create developer input
    devlabel.grid(row=3, column=0)
    newdev = tk.Entry(add_window, width=40)
    newdev.grid(row=3, column=1, pady=1, padx=2)
    
    publabel = tk.Label(add_window, text = gamedetails[4])  #Create publisher input
    publabel.grid(row=4, column=0)
    newpub = tk.Entry(add_window, width=40)
    newpub.grid(row=4, column=1, pady=1, padx=2)
    
    clabel = tk.Label(add_window, text = gamedetails[5])    #Create completed input
    clabel.grid(row=5, column=0)
    newc = tk.Entry(add_window, width=40)
    newc.grid(row=5, column=1, pady=1, padx=2)

    add_windowbtn = tk.Button(add_window, text="Add Game", command=submit)  #Create add game button
    add_windowbtn.grid(row=6, column=1, pady=4, padx=55, sticky="e")

    cancelbtn = tk.Button(add_window, text="Cancel", command=add_window.destroy)  #Create cancel button
    cancelbtn.grid(row=6, column=1, pady=4, padx=4, sticky="e")
    
    add_window.mainloop()

def showgames():
    print("-------------------------------------gc-----------------------------------------")
    for obj in gc.get_objects():
        if isinstance(obj, Game):
            print(obj, obj.gametitle)
    print("-------------------------------------gc-----------------------------------------")

window = tk.Tk()
window.title("Game Database")

lframe = tk.Frame(window)
lframe.grid(row=0, column=0, sticky="ns")
addbutton = tk.Button(lframe, text="Add Game", command=add_game)
addbutton.grid(row=0, column=0, padx=10, pady=5)

initgames()
showgames()

window.mainloop()
