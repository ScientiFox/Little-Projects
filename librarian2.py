###
#
# Webcam-based bar code reader for LVL1 makerspace book checkout
#
###

#zbar barcode reading from images
import zbar

#image processing
import Image
import cv2
import numpy as np

#for grabbing ISBN lookup
import urllib2

 #Open the camera
cam = cv2.VideoCapture(1)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 120);
cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 180);

#Make a viewing window
winName = "Sighting"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

#A mask to overlay on the image
window_mask = np.zeros((120, 180))

#Main loop
while True:

    # create a reader
    scanner = zbar.ImageScanner()

    # configure the reader
    scanner.parse_config('enable')

    # obtain image data
    t_i = cam.read()[1]

    # process the image to send to zbar    
    pil = Image.fromarray(t_i).convert('L')
    width, height = pil.size
    raw = pil.tostring()

    # wrap image data
    image = zbar.Image(width, height, 'Y800', raw)

    # scan the image for barcodes
    scanner.scan(image)

    # extract results
    for symbol in image: #for each found code

        # do something useful with results
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

        #ISBN lookup
        url_pre_ISBN = "http://www.isbnsearch.org/isbn/"

        #Grab ISBN type
        if (symbol.type == symbol.ISBN10) or (symbol.type == symbol.ISBN13):
            ISBN = symbol.data #Get the data from the symbol
            ISBN_String = str(ISBN) #Make it a string

            #use urllib to get the lookup page
            req = urllib2.Request(url_pre_ISBN+ISBN_String, headers={'User-Agent' : "Magic Browser"}) 
            con = urllib2.urlopen( req ) #Grab request data
            html = con.read() #read the data

            #Extract the book title from the returned HTML
            D = html.split("title>")[1].split("<")[0]
            print D.split("|")[1] #Output to terminal

    #Show the image
    cv2.imshow( winName,  t_i)
    key = cv2.waitKey(10) #display image feed

    if key == 27: #Exit on esc press
       cv2.destroyWindow(winName)
       break
