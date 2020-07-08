import turtle, random

'''
TODO:
DONE 1. Make a little tree as a step toward genetic algorithm.
DONE 2. Add a seed
DONE 3A. Put all the parameters in a list.
DONE 3B. Pass a new random list to each makeTree function.
DONE 3C. Use values in the list, (but converted from 0 to 1 to an appropriate range.
DONE 4. produce a couple rows of trees with random parameters
DONE 5. Normalize all parameters in range 0 to 1
DONE 6. Create randomized lists for diverse trees.
DONE 7. Incorporate a random seed so these are replicable.
DONE 8. Adjust the mins and maxes so the trees look more reasonable
9. make it so you can click to further evolve a particular tree.

How much can you simplify this? Make a recursive version?
'''

#Don't update the screen until the very end. This will greatly speed things up.
#https://stackoverflow.com/questions/16119991/how-to-speed-up-pythons-turtle-function-and-stop-it-freezing-at-the-end
turtle.tracer(0, 0)

screen = turtle.getscreen()
screen.colormode(255)

#Change screen dimensions
screen.setup (width=1100, height=650, startx=0, starty=0)

#Min values for each gene
gene_mins = [0,#seed
             5,#min_angle_range
             5,#angle_range
             0.5,#angle_range_increase
             6,#depth
             10,#branch_length
             1,#length_decrease
             8,#pensize
             0.2,#thinning
             0.5,#thinning_random
             0,#red
             0,#green
             0,#blue
             0,#d_red1
             0,#d_green1
             0,#d_blue1
             0,#color_change_threshold
             0,#d_red2
             0,#d_green2
             0,#d_blue2
             0,#single_branch
             0,#layering_factor
             0#rand_color_adjust
             ]
#Max values for each gene
gene_maxes = [1,#seed
             30,#min_angle_range
             90,#angle_range
             25,#angle_range_increase
             12,#depth
             80,#branch_length
             10,#length_decrease
             30,#pensize
             2,#thinning
             1.5,#thinning_random
             255,#red
             255,#green
             255,#blue
             100,#d_red1
             100,#d_green1
             100,#d_blue1
             255,#color_change_threshold
             100,#d_red2
             100,#d_green2
             100,#d_blue2
             0.15,#single_branch
             1,#layering_factor
             10#rand_color_adjust
             ]

#This function takes DNA and index and returns appropriate value back
#by using the min and max arrays
def expressGene(dna, gene):
    return gene_mins[gene]+dna[gene]*(gene_maxes[gene]-gene_mins[gene])

#Indicies in into the dna
i_seed = 0
i_min_angle_range = 1
i_angle_range = 2
i_angle_range_increase = 3
i_depth = 4
i_branch_length = 5
i_length_decrease = 6
i_pensize = 7
i_thinning = 8
i_thinning_random = 9
i_red = 10
i_green = 11
i_blue = 12
i_d_red1 = 13
i_d_green1 = 14
i_d_blue1 = 15
i_color_change_threshold = 16
i_d_red2 = 17
i_d_green2 = 18
i_d_blue2 = 19
i_single_branch = 20
i_layering_factor = 21
i_rand_color_adjust = 22

turtle.hideturtle()

def getChildColor(parent, depth, dna):
    i = depth
    parent_red, parent_green, parent_blue = parent.color()[0]
    rand_color_adjust = int(expressGene(dna,i_rand_color_adjust))
    if parent_red + parent_green + parent_blue > expressGene(dna,i_color_change_threshold):
        new_red = int(max(min(parent_red+i*expressGene(dna,i_d_red2)+random.randint(-rand_color_adjust,rand_color_adjust), 255), 0))
        new_green = int(max(min(parent_green+i*expressGene(dna,i_d_green2)+random.randint(-rand_color_adjust,rand_color_adjust), 255), 0))
        new_blue = int(max(min(parent_blue+i*expressGene(dna,i_d_blue2)+random.randint(-rand_color_adjust,rand_color_adjust), 255), 0))
    else:
        new_red = int(max(min(parent_red+i*expressGene(dna,i_d_red1)+random.randint(-rand_color_adjust,rand_color_adjust), 255), 0))
        new_green = int(max(min(parent_green+i*expressGene(dna,i_d_green1)+random.randint(-rand_color_adjust,rand_color_adjust), 255), 0))
        new_blue = int(max(min(parent_blue+i*expressGene(dna,i_d_blue1)+random.randint(-rand_color_adjust,rand_color_adjust), 255), 0))
    return (new_red, new_green, new_blue)

