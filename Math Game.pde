
import processing.net.*;

//loop counter
int i = 0;
int fctr = 0;

//score timer
long ttimer = millis();
int min = 0;
int sec = 0;

//delay setting
int delay = 500;

//Blink timer & counter
long btimer = millis();
int bctr = 0;

//Button selection array
int[] selected = {0,0,0,0,0};

//to display the time
String timeStr = "";

//Values for problem
int A = 7;
int B = 12;
int C = 4;

//0ps for problem
int o1 = 0;
int o2 = 2;
char ops[] = {'+','-','x'};

//Answer counter & timer
long atimer;
int answers = 0;
int ans_state = 0;

//Answers
int ans[] = {0,10,55,9,4};
int submit = 0;
int answer = 55;
int deld = 1;
long ans_timer;

//points stuff
long points_timer;
long points;
int bonus = 0;
int dpts;

//button selected
int button = -1;

//Function to calculate an answer base don all 8 fundamantal operation combinations
int get_answer(int A, int B, int C, int op1, int op2){
  if ((op1 == 0)&(op2 == 0)){
    return A+B+C;}
  if ((op1 == 1)&(op2 == 0)){
    return A-B+C;}
  if ((op1 == 2)&(op2 == 0)){
    return A*B+C;}
  if ((op1 == 0)&(op2 == 1)){
    return A+B-C;}
  if ((op1 == 1)&(op2 == 1)){
    return A-B-C;}
  if ((op1 == 2)&(op2 == 1)){
    return A*B-C;}
  if ((op1 == 0)&(op2 == 2)){
    return A+B*C;}
  if ((op1 == 1)&(op2 == 2)){
    return A-B*C;}
  if ((op1 == 2)&(op2 == 2)){
    return A*B*C;}
  else{
    return 0;}
}

void setup() {

  size(400, 300); //Build the window
  noStroke(); //Clear it
  frameRate(30); //Set the update rate
  background(102); //Neutral base background
  textSize(10); //Set the size of the text
  fill(202,201,218);  //Put in the actual background
}

