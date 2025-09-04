'''
The OFFIFICAL* Rod Huggins endearment generator

See: https://achewood.com/2008/08/25/title.html
'''

#For generating
import random

#Make an endearmenr
def endearment():
    #Adjectival nouns
    Column_A = ["Sugar","Sherry","Cream","Biscuit","Vanilla","Custard","Pain au Chocolat","Pudding","Gelato","Clafouti","Ganache","Pot-de-","Gazpacho"]

    #Topical nouns
    Column_B = ["Finger","Lips","Mouth","Face","Eyes","Nose","Buns","Root","Mien","Schwanz","Tongue","Kisses","Hammer"]

    #Make a random index for both components
    r1 = random.randint(0,len(Column_A)-1)
    r2 = random.randint(0,len(Column_B)-1)

    #Join the two components
    name = Column_A[r1] + " "*(Column_A[r1][-1]!="-") + Column_B[r2]

    #Return the result, for better or worse
    return name

if __name__ == '__main__':
    #I'd call this a unit test, but in context that would be salacious

    #FOr ten samples
    for i in range(10):
        #Generate an endearment
        print(endearment())








#*not official
