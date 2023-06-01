# code used to produce plots of the reduced and calibrated X - Shooter AT2017gfo spectrum
# that was produced using 'PypeIt'
# I DID NOT ENGINEER THIS CODE MYSELF, 
# I GOT IT PROVIDED FROM: Tom Reynolds (NBI), and modified it slightly


from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

spec_file_f = "./GRB230325A_NIR_tellcorr.fits"
spec_f = fits.getdata(spec_file_f,1)
NIRcoadded = np.array([spec_f.field("wave"),spec_f.field("flux")*1E-17])



fig,ax=plt.subplots(1,1,figsize=(16,12))

ax.plot(NIRcoadded[0],
        NIRcoadded[1],
         lw=0.2,color="k")
ax.axes.set_ylim(-1E-16,3E-16)

ax.axes.set_ylim(-1E-16,0.2E-15)
ax.set_xlabel("Observed Wavelength (Å)",fontsize=12)
ax.set_ylabel("Flux (erg/s/cm²/Å))",fontsize=12)

plt.savefig("./GRB230325A_NIR_WithTelluricCorrection.png",bbox_inches="tight",facecolor="white")
plt.show()
