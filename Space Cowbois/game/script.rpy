﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define C1 = Character("Cowboy #1")
define C2 = Character("Cowboy #2")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene space

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    C1 "Greetings!"

    C1 "This is initial set up."

    C2 "Yeah, it's kinnda bad but better then nothing, I guess."

    # This ends the game.

    return
