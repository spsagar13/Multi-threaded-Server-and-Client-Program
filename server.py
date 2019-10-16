############################################################
# Author        :   Sagar Surendran
# UTA ID        :   1001348700
# Date Created  :   10/15/2019
# Brief         :   A simple web server
#                   Default port on server listen to is 8080
#                   Default file to download is default.html
#                   This program will behave as a multi threaded 
#                   HTTP server that accepts connections from 
#                   appropriate clients. This server serves the 
#                   request of the clients.
############################################################

# import packages
from http.server import HTTPServer, BaseHTTPRequestHandler
import sys

# define default values
server_port = 8080 #default port

#if there is an optional port number parameter is passed; port on which the server is listening to clients
if 2 == len(sys.argv):
    server_port = int(sys.argv[1])

print('Server is listening on port:', server_port)

# initialise the http server
class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/default.html' #setting the default html page
        print('File to access is ', self.path[1:])
        try:
            #try to open the file
            file_to_open = open(self.path[1:]).read()
            #send successful response
            self.send_response(200)
        except:
            file_to_open = "Not Found"
            #send failure response since the content was not accessable
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open,'utf-8'))

# create the multi thread HTTP server with the port
httpd = HTTPServer(('localhost',server_port),Serv)
# enable to server to be open always.
httpd.serve_forever()