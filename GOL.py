###
#
# Conway's Game of Life simulator
#  A rite of passage for every programmer-scientist!
#
###

#Standard
import math,random,time

#For numerical processing
import numpy as np

#For display
import cv2

#Wrapper to shift an array up one cell
def shift_up(array):
    size = np.shape(array)
    return np.vstack((array[1:,:],np.zeros((1,size[1]))))

#Wrapper to shift an array down one cell
def shift_down(array):
    size = np.shape(array)
    return np.vstack((np.zeros((1,size[1])),array[:-1,:]))

#Wrapper to shift an array left one cell
def shift_left(array):
    size = np.shape(array)
    return np.hstack((array[:,1:],np.zeros((size[0],1))))

#Wrapper to shift an array, yup, right one cell
def shift_right(array):
    size = np.shape(array)
    return np.hstack((np.zeros((size[0],1)),array[:,:-1]))

#Function to label a cell by its neighbors
def label_neighbours(array):
    #Zero array size of original
    neighbours = np.zeros(np.shape(array))

    #add shifted arrays in 8 cardinal directions to get counts of neighbors
    neighbours = neighbours + shift_down(array)
    neighbours = neighbours + shift_up(array)
    neighbours = neighbours + shift_left(array)
    neighbours = neighbours + shift_right(array)        
    neighbours = neighbours + shift_up(shift_left(array))
    neighbours = neighbours + shift_up(shift_right(array))
    neighbours = neighbours + shift_down(shift_left(array))
    neighbours = neighbours + shift_down(shift_right(array))    

    #return counts array
    return neighbours

#Core Game of Life Class
class GOL:
    def __init__(self,size):
        #build an empty array of a given size
        self.world = np.zeros(size)
        self.size = size

    def populate(self,image,_mode=False):
        #Populate based on an input image

        #get size for insertion
        i_size = np.shape(image)

        #flatten if needed
        if (len(i_size)>2):
            image = np.sum(image,axis=2)/i_size[2]

        if (_mode):
            #Original threshold-to binary version
            self.world[:i_size[0],:i_size[1]] = 1*(image>np.average(image))
        if not(_mode):
            #Direct input- does weird things!
            self.world[:i_size[0],:i_size[1]] = image

    #Do a GOL step
    def iterate(self):
        #get neighbor sum array
        neighbours = label_neighbours(self.world)

        #Change condition logic
        die = 1 - (1*(neighbours > 3) + 1*(neighbours < 2))
        born = (1 - self.world)*1*(neighbours == 3)

        #Update world array
        step = (die*self.world) + born

        #return updated world
        return step

#restrained linear GOL
class GOL_2D:
    def __init__(self,size):
        #world is 1xsize now
        self.world = np.zeros((1,size))
        self.size = size

    def populate(self,row):
        #populate the linear world with a line input
        self.world[:len(row)] = row

    def iterate(self):
        #iterate- neighborhood is simple translation now
        neighbourhood = np.zeros((1,self.size)) + shift_left(self.world) + shift_right(self.world)

        #Same rule for updates
        die = 1 - (1*(neighbourhood == 2)+ 1*(neighbourhood==0))
        born = (1 - self.world)*(neighbourhood == 1)

        #update the array
        step = die*self.world + born

        #return new array
        return step

if __name__ == '__main__':

    #Make GoL simulator
    size = 300
    G = GOL((size,size))

    #Build a random init array
    init = np.random.random(size=(size,size))
    init = 1*(init>0.5)

    #Put the array in the sim
    G.populate(init)

    #previous step monitor
    step_p = init

    running = True #Run flag
    while (running): #Loop until killed

        #Do an update step
        step = G.iterate()

        #Show the step in-window
        cv2.imshow("GoL",step)

        #Watch for key press
        key = cv2.waitKey(10) #100Hz update rate
        if key == 27: #On 'esc' key
            running = False #set to stop running

        #Watch for static world
        if (step==step_p).all():
            print("Dead World") #Note it's static and end
            running = False

        G.world = step #update GoL world
        step_p = step #update prior step

    input("Done looking?") #Hold to observe endpoint until ready to quit

    #Kill windows on quit
    cv2.destroyAllWindows()
