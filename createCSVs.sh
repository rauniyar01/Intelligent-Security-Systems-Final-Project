#!/bin/bash

for file in $(ls input-files); do
    echo $file
    inFile="input-files/"$file
    outFile="output-files/"$file".csv"
    ./preprocess.py $inFile $outFile
done
