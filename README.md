#Final Project

##Objective
Read dataset
Generate Model

#Preprocessing
The preprocessing script is preprocess.py.  This script takes the JSON object as input, extracts useful information from it, and then writes it to a CSV file format.  The script has the following usage:

```
python preprocess.py <JSON input file> <CSV output file>
```

#Clustering
The clustering script is kmeans.py. This script has the following usage:

```
python kmeans.py <number of clusters> <CSV input file>
```

#Map Plotting
The map plotting script is plot-map.py.  This script will plot the location of servers on a map according to their latitude and longitude.  The program has the following usage:

```
python plot-map.py <CSV input file>
```
