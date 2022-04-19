from math import*
from numpy import*
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager, FontProperties
import shutil
import pyfits
import aplpy
from pyavm import AVM
import os
f = open("hicatlist","r")
for line in f:
 xx0 = str(line.split()[0])
 xx2 = str(line.split()[2])
 print xx2
 
 
 print "/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/gal_j"+str(xx2)+".fits"
 os.system("cp /Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/gal_j"+str(xx2)+".fits .")
 os.system("cp /Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/gal_h"+str(xx2)+".fits .")
 os.system("cp /Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/gal_k"+str(xx2)+".fits .")

 im=pyfits.getdata("/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_j"+str(xx2)+".fits")
 hdr1=pyfits.getheader("/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_j"+str(xx2)+".fits")
 hdr1.update('EPOCH', 2000.0 , comment="epoch")
 pyfits.update("/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_j"+str(xx2)+".fits",im,hdr1)

 im=pyfits.getdata("/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_h"+str(xx2)+".fits")
 hdr1=pyfits.getheader("/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_h"+str(xx2)+".fits")
 hdr1.update('EPOCH', 2000.0 , comment="epoch")
 pyfits.update("/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_h"+str(xx2)+".fits",im,hdr1)
                
 im=pyfits.getdata("/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_k"+str(xx2)+".fits")
 hdr1=pyfits.getheader("/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_k"+str(xx2)+".fits")
 hdr1.update('EPOCH', 2000.0 , comment="epoch")
 pyfits.update("/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_k"+str(xx2)+".fits",im,hdr1)
 
 
 headj=pyfits.getheader("/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_j"+str(xx2)+".fits")
 headh=pyfits.getheader("/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_h"+str(xx2)+".fits")
 headk=pyfits.getheader("/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_k"+str(xx2)+".fits")

 ximgsize = 0.45*headj.get('NAXIS1')
 yimgsize = 0.45*headj.get('NAXIS2')


 aplpy.make_rgb_cube(["/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_k"+str(xx2)+".fits","/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_h"+str(xx2)+".fits","/Users/khaled/Desktop/PhD/IRSF/phd_n/IRSFdata/calibrated/stamps/newstamps/gal_j"+str(xx2)+".fits"],str(xx2)+".fits")
 aplpy.make_rgb_image(str(xx2)+".fits",str(xx2)+"_log.png",stretch_r='log', stretch_g='log', stretch_b='log',vmin_b=472)
 ggcc = aplpy.FITSFigure(str(xx2)+"_log.png")
 ggcc.add_label(0.75, 0.06, str(xx0)+" ["+str(ximgsize)+"'' x "+str(ximgsize)+"'']", color='white',relative=True)
 #ggcc.add_label(0.75, 0.02, "By Khaled Said (UCT)", color='white',relative=True)
 
 #ggcc.label.set_color('white')
 ggcc.add_grid()
 ggcc.grid.hide()
 ggcc.axis_labels.hide_y()
 ggcc.tick_labels.hide_y()
 ggcc.axis_labels.hide_x()
 ggcc.tick_labels.hide_x()
 ggcc.ticks.hide_x()
 ggcc.ticks.hide_y()
 #ggcc.hide_grayscale()
 ggcc.show_rgb()
 ggcc.save(str(xx2)+'.eps')

os.system('rm -Rf *.fits')
os.system('rm -Rf *.png')
f.close()
#f1.close()

