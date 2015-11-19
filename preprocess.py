#!/usr/bin/env python

import sys                  #To drive the program
import argparse             #To parse all of the arguments
#import ipaddress            #To deal with IP addresses
import json                 #To read the data in from the file
from pprint import pprint   #To print things nicely for testing

"""
@Class: item
@Attribute: ip: IP address
@Attribute: port: Port of the web server
@Attribute: httpVersion: HTTP version
@Attribute: contentType: content type
@Attribute: serverType: Server version string
@Attribute: SSL: True || False
@Attribute: certificate: holds SSL/TLS Cert if true
@Attribute: defaultPage: name of page returned
@Attribute: GeoIP: result of GeoIP lookup
"""
class item:
    IP              = str()#ipaddress.ipaddress()
    port            = str()
    httpVersion     = str()
    httpcode        = str()
    contentType     = str()
    serverType      = str()
    SSL             = bool()
    certificate     = str()
    defaultPage     = str()
    GeoIP           = str()     #Maybe not a str(), we will see later


"""
@Function: getIP
@Description: Get the IP address from the JSON object
@Parameter: JSON object
@Returns: IP address from the JSON object
"""
def getIP():
    pass

"""
@Function: getport
@Description: Get the port from the JSON object
@Parameter: JSON object
@Returns: Port from the JSON object
"""
def getport():
    pass

"""
@Function: getHTTPVersion
@Description:
@Parameter:
@Returns:
"""
def getHTTPVersion():
    pass

"""
@Function:
@Description:
@Parameter:
@Returns:
"""
def gethttpcode():
    pass

"""
@Function:
@Description:
@Parameter:
@Returns:
"""
def getcontentType():
    pass

"""
@Function:
@Description:
@Parameter:
@Returns:
"""
def getserverType():
    pass

"""
@Function:
@Description:
@Parameter:
@Returns:
"""
def getSSL():
    pass

"""
@Function:
@Description:
@Parameter:
@Returns:
"""
def getcertificate():
    pass

"""
@Function:
@Description:
@Parameter:
@Returns:
"""
def getdefaultPage():
    pass

"""
@Function:
@Description:
@Parameter:
@Returns:
"""
def getGeoIP():
    pass



def main():
    #Create the argument parser and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("inFile", help="JSON file convert to output file format.")
    parser.add_argument("outFile", help="File name to save the file to.")
    args = parser.parse_args()

    #open the file and import the first JSON object
    inFile = open(args.inFile, 'r') 
    for line in inFile:
        data = json.loads(line)
        #The data object now holds all of the stuff, and we can access it like
        #this: data['host'] would yield the IP address


if __name__ == "__main__":
    sys.exit(main())
