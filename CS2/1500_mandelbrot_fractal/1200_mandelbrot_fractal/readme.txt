
For 300 points, write a program that draws the Mandelbrot fractal
which can be seen in the image in this folder, and is also hanging
on the wall next to the door.

You should be comfortable with (or eager to learn more about) 
imaginary and complex numbers if you are considering this project.

You may work in groups of no more than 2. Both students are
eligible for 300 points each.

Before starting, create a Program Plan.
You must write down the pieces of the program that are 
needed, in what order you will write them, and who will 
work on what task.

You will turn in your Program Plan and code.


How to write a program to draw a fractal:

The Mandelbrot fractal (as shown on the wall) is a visual 
representation of the question: If I square a complex number 
and add that number to itself repeatedly, how many times do I 
have to repeat the process before the result "escapes" the 
radius 2 circle centered at the origin of the complex plane (the
x axis is real and the y axis is imaginary).

Example in the real numbers:
If I square a number, does it get bigger or smaller?
Answer: it depends on if the number is greater than or less than one.

But complex numbers are more complex.

What happens when I square 1+0.5i?

(1+0.5i)^2
I get the following after I FOIL is
1 + 0.5i + 0.5i - 0.25
= 0.75 + i

Which number is closer to the origin?

We find out by first looking at the complex plane. Our "x" axis will 
be our real component. Our "y" axis will be our imaginary component.

If we plot these two points, we can see which is closer to the origin, but let's remind ourselves how to calculate the distance.

If you remember the distance formula, great, use it. If you don't,
then draw a right triangle to the point and calculate the length of
the hypotenuse using the pythagorean theorem.
Then realize that the length of the hypotenuse formula IS the distance
formula.

Let's go through our algorithm a few more times and see where we end 
up. We started with
1+0.5i
We squared it and added in the original to get
0.75 + i + 1+0.5i
=1.75 + 1.5i
The distance of this point from the origin is
square root of (1.75^2 + 1.5^2)

... Repeat process until we are more than 2 from the origin.
How many repetitions did that take?

However many it is, we use that number to color a point at the
coordinate 1,0.5. For example, we could pair up every number with
a color or color the point lighter the higher the number and darker
the lower the number.


Small changes in our coordinates can produce vastly different results.
In other words, there is a sensitive dependence on initial conditions.
In other words, chaos theory!
Small changes in initial conditions greatly affect whether the 
calculation increases enormously, collapses to zero, or does something 
intermediate.


Ok, so what is our algorithm from start to finish:
We are going to iterate over every pixel on the screen
	We will map the x,y values of the pixel into the range from -2 to 2
		Then we will pass those values to the mandelbrot function.
		The value returned by the function (a whole number) should 
		be used to color the pixel at x,y

The mandelbrot function must treat the x and y values as the real 
and imaginary parts of a complex number. The function must repeatedly 
square the complex number and add the original number to the result,
incrementing a counter each time it does so.

As soon as the maximum number of iterations is reached or the complex 
number leaves the radius 2 circle centered at the origin, the function 
should return the number of iteration.

An easy way to color the pixel is to have a list of colors. The maximum 
number of iterations is then the length of the color list. The number of
iterations tells us what index to use in the color list.


If you're wondering how to color the pixel at x,y in pygame, it 
looks like this:
    screen = pygame.display.set_mode((width,height))
    screen.set_at((x,y), color)


Write this code one step at a time.
Start by squaring a general complex number on paper. What is a+bi squared?
Then write code that will square a complex number and test your code by 
comparing it to your paper calculations. Remember we are simply 
representing a complex number by two variables.

Then measure the distance of a complex number from the origin. You may 
want to write a distance function to do this.

Finally start putting pieces together to measure how many iterations it 
takes to leave the radius 2 circle.


For more help, check out:
http://stackoverflow.com/questions/425953/how-to-program-a-fractal
And scroll down to "Programming the Mandelbrot is easy"


If you are interested in extending this project for more points, we 
can talk about your options. The following two websites would be good 
places to start:

http://www.fractal.org/Bewustzijns-Besturings-Model/Fractals-Useful-Beauty.htm

https://www.intmath.com/complex-numbers/fractals.php
