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
            result = str(self.IP) + ", " + str(self.port) + ", " + str(self.certificate) + "\n"
        elif self.data:
            result = str(self.IP) + ", " + str(self.port) + ", " + str(self.httpVersion) + ", " + str(self.httpcode) + ", " + str(self.serverType) + ", " + str(self.contentType) + "\n"
        else:
            result = result = str(self.IP) + ", " + str(self.port) + "\n"
        return result

    """
    @Function: getIP
    @Description: Get the IP address from the JSON object
    @Parameter: JSON object
    @Returns: IP address from the JSON object
    """
    def getIP(self):
        return self.IP

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

