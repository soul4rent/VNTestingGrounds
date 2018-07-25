label redditTesting:

    python:
        import re

        resp = urllib2.urlopen("https://news.ycombinator.com/", context=gcontext) #gcontext declared in script.rpy
        html = resp.read()
        preresult = re.sub('[ ]+|[\r\n]+',' ', strip_tags(html)) #strip string of whitespace
        result = preresult[preresult.find("1."):preresult.find("2.")] #strip string of anything that isn't a post

        e("So I found this on hacker news you cutie, what do you think about it?")
        e(result)

    e "The start of reddit testing"

    jump start
