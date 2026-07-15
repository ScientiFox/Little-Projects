import math,time,random
from playsound import playsound
import os
#Fetch Libs
import finnhub as FH

fh_api_key = "d9b7iapr01qmk4gkilh0d9b7iapr01qmk4gkilhg"
client = FH.Client(api_key=fh_api_key)

DURATION = 38
PLAYING = 0

VOLUME = 0
UP_RAMP = 2.0
DOWN_RAMP = 3.0

ti = 0#time.time()
tme = time.time()

symbol = "AAPL"
prev_val = None

ct = 0

while (True):

    if PLAYING == 0:
        if time.time()-ti > 15.0:
            ct+=1
            print("checking...")
            try:
                quote = client.quote(symbol)
                print("Current: "+str(quote.get('c')))
            except:
                quote = prev_val
                print("Well, that didn't work....")
            ti = time.time()

            if ((prev_val != None) and (prev_val != quote)) or (ct == 3):
                PLAYING = 1
            else:
                pass

    elif PLAYING == 1:
        playsound("guitar8.mp3",block=False)
        tme = time.time()
        print("PLAYING NOW...")
        PLAYING = 2

    elif PLAYING == 2:
        if time.time()-tme < UP_RAMP:
            VOLUME = int(100*(time.time()-tme)/UP_RAMP)
            os.system("amixer sset Master "+str(VOLUME))

        if (time.time()-tme > DURATION-DOWN_RAMP):
            VOLUME = int(50+50*(DURATION-(time.time()-tme))/DOWN_RAMP)
            os.system("amixer sset Master "+str(VOLUME))

        if time.time()-tme < DURATION:
            print(VOLUME,round(time.time()-tme,2))
            pass
        else:
            PLAYING = 0
            ti = time.time()

    else:
        pass

