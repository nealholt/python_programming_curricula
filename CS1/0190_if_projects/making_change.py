
'''
Discuss structure:
	Getting input from user
	Formatting the input (multiply by 100 then convert to integer)
	Getting total amount of change (amount paid minus bill)
	Getting dollars of change (divide by 100 then convert to integer)
	Getting the amount of change leftover (either change minus dollars times 100 or change modulus 100)
	Getting quarters of change (divide by 25 then convert to integer)
	Getting the amount of change leftover (either change minus quarters times 25 or change modulus 25)
	and so on.

Stress the use of comments to at least segment the project.
Stress the use of print statements to test regularly.
Stress the use of working it out on paper in detail to see the calculations that need to be made.
'''

#EXAMPLE SOLUTION:
#The following is not perfect but would benefit from some rounding.
bill=input("How many dollars is the bill for? ")
pay=input("How many dollars will you give the cashier? ")
change=float(pay)-float(bill)
dollars=int(change/1)
left=(change%1)
quarters=int(left/.25)
left=(left%.25)
dimes=int(left/.1)
left=left%.1
nickles=int(left%.05)
pennies=int(100*(left%.05))
left=left%.01
print("If you don't turn things into ints, you are in danger of getting this: "+str(left)+", instead of zero")
print("The bill is for $" + bill + ".  You are giving the cashier $" + pay +".  You will recieve $"+str(change) + " in the form of " + str(dollars) +" dollars, "+str(quarters)+" quarters, "+str(dimes)+" dimes, "+str(nickles)+" nickles and "+str(left)+" pennies.  Thank you for your business")

