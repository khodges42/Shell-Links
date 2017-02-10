import webbrowser, sys, shlex
new = 2 # open in a new tab, if possible
if len(sys.argv) >= 2:

	if len(sys.argv) == 2:

		if sys.argv[1][:1] == "/":
			url = "http://www.4chan.org/"+sys.argv[1]

		else:
			print "enter a board you weeb"
			url = "http://www.4chan.org/"
else:
	url = "http://www.4chan.org/"

webbrowser.open(url,new=new)
