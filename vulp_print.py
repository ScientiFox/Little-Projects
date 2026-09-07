###
# Convert phonetic vulpish to print
###

phon = ['y','a','k','f','e','h','o','p','w','u','n','r','i','m',"0","1","2","3","4","5","6","7","8","9"]
char = ['જ','ﻌ','ല','ϟ','⋏','ഗ','—','υ','ᕓ','⋎','η','Ʝ','ɣ','℘','0','1','2','3','4','5','6','7','8','9']

p2c = {phon[i]:char[i] for i in range(len(phon))}
c2p = {char[i]:phon[i] for i in range(len(phon))}


'''
##Y		A		K
જ		ﻌ		ല

F		E		H
ϟ		⋏		ഗ

	O		P
	—		υ

W		U		N
ᕓ		⋎		η

R		I		M
Ʝ		ɣ		℘
'''

def vulp_to_print(vulp):

    p_out = ""

    for c in vulp:
        if c in p2c:
            p_out = p_out + p2c[c]
        elif c == ' ':
            p_out = p_out + "   "
        elif c in [',',';','.','!','?','~','-']:
            p_out = p_out + c
        else:
            p_out = p_out + '█'

    return p_out        

def print_to_vulp(prnt):

    v_out = ""

    for c in prnt:
        if c in c2p:
            v_out = v_out + c2p[c]
        elif c in [' ',',',';','.','!','?','~','-']:
            v_out = v_out + c
        else:
            v_out = v_out + '█'

    return v_out

if __name__ == '__main__':
    term = True

    while term:

        inp = input("Vulpish:")

        if inp != "x":
            p_out = vulp_to_print(inp.lower())
            print("print: ",p_out)

        else:
            term = False











