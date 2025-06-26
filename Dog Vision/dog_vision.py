####
#
# Dog Vision
#
#   A brief script to transform image values to eliminate and re-map an image
#   to replicate the visual color spectrum accessible to canines. Based on research
#   into spectral sensitivity of canine cone receptors and image mapping for
#   monitors.
#
####

#Standard
import math,time,random

#Image processing
import numpy as np
import cv2

#File operations
import glob

#Grab list of files of several types in the local source file
files = glob.glob("imgs/*.jpg")
files = files + glob.glob("imgs/*.jpeg")
files = files + glob.glob("imgs/*.png")
files = files + glob.glob("imgs/*.bmp")

#Vision space transform constants- inferred from research papers on canine vision
# and interpolations on screen visibility
J = 0.35
K = 0.6
L = 1.0-K
g = 1.9

#For each of the files found
for fil in files:

    #Load up the files and make an output copy
    im = cv2.imread(fil)
    im_out = np.copy(im)

    #Scale the BGR values against max
    B = im[:,:,0]/255
    G = im[:,:,1]/255
    R = im[:,:,2]/255

    #Calculate proportional geometric weighted averages
    Rp = np.sqrt((R**K)*(G**L))
    Gp = np.sqrt((R**K)*(G**L))
    Bp = 1.0*B**J

    #Rescale to 255 with gamma transform factor g
    im_out[:,:,0] = np.astype(255*Bp**g,np.uint8)
    im_out[:,:,1] = np.astype(255*Gp**g,np.uint8)
    im_out[:,:,2] = np.astype(255*Rp**g,np.uint8)

    #PREVIEW the outputs as thumbnails
    sz = np.shape(im_out)
    W_th = 300
    scaleF = 300/sz[1]
    cv2.imshow("win",cv2.resize(im_out,(int(sz[1]*scaleF),int(sz[0]*scaleF))))
    cv2.waitKey(300)

    #Write the output files
    cv2.imwrite("op/dog_vision_"+fil.split("/")[-1],im_out)

#Close the preview windows
cv2.destroyAllWindows()
