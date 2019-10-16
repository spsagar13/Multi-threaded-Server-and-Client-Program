#####################################################################
# Author        :   Sagar Surendran
# UTA ID        :   1001348700
# Date Created  :   10/15/2019
# Brief         :   A simple web client
#                   Default server is localhost
#                   Default port is 8080
#                   Default file to download is index.html
#                   This program will behave as an HTTP client
#                   that will query files and download from a server.
######################################################################

# Importing packages
import http.client
import sys

# Assigning default values
server_name = "localhost"
server_port = 8080
file_name = "index.html"

# Defining the usage of the program
def usage():
    print("\nUsage  : py client.py  <server_IPaddress/name> [<port_number>] [<requested_file_name>]"
          "\n         <server_IPaddress/name> : Mandatory, <port_number> : Optional, <requested_file_name> : Optional"
          "\nexample  : py client.py localhost"
          "\n           py client.py 127.0.01 8080 default.html"
          "\n           py client.py 127.0.01 default.html")


# checking if the necessary arguments are present
if 1 == len(sys.argv):
    print("\nInadequate number of arguments")
    usage()
    exit()

# get the server name
server_name = str(sys.argv[1])

# get the port number and file name based on the number of arguments.
if 4 == len(sys.argv):
    server_port = int(sys.argv[2])
    file_name = str(sys.argv[3])
if 3 == len(sys.argv):
    try:
        server_port = int(sys.argv[2])
    except ValueError:
        file_name = str(sys.argv[2])


print("\nServer name/IP: ", server_name, ", Server port: ", server_port, ", Name of the file to download: ", file_name)

file_name = '/' + file_name # since the server strips off the first character while fetching the file with this name

#establishing the HTTP connection
try:
    connection = http.client.HTTPConnection(server_name, server_port, timeout=10)
    # get the file
    connection.request("GET",file_name)
    # get the response
    response = connection.getresponse()
    print("\nStatus code: {}, Reason phrase: {}".format(response.status, response.reason))

    #read the content to display
    content = response.read()
    if 'Not Found' != str(content.decode()):
        print("\nRequested content is below\n")
    else:
        print("Content")
    # printing the content into the console
    print(content.decode())
except:
    print("\nConnection could not be made due to unexpected error. Please check Server Name/IP or Port Number")
    usage()

#close the connection.
connection.close()