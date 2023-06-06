# code used to produce plots of the reduced and calibrated X - Shooter AT2017gfo spectrum
# that was produced using 'PypeIt'
# The building blocks for this code was helpfully provided by Tom Reynolds (NBI)

# This exact plot is made to fit the format of the thesis, and is only provided for reference
# For better scaled plots, see the other scripts in the directory

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

def DatReader(filePath):
        return np.loadtxt(filePath, unpack=True)

NIReso = DatReader(
    "../NIR_AT2017gfo_ENGRAVE_v1.0_XSHOOTER_MJD-57983.969_Phase+1.43d.dat",
    )
VISeso = DatReader(
    "../VIS_AT2017gfo_ENGRAVE_v1.0_XSHOOTER_MJD-57983.969_Phase+1.43d.dat",
    )
UVBeso = DatReader(
    "../UVB_AT2017gfo_ENGRAVE_v1.0_XSHOOTER_MJD-57983.969_Phase+1.43d.dat",
    )

waveESO = np.array([UVBeso[0],VISeso[0],NIReso[0]], dtype = object)
specESO = np.array([UVBeso[1],VISeso[1],NIReso[1]], dtype = object)

def FitsReader(filePath):
        spec_file_f = filePath
        spec_f = fits.getdata(spec_file_f,1)
        return np.array([spec_f.field("wave"),spec_f.field("flux")*1E-17])

NIRpypeIt = FitsReader("../AT2017gfoNIR_tellcorr.fits")
VISpypeIt = FitsReader("../AT2017gfoVIS_tellcorr.fits")
UVBpypeIt = FitsReader("../AT2017gfoUVB.fits")

wavePypeit = np.array([UVBpypeIt[0],VISpypeIt[0],NIRpypeIt[0]], dtype = object)
specPypeit = np.array([UVBpypeIt[1],VISpypeIt[1],NIRpypeIt[1]], dtype = object)

SEP_CONST = 2E-17

plt.figure(figsize=(16,2.5))
plt.ylim(-1E-16,0.23E-15)
#plt.xlabel("Observed Wavelength (Å)",fontsize=12)
#plt.ylabel("Flux (erg/s/cm²/Å))",fontsize=12)

for i in range(3): 
	plt.plot(
		waveESO[i], specESO[i],
		color="r", lw=0.2, label=("ESO reduction" if i < 1 else None)
		)
	plt.plot(
		wavePypeit[i], specPypeit[i]-SEP_CONST,
		color="k",lw=0.2, label=("PypeIt reduction-2E-17 erg/s/cm²/Å" if i < 1 else None)
		)

for i in plt.legend().get_lines(): i.set_linewidth(2) 
plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))

plt.savefig("./ATcompared_glued_tellCorr_narrowNoLabels.png",bbox_inches="tight",facecolor="white")
plt.show()