def getLayeringColor(turt, dna):
    c = turt.color()[0]
    layering_factor = expressGene(dna,i_layering_factor)
    return (int(max(0,min(255,c[0]*layering_factor))), int(max(0,min(255,c[1]*layering_factor))), int(max(0,min(255,c[2]*layering_factor))))

def getChild(parent, depth, left, dna):
    heading = parent.heading()
    child = turtle.Turtle()
    child.hideturtle()
    child.penup()
    child.clear()
    #child.shape("turtle")
    #Increase the angle range as depth increases
    range_val_min = int(expressGene(dna,i_min_angle_range))
    range_val_max = int(expressGene(dna,i_angle_range)+expressGene(dna,i_angle_range_increase)*depth)
    if(range_val_min > range_val_max):
        temp = range_val_min
        range_val_min = range_val_max
        range_val_max = temp
    rand_int = range_val_min
    if range_val_min!=range_val_max:
        rand_int = random.randint(range_val_min, range_val_max)
    if left:
        child.setheading(heading-rand_int)
    else:
        child.setheading(heading+rand_int)
    child.setx(parent.xcor())
    child.sety(parent.ycor())
    child.color(getChildColor(parent, depth, dna))
    temp = int(expressGene(dna,i_thinning_random))
    rand_temp = 0
    if temp>0:
        rand_temp = random.randint(0,temp)
    new_pensize = int(parent.pensize()-expressGene(dna,i_thinning)-rand_temp)
    if new_pensize <= 0:
        new_pensize = 1
    child.pensize(new_pensize)
    child.pendown()
    return child

def makeTree(startx, starty, dna):
    random.seed(expressGene(dna,i_seed))
    new_turtle1 = turtle.Turtle()
    new_turtle1.penup()
    new_turtle1.clear()
    new_turtle1.setheading(90)
    new_turtle1.color(int(expressGene(dna,i_red)),int(expressGene(dna,i_green)),int(expressGene(dna,i_blue)))
    new_turtle1.pensize(int(expressGene(dna,i_pensize)))
    new_turtle1.goto(startx, starty)
    #new_turtle1.shape("turtle")
    new_turtle1.hideturtle()
    new_turtle1.pendown()
    turtles = []
    turtles.append(new_turtle1)
    depth = int(expressGene(dna,i_depth))
    branch_length = expressGene(dna,i_branch_length)
    length_decrease = expressGene(dna,i_length_decrease)
    for i in range(depth):
        new_turtles = []
        for t in turtles:
            #Only grow the branch if the branch thickness supports it
            if t.pensize() > 1 and branch_length-length_decrease*i > 0:
                #Draw the branch
                t.forward(int(branch_length-length_decrease*i))
                #Create first child to continue the branch
                direction = random.random()>0.5
                new_turtle1 = getChild(t, i, direction, dna)
                new_turtles.append(new_turtle1)
                #Chance to have single branch instead of two forking branches
                if random.random()>expressGene(dna,i_single_branch):
                    new_turtle2 = getChild(t, i, not direction, dna)
                    new_turtles.append(new_turtle2)
                #Create layered effect by changing color and walking back over
                #same branch twice more
                t.pensize(int(max(1,t.pensize()*3/4)))
                t.color(getLayeringColor(t, dna))
                t.backward(branch_length-length_decrease*i)
                t.pensize(int(max(1,t.pensize()*3/4)))
                t.color(getLayeringColor(t, dna))
                t.forward(branch_length-length_decrease*i)
        turtles = new_turtles


#Draw the forest
start_row = 20
start_col = -400
rows = 2
cols = 3
col_gap = 350
row_gap = 300
for row in range(rows):
    for col in range(cols):
        #A random tree's dna
        dna = []
        for i in range(23):
            dna.append(random.random())
        x = start_col+col*col_gap
        y = start_row-row*row_gap
        makeTree(x,y,dna)
#Refresh the screen
turtle.update()
turtle.done()