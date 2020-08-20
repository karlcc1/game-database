# game_database

A simple game database application to display current PS3 games in my collection.

I was thinking of keeping track of the games I currently owned. I was using just a .txt file with a list, then an Excel file. So why not build a program?

I started off with a simple CLI-based program:

![CLI](/readme_imgs/cli.PNG)

This is just to set up most of the backend and code most of the application's features such as add, edit, and delete.
File I/O was first implemented through Python's native file read and write. I then used [tinydb](https://tinydb.readthedocs.io/en/stable/) for a more efficient data transfer and usability.

After finishing the CLI, I then moved on to making a simple GUI:

![CLI](/readme_imgs/gui_main.PNG)

I used Python's included Tkinter for the GUI toolkit. It presents the same information as the CLI, but in a much more recognisable (although old-fashioned) interface. Add game is more nicely laid out and easier to follow:

![CLI](/readme_imgs/gui_add.PNG)

Edit game brings up a popup window wich prefills the form so users can edit what they need:

![CLI](/readme_imgs/gui_edit.PNG)

Both windows of add and edit has got a cancel button and a message if the input is invalid such as an empty required field:

![CLI](/readme_imgs/gui_err.PNG)

Lastly, the delete button brings up a confirmation window for accidental clicks:

![CLI](/readme_imgs/gui_del.PNG)

I am wishing to add more content and maybe migrate to a more modern GUI toolkit in the future.
