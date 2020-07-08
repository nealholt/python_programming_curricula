
#For 18 points, read this and answer the questions.

#Lists (also known as arrays) are for groups of related values.

#If you have ever been tempted to name your variables like the 
#following, what you really needed was a list:
var1 = 'sword'
var2 = 'shield'
var3 = 'armor'
var4 = 'boots'
var5 = 'helmet'

#Creating lists. You have two options:

#Option 1: Empty list:
activities_list = []
#Option 2: list with values already in it
activities_list = ['classes', 'hobbies', 'friends', 'sports']

#The len function can be used to determine how many
#values are in a list.


#1. What does this print?
print(len(activities_list))


#2. What does this print?
activities_list = []
print(len(activities_list))


#But if you create your list like this
activities_list = []
#how do you put things in it?
#The answer is append
activities_list.append('classes')
activities_list.append('hobbies')
activities_list.append('friends')
activities_list.append('sports')


#3. Write a line of code that appends another activity to the list.


#4. Compare what this code prints:
print(activities_list)
#versus what this code prints:
print(len(activities_list))


#The following three pieces of code print the same thing. 
#5. Which option is best in your opinion and why?

#Option A:
print(activities_list[0])
print(activities_list[1])
print(activities_list[2])
print(activities_list[3])

#Option B:
for item in activities_list:
    print(item)

#Option C:
for i in range(len(activities_list)):
    print(activities_list[i])


#Values in a list can be changed individually by accessing the value 
#with brackets [] and setting the list position equal to a new value.
#6. How is activities_list changed by    activities_list[2] = 'job'   ?
print(activities_list)
activities_list[2] = 'job'
print(activities_list)


#7. What will this print?
print(activities_list[1])


#8. What does this code print? Guess before running it.
drawers = ["socks", "underwear", "shirts", "pants"]
n = 2
print("Drawer "+str(n)+" contains "+drawers[n])
n = n+1
print("Drawer "+str(n)+" contains "+drawers[n])


#9. What does this code print? Guess before running it.
x=['python','list',1995,'age']
print(x[0])
print(x[1])
print(x[3])
print(x[2])
print(x[len(x)-1])
print(len(x))


#10. How is this list different after line two?
science_subjects=['chemistry','physics','biology','mathematics']
science_subjects[2]='english'
print(science_subjects)

