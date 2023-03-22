# code used to rebin X - Shooter data
# I DID NOT ENGINEER THIS CODE MYSELF, 
# I GOT IT PROVIDED FROM MY THESIS SUPERVISOR: Johan Peter Uldall Fynbo 

from astropy.io import fits                                                                                                                
import numpy as np
from astropy.io.fits import getheader
from astropy.io.fits import setval
from astropy.utils.data import get_pkg_data_filename
from scipy import ndimage
 
# Utility to reshape and average an array for fast binning
# See: http://scipython.com/blog/binning-a-2d-array-in-numpy/
 
def rebin(arr, new_shape):
  shape = (new_shape[0], arr.shape[0] // new_shape[0],
    new_shape[1], arr.shape[1] // new_shape[1])
  return arr.reshape(shape).mean(-1).mean(1)
 
#frame = fits.open('M.XSHOOTER.2019-04-04T09:52:07.000.fits')
inname = 'XSHOO.2017-08-19T15:55:14.764'
outname = inname+'_binnned'
fits_file = get_pkg_data_filename(inname+'.fits')
fits.info(fits_file)
data = fits.getdata(fits_file, ext=0)
hdr = getheader(inname+'.fits')
 
#Read the file size and x and y
NAXIS1 = hdr['NAXIS1']
NAXIS2 = hdr['NAXIS2']
 
#Bin the file
binfactory = 2
binfactorx = 1
meanfactor = float(binfactorx*binfactory)
newysize = int(NAXIS2/binfactory)
newxsize = int(NAXIS1/binfactorx)
out = np.zeros((newysize, newxsize))
thisimage = np.copy(data[:,:])
out[:,:] = rebin(thisimage, (newysize, newxsize))
out[:,:] = meanfactor*out[:,:]
 
#Update the header with new binning and write to fits file
fits.writeto(outname+'.fits',out,hdr,overwrite=True)
fits_file = get_pkg_data_filename(outname+'.fits')
fits.setval(fits_file, 'HIERARCH ESO DET WIN1 BINX', value=binfactorx, ext=0)
fits.setval(fits_file, 'HIERARCH ESO DET WIN1 BINY', value=binfactory, ext=0)
fits.info(fits_file)
