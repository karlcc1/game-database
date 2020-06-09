#Game Database Application

class Game:
    def __init__(self, title, genre, year, developer, publisher, completed):
        self.title = title
        self.genre = genre
        self.year = year
        self.developer = developer
        self.publisher = publisher
        self.completed = completed

    def __str__(self):
        return self.title + ", " + self.genre + ", " + str(self.year) + ", " \
                + self.developer + ", " + self.publisher + ", " + str(self.completed)
    

game1 = Game("Resistance: Fall of Man", "FPS", 2006, "Insomniac", "Sony Interactive", False)
game2 = Game("God of War III", "Adventure", 2010, "SIE", "Sony Computer", False)
game3 = Game("Far Cry 2", "FPS", 2008, "Ubisoft", "Ubisoft", True)
game4 = Game("Assassin's Creed III", "Adventure", 2012, "Ubisoft", "Ubisoft", True)

games = []
games.append(game1)
games.append(game2)
games.append(game3)
games.append(game4)

def show_games():
    print()
    print("=="*32)
    print("Game Library")
    print()
    for g in games:
        print(g)

print("Game Database")
print()
print("A. Show Library")
print("Z. Exit")
print()
print("Input:")
menu_select = input()

if menu_select == "A":
    show_games()
