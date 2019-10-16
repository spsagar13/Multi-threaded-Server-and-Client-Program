##########################################################
UTA ID	: 1001348700
Name	: Sagar Surendran
Email	: sagar.surendran@mavs.uta.edu
Readme file for Client-Server program
##########################################################
Kindly follow the below instruction to successfully run the code.

#Precondition
The code is written in Python, version : Python 3.7.4

1. Use command prompt to access the directory Multi-threaded-Server-and-Client-Program
	Make sure that you have the following files in it
	1. server.py
	2. client.py
	3. default.html
	4. index.html
	5. a directory structure "path/to/file"
	   Content of the child directory: example.html
2. Run: py server.py
   You will be able to see the below
   "Server is listening on port: 8080"
3. Open any browser, preferrably Chrome.
4. Type http://localhost:8080/
   This will load the default page
5. Open another tab in the browser
   Type http://localhost:8080/index.html
   This will load the index page
6. Open another tab in the browser
   Type http://localhost:8080/path/to/file/example.html
   This will load the example page in the respectieve path
7. Open another tab in the browser
   Type http://localhost:8080/dummy.html
   Since the content is unavailable, we can see "Not Found"
8. Open another instance of command prompt.
9. Go to the directory 1001348700_SagarSurendran
10.Run: py client.py localhost  
        OR 
		py client.py 127.0.0.1
   This will load the content of the Index page.
11.Run: py client.py localhost 8080
   This will load the content of the Index page.
12.Run: py client.py localhost 8080 default.html
   This will load the content of the Default page.
13.Run: py client.py localhost 8080 path/to/file/example.html
   This will load the content of the Example page from the respectieve path.
14.Run: py client.py localhost dummy.html
   This will tell that the page is not found
   
#################################################################################
References:
https://docs.python.org
https://docs.python.org/3/library/http.server.html
https://docs.python.org/3/library/http.client.html

Python Tutorials for Web server and clients from YouTube
https://www.youtube.com/watch?v=Lbfe3-v7yE0&t=307s
https://www.youtube.com/watch?v=pP8F7tRIPyo
#################################################################################
