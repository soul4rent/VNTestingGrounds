label audioTesting:

    "performing audio tests"

    menu:
        "Select track:"

        "Generic_Filler":
            $song = "Generic_Filler.wav"



    play music [song]

    "Now testing Fadein/Out"

    stop music fadeout 1.0

    "..."

    play music [song] fadein 1.0

    "..."

    stop music fadeout 5.0

    "..."

    play music [song] fadein 5.0

    jump start
