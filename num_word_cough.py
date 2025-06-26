####
#Num Word <cough>
#
# A cute litle script to generate words that can be constructed using numbers as digits.
#   eg. ABATE : 48473
#
# Mostly used to tease people
#
####

#Standard
import math,time,random

#PyEnchant is a nice little spellchecker!
import enchant

#Grab the US english dictionary
en_dict = enchant.Dict("en_US")

#Map numbers onto letters
lets = {0:"O",1:"I",2:"Z",3:"E",4:"A",5:"S",6:"G",7:"T",8:"B",9:"P"}
nums = {lets[a]:a for a in lets} #And then letters onto numbers

#A list of one-letter words to extract out
ONE_L = ["A","I"]

#Prep a list of 2-letter words to extract out
TWO_L = ['ab', 'ad',' ah', ' ai', ' al', ' am', ' an',' as', ' at', ' aw', ' ax', ' ay', ' be', ' bi', ' by', ' da', ' do', ' ed', ' eh', ' el',' et', ' ex',' gi', ' go', ' ha', ' he', ' hi', ' hm', ' ho', ' id', ' if', ' in', ' is', ' it',' ki', ' la',' ma', ' me', ' mi',' my',' no',' od',' of', ' oh', ' oi', ' ok', ' om', ' on', ' op', ' or', ' os', ' ow', ' ox', ' oy', ' pa',' re',' so', ' ta', ' to', ' uh', ' um', ' up', ' us',' we',' ya', ' ye', ' yo', ' ew']
TWO_L = [a.upper().strip(" ") for a in TWO_L] #Convert them to upper case. I know, I'm lazy.

#Output dictionary
output = {}

#A recursive space search 
def rec_check(length=1,max_depth=7,prev=""):

    #Loop over all 10 numbers less than 10!
    for i in range(10):

        #Recursively construct a new 'word'
        word = prev + lets[i]

        #Check and see if the word is real, in the allowed one- or two-letter words
        if en_dict.check(word) and ((len(word)==2 and word in TWO_L) or len(word)>2 or (len(word)==1 and word in ONE_L)):

            #if so, make the word string from number strings
            num = sum([10**(len(word)-i-1)*nums[word[i]] for i in range(len(word))])

            #Add it to the output for the word that sourced it
            output[word] = num
            print(str(num),":",word)#display

        #If we're still below the depth limit
        if length < max_depth:
            #Call the recursive check on the new word
            rec_check(length=length+1,max_depth=max_depth,prev=word)

#A function to directly convert as much of a string to numbers as possible
def make_to_numbers(S):

    #Output string
    S_convert = ""
    n_converted = 0 #Number converted, for checking if they're all converted elsewhere

    #Loop over characters
    for c in S.upper():
        if c in nums: #If that character is number-able
            S_convert = S_convert + str(nums[c]) #Add the number form
            n_converted+=1 #Increment the counter
        else: #Otherwise
            S_convert = S_convert + c #Just add the character

    #Return the converted character
    return S_convert,n_converted

if __name__ == '__main__':
    rec_check()





