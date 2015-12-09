#Final Project

##Abstract
Read dataset
Generate Model

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
###Normalization of Non-numerical Data Points

##Refernces
###Project 25499
[Project 25499](https://scans.io/study/mi) is a project by Silas Cutler that scans parts of the IPv4 Internet and aggregates data.

###Visualization: Mapping Global Earthquake Activity
[http://introtopython.org/visualization_earthquakes.html](This) page was used to set up and write code for plot-map.py.
