####
#Morse trial
#
# A set of functions to decode Morse Code, using PyEnchant to look for viable
#   english words. Mainly used for decoding puzzles and things like that,
#   which is where the spell-check comes in- they don't always have actual
#   real-word spacing and breaks and such.
#
####

#Standard
import math.time.random

#Enchant for looking for words
import enchant

#Load the US english dictionary
en_dict = enchant.Dict("en_US")

#The Morse code table
MORSE2 = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
'''
#An alternate morse dictionary, throwing out 0-9
MORSE2 = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    ',':'--..--', '.':'.-.-.-',
                    '?':'..--..'}
'''

#One and two letter combination words for extracting out
ONE_L = ["A","I"]
TWO_L = ['ab', 'ad',' ah', ' ai', ' al', ' am', ' an',' as', ' at', ' aw', ' ax', ' ay', ' be', ' bi', ' by', ' da', ' do', ' ed', ' eh', ' el',' et', ' ex',' gi', ' go', ' ha', ' he', ' hi', ' hm', ' ho', ' id', ' if', ' in', ' is', ' it',' ki', ' la',' ma', ' me', ' mi',' my',' no',' od',' of', ' oh', ' oi', ' ok', ' om', ' on', ' op', ' or', ' os', ' ow', ' ox', ' oy', ' pa',' re',' so', ' ta', ' to', ' uh', ' um', ' up', ' us',' we',' ya', ' ye', ' yo', ' ew']
TWO_L = [a.upper().strip(" ") for a in TWO_L] #Lazy, I know, I know

#Build up the reverse code to letter dictionary (that's why the former is MORSE2)
MORSE = {}
for a in MORSE2:
    MORSE[MORSE2[a]] = a

#Forbidden 2-character sets to block, if you expect to have to
FORBID = ['bx', ' cj', ' cv', ' cx', ' dx', ' fq', ' fx', ' gq', ' gx', ' hx', ' jc', ' jf', ' jg', ' jq', ' js', ' jv', ' jw', ' jx', ' jz', ' kq', ' kx', ' mx', ' px', ' pz', ' qb', ' qc', ' qd', ' qf', ' qg', ' qh', ' qj', ' qk', ' ql', ' qm', ' qn', ' qp', ' qs', ' qt', ' qv', ' qw', ' qx', ' qy', ' qz', ' sx', ' vb', ' vf', ' vh', ' vj', ' vm', ' vp', ' vq', ' vt', ' vw', ' vx', ' wx', ' xj', ' xx', ' zj', ' zq', ' zx']
FORBID = [a.upper() for a in FORBID]

#Longest morse sequence
M_max = max([len(MORSE2[a]) for a in MORSE2])

#Sample messages to decode
msg = "-.-..-.-...-.--.-"

msg2 = '-.-..-.-...-'
msg3 = '-.-..-.-...'
msg6 = "-.-..-.-...-.-.-"

msg4 = '-...-.--.-'
msg42 = '-...-.-.-'
msg5 = '-.'

def to_morse(seg):
    #Convert a character segment from morse code, if possible
    if seg in MORSE:
        return MORSE[seg] #Return converted if you can
    else:
        return False #Annote it's not valid if not

#Validate solutions against a message
def check_all(sols,msg):

    k = True #Loop flag
    i = 0 #Incrementor

    #While still running and less than the length of the solution
    while k and i < len(sols):
        cvt = "" #For a conversion

        for l in sols[i]: #Loop over letters
            cvt = cvt + MORSE2[l] #Convert solution letter to morse

        print(cvt) #Output the converted string

        #Check if the converted string is the message
        if cvt != msg:
            print(sols[i]) #Output results if so
            print(cvt)
            print(msg)
            k = False #And terminate

        i+=1 #increment pointer

#Filter out solutions with punctuation right in the middle
def check_punctuation(sols):

    op = [] #Output list

    #Look through the solutions
    for soln in sols:

        is_good = True #Check flag

        #Check against punctuation characters
        for a in ['.','?']:
            #If punctuation in there, and not at the end
            if (a in soln) and not(soln.split(a)[0] == soln[:-1]):
                is_good = False #reject the solution

        #If you didn't rule it out on that basis
        if is_good:
            op = op + [soln] #Keep the solution

    #Return the filtered list
    return op 

