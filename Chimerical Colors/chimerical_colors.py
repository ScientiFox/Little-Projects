###
#
# A test script for looking at Chimerical colors!
#   from: https://en.wikipedia.org/wiki/Impossible_color#Chimerical_colors
#
###

import math,time,random
import numpy as np
import cv2

def drawX(im,L,I):
    #Drawn an X on im, of length L, and intensity I

    cx,cy = int(im.shape[0]/2),int(im.shape[1]/2)
    cv2.line(im,(cx-L,cy+L),(cx+L,cy-L),(I,I,I),7)
    cv2.line(im,(cx-L,cy-L),(cx+L,cy+L),(I,I,I),7)

if __name__ == '__main__':

    #Set image size
    S = 1000
    c = int(S/2)
    i = 0 #Output counter

    #Background
    img_bk = (217)*np.ones((S,S,3))
    img_bk = img_bk.astype(np.uint8)

    ###
    # Stygian blue
    ###

    #Instructions
    img_disp = np.copy(img_bk)
    cv2.putText(img_disp,"Stare at black cross",(int(c*0.15),int(c*0.25)),cv2.FONT_HERSHEY_SIMPLEX,2.0,(0,0,0),3)
    drawX(img_disp,25,0)
    time_inst = time.time()
    while (time.time()-time_inst < 3.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    #Just X
    img_disp = np.copy(img_bk)
    drawX(img_disp,25,0)
    time_inst = time.time()
    while (time.time()-time_inst < 0.5):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    #Burn-in
    cv2.circle(img_disp,(c,c),int(c/2),(0,255,255),-1)
    drawX(img_disp,25,0)
    time_target = time.time()
    while (time.time()-time_inst < 8.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    #Target
    img_disp = np.copy(img_bk)*0
    drawX(img_disp,25,255)
    time_target = time.time()
    while (time.time()-time_target < 4.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    cv2.putText(img_disp,"Stygian Blue",(int(c/2),int(c)-int(c/6)),cv2.FONT_HERSHEY_SIMPLEX,2.0,(64,64,64),8)
    cv2.putText(img_disp,"Stygian Blue",(int(c/2),int(c)-int(c/6)),cv2.FONT_HERSHEY_SIMPLEX,2.0,(96,0,0),3)

    while (time.time()-time_target < 8.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    ###
    # Break
    ###
    img_disp = np.copy(img_bk)
    cv2.putText(img_disp,"Retina break",(int(c*0.15),int(c*0.25)),cv2.FONT_HERSHEY_SIMPLEX,2.0,(0,0,0),3)
    time_break = time.time()
    while (time.time()-time_break < 3.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    ###
    # Self-luminous red
    ###

    #Instructions
    img_disp = np.copy(img_bk)
    cv2.putText(img_disp,"Stare at black cross",(int(c*0.15),int(c*0.25)),cv2.FONT_HERSHEY_SIMPLEX,2.0,(0,0,0),3)
    drawX(img_disp,25,0)
    time_inst = time.time()
    while (time.time()-time_inst < 3.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    #Just X
    img_disp = np.copy(img_bk)
    drawX(img_disp,25,0)
    time_inst = time.time()
    while (time.time()-time_inst < 0.5):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    #Burn-in
    cv2.circle(img_disp,(c,c),int(c/2),(0,255,0),-1)
    drawX(img_disp,25,0)
    time_target = time.time()
    while (time.time()-time_inst < 8.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    #Target
    img_disp = 255*np.ones((S,S,3))
    img_disp = img_disp.astype(np.uint8)
    drawX(img_disp,25,0)
    time_target = time.time()
    while (time.time()-time_target < 4.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    cv2.putText(img_disp,"Self-luminous Red",(int(c/2),int(c)-int(c/6)),cv2.FONT_HERSHEY_SIMPLEX,2.0,(204,204,204),8)
    cv2.putText(img_disp,"Self-luminous Red",(int(c/2),int(c)-int(c/6)),cv2.FONT_HERSHEY_SIMPLEX,2.0,(219,219,255),3)

    while (time.time()-time_target < 8.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    ###
    # Break
    ###
    img_disp = np.copy(img_bk)
    cv2.putText(img_disp,"Retina break",(int(c*0.15),int(c*0.25)),cv2.FONT_HERSHEY_SIMPLEX,2.0,(0,0,0),3)
    time_break = time.time()
    while (time.time()-time_break < 3.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    ###
    # Hyperbolic Orange
    ###

    #Instructions
    img_disp = np.copy(img_bk)
    cv2.putText(img_disp,"Stare at black cross",(int(c*0.15),int(c*0.25)),cv2.FONT_HERSHEY_SIMPLEX,2.0,(0,0,0),3)
    drawX(img_disp,25,0)
    time_inst = time.time()
    while (time.time()-time_inst < 3.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    #Just X
    img_disp = np.copy(img_bk)
    drawX(img_disp,25,0)
    time_inst = time.time()
    while (time.time()-time_inst < 0.5):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    #Burn-in
    cv2.circle(img_disp,(c,c),int(c/2),(215,212,0),-1)
    drawX(img_disp,25,0)
    time_target = time.time()
    while (time.time()-time_inst < 8.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    #Target
    img_disp = np.ones((S,S,3))
    img_disp[:,:,1] = 179*img_disp[:,:,1]
    img_disp[:,:,2] = 255*img_disp[:,:,2]
    img_disp = img_disp.astype(np.uint8)
    drawX(img_disp,25,0)
    time_target = time.time()
    while (time.time()-time_target < 4.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    cv2.putText(img_disp,"Hyperbolic Orange",(int(c/2),int(c)-int(c/6)),cv2.FONT_HERSHEY_SIMPLEX,2.0,(61,192,247),10)
    cv2.putText(img_disp,"Hyperbolic Orange",(int(c/2),int(c)-int(c/6)),cv2.FONT_HERSHEY_SIMPLEX,2.0,(0,179,255),3)

    while (time.time()-time_target < 8.0):
        cv2.imshow("Chimerical Colors",img_disp)
        cv2.imwrite("/home/lancaster/Downloads/WDP Work File/PuppyRetriever_x64_433/net7.0-windows/win10-x64/Output/Run_data_check/full/make_gif/to_gif/chimerical_"+str(i)+".png",img_disp)
        i+=1
        cv2.waitKey(100)

    cv2.waitKey(-1)

    cv2.destroyAllWindows()