void draw() {

  //Wipe screen
  clear();

  //set background
  background(61,135,201);

  //On start of a cycle, start timer
  if (i == 0){
    btimer = millis();
    i++; //Increment loop
  }

  //Do once - show instruction panel
  if (i == 1){
    fill(100,10,150); //Instruction color
    textSize(25); //Larger text for this

    if (millis()-btimer>1000){ //1st second
      text("Select your answer to",10,50); //initial text
      text("the question.",10,72);}
    if (millis()-btimer>2000){ //Next text after a second
      text("the question. You will be timed.",10,72);}
    if (millis()-btimer>4000){ //next text after 2 seconds
      text("click to begin!",10,135);}
    if ((millis()-btimer>4000)&(mousePressed)){ //wait for click
      ttimer = millis(); //main timer resets
      atimer = millis();
      points_timer = millis();
      i++;} //Move to next state
  }

  //Main loop      
  if (i == 2){ //game start

    fill(100,10,150); //Game fill

    //Display question
    textSize(25);
    text(str(A)+" "+ops[o1]+" "+str(B)+" "+ops[o2]+" "+str(C)+" = ?",50,50);

    //draw loop ctr
    textSize(10);
    text(str(fctr),389-6*floor(log(float(i))/log(10)),290); //Magic points calculation
    
    //draw answers and buttons, also check button
    for (int k=0;k<answers;k++){ //over the number of answers

      textSize(20);
      fill(100,10,150); //Set colot
      text(str(ans[k]),50,90+30*k); //draw kth answer at height set by k

      //Draw select button
      fill(202,201,218);
      ellipse(45,82+30*k,10,10);

      //Check if select button clicked
      if ((dist(45,82+30*k, mouseX, mouseY)<10)|(button == k)){
        fill(110,110,218); //fill button
        ellipse(45,82+30*k,8,8);
        if (mousePressed){
          button = k; //Mark which answer was selected
        }
      }
      
    //Draw 'submit' button
    if (((mouseY > 170)&(mouseY<200)&(mouseX>160)&(mouseX<250)|(ans_state > 0))&(answers == 5)){
      fill(120,170,225); //highlight button
      if ((mousePressed)&(ans_state == 0)){ //if clicked, submit answer from button
        submit = 1;}
    }
    else{fill(120,130,225);} //otherwise lowlight

    //draw the actual button and text
    rect(160,200,90,-30);
    fill(180,10,10);
    text("Submit!",170,195);

    //If submitting an actual answer
    if ((submit == 1)&(button != -1)){ 
      ans_timer = millis(); //mark answer time
      if (ans[button] == answer){ //if right answer
        ans_state = 1; //flag for true
        submit = 0; //clear submit flag
      }
      if (ans[button] != answer){ //if wrong
        ans_state = 2; //set flag to answered but incorrect
        submit = 0; //clear submit flag
      }
    }

    //FOr correct answer
    if (ans_state == 1){
      fill(10,240,50); //Set note color
      text("Yeah!",100,200); //display correct text

      
      if (millis() - ans_timer > 1000){ //After 1st second after answer
        ans_state = 0; //resetn answer flag
        A = int(random(4,20)); //New problem variables
        B = int(random(0,20));
        C = int(random(3,20));
        o1 = int(random(0,3));
        o2 = int(random(0,3));
        answer = get_answer(A,B,C,o1,o2); //new answer
 
        for (int j = 0; j < 5; j++){ //Random wrong answers
          ans[j] = j + int(random(min(-2*answer,2*answer),max(-2*answer,2*answer)));
        }
        
        //Add in real answer at random location
        ans[int(random(0,5))] = answer;
        bonus = int(o1 == 2) + int(o2 == 2); //bonus points for 2x multiplication problem
        points += dpts; //Increment points counter
        points_timer = millis(); //reset timer for points
        answers = 0; //Answer state reset to 0
        button = -1; //button flag cleared
        deld = int(random(0,5)<2); //Random answer display delay - for DRAMA!
      }
    }
    
    if (ans_state == 2){ //If the wrong answer
      fill(240,10,50); //wrong color
      text("No.",100,200); //Wrong answer message
      if (millis() - ans_timer > 1000){ //give it 1 second
        ans_state = 0; //reset answer
        points += max(-20,dpts - 25); //decrease points by penalty
      }
    }
  }
  
    //increment #answers
    if (millis() - atimer > delay*(1+(deld)*3*int(answers == 4))){ //semi-random delay to put answers up
      answers = answers + 1*int(answers != 5); //looped incrementor over all 5 answers
      atimer = millis();} //answer display timer
    
    //Track the elapsed time  
    int i_sec = int((millis() - ttimer))/1000; //total seconds incremented
    sec = sec + i_sec; //total seconds counter
    ttimer = ttimer + 1000*i_sec; //ms based timer
    if (sec >= 60){ //Minute incrementor
      min++;
      sec = sec - 60;
    }
  
    //display elapsed time
    timeStr = str(min)+":";
    if (sec < 10){
      timeStr = timeStr+"0";}
    timeStr = timeStr + str(sec);
    textSize(40);
    fill(6,82,139);
    text(timeStr,150-10*int((log(min)/log(10))),270); //calculate length of string for positioning constant last number
    
    //frame counter
    if (fctr != -1){
      fctr++;} //Diagnostic

    //display points
    dpts = max(1,(15000+bonus*5000 - int((millis()-points_timer)))/1000);
    textSize(15);
    fill(220,200,20);
    text("Points: " + str(dpts),260,180);
    text(str(int(points)),260,195);
    text(str(int(deld)),260,210);

    //win/lose conditions >100 or <-100 points
    if (points >= 100){
      i = 3;
      atimer = millis();}
    if (points <= -100){
       i = 4;
       atimer = millis();}
      
  }
  
  //Win condition display
  if (i == 3){
    //you win!
    textSize(30);
    fill(20,190,80);
    text("win.",150,200);
    if (millis() - atimer > 3000){
      exit(); //close on win
    }
  }

  //Lose condition display
  if (i == 4){
    //you lose!
    textSize(30);
    fill(190,80,20);
    text("loes[sic].",150,200);
    if (millis() - atimer > 3000){
      exit();//also close on lose
    }
  }
}
