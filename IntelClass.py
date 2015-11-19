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
    IP              = str()#ipaddress.ipaddress()
    port            = str()
    data            = False #True if data is present (response was received)
    httpVersion     = str()
    httpcode        = str()
    contentType     = str()
    serverType      = str()
    SSL             = False#bool()
    certificate     = str()
    defaultPage     = str()
    GeoIP           = str()     #Maybe not a str(), we will see later

    def __str__(self):
        result = ""
        if self.SSL:
            result = str(self.IP) + "\n" + str(self.port) + "\n" + str(self.certificate) + "\n"
        elif self.data:
            result = str(self.IP) + "\n" + str(self.port) + "\n" + str(self.httpVersion) + "\n" + str(self.httpcode) + "\n" + str(self.serverType) + "\n" + str(self.contentType) + "\n"
        else:
            result = result = str(self.IP) + "\n" + str(self.port) + "\n"
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

