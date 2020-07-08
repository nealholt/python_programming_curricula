/* This script is copied elsewhere. Consider this a read-only copy.

<!-- Version 1.0 If any changes are made to this file, change the version, because this file 
<!-- is copied in multiple locations including "functions objects and snippets", "website", and "smartamusement.com".

-Using a timer to periodically change html elements. See the functions "timedCount()" and "stopCount()".

-Variable functions. Storing functions in, and calling them from, variables.
You can call functions via variable names in javascript.
This is fantastic. It means you can pass function names as variables.
http://www.webmasterworld.com/forum91/4113.htm

//-------------------------------------------------
Variable Functions
You can call functions via variable names in javascript.
This is fantastic. It means you can pass function names as variables.
This needs to be stored in snippets separately from this script.
http://www.webmasterworld.com/forum91/4113.htm
//-------------------------------------------------
Time functions: 
http://www.w3schools.com/JS/js_timing.asp 
http://www.w3schools.com/JS/tryit.asp?filename=tryjs_timing_stop
//------------------------------------------------- 
Date Object
http://www.w3schools.com/jsref/jsref_obj_date.asp
//------------------------------------------------- */

var wait=500; //Default the wait time to a half second or 500 milliseconds.

//-------------------------------------------------
//Execute the given function 'func' then wait for 'wait' milliseconds, then repeat until someone says stop.
function timedCount(func){
	
	alert('have you considered set interval instead? http://www.elated.com/articles/javascript-timers-with-settimeout-and-setinterval/');
	
	//If the function fails, then return.
	if(!eval(func)){ return 0; }
	timer=setTimeout('timedCount("'+func+'")',wait); //pause for 'wait' milliseconds.
}
//-------------------------------------------------
//STOP
function stopCount(){ clearTimeout(timer); }
//-------------------------------------------------
//set the wait time in milliseconds.
function setWait(newWait){ wait=newWait; }
//-------------------------------------------------

//Stopwatch variables
var hour=0;
var minute=0;
var second=0;
var countdown=0; //a countdown can be set in seconds.
//-------------------------------------------------
//Start a "stop watch"
function startWatch(){
	var today=new Date();
	hour=today.getHours();
	minute=today.getMinutes();
	second=today.getSeconds();
}
//-------------------------------------------------
//Return the formatted elapsed time of the "stop watch"
function elapsedTime(){
	var today=new Date();
	var lapsHour=today.getHours() - hour;
	var lapsMin=today.getMinutes() - minute;
	var lapsSec=today.getSeconds() - second;

	/* If the number of elapsed minutes equals 1 then set the seconds of the 
	start time to zero. This prevents negative seconds from showing up. 
	Do the same thing with the minutes. */
	if(lapsMin==1){ second=0; }
	if(lapsHour==1){ minute=0; }

	return formatTime(lapsSec,lapsMin,lapsHour);
}
//-------------------------------------------------
//Return the elapsed time in seconds of the "stop watch"
function elapsedSeconds(){
	var today=new Date();
	var lapsHour=today.getHours() - hour;
	var lapsMin=today.getMinutes() - minute;
	var lapsSec=today.getSeconds() - second;

	/* If the number of elapsed minutes equals 1 then set the seconds of the 
	start time to zero. This prevents negative seconds from showing up. 
	Do the same thing with the minutes. */
	if(lapsMin==1){ second=0; }
	if(lapsHour==1){ minute=0; }

	return lapsSec+60*lapsMin+3600*lapsHour;
}
//-------------------------------------------------
//Takes seconds, minutes, hours. returns the formatted time.
function formatTime(s, m, h){
	m=checkTime(m); //add a zero in front of numbers<10
	s=checkTime(s); //add a zero in front of numbers<10

	return h+":"+m+":"+s;
}
//-------------------------------------------------
//add a zero in front of numbers<10
function checkTime(i){
	if (i<10){ i="0" + i; }
	return i;
}
//-------------------------------------------------
//set the number of seconds to countdown from.
function setCountdown(tSec){ countdown=tSec; }
//-------------------------------------------------
//get the time remaining in the countdown.
function getCountdown(){

	//Get the amount of time elapsed
	var today=new Date();
	var lapsHour=today.getHours() - hour;
	var lapsMin=today.getMinutes() - minute;
	var lapsSec=today.getSeconds() - second;

	var remaining = countdown - lapsSec - lapsMin*60 - lapsHour*3600;
	//Prevent negative time remaining
	if(remaining<0){ remaining=0; }
	var hourLeft = parseInt(remaining/3600);
	remaining = mod(remaining, 3600);
	var minLeft = parseInt(remaining/60);
	remaining = mod(remaining, 60);
	var secLeft = remaining;

	return formatTime(secLeft,minLeft,hourLeft);
}
//-------------------------------------------------
function mod(divisee,base) {
	// Created 1997 by Brian Risk.  http://members.aol.com/brianrisk
	return Math.round(divisee - (Math.floor(divisee/base)*base));
}
//-------------------------------------------------
//The following eats cpu cycles, but unlike setTimeout it is a synchronous call.
//http://www.sean.co.uk/a/webdesign/javascriptdelay.shtm
function pausecomp(ms){
	ms += new Date().getTime();
	while (new Date() < ms){}
}
