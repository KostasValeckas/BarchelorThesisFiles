# code used to produce plots of the reduced and calibrated X - Shooter AT2017gfo spectrum
# that was produced using 'PypeIt'
# The building blocks for this code was helpfully provided by Tom Reynolds (NBI)

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

linewidth=0.2

# Load many files

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
def FitsReader(filePath):
        spec_file_f = filePath
        spec_f = fits.getdata(spec_file_f,1)
        return np.array([spec_f.field("wave"),spec_f.field("flux")*1E-17])

NIRpypeIt = FitsReader("../AT2017gfoNIR_tellcorr.fits")
VISpypeIt = FitsReader("../AT2017gfoVIS_tellcorr.fits")
UVBpypeIt = FitsReader("../AT2017gfoUVB.fits")

    
fig,(ax1,ax2,ax3)=plt.subplots(3,1,figsize=(20,36))

ax1.plot(UVBeso[0],UVBeso[1],lw=linewidth,color="r",label="UVB ESO")
ax1.plot(UVBpypeIt[0],UVBpypeIt[1],lw=linewidth,color="k",label="UVB Pypeit")
ax1.axes.set_ylim(-0.5E-16,2E-16)


ax2.plot(VISeso[0],VISeso[1],lw=linewidth,color="r",label="VIS ESO")
ax2.plot(VISpypeIt[0],VISpypeIt[1],lw=linewidth,color="k",label="VIS Pypeit")
ax2.axes.set_ylim(-0.5E-16,2.3E-16)

ax3.plot(NIReso[0],NIReso[1],lw=linewidth,color="r",label="NIR ESO")
ax3.plot(NIRpypeIt[0],NIRpypeIt[1],lw=linewidth,color="k",label="NIR Pypeit")
ax3.axes.set_ylim(-0.5E-16,1.5E-16)

fig.supxlabel("Observed Wavelength (Å)", y=0.05 ,fontsize=35)
fig.supylabel("Flux (erg/s/cm²/Å))",fontsize=34)

for ax in (ax1,ax2,ax3):
	ax.tick_params(length=10, width=4,labelsize=24)
	for i in ax.legend(fontsize=28).get_lines(): i.set_linewidth(8)
	ax.yaxis.get_offset_text().set_fontsize(26)


plt.savefig("./ATcomapred_tellCorr.png",bbox_inches="tight",facecolor="white")
plt.show()
