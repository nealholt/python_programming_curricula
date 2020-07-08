
/* A bunch of functions to indicate goodness or badness of something using color. */

/* Based on the given value and the maximum possible value, return a color showing the strength of the number. Green is best. Pink is bad. */
function color_strength1($val, $max){
	var frac = Math.min(1,$val / $max);
	var red = Math.round(255 * (1-frac));
	var green = Math.round(255 * frac);
	var blue = Math.round(255 * (1-frac)/2); //muddy up the lower values because red could be interpreted as good.
	return 'rgb('+red+','+green+','+blue+')';
}

//Nice green=good progression.
function color_strength2($val, $max){
	var percent = Math.min(100,Math.round(100* $val / $max));
	var red = 200-percent*2;
	var green = 155+percent;
	var blue = Math.round(50 - (percent/2)); //muddy up the lower values because red could be interpreted as good.
	return 'rgb('+red+','+green+','+blue+')';
}

//Nice red=good progression.
function color_strength3($val, $max){
	var percent = Math.min(100,Math.round(100* $val / $max));
	var green = 200-percent*2;
	var red = 155+percent;
	var blue = Math.round(50 - (percent/2)); //muddy up the lower values because red could be interpreted as good.
	return 'rgb('+red+','+green+','+blue+')';
}

//Nice blue=good progression.
function color_strength4($val, $max){
	var percent = Math.min(100,Math.round(100* $val / $max));
	var red = Math.round(50 - (percent/2));
	var green = 200-percent*2; //muddy up the lower values
	var blue = 155+percent;
	return 'rgb('+red+','+green+','+blue+')';
}

//Nice blue=good progression.
function color_strength5($val, $max){
	var percent = Math.min(100,Math.round(100* $val / $max));
	var red = 200-percent*2
	var green = Math.round(50 - (percent/2));;
	var blue = 155+percent;
	return 'rgb('+red+','+green+','+blue+')';
}
