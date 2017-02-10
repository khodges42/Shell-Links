import webbrowser, sys, shlex
new = 2 # open in a new tab, if possible
if len(sys.argv) >= 2:

	if len(sys.argv) == 2:

		if sys.argv[1][:3] == "/r/":
			url = "https://www.reddit.com"+sys.argv[1]

		else:
			string = sys.argv[1]
			url = "https://www.reddit.com/search?q="+string.replace(" ", "+")
	else:	
		args = sys.argv[1:]
		string = '+'.join(args)
		url = "https://www.reddit.com/search?q="+string.replace(" ", "+")
else:
	url = "https://www.reddit.com/"

webbrowser.open(url,new=new)
