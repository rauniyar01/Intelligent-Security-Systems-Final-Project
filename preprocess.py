#!/usr/bin/env python

import sys                  #To drive the program
import argparse             #To parse all of the arguments
import json                 #To read the data in from the file
from pprint import pprint   #To print things nicely for testing
from base64 import b64decode #decode base64
import re                   #parse http headers
import IntelClass           
from geoip import geolite2

def main():
    #Create the argument parser and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("inFile", help="JSON file convert to output file format.")
    parser.add_argument("outFile", help="File name to save the file to.")
    parser.add_argument("-nd", "--no-data", help="Include servers with no data", action='store_true')
    args = parser.parse_args()

    #open the file and import the first JSON object
    inFile = open(args.inFile, 'r') 
    outFile = open(args.outFile, 'w')
    i = 1
    for line in inFile:
        data = json.loads(line)
        #The data object now holds all of the stuff, and we can access it like
        #this: data['host'] would yield the IP address
        if data['data'] != "":
            #if args.nd != True: # I think it has to be args.-nd but I just commented it out for now
            #    continue
            #Create the object and put stuff in it
            obj = IntelClass.item()
            obj.IP = data['host']
            obj.port = data['port']
            obj.data = True
            header = b64decode(data['data'])
            if re.match("-----BEGIN CERTIFICATE-----", header):
                obj.SSL = True
                obj.certificate = header.replace("\n","")
            else:
                header = header.split("\n")
                for field in header:
                    if re.match( "HTTP", field):
                        http = field.split(" ")
                        if len(http) == 2:
                            obj.httpVersion = http[0]
                            obj.httpcode = http[1].strip("\r ")
                    elif re.match("Server", field):
                        server = field.split(":")   
                        if len(server) == 2:
                            obj.serverType = server[1].strip("\r ")
                    elif re.match("Content-Type", field):
                        content = field.split(":")
                        if len(content) == 2:
                            obj.contentType = content[1].strip("\r ")
                    elif re.match("<HTML>", field):
                        break

            if obj.IP:
                lookup = geolite2.lookup(obj.IP)
                obj.country = lookup.country
                obj.continent = lookup.continent
                obj.lat = lookup.location[0]
                obj.lon = lookup.location[1]
            #print(obj)
            outFile.write(str(obj))

        #else:
        #        print("No DATA: ", i, "data=",data['data'])
        #        i = i+1
        #geoip stuff
    outFile.close()
    inFile.close()

if __name__ == "__main__":
    sys.exit(main())
