# code used to produce plots of the reduced and calibrated X - Shooter AT2017gfo spectrum
# that was produced using 'PypeIt'
# The building blocks for this code was helpfully provided by Tom Reynolds (NBI)

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

linewidth=0.5

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
        return np.array([spec_f.field("wave"),spec_f.field("ivar")])



NIRpypeIt = FitsReader("../AT2017gfoNIR_tellcorr.fits")
VISpypeIt = FitsReader("../AT2017gfoVIS_tellcorr.fits")
UVBpypeIt = FitsReader("../AT2017gfoUVB.fits")


# cut off the ends where errors explode due to noise:
CUTOFF_INDEX = 2000

NIResoCutWave = NIReso[0][CUTOFF_INDEX:len(NIReso[0])-CUTOFF_INDEX]
VISesoCutWave = VISeso[0][CUTOFF_INDEX:len(VISeso[0])-CUTOFF_INDEX]
UVBesoCutWave = UVBeso[0][CUTOFF_INDEX:len(UVBeso[0])-CUTOFF_INDEX]

NIResoVar = NIReso[3][CUTOFF_INDEX:len(NIReso[3])-CUTOFF_INDEX]
VISesoVar = VISeso[3][CUTOFF_INDEX:len(VISeso[3])-CUTOFF_INDEX]
UVBesoVar = UVBeso[3][CUTOFF_INDEX:len(UVBeso[3])-CUTOFF_INDEX]

NIRpypeItCutWave = NIRpypeIt[0][CUTOFF_INDEX:len(NIRpypeIt[0])-CUTOFF_INDEX]
VISpypeItCutWave = VISpypeIt[0][CUTOFF_INDEX:len(VISpypeIt[0])-CUTOFF_INDEX]
UVBpypeItCutWave = UVBpypeIt[0][CUTOFF_INDEX:len(UVBpypeIt[0])-CUTOFF_INDEX]

NIRpypeItvar = NIRpypeIt[1][CUTOFF_INDEX:len(NIRpypeIt[1])-CUTOFF_INDEX]
VISpypeItvar = VISpypeIt[1][CUTOFF_INDEX:len(VISpypeIt[1])-CUTOFF_INDEX]
UVBpypeItvar = UVBpypeIt[1][CUTOFF_INDEX:len(UVBpypeIt[1])-CUTOFF_INDEX]


# pypeit format is 1/var:
NIRpypeItvar = (1/NIRpypeItvar) * 1E-17
VISpypeItvar = (1/VISpypeItvar) * 1E-17
UVBpypeItvar = (1/UVBpypeItvar) * 1E-17
	      
    
fig,(ax1,ax2,ax3)=plt.subplots(3,1,figsize=(20,36))

ax1.plot(UVBesoCutWave,UVBesoVar,lw=linewidth,color="r",label="UVB ESO")
ax1.plot(UVBpypeItCutWave,UVBpypeItvar,lw=linewidth,color="k",label="UVB Pypeit")
#ax1.axes.set_ylim(np.min(UVBpypeIt[1]),np.max(UVBpypeIt[1]))


ax2.plot(VISesoCutWave,VISesoVar,lw=linewidth,color="r",label="VIS ESO")
ax2.plot(VISpypeItCutWave,VISpypeItvar,lw=linewidth,color="k",label="VIS Pypeit")
ax2.axes.set_ylim(0.0E-17,1.5E-17)

ax3.plot(NIResoCutWave,NIResoVar,lw=linewidth,color="r",label="NIR ESO")
ax3.plot(NIRpypeItCutWave,NIRpypeItvar,lw=linewidth,color="k",label="NIR Pypeit")
ax3.axes.set_ylim(0.0E-17,1.0E-17)

fig.supxlabel("Observed Wavelength (Å)", y=0.05 ,fontsize=35)
fig.supylabel("Flux-error (erg/s/cm²/Å))",fontsize=34)

for ax in (ax1,ax2,ax3):
	ax.tick_params(length=10, width=4,labelsize=24)
	for i in ax.legend(fontsize=28).get_lines(): i.set_linewidth(8)
	ax.yaxis.get_offset_text().set_fontsize(26)


plt.savefig("./ATcompared_var.png",bbox_inches="tight",facecolor="white")
plt.show()
