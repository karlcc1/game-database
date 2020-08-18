import tkinter as tk
from tinydb import TinyDB, Query

db = TinyDB('db.json')
Gamedb = Query()

gamedetails = ["Title", "Genre", "Year", "Developer", "Publisher", "Completed"]

rowcount = 0
colcount = 0

class Game:
    def __init__(self, master, gridrow, gridcol, gameinfo, gametitle):
        self.gametitle = gametitle
        self.frame = tk.Frame(master, borderwidth=1, relief=tk.SUNKEN)
        self.frame.grid(row=gridrow, column=gridcol, padx=5, pady=5)
        
        self.gamelabel = tk.Label(self.frame, text=gameinfo)
        self.gamelabel.grid(row=0, column=0)
        self.editbutton = tk.Button(self.frame, text="Edit", command=self.editgame)
        self.editbutton.grid(row=0, column=1, sticky="ne")
        self.delbutton = tk.Button(self.frame, text="Delete", command=self.delete)
        self.delbutton.grid(row=0, column=2, padx=1, sticky="ne")

    def delete(self):
        global rowcount
        global colcount
        print(db.remove(Gamedb.title == self.gametitle))
        self.frame.destroy()
        if colcount == 0:
            rowcount -= 1
            colcount = 2
        else:
            colcount -= 1

    def editgame(self):
        def savegame():
            print("savegame()")

            db.update({'title': newtitle.get(), 'genre': newgenre.get(), 'year': newyear.get(), 'developer': newdev.get(), 'publisher': newpub.get(), 'completed': newc.get(), }, Gamedb.title == self.gametitle)
            t = newtitle.get() + "\n" + newgenre.get() + "\n" + newyear.get() + "\n" + newdev.get() + "\n" + newpub.get() + "\n" + newc.get()

            self.gametitle = newtitle.get()
            
            self.gamelabel.destroy()
            self.gamelabel = tk.Label(self.frame, text=t)
            self.gamelabel.grid(row=0, column=0)

            
            
            print(self.gametitle)
            
            edit_window.destroy()
        
        print("editgame()", self.gametitle)
        q = db.search(Gamedb.title == self.gametitle)

        edit_window = tk.Tk()
        edit_window.title("Edit Game")

        titlelabel = tk.Label(edit_window, text = gamedetails[0])
        titlelabel.grid(row=0, column=0)
        newtitle = tk.Entry(edit_window, width=40)
        newtitle.insert(0, self.gametitle)
        newtitle.grid(row=0, column=1, pady=1, padx=2)
        
        genrelabel = tk.Label(edit_window, text = gamedetails[1])
        genrelabel.grid(row=1, column=0)
        newgenre = tk.Entry(edit_window, width=40)
        newgenre.insert(0, q[0]['genre'])
        newgenre.grid(row=1, column=1, pady=1, padx=2)
        
        yearlabel = tk.Label(edit_window, text = gamedetails[2])        
        yearlabel.grid(row=2, column=0)
        newyear = tk.Entry(edit_window, width=40)
        newyear.insert(0, q[0]['year'])
        newyear.grid(row=2, column=1, pady=1, padx=2)
        
        devlabel = tk.Label(edit_window, text = gamedetails[3])
        devlabel.grid(row=3, column=0)
        newdev = tk.Entry(edit_window, width=40)
        newdev.insert(0, q[0]['developer'])
        newdev.grid(row=3, column=1, pady=1, padx=2)
        
        publabel = tk.Label(edit_window, text = gamedetails[4])
        publabel.grid(row=4, column=0)
        newpub = tk.Entry(edit_window, width=40)
        newpub.insert(0, q[0]['publisher'])
        newpub.grid(row=4, column=1, pady=1, padx=2)
        
        clabel = tk.Label(edit_window, text = gamedetails[5])
        clabel.grid(row=5, column=0)
        newc = tk.Entry(edit_window, width=40)
        newc.insert(0, q[0]['completed'])
        newc.grid(row=5, column=1, pady=1, padx=2)

        edit_windowbtn = tk.Button(edit_window, text="Save", command=savegame)
        edit_windowbtn.grid(row=6, column=1, pady=4, padx=4, sticky="ne")
        
        edit_window.mainloop()

def add_game():
    def submit():
        print("submit()")
        db.insert({'title': newtitle.get(), 'genre': newgenre.get(), 'year': newyear.get(), 'developer': newdev.get(), 'publisher': newpub.get(), 'completed': newc.get()})

        global rowcount
        global colcount
        if colcount == 3:
            rowcount += 1
            colcount = 0
            
        t = newtitle.get() + "\n" + newgenre.get() + "\n" + newyear.get() + "\n" + newdev.get() + "\n" + newpub.get() + "\n" + newc.get()
        
        g = Game(rframe, rowcount, colcount, t, x['title'])
        
        colcount += 1
        
        add_window.destroy()
    
    print("add_game()")
    add_window = tk.Tk()
    add_window.title("Add Game")

    titlelabel = tk.Label(add_window, text = gamedetails[0])
    titlelabel.grid(row=0, column=0)
    newtitle = tk.Entry(add_window, width=40)
    newtitle.grid(row=0, column=1, pady=1, padx=2)
    
    genrelabel = tk.Label(add_window, text = gamedetails[1])
    genrelabel.grid(row=1, column=0)
    newgenre = tk.Entry(add_window, width=40)
    newgenre.grid(row=1, column=1, pady=1, padx=2)

    
    yearlabel = tk.Label(add_window, text = gamedetails[2])        
    yearlabel.grid(row=2, column=0)
    newyear = tk.Entry(add_window, width=40)
    newyear.grid(row=2, column=1, pady=1, padx=2)
    
    devlabel = tk.Label(add_window, text = gamedetails[3])
    devlabel.grid(row=3, column=0)
    newdev = tk.Entry(add_window, width=40)
    newdev.grid(row=3, column=1, pady=1, padx=2)
    
    publabel = tk.Label(add_window, text = gamedetails[4])
    publabel.grid(row=4, column=0)
    newpub = tk.Entry(add_window, width=40)
    newpub.grid(row=4, column=1, pady=1, padx=2)
    
    clabel = tk.Label(add_window, text = gamedetails[5])
    clabel.grid(row=5, column=0)
    newc = tk.Entry(add_window, width=40)
    newc.grid(row=5, column=1, pady=1, padx=2)

    add_windowbtn = tk.Button(add_window, text="Add Game", command=submit)
    add_windowbtn.grid(row=6, column=1, pady=4, padx=4, sticky="ne")
    
    add_window.mainloop() 

window = tk.Tk()
window.title("Game Database")

lframe = tk.Frame(window)
rframe = tk.Frame(window, relief=tk.RAISED)
lframe.grid(row=0, column=0, sticky="ns")
rframe.grid(row=0, column=1)

addbutton = tk.Button(lframe, text="Add Game", command=add_game)
addbutton.grid(row=0, column=0, padx=10, pady=5)


for x in db:    
    if colcount == 3:
        rowcount += 1
        colcount = 0
        
    t = x['title'] + "\n" + x['genre'] + "\n" + x['year'] + "\n" + x['developer'] + "\n" + x['publisher'] + "\n" + x['completed']
    
    g = Game(rframe, rowcount, colcount, t, x['title'])
    
    colcount += 1

window.mainloop()
