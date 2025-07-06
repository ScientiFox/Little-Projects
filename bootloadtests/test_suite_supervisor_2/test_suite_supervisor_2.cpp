/*
Larger, full-scale Arduino unit testing
Runs a multi-level check on active pins and utilities- this is supervisor side
Hardware socket for MCU has hardware-set values on each check pin
*/

//PWM pins
int PWMlist[] = {3,5,6,9,10,11};
String analogList[] = {"A0","A1","A2","A3"}; //Analog pins
int FAULTS[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}; //Holder for measured faults

//Note and freeze on failure
void serfail(){
  Serial.println("Serialfault");
  while(1);
}

//Wait for signal from supervisor
void wait_for_ack(){
  char s; //Incoming char
  long timer = millis(); //Timer set

  while (Serial.available()==0){} //Wait for data

  s = Serial.read(); //read data
  while (s != '&'){ //Wait for start-of-frame
    s = Serial.read(); //Read data
    while (Serial.available()==0){ //wait for more data
      if (millis()-timer > 3000){ //Failure ofter 3s with no signal
        serfail();
      }
    }
  }
}

//Pin testing
void IOTest(int pin){
  pinMode(pin,INPUT); //Input mode
  wait_for_ack(); //Wait for signal to continue test- will have set pin high
  delay(100); //Wait 0.1s
  if (digitalRead(pin)){ //Read pin
    Serial.print(pin); //Report successful value
    Serial.print(" test successful");
    Serial.println();
  }
  else{ //Otherwise, pin failed, report, mark fault
    Serial.print(pin);
    Serial.print(" test fail");
    FAULTS[pin-2] = 1;
    Serial.println();
  }
  Serial.println('&'); //Progress character sent
}

//Check PWM
void PWMTest(int id){

  int pin = PWMlist[id]; //Grab pin to test

  pinMode(pin,INPUT); //Set read mode

  wait_for_ack(); //Wait for test to start
  delay(100); //Delay

  long val = pulseIn(pin,HIGH); //Read pin

  Serial.print(pin); //Report value
  Serial.print(" PWM test: ");
  Serial.print(val);
  Serial.println();
  if (val < 10){ //If outside set value, note failure
    FAULTS[11+id] = 1;
  }
  Serial.println('&');
}

//Analog pin test
void analogTest(int pin){

  wait_for_ack(); //Wait for test to start
  delay(100);

  while (1){ //run indefinitely
    char s = Serial.read(); //Read serial value
    if (s == 'b'){ //mark failure if wrong value observed
      FAULTS[pin+4] = 1;
      break;}
    if (s == 'a'){ //Move along if successful
      break;}
  }
  Serial.println('&'); //Progress test
}

//State machine variable
int state = 0;

void setup(){
  Serial.begin(9600); //Start serial port
 
  //Serial test
  Serial.println('&');
  wait_for_ack();
  Serial.println("Serial test complete");

  //IO test
  for(int i = 2;i<14;i++){
    wait_for_ack();
    Serial.println('&');
    IOTest(i);
    while (Serial.available()){Serial.read();}
  }
  
  //PWM test
  for(int i = 0;i<6;i++){
    wait_for_ack();
    Serial.println('&');
    PWMTest(i);
    while (Serial.available()){Serial.read();}
  }
  
  //Analog test
  for(int i = 14;i<18;i++){
    wait_for_ack();
    Serial.println('&');
    analogTest(i);
    if (FAULTS[i+4] == 0){
      Serial.print("Analog ");
      Serial.print(analogList[i-14]);
      Serial.print(" check");
      Serial.println();}
    else{
      Serial.print("Analog ");
      Serial.print(analogList[i-14]);
      Serial.print(" Fault");
      Serial.println();}
  }
  
}


//Main loop
void loop(){

  Serial.println("Test Complete"); //Annotate test completion

  //Looping over possible faults
  for (int i=0;i<22;i++){
    if (i <= 11){
      if (FAULTS[i] == 1){
        Serial.print("IO Fault on: "); //Report IO pin fault
        Serial.println(i+2);
      }
    }
    if ((i >= 12)&(i < 18)){
      if (FAULTS[i] == 1){
        Serial.print("PWM Fault on: ");
        Serial.println(PWMlist[i-11]); //Report PWM fault
      }
    }
    if (i >= 18){
      if (FAULTS[i] == 1){
        Serial.print("Analog Fault on: ");
        Serial.println(analogList[i-18]); //Report analog pin Fault
      }
    }
  }
  while(1); //Freeze forever
}
