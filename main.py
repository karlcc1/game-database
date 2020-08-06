import time
from tinydb import TinyDB, Query
import os

clear = lambda: os.system('cls')
menu_separator = "=="*50
db = TinyDB('db.json')
Game = Query()

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
    for x in db:
       print(x['title'], x['genre'], x['year'], x['developer'], x['publisher'], x['completed'], sep = ", ")
    print()
    select_menu()

def add_game():
    #clear()
    print(menu_separator)
    print("**Add Game**")
    print()
    print("Please type game info in following format [Title, Genre, Year, Developer, Publisher, Completed [Y/N]]:")
    new_game = input()
    new_game2 = new_game.split(", ")
    db.insert({'title': new_game2[0], 'genre': new_game2[1], 'year': new_game2[2], 'developer': new_game2[3], 'publisher': new_game2[4], 'completed': new_game2[5]})
    print()
    print("New game added!")
    select_menu()

def del_game():
    #clear()
    print(menu_separator)
    print("**Delete game**")
    print()
    game_to_del = input("Please type game title (case-sensitive):")
    print()

    q1 = db.remove(Game.title == game_to_del)
    if q1:
        print(game_to_del + " has been deleted.")
    else:
        print("Game not found!")
    
    select_menu()

def edit_game():
    #clear()
    print(menu_separator)
    print("**Edit game**")
    print()
    game_to_edit = input("Please type game title (case-sensitive):")

    q1 = db.search(Game.title == game_to_edit)
    if q1:
        print("Please type game info in following format [Title, Genre, Year, Developer, Publisher, Completed [Y/N]]:")
        game_edit = input()
        game_edit = game_edit.split(", ")
        db.update({'title': game_edit[0], 'genre': game_edit[1], 'year': game_edit[2], 'developer': game_edit[3], 'publisher': game_edit[4], 'completed': game_edit[5]}, Game.title == game_to_edit)
    else:
        print("Game not found!")
    
    select_menu()

def exit_program():
    print(menu_separator)
    
select_menu()
