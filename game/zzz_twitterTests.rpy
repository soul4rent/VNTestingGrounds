label twitterTesting:

    "Now testing twitter scraping (urllib2):"

    python:
        import urllib2 #only way to get this to work -_-
        #TODO: Beautiful soup or native html parser. Most likely BS.

        resp = urllib2.urlopen("https://twitter.com/WebDevWith8051", context=gcontext) #gcontext declared in script.rpy
        html = resp.read()
        print("If this returns true, this game can literally check your twitter to see if you posted something specific:")
        print("Kyle" in html and "Me:" in html) #the start of something potentially beautiful
        html2 = html[0:200]

    "EX results: [html2]"

    "Example of Twitter Usage"


    jump start
