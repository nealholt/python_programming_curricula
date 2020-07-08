/*
<!-- Version 1.0 If any changes are made to this file, change the version, because this file 
<!-- is copied in multiple locations including "functions objects and snippets", "website", and "smartamusement.com".

This document contains useful code for the following:
-Arrays, both one and two dimensional. Be very careful how you declare arrays. 
Refer to your own working examples of 2-d array use as this
(http://www.trans4mind.com/personal_development/JavaScript/Array2D.htm)
otherwise useful tutorial can be misleading.

-Variable scope is not an issue within this code, but was researched while troubleshooting.
http://www.mredkj.com/tutorials/reference_js_intro_ex.html

-Javascript HTML DOM: Table Cells
http://www.w3schools.com/htmldom/coll_table_cells.asp

-parseInt Function. Useful for chopping off decimal points.
http://www.w3schools.com/jsref/jsref_parseInt.asp

-Limiting / formatting / masking user input to a text field.
See the numbersonly(myfield, e, dec) function at the bottom of this document.

-Variable functions. Storing functions in, and calling them from, variables.
You can call functions via variable names in javascript.
This is fantastic. It means you can pass function names as variables.
http://www.webmasterworld.com/forum91/4113.htm

-Dynamically changing page elements with javascript (without a page reload).
See printTable function.

-Representing parallel, discrete heat flow in a grid and displaying it in an HTML table.
--------------------------------------------------- */

/* Time variable. 
http://www.w3schools.com/JS/js_timing.asp 
http://www.w3schools.com/JS/tryit.asp?filename=tryjs_timing_stop */
var timer; 

initialize = 0; //track whether or not the table has been initialized

row_max = 15;
col_max = 15;
nextVals=new Array(row_max);
currentVals=new Array(row_max);

