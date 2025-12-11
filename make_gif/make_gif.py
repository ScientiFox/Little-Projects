#Regex to sort the images and make the titles
import re

#Glob to find the files
import glob

#PIL to make the gif
from PIL import Image

N_startup = 1 #Number of times to repeat first image (aesthetic start delay)
dur = 450 #How long the gif loop should be
lp = 0 #Whether to loop or not

#Find files in the root directory ("to_gif/")
filenames = []
for ext in ['jpg','jpeg','bmp','png','tif','tiff','gif']:
    filenames = filenames + glob.glob("to_gif/*."+ext)

#Get indexed numbers out of titles to sort
f_aug = [(f,int(re.findall("\d+",f)[-1])) for f in filenames]
f_aug.sort(key=lambda x:x[1]) #actually sort them
filenames = [f[0] for f in f_aug] #make a new ordered file list

#Image lists
ims = []
for f in filenames: #loop over the list
    print(f) #not the file for checking order
    ims = ims + [Image.open(f)] #make list of PIL images

#Get a root filename
root = re.findall("/(.+)\.",filenames[0])[0]
root = re.sub("[-_]+\d+","",root) #Take out numbers and digit ligatures

#Actually save the gif
ims[0].save(root+".gif", save_all=True, append_images=[ims[0]]*N_startup+ims[1:], duration=dur, loop=lp)

