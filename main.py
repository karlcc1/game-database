import time
import os
clear = lambda: os.system('cls')
menu_separator = "=="*50

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
    
#Initial games
"""game1 = Game("Resistance: Fall of Man", "FPS", 2006, "Insomniac", "Sony Interactive", False)
game2 = Game("God of War III", "Adventure", 2010, "SIE", "Sony Computer", False)
game3 = Game("Far Cry 2", "FPS", 2008, "Ubisoft", "Ubisoft", True)
game4 = Game("Assassin's Creed III", "Adventure", 2012, "Ubisoft", "Ubisoft", True)

games = []
games.append(game1)
games.append(game2)
games.append(game3)

games.append(game4)"""

#Interact w/ txt files
games = []
f = open("PS3.txt", "r")
if f.mode == 'r':
    contents = f.readlines()
    #print(contents)
    for c in contents:
            c1 = str.rstrip(c)
            c2 = c1.split(", ")
            game = Game(c2[0], c2[1], c2[2], c2[3], c2[4], c2[5])
            games.append(game)
#print(str(games[0]))

def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

#Main Menu
def select_menu():
    #clear()
    print(menu_separator)
    print("**Welcome to your Game Database. Choose an option:**")
    print()
    print("A. Show Library")
    print("B. Add Game")
    print("C. Edit Game")
    print("D. Delete Game")
    print("Z. Exit")
    print()
    menu_letter = input("Input:")
    if menu_letter == "A" or menu_letter == "a":
        show_games()
    elif menu_letter == "B" or menu_letter == "b":
        add_game()
    elif menu_letter == "C" or menu_letter == "c":
        edit_game()
    elif menu_letter == "D" or menu_letter == "d":
        del_game()
    elif menu_letter == "Z" or menu_letter == "z":
        exit_program()

def show_games():
    #clear()
    print()
    print(menu_separator)
    print("**Game Library**")
    print()
    for g in games:
        print(g)
    print()
    print(str(len(games)) + " games total")
    select_menu()

def add_game():
    #clear()
    print(menu_separator)
    print("**Add Game**")
    print()
    print("Please type game info in following format [Title, Genre, Year, Developer, Publisher, Completed [Y/N]]:")
    new_game = input()
    try:
        new_game2 = new_game.split(", ")
        game = Game(new_game2[0], new_game2[1], new_game2[2], new_game2[3], new_game2[4], new_game2[5])
        games.append(game)
        print()
        print("New game added!")
    except:
        print("Invalid format!")
    select_menu()

def del_game():
    #clear()
    print(menu_separator)
    print("**Delete game**")
    print()
    game_to_del = input("Please type game title (case-sensitive):")
    print()
    if contains(games, lambda x: x.title == game_to_del):
        del_input = input("Deleting " + game_to_del + ". Are you sure? [Y/N]: ")
        if del_input == "Y" or del_input == "y":
            for g in games:
                if g.title == game_to_del:
                    games.remove(g)
            print(game_to_del + " has been deleted!")
        elif del_input == "N" or del_input == "n":
            select_menu()
        else:
            print("Invalid input!")
            select_menu()
    else:
        print("Game not found!")
    select_menu()

def edit_game():
    #clear()
    print(menu_separator)
    print("**Edit game**")
    print()
    game_to_edit = input("Please type game title (case-sensitive):")
    if contains(games, lambda x: x.title == game_to_edit):
        print()
        edit_form = input("Enter new game details:")
        try:
            print()
            for g in games:
                if g.title == game_to_edit:
                    games.remove(g)
            edit_form2 = edit_form.split(", ")
            game = Game(edit_form2[0], edit_form2[1], edit_form2[2], edit_form2[3], edit_form2[4], edit_form2[5])
            games.append(game)
            print(game_to_edit + " has been edited!")
        except:
            print("Invalid format!")
    else:
        print("Game not found!")
    select_menu()

def exit_program():
    print(menu_separator)
    exit_input = input("Are you sure you want to exit? [Y/N]: ")
    if exit_input == "Y" or exit_input == "y":
        print("Goodbye!")
        f = open("PS3.txt", "w")
        for g in games:
            f.write(str(g) + "\n")
        time.sleep(0.5)
    elif exit_input == "N" or exit_input == "n":
        select_menu()
    else:
        print("Invalid input!")
        select_menu()

select_menu()
