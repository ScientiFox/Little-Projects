/*
 * Version 3 test suite: testee side
 */

//Include soft serial port
#include <SoftwareSerial.h>

//Attach software serial
SoftwareSerial mySerial(9, 8); // RX, TX

//Flag for failure state
int failState = 1;

//Startup
void setup() {
  mySerial.begin(9600); //Start serial port (to supervisor)

  while (mySerial.available() == 0){} //Wait for data

  //Flash pin 10 for note of ack to observer
  pinMode(10,OUTPUT);
  digitalWrite(10,HIGH);
  delay(100);
  digitalWrite(10,LOW);
  
}

//Main loop
void loop() {

  //Looping over analog pins
  for (int i = 14; i < 19;i++){
    int Read = analogRead(i); //Read A* port
    if ((Read > 400)&&(Read < 700)){} //Check value is in acceptable range
    else if (failState){ //Otherwise, transmit a failure
      mySerial.write("F");
      failState = 0; //Note failure
    }
  }

  //Looping over digital pins- tests them in IO pairs- one out to other in, then flip
  for (int i = 2;i < 7;i=i+2){
    pinMode(i,OUTPUT); //Set output
    pinMode(i+1,INPUT); //Set input
    digitalWrite(i,HIGH); //Write the first IO test

    if (digitalRead(i+1)){} //If both work, first O and I both work
    else if (failState){ //Else, note failure
      mySerial.write("F");
      failState = 0;
    }

    pinMode(i+1,OUTPUT); //Swap IO to OI test
    pinMode(i,INPUT); 
    digitalWrite(i+1,HIGH);

    if (digitalRead(i)){} //Check if reverse works
    else if (failState){
      mySerial.write("F");
      failState = 0;
    }

  }

  if (failState == 1){ //If no fault found, report test success
    mySerial.write("S");
  }
  
}
