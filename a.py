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

#Main Menu

def select_menu():
    print("=="*32)
    print("*Game Database")
    print()
    print("A. Show Library")
    print("B. Add Game")
    print("C. Delete Game")
    print("D. Edit Game")
    print("Z. Exit")
    print()
    menu_letter = input("Input:")
    if menu_letter == "A":
        show_games()
    elif menu_letter == "B":
        add_game()
    elif menu_letter == "C":
        del_game()
    elif menu_letter == "Z":
        exit_program()

def show_games():
    print()
    print("=="*32)
    print("Game Library")
    print()
    for g in games:
        print(g)
    select_menu()

#incomplete
def add_game():
    print("=="*32)
    print("Add new game . . .")
    print()
    print("Please type game info in following format [Title, Genre, Year, Developer, Publisher, Completed (boolean)]:")
    new_game = input()
    #
    #print("New game added!")
    select_menu()

def del_game():
    print("=="*32)
    print("Delete game . . .")
    print()
    game_to_del = input("Please type game title:")
    print()
    for g in games:
        if g.title == game_to_del:
            games.remove(g)
    print(game_to_del + " has been deleted!")
    select_menu()

def exit_program():
    print("Goodbye!")

select_menu()