#Recursively try decoding of sub-strings of a solution
def dec_en(soln):

    #If there's a comma in the solution
    if "," in soln:
        soln_part = soln.split(",") #Split by commas
        pt_sols = [] #Make a solution list

        #Looping over each part of the split solution
        for pt in soln_part:

            pt_sol = dec_en(pt)#Recursively decode

            if pt_sol == []: #Return nothing at the bottom of the recursion
                return []

            #Add in the solution to the solution parts list
            pt_sols = pt_sols + [pt_sol]

        #If at single-part level after commas
        while len(pt_sols) > 1:

            pt_join = [] #make a list for join parts

            #Loop over the latter partitions
            for a in pt_sols[-2]:
                for b in pt_sols[-1]:
                    pt_join = pt_join+[a+", "+b] #Here's where the commas show up

            #Put the joined solutions into the partition list
            pt_sols[-2] = pt_join
            pt_sols = pt_sols[:-1] #pop the original last partition set off

        #Return the earlier partition set
        return pt_sols[0]

    #Make a list of solutions and an iterator
    sols = []
    i = 0

    #Looping over the solutions
    while i < len(soln):

        p1 = soln[:i+1] #Partition 1 is the first split about i
        p2 = soln[i+1:] #Partition 2 the second

        #Construct a logic case for valid words:
        #   p1 is real and longer than 2 characters
        #   OR it's a valied 1 or 2 letter word
        check = (en_dict.check(p1) and len(p1) > 2)
        check = check or (len(p1)==1 and p1 in ONE_L)
        check = check or (len(p1)==2 and p1 in TWO_L)

        #If the p1 partition is a valid word 
        if check:

            #Check that p2 isn't ""
            if len(p2) > 0:
                sols_p2 = dec_en(p2) #Recursively decode the second partition

                #If there's words in there...
                if len(sols_p2) > 0:
                    #append p1 and all the p2 solutions to the list
                    sols = sols + [p1 + " " + a for a in sols_p2]
            else:
                #If p2 is "", just add p1 as a remainder soltuon
                sols = sols + [p1]
        else: #If p1 isn't a valid partition, pass
            pass

        i+=1 #Increment partition pointer

    #return the solution list
    return sols

#Filter solutions
def en_filt_sols(sols):

    op = [] #Output list

    #Looping over all solutions
    for sol in sols:

        # If the last character is punctuation
        if sol[-1] in [".","?"]:
            ens = dec_en(sol[:-1]) #remove the punctuation and decode the rest

            #If there's any solutions in there
            if len(ens) > 0:
                print(ens) #Display it
                ens = [a+sol[-1] for a in ens] #Populate the list with punctuation back in
                op = op + [(sol,ens)] #Add the solution and decode lists to output
        else: #Otherwise
            ens = dec_en(sol) #Just decode the solution
            if len(ens) > 0: #If there's answers found
                op = op + [(sol,ens)] #Add them to the output
    # reutrn the output list
    return op

#Recursive decomposition function
def decompose(msg,depth=0):

    #List of solutions
    sols = []
    i = 0 #Incrementor

    #While the incrementor is lower that the longest mores code character and the message
    while i < min([M_max,len(msg)]):

        sols_i = [] #Solutions up to i length

        #Make into two partitions
        p1 = msg[:i+1]
        p2 = msg[i+1:]

        #Make partition 1 into morse code
        p1_dec = to_morse(p1)

        #If valid under morse conversion
        if p1_dec:
            if len(p2)>0: #If p2 isn't empty
                sols_p2 = decompose(p2,depth=depth+1) #recursively decompose p2
                #Add the solutions of the two partitions to the i solutions list
                sols_i = [p1_dec+a for a in sols_p2]
            else: #Otherwise, just add p1
                sols_i = [p1_dec]

        #Append the solutions for i to the full solutions
        sols = sols + sols_i
        i+=1 #Increment i

    #Return the solution list
    return sols

#Optional function to remove non-allowed 2-character words
def remove_forbid(sols,forbid):

    #Processed solutions list and incrementor
    sols_proc = []
    i = 0

    #Looping over all solutions
    for s in sols:
        is_good = True #Pass flag

        #Check all forbidden character codes
        for f in forbid:
            if f in s: #if you find one
                print("tivk") #Display note
                is_good = False #Mark flag as bad
            else: #Otherwise carry on
                pass

        #If no forbidden pairs found
        if is_good:
            sols_proc = sols_proc + [s] #Add to solution list
        else: #Otherwise do nothing
            pass

        i+=1 #Increment index

        if i%1000 == 0: #Every thousand solutions...
            print(i,len(sols_proc)) #Print a status update

    #Return processed solutions
    return sols_proc

#Main function
if __name__ == '__main__':

    #Decompose the first message
    sols = decompose(msg)
    print(len(sols))

    #Check it was validly translated
    sols = check_punctuation(sols)
    print(len(sols))

    #Filter out solutions for punctuation
    en_sols = en_filt_sols(sols)
    print(len(en_sols))

    #prepare an output string
    op_str = ""
    for soln in en_sols: #Over all valid solutions
        print(soln[0]) #Display the solution
        op_str = op_str + soln[0] + "\n" #Append to the string

        #Add each full decomposition into the string
        for interp in soln[1]:
            op_str = op_str + "  " + interp + "\n"
            print("  ",interp)

    #Open up an output filr
    f = open("basic_en_cands.txt",'w+')
    f.write(op_str) #Write solution candidates filr
    f.close() #close file




