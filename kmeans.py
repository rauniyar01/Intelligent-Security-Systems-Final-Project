#!/usr/bin/python

# This program attend to read data from a csv file,
# and apply kmean, then output the result.

from pylab            import plot,show
from numpy            import vstack,array
from numpy.random     import rand
from scipy.cluster.vq import kmeans, vq, whiten

from csv import reader 
import sys
from struct import unpack
from socket import inet_aton

if __name__ == "__main__":

    # clusters
    K = int(sys.argv[1])

    data_arr = []
    
    names = ['latitude', 'longitude']

    print("opening file")
    with open(sys.argv[2], 'rb') as f:
        reader = reader(f)
        for row in reader:
            j=0
            #data_arr.append([float(x) for x in row[1:]]) doesnt do anything...?
            ip = unpack("I", inet_aton(row[0]))[0]
            if len(row) == 10: #works for lat and long cluster 
                #data_arr.append([(float(row[8]),float(row[9]))]) #works with lat and long 
                data_arr.append([float(ip),(float(row[8]))])
                
                #for letter in row[7] + row[8]: #try with continent and country 
                #    j+=ord(letter)
                #data_arr.append([float(ip), float(j)])

    data = vstack( data_arr )
    #meal_name = vstack(meal_name_arr)

    # normalization
    print("normalizing")
    data = whiten(data)

    # computing K-Means with K (clusters)
    print("computing kmeans")
    centroids, distortion = kmeans(data,K)
    print "distortion = " + str(distortion)

    # assign each sample to a cluster
    idx,_ = vq(data,centroids)

    # some plotting using numpy's logical indexing
    plot(data[idx==0,0], data[idx==0,1],'ob',
         data[idx==1,0], data[idx==1,1],'or',
         data[idx==2,0], data[idx==2,1],'oy')
         
         #data[idx==3,0], data[idx==3,1],'og')

    #print meal_name
    print data
    #for i in range(K):
     #   result_names = names[idx==i, 0]
      #  print "================================="
       # print "Cluster " + str(i+1)
        #for name in result_names:
         #   print name

    plot(centroids[:,0],
         centroids[:,1],
         'sg',markersize=8)

    show()
