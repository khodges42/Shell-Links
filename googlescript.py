import webbrowser, sys, shlex
new = 2 # open in a new tab, if possible

if len(sys.argv) >= 2:

	if len(sys.argv) == 2:
		string = sys.argv[1]
		url = "http://www.google.com/search?"+"q="+string.replace(" ", "+")
	else:	
		args = sys.argv[1:]
		string = '+'.join(args)
		url = "http://www.google.com/search?"+"q="+string.replace(" ", "+")
else:
	url = "http://www.google.com/"

webbrowser.open(url,new=new)

