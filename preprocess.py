#!/usr/bin/env python

import argparse
import ipaddress

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
    IP              = ipaddress.ipaddress()
    port            = str()
    httpVersion     = str()
    httpcode        = str()
    contentType     = str()
    serverType      = str()
    SSL             = bool()
    certificate     = str()
    defaultPage     = str()
    GeoIP           = str()     #Maybe not a str(), we will see later



def getIP():
    pass

def getport():
    pass

def gethttpVersion():
    pass

def gethttpcode():
    pass

def getcontentType():
    pass

def getserverType():
    pass

def getSSL():
    pass

def getcertificate():
    pass

def getdefaultPage():
    pass

def getGeoIP():
    pass


