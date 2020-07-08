'''You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
(Therefore 7 Jan 1900 was the first Sunday.)

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''


#Given a month and a year, return the number of days in the month
def daysInMonth(month, year):
	if month in [4,6,9,11]: #April, June, September, and November
		return 30
	elif month == 2: #February
		isLeap = False
		if year % 4 == 0:
			isLeap = True
		if year % 100 == 0 and year % 400 != 0:
			isLeap = False
		if isLeap:
			return 29
		else:
			return 28
	else:
		return 31

#The first sunday in january 1901 is the 6th, according to the internet.
day = 6
month = 1
year = 1901
firstSundayCount = 0
while year < 2001:
	day += 7
	days_in_month = daysInMonth(month, year)
	if days_in_month < day:
		day -= days_in_month
		month += 1
		if month > 12:
			month -= 12
			year += 1

	if day == 1:
		firstSundayCount += 1

print firstSundayCount #Answer 171. Correct!

