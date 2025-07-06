###
#
# Arduino automatic bootload and test routine
#  Sends avrdude commands to upload to a connected Arduino-compatible, and run test
#  routines- for automated QA. Bootloader ISP AVR MCU is also configured with test hardware,
#  so it gets the ISP firmware, runs the upload, then gets the test supervisor firmware,
#  and then runs QA on the newly bootloaded chip.
#
###


#Standard Commands:
#avrdude -P COM34 -b 19200 -c avrisp -p m328p -v -e -U efuse:w:0x05:m -U hfuse:w:0xD6:m -U lfuse:w:0xFF:m
#avrdude -P COM34 -b 19200 -c avrisp -p m328p -v -e -U flash:w:hexfilename.hex -U lock:w:0x0F:m
#optiboot_atmega328.hex

#For sending CLI commands
import os,subprocess

#Upload Counter
ct = 0

#Run forever
while (1):

    #put avrisp on parent - bootload hardware.
    subprocess.call("arduino --board arduino:avr:micro:cpu=atmega328 --port COM34 --upload ArduinoISP.ino")

    #set child fuses
    subprocess.call("avrdude -P COM9 -b 19200 -c avrisp -p m328p -v -e -U efuse:w:0x05:m -U hfuse:w:0xD6:m -U lfuse:w:0xFF:m",shell=True)

    #upload child test
    subprocess.call("avrdude -P COM34 -b 19200 -c avrisp -p m328p -v -V -e -U flash:w:makerboard_test_3.hex -U lock:w:0x0F:m",shell=True)

    #Put supervisor script on parent
    subprocess.call("arduino --board arduino:avr:micro:cpu=atmega328 --port COM34 --upload test_supervisor_3.ino")

    #put avrisp on parent
    subprocess.call("arduino --board arduino:avr:micro:cpu=atmega328 --port COM34 --upload ArduinoISP.ino")

    #upload child bootloader
    subprocess.call("avrdude -P COM9 -b 19200 -c avrisp -p m328p -v -e -U flash:w:optiboot_atmega328.hex -U lock:w:0x0F:m",shell=True)

    #Increment counter
    ct=ct+1

    #Input to hold until new chip inserted
    raw_input("---" + str(ct))

