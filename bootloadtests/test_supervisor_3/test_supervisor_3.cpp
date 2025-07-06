/*
 * Makerboard test supervisor
 */

//Include soft serial library
#include <SoftwareSerial.h>

//Start soft serial
SoftwareSerial mySerial(8, 9); // RX, TX

void setup() {
  //make the software and standard serial port
  mySerial.begin(9600);
  Serial.begin(9600);

  //Send a start character
  mySerial.print("a");

  delay(500); //Wait half a second
  
}

void loop() {

  //Wait until serial data available on soft port
  while (mySerial.available() == 0){
    Serial.println("w");}

  //Read the character
  char Read = mySerial.read();

  //Report read to PC
  Serial.println(Read);

  //Hold forever
  while (1){}
}
