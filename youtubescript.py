import webbrowser, sys, shlex
new = 2 # open in a new tab, if possible





if len(sys.argv) >= 2:

	if len(sys.argv) == 2:
		print (sys.argv)
		string = sys.argv[1]
		url = "https://www.youtube.com/results?search_query="+string.replace(" ", "+")


	else:	
		args = sys.argv[1:]
		string = '+'.join(args)
		url = "https://www.youtube.com/results?search_query="+string.replace(" ", "+")

else:
	url = "https://www.youtube.com/"

webbrowser.open(url,new=new)
