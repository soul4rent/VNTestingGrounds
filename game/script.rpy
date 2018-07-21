init python:
    import urllib2 #only way to get this to work -_-
    resp = urllib2.urlopen("https://twitter.com/WebDevWith8051")
    html = resp.read()
    print("If this returns true, this game can literally check your twitter to see if you posted something specific:")
    print("Kyle" in html and "Me:" in html) #the start of something potentially beautiful
    html2 = html[0:200]
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

    play music "Generic_Filler.wav"

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "By the way, I can check your friggin twitter. Here's the proof:"

    e "PROOF: [html2]"

    jump sideLabelTesting

# This ends the game.
label endGame:
    return
