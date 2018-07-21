init python:
    import urllib2 #only way to get this to work -_-
    resp = urllib2.urlopen("https://twitter.com/WebDevWith8051")
    html = resp.read()
    print("Twitter Check Complete")
    print("Kyle" in html and "Me:" in html) #the start of something potentially beautiful
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.


    #testing audio functionality

    e "This is a renpy testing ground for dev mechanics."

    menu:
        "Select option:"

        "audiotesting":
            jump audioTesting

        "twitter testing":
            jump twitterTesting

        "Continue":
            "now continuing"


    jump sideLabelTesting #in testarc.py

# This ends the game.
label endGame:
    return