//---------------------------------------------------
function randomStart(){
	for(var r=0;r<row_max;r++) {
		currentVals[r] = new Array(col_max);
		nextVals[r] = new Array(col_max);
		for (var c=0;c<col_max;c++) {
			currentVals[r][c] = parseInt(Math.random()*255*3);
		}
	}
	displayHeat();
	initialize=1;
}
//---------------------------------------------------
function initializeStart(){
	for(var r=0;r<row_max;r++) {
		currentVals[r] = new Array(col_max);
		nextVals[r] = new Array(col_max);
		for (var c=0;c<col_max;c++) {
			currentVals[r][c] = parseInt(document.getElementById(c+","+r).value);
		}
	}
	displayHeat();
	initialize=1;
}
//---------------------------------------------------
//Display the current heat in the HTML table.
function displayHeat(){
	for (var r=0;r<row_max;r++) {
		for (var c=0;c<col_max;c++) {
			hot_setXY(c, r, currentVals[r][c]);
		}
	}
}
//---------------------------------------------------
//Print a CSV representation of the heat in the text area "csvOutput".
function csvHeat(){
	$csv=""; //Create a variable to hold CSV representation of heat flow.
	for (var r=0;r<row_max;r++) {
		for (var c=0;c<col_max;c++) {
			$csv += currentVals[r][c]+",";
		}
		$csv += "\n";
	}
	//Write csv output to text area
	document.getElementById("csvOutput").innerHTML = $csv;
}
//---------------------------------------------------
function step(){

	//Stop here and alert if not initialized.
	if(!initialize){ alert("Not initialized. Please initialize before beginning."); return 0; }

	//Load all the cell next values into a 2d array nextVals
	for (var r=0;r<row_max;r++) {
		for ( var c=0;c<col_max;c++) {
			nextVals[r][c] = next_value(c,r);
		}
	}

	//update the table
	for (var r=0;r<row_max;r++) {
		for (var c=0;c<col_max;c++) {
			currentVals[r][c] = nextVals[r][c];
			hot_setXY(c, r, nextVals[r][c]);
		}
	}
	return 1;
}
//<!-- ----------------------------------------------------------------------------------------- -->
//<!-- Set the contents of cell x,y in hot table to be content -->
function hot_setXY(x,y,content){

	if(content > 255*3){ content=255*3; }

	var red=0;
	var green=0;
	var blue=0;
	if(content > 510){
		blue = content - 510;
		green = 255;
		red = 255;
	}else if(content > 255){
		green = content - 255;
		red = 255;
	}else{
		red = content;
	}

	var cell=document.getElementById("hot").rows[y].cells;
	cell[x].style.background = "rgb("+red+","+green+","+blue+")";

/*	//Do not delete this code, though it is no longer being used.
	var cell=document.getElementById("test").rows[y].cells;
	cell[x].innerHTML=content; 
*/
/* //PREVIOUS CODE
	var cell=document.getElementById("hot").rows[y].cells;
	cell[x].style.background = "rgb("+content+",0,0)";

	var cell=document.getElementById("test").rows[y].cells;
	cell[x].innerHTML=content;
*/
}
//<!-- ----------------------------------------------------------------------------------------- -->
//<!-- Get all the next values loaded into a 2-d array with out changing the old values.
//<!-- Then when the new values are all acquired change all the old values to new values -->
//<!-- Make change with every push of a button so it can be iterative. -->
//<!--Get the next value in a cell. -->
function next_value(x,y){
	var thiscell=currentVals[y][x];

	//<!--Get temperature of the above cell if it is on the grid -->
	var above = thiscell; //<!--Initialize boundary to this cell's temperature -->
	if(y>0){ above=currentVals[(y-1)][x]; }

	//<!--Get temperature of the below cell if it is on the grid -->
	var below = thiscell; //<!--Initialize boundary to this cell's temperature -->
	if(y<(row_max-1)){ below=currentVals[(y+1)][x]; }

	//<!--Get temperature of the left cell if it is on the grid -->
	var left = thiscell; //<!--Initialize boundary to this cell's temperature -->
	if(x>0){ left=currentVals[y][(x-1)]; }

	//<!--Get temperature of the right cell if it is on the grid -->
	var right = thiscell; //<!--Initialize boundary to this cell's temperature -->
	if(x<(col_max-1)){ right=currentVals[y][(x+1)]; }

	return parseInt((thiscell+above+below+left+right)/5);
}
//---------------------------------------------------
function printTable(){

	//Set rows and columns to specified values.
	if(document.getElementById("rows").value<=0){
		alert('ERROR: Must input a positive number of rows. Rows reset to 3.'); 
		document.getElementById("rows").value=3;
	}
	if(document.getElementById("cols").value<=0){
		alert('ERROR: Must input a positive number of columns. Columns reset to 3.');
		document.getElementById("cols").value=3;
	}
	row_max = document.getElementById("rows").value;
	col_max = document.getElementById("cols").value;

	//Make three tables (only two tables now).
	var str = makeTable(row_max,col_max,'id="hot" border=1','height=10 width=10','')+

	//This test table is nolonger needed, but keep the code. Don't delete this.
	//makeTable(row_max,col_max,'id="test" border=1','height=10 width=10','')

	makeTable(row_max,col_max,'id="input" border=1 bgcolor="#CCFF99"','','makeInputCell')+
	"<textarea rows='"+(row_max-1)+"' cols='"+(col_max*4)+"' id='csvOutput' readonly=1></textarea>"+
	"<form><input type='button' value='Print CSV of heat' onClick='csvHeat(); return true'>"+
	"</form>";

	//Write the two tables and text area to the main div.
	document.getElementById("main").innerHTML=str;
}
/* -------------------------------------------------
Variable Functions
You can call functions via variable names in javascript.
This is fantastic. It means you can pass function names as variables.
This needs to be stored in snippets separately from this script.
http://www.webmasterworld.com/forum91/4113.htm
*/
/* Pre: cellInnerHTML is either blank or the name of a function taking
the rows and columns of a matrix as arguments. */
function makeTable(rows, cols, tableAtts, cellAtts, cellInnerHTML){
	var str='<table '+tableAtts+'>';
	for (var r=0;r<rows;r++){
		str+='<tr>';
		for (var c=0;c<cols;c++){
			str+='<td '+cellAtts+'>';
			if(cellInnerHTML){ str+= eval(cellInnerHTML + '('+c+','+r+')'); }
			str+='</td>';
		}
		str+='</tr>';
	}
	return str + '</table>';
}
//-------------------------------------------------
/* Returns the html for an "input table" cell, given 
the x, y coordinates of the cell. */
function makeInputCell(x,y){
	return '<input type="text" size=4 id="'+x+','+y+'" value="0"/>';
}
//-------------------------------------------------
/* 
<!-- Here is javascript code for restricting an input field to nondecimal numbers.
<!-- By adding "maxlength=3" in the input tag below, you can limit the input further.
<!-- http://www.htmlcodetutorial.com/forms/index_famsupp_158.html 
<!-- Here is another resource for "masking" user input. This is perfect for formatting
<!-- times and dates. http://www.xaprb.com/html-input-mask/html-form-input-mask.html -->
 Only non-decimal numbers will appear in the text box.
 copyright 1999 Idocs, Inc. http://www.idocs.com
 Distribute this script freely but keep this notice in place
*/
function numbersonly(myfield, e, dec)
{
var key;
var keychar;

if (window.event)
   key = window.event.keyCode;
else if (e)
   key = e.which;
else
   return true;
keychar = String.fromCharCode(key);

// control keys
if ((key==null) || (key==0) || (key==8) || 
    (key==9) || (key==13) || (key==27) )
   return true;

// numbers
else if ((("0123456789").indexOf(keychar) > -1))
   return true;

// decimal point jump
else if (dec && (keychar == "."))
   {
   myfield.form.elements[dec].focus();
   return false;
   }
else
   return false;
}
//-------------------------------------------------