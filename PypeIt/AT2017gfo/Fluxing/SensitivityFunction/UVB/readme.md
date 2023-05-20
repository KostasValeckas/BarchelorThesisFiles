The two '.pdf' files are quality assesment of the zeropoint and spectroscopic throughput.

The sped1d file is a spectrum of a spectrophotometric standard star produced in the main run.

The '.par' file is generated automatically when running the algorithm.

The sens file is the sensitivity function.

### to create the sensitivity function, excecute:

pypeit_sensfunc -s sensfuncAdjustedPar.txt  spec1d_XSHOO.2017-08-18T23:05:11.602-STD,FLUX_XShooter_UVB_20170818T230511.602.fits

### the 'BeforeAdjustments' directory is the output when 'sensfuncAdjustedPar.txt' is excluded, with the following command:

pypeit_sensfunc spec1d_XSHOO.2017-08-18T23:05:11.602-STD,FLUX_XShooter_UVB_20170818T230511.602.fits
