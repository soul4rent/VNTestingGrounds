init python:
    print("Import tests / basic internet connection tests")
    #because apparently imports fail often in renpy

    #from bs4 import BeautifulSoup
    #TODO: Try to get above import to work. If still doesn't work, might have to force regex on html

    import urllib2 #because requests is broken :^)
    import ssl
    from HTMLParser import HTMLParser

    print("Creating Classes/Universal Functions")
    class MLStripper(HTMLParser):
        def __init__(self):
            self.reset()
            self.fed = []
        def handle_data(self, d):
            self.fed.append(d)
        def get_data(self):
            return ''.join(self.fed)

    def strip_tags(html):
        s = MLStripper()
        s.feed(html)
        return s.get_data()


    print("SSL test, cross fingers")
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  #WORKAROUND. IF BETTER WAY FOUND FIX HERE.

    resp = urllib2.urlopen("https://twitter.com/WebDevWith8051", context=gcontext)
    html = resp.read()
    print("Twitter Check Complete")
    print("Kyle" in html and "Me:" in html) #the start of something potentially beautiful

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("TTMain")

image TTmain = im.Scale("Tinsel_Teeth_main.png", 540, 720)
#Dang it, had to do it manually in the end. At least once you do it once, you in theory NEVER have to do it again.



# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    #shows TTmain image
    show TTmain


    e "This is a renpy testing ground for dev mechanics."

    menu:
        "Select option:"

        "audio testing":
            jump audioTesting

        "twitter testing":
            jump twitterTesting

        "reddit/hacker news tests":
            jump redditTesting

        "Continue":
            "now continuing"


    jump sideLabelTesting #in testarc.py

# This ends the game.
label endGame:
    return
