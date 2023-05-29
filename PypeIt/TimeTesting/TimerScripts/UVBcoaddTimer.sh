#!/bin/bash

#################################
# THIS BLOCK SETS THE PARAMETERS:


# command to excecute (str):
# example : "run_pypeit -v 0 -o vlt_xshooter_nir_Science.pypeit"
command="pypeit_coadd_1dspec vlt_xshooter_uvb.coadd1d"

# number of test runs (int): 
N=10

#  output file name used both for output table ang log:
#  example : myFile (!WARNING - WILL OVERWRITE)
outputName=UVBcoadd10


# array of files and directories to move into command output folder after each test run:
# example: (Masters QA Science)
removeList=() 

#################################

# creating/overwriting the output and log file:

outputFile=$outputName.csv
echo "Test run number, Time (seconds)" > $outputFile

logFile=timerLog_$outputName.log
echo "Log for output file $outputFile" > $logFile

# excecution loop: 

printf "\nTHIS SCRIPT WILL RUN: \n '$command' \n$N TIMES AND LOG EXCECUTION TIMES in:\
\n '$outputFile'\nLOGS ARE SAVED IN :\n '$logFile' \n"

printf "\nSTARTING THE TESTING LOOP:\n"

for (( i=1; i<=$N; i++ ))

do 
    printf "\n################\n" | tee -a $logFile
    printf "Testing run $i\n\n" | tee -a $logFile
    
    echo "Removing requested files and directories: " | tee -a $logFile
    echo "${removeList[@]}" | tee -a $logFile 
    for y in "${removeList[@]}"
    do
       rm -rf $y
    done
    printf "\nRemoving done!\n\n" | tee -a $logFile
    
    printf "\nStarting the command excecution: \n\n" | tee -a $logFile
    
    printf "\n### This is PypeIt log for run $i ###\n\n" >> $logFile
        
    start=`date +%s`
    $command 2>&1 | tee -a $logFile
    stop=`date +%s`
    
    printf "\n### PypeIt log for run $i is complete ###\n\n" >> $logFile
    
    printf "\n\nTesting run $i complete\n" | tee -a $logFile
    

    timer=`expr $stop - $start`

    echo "Excecution time: $timer" | tee -a $logFile
    echo "################" | tee -a $logFile

    echo "$i,$timer" >> $outputFile
done


printf "\nTESTING DONE!\n" | tee -a $logFile
echo "Results:"
cat $outputFile
