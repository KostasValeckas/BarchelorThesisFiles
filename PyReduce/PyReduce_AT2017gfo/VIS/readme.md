## This directory contains the files needed to recreate the reduction of AT2017gfo X-shooter VIS data with 'PyReduce' that is discussed in the thesis. 

### Contents:

### Adjusted files:
Files that were altered from the main 'pip' distribution and the files described in: 
https://github.com/KostasValeckas/BarchelorThesisFiles/tree/main/PyReduce/PyReduce%20altered%20files

### CreatingWavecalGuess :
Files used to attemp the creation of initial guess, as described in: 
https://pyreduce-astro.readthedocs.io/en/latest/wavecal_linelist.html
DOES NOT WORK, only provided for refference 

### OUTPUT:
Results obtained.

### OutputPlots:
Plots returned by the software while running the reduction.

### ReBinnedData
Data that has been rebinned, as no frames of the type are present with same binning as the object frames. 
Use this TOGETHER with the data listed in VISdataOnly1x2Bin.csv

### logs
Logs produced while running the software.

### VISdataOnly1x2Bin.csv
NOT ALL PROVIDED RAW DATA was used in this reduction. This is the list of the files used (TOGETHER with files in the 'ReBinnedData' directory).

### x_shooter_vis_AT2017gfo.py
Run this script to excecute the reduction.
