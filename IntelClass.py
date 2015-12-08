#!/usr/bin/env python

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
    IP              = ""#ipaddress.ipaddress()
    port            = ""
    data            = False #True if data is present (response was received)
    httpVersion     = ""
    httpcode        = ""
    contentType     = ""
    serverType      = ""
    SSL             = False#bool()
    certificate     = ""
    defaultPage     = ""
    country         = ""
    continent       = ""
    lat             = ""
    lon             = ""

    def __str__(self):
        result = ""
        if self.SSL:
            #result = str(self.IP) + "," + str(self.port) + "," + str(self.certificate) + "\n"
            result = str(self.IP) + "," + str(self.port) + "," + str(self.certificate) + "," + str(self.continent) + "," + str(self.country) + "," + str(self.lat) + "," + str(self.lon) + "\n"
        elif self.data:
            result = str(self.IP) + "," + str(self.port) + "," + str(self.httpVersion) + "," + str(self.httpcode) + "," + str(self.serverType) + "," + str(self.contentType) + "," + str(self.continent) + "," + str(self.country) + "," + str(self.lat) + "," + str(self.lon) + "\n"
        else:
            result = result = str(self.IP) + "," + str(self.port) + "\n"
        return result
