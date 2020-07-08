hoc.nclab.com/karel/


I'm introducing this much later in the year. Students should have seen all these concepts. Students will still struggle with some of the levels, but this should be a good little review and consolidation of skills.

You can use this to burn a long period perhaps if you need a break.



Experiment with pair programming in CS for this and maze project.


Some students got very frustrated by this. Many could not finish in a long period even though it is all we did.
It is important to debrief this project and talk about repeat, while, if, and def. Generally you should discuss execution order. With these new tools, programs can no longer be read from top to bottom.


Karel passwords are reset after about a day so there is no sense even in saving them.



Introduce this exercise a little bit, but mainly the students will follow the assignment handout. The debrief is the important part.

Do the debrief with the students. You, the teacher, will guide them through it.

This project will introduce 3 new things: loops, conditions, and function definitions.


My Karel the Robot Notes. You do not need to review these. These have mostly been copied into the assignment document, but there are some answers to those questions here:
https://hoc.nclab.com/karel/
Pre: You need to show students the start of it, the instructions available, high score, short code (which can give you more points). Also make sure to clarify that indentation is used to specify blocks of code (tell them about upcoming repeat and if). Note that the indentation is 2 spaces.
03 - List the 5 basic commands: 
	go
	left
	right
	get
	put
06 - what does the repeat command let you do?
08 - what does the if command let you do
09 - There is a trick to getting the shortest code on this level. Think about putting a repeat command INSIDE another repeat command. Copy down your best solution to this map here.
10 - introduces not and while
What does the not command let you do? What does the while command let you do?
11 - fortress: copy down your best solution to this map here. Can you get the short program? Short code is valuable because it is usually easier to understand and easier to fix and often it runs faster on the computer.
12 - dungeon: copy down your best code. You might consider putting ifs inside of other ifs to get the points for the short code challenge.
12 - after 12: when is the while loop useful? Answer: when you don't know how many repetitions will be needed.
13 - introduces the def keyword. I think this is also the first time comments have been introduced.

13 In the Mountains
Karel is now in the mountains. To reach his home square, he needs to define and use a new command climb. This command helps Karel find the next step and climb on it. New commands are defined using the keyword def followed by the name of the new command, and a short program that we call the body of the command. The body ends with the optional command return. To begin with, step through the program below to see how it works!

# New command:
def climb
  while not wall
    go
  right
  go
  left
  go
  return

# Main program:
while not home
  climb

14 In the Factory
Complete a new command four for Karel to collect four barrels! 

Solution:
# New command:
def four
  repeat 4
    go
    get
  return

# Main program:
four
right
four
left
four
go

15 In the Bakery
Almost done! Your final task is to complete a new command pies for Karel to walk straight to the next wall, collecting all pies!

I feel like this one didn't tell the student anything about the possibility of the "or" keyword so you should introduce this. or anticipate the error and ask a question about it.

They give you everything but fill in the blank:
def pies
  while ...
    ...
    if ...
      ...
  return

Solution:
# Walk to the next wall
# and collect all pies:
def pies
  while not wall and not home
    go
    if pie
      get
  return

# Turn left. If there is 
# a wall, turn around:
def turn
  left
  if wall
    right
    right
  return

# Main program:
while not home
  pies
  turn

How many points did you get?

The end. Add guided debriefing notes on how repeat corresponds to for.
