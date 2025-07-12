###
# Monty Hall quick one
#
#  Entirely to prove the conjecture to someone
#
###

#Standards
import math,time,random

#Run a single sim
def run_sim(switch):

    doors = [0,1,2] #Make up the doors
    prize = random.randint(0,2) #Assign the prize
    guess = random.randint(0,2) #Assign the guess

    #If you are going to switch if you don't get it
    if switch:
        if prize == guess: #If you got it on the first try
            doors.remove(prize) #Take the prize out- switching means you won't get it now
        else: #If you didn't get it,
            doors.remove(prize) #remove the first guess and prize (leaving the un-guessed no-prize)
            doors.remove(guess) 
        opened = doors[random.randint(0,len(doors)-1)] #pick one of the remaining doors
        doors = [0,1,2] #reset doors
        doors.remove(opened) #remove the picked door after switch
        doors.remove(guess) #remove the original guess
        new_guess = doors[0] #the new guess is whichever is left
        return prize == new_guess #return if you got it after the switch
    else: #Otherwise
        return prize == guess #return if you got it without a switch!

#Loop over 100 tests total
for b in range(100):

    ns_ct = 0 #number of non-switch wins
    for a in range(10000): #10k instances
        if run_sim(0): #run the sims without switching
            ns_ct+=1 #increment if you win

    s_ct = 0 #number of switch wins
    for a in range(10000): #10k instances
        if run_sim(1): #run sim with switching
            s_ct+=1 #increment if you win

    #return the number of non-switch and switch wins
    print(ns_ct,s_ct)
