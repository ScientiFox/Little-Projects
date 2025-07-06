//Timer variables
let clock;
d = new Date();
i_time = d.getTime();

//Variables for output display
let opStr,resultsString;
opStr = "";
resultsString = "";

//Function execution flags and object holders
let Fn,exitCond,intervalRun;
initFn = null;
loopFn = null;
exitCond = false;
intervalRun = null;

//Initial start examples
globalsExample = 'i,j,counter,timer';

setupExample = 'i = 0;\n\
j = 100;\n\
\n\
counter = 0;\n\
\n\
timer = clock;';

loopExample = 'counter++;\n\
\n\
if (clock-timer>100){\n\
  j--;\n\
  i++;\n\
  setRes(i*j);\n\
  timer = clock;\n\
}\n\
\n\
if (j==10){\n\
  setRes(getRes() + "<br/> DONE")\n\
  exitCond = true;\n\
}\n\
\n\
opStr = q;'

//Load usage examples into input boxes
document.getElementById('globalVars').value = globalsExample;
document.getElementById(`setupArea`).value = setupExample;
document.getElementById(`loopArea`).value = loopExample;

//Start supervisor on 100Hz rate
setInterval(tickTock,10)

//Supervisor routine
function tickTock(){
	//Update time
	d = new Date();
	clock = d.getTime()-i_time;
	document.getElementById('clock').innerHTML=(clock/1000.0)+"s";

	//Update output regularly
	document.getElementById("outputText").innerHTML = opStr;
	
	//Watch for internal exit
	if (exitCond){killCode();}
}

//Function to stop loop execution
function killCode(){
	if (intervalRun != null){clearInterval(intervalRun);} //clear interval function
	intervalRun = null; //set function holder null
}

//Wrapper to set the 'results' div
function setRes(str){document.getElementById('resultsText').innerHTML = str;}

//Wrapper to fetch the 'results' div
function getRes(str){return document.getElementById('resultsText').innerHTML;}

//Function to parse globals into useable code
function parseGlobals(){
	globalString = document.getElementById('globalVars').value; //Grab the input
	cVar = ""; //Current variable
	prepString = ""; //Global-making code string
	for (let i=0;i<globalString.length;i++){ //looping over input
		if (globalString[i] != ","){cVar = cVar + globalString[i];} //If not delimiter, add to current var
		else if (globalString[i] == ",") { //if delimiter
			if (cVar != ''){prepString = prepString + "this." + cVar + "= null;\n";} //Make a this.* snip for the variable setting
			cVar = ''; //clear current to new variable
		}
	}
	return prepString; //return preamble string
}

//Function to execute scratchpad code
function runCode(){

	prepString = parseGlobals(); //Parse the globals to code
	setupString = document.getElementById('setupArea').value; //grab the setup code
	loopString = document.getElementById('loopArea').value; //grab the loop code
	loopPeriod = parseInt(document.getElementById('loopPeriod').value); //grab loop run frequency

	if (intervalRun != null){clearInterval(intervalRun);} //If another loop going, clear it

	//Eval of global making string and setup together puts them into workspace
	const initFn = eval(prepString+setupString);
	const loopFn = Function(loopString); //Build loop function to run on set period

	exitCond = false; //CLear the exit for an internal quit
	intervalRun = setInterval(loopFn,loopPeriod); //Set the loop function to run on regular period
}


