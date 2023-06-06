# code used to produce plots of the reduced and calibrated X - Shooter AT2017gfo spectrum
# that was produced using 'PypeIt'
# The building blocks for this code was helpfully provided by Tom Reynolds (NBI)

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt


def FitsReader(filePath):
        spec_file_f = filePath
        spec_f = fits.getdata(spec_file_f,1)
        return np.array([spec_f.field("wave"),spec_f.field("flux")*1E-17])

NIRpypeIt = FitsReader("../AT2017gfoNIR.fits")
VISpypeIt = FitsReader("../AT2017gfoVIS.fits")
UVBpypeIt = FitsReader("../AT2017gfoUVB.fits")

wavePypeit = np.array([UVBpypeIt[0],VISpypeIt[0],NIRpypeIt[0]], dtype = object)
specPypeit = np.array([UVBpypeIt[1],VISpypeIt[1],NIRpypeIt[1]], dtype = object)


plt.figure(figsize=(16,12))
plt.ylim(-1E-16,0.23E-15)
plt.xlabel("Observed Wavelength (Å)",fontsize=12)
plt.ylabel("Flux (erg/s/cm²/Å))",fontsize=12)

for i in range(3): plt.plot(wavePypeit[i], specPypeit[i], color="k",lw=0.2, )

plt.savefig("./ATalone_glued.png",bbox_inches="tight",facecolor="white")
plt.show()
