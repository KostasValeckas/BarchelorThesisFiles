### These are the shell scripts used to excecute time testing and logging times.

MODEcoaddTimer.sh times coadding 1d spectra. 

MODEmainStarTimer.sh times the main run of reducing the spectrophotometric standard star. 

MODEmainTimer.sh times the main run of reducing AT2017gfo X-shooter data. 

MODEsensCreateTimer.sh times the creation of the sensitivity function. 

MODEsensApplyTimer.sh times the application of the sensitivity function. 

MODEsensApplyTimer.sh times the telluric corrections (NIR/VIS only). 

'QuickRuns' directory contains the shell scripts used to time the quick-look reductions.

for now all set to 10 repetitions, this can be changed by re-definning the 'N' parameter.

All commands called and the needed products are described and provided within the directory:
'PypeIt/AT2017gfo' within this repository.
