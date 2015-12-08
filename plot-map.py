#!/usr/bin/env python

from pylab            import plot,show
from numpy            import vstack,array
from numpy.random     import rand
from scipy.cluster.vq import kmeans, vq, whiten

from csv import reader 
from struct import unpack
from socket import inet_aton

import sys                                  #Drive the program
import argparse                             #Parse arguments
from mpl_toolkits.basemap import Basemap    #Map module
import matplotlib.pyplot as plt             #Plot things
import numpy as np                          #Numpy things :)

if __name__ == "__main__":
    lats = []
    lons = []

    print("opening file")
    with open(sys.argv[1], 'rb') as f:
        reader = reader(f)
        try:
            for row in reader:
                if len(row) == 10 and row[8] and row[9]:
                    lats.append(float(row[8]))
                    lons.append(float(row[9]))
        except:
            pass

    eq_map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
                          lat_0=0, lon_0=-130)
    eq_map.drawcoastlines()
    eq_map.drawcountries()
    eq_map.fillcontinents(color = 'gray')
    eq_map.drawmapboundary()
    eq_map.drawmeridians(np.arange(0, 360, 30))
    eq_map.drawparallels(np.arange(-90, 90, 30))
     
    x,y = eq_map(lons, lats)
    eq_map.plot(x, y, 'ro', markersize=6)

    plt.show()

