#Final Project

##Abstract
We have around 120GB of data from an [Project 25499](https://scans.io/study/mi), an Internet wide scan looking for web servers running on ports 0, 80, 8080, and 443. The data contains the HTTP responses from all the different servers. Our goal is to extract important features from the response and perform clustering on our data. We hope to be able to find patterns based on geolocation of the web server such as concentration of web servers, type of server such as apache or nginx, port the web server is running on, and the concentration of SSL being used in certain areas.

##Dependencies
These scripts rely on the following python libraries:

- [numpy](http://docs.scipy.org/doc/numpy-1.10.1/user/install.html)
- [scipy](http://www.scipy.org/install.html)
- [geoip](http://pythonhosted.org/python-geoip/)
- [argparse](https://pypi.python.org/pypi/argparse)
- [matplotlib](http://matplotlib.org/users/installing.html)
- [mpl_toolkits.basemap](http://matplotlib.org/basemap/users/installing.html)

##Preprocessing
The preprocessing script is preprocess.py.  This script takes the JSON object as input, extracts useful information from it, and then writes it to a CSV file format.  The script has the following usage:

```
python preprocess.py <JSON input file> <CSV output file>
```

##Clustering
The clustering script is kmeans.py. This script runs kmeans and displays a graph of the data.  This script has the following usage:

```
python kmeans.py <number of clusters> <CSV input file>
```

##Map Plotting
The map plotting script is plot-map.py.  This script will plot the location of servers on a map according to their latitude and longitude.  The program has the following usage:

```
python plot-map.py <CSV input file>
```

##Problems Encountered
###Make Non-numerical data Numerical
There were many data fields extracted from the http response but most of it was text data. To do the clustering we needed to make the data numerical in order to normalize and graph the clusters.
###Normalization of Non-numerical Data Points
There was not a good way to take some fields, such as server type, and convert them to numerical data to normalize and cluster. All the attempts created dnormalized data that was to close and the clusters were not meaningful.
##References
###Project 25499
[Project 25499](https://scans.io/study/mi) is a project by Silas Cutler that scans parts of the IPv4 Internet and aggregates data.

###Visualization: Mapping Global Earthquake Activity
[http://introtopython.org/visualization_earthquakes.html](This) page was used to set up and write code for plot-map.py.
