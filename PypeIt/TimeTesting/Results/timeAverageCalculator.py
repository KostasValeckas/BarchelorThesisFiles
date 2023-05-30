import numpy as np
import datetime
import math
import sys
import glob

files = (glob.glob("./*.csv"))

files.sort()

resultArray = np.empty([len(files), 2], dtype="S450")

def calculator(arg):
    
    data = np.genfromtxt(arg, skip_header = 1, delimiter=',')

    times = data[:,1]

    print("\nCalculating average time for ", len(times), "runs in ", arg, "\n")
    
    unround_mean = np.mean(times)
    unround_std = np.std(times)

    print("Undrounded time average in seconds: ", unround_mean)
    print("Unrounded standard deviation in seconds: ", unround_std, "\n")

    significant_digit = int(math.floor(math.log10(abs(unround_std))))

    rounded_mean  = round(unround_mean, -significant_digit)
    rounded_std  = round(unround_std, -significant_digit)

    print("Rounded time average in seconds: ", rounded_mean)
    print("Rounded standard deviation in seconds: ", rounded_std, "\n")

    print(
        "Final result: ",
        str(datetime.timedelta(seconds = rounded_mean)),
        "+/-", 
        str(datetime.timedelta(seconds = rounded_std))
        )
    return np.array([arg, str(datetime.timedelta(seconds = rounded_mean)) + "+/-" + str(datetime.timedelta(seconds = rounded_std))])


for i in range(len(files)): 
	resultArray[i] = calculator(files[i])
	
np.savetxt('timeAverageResults.txt', resultArray, fmt = "%s", delimiter = ',')

print("\n DONE! results saved in timeAverageResults.txt")
	


