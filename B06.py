year = int(input())
s = "a leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "a normal year"
#閏年的條件要符合可以整除4且不會被100整除或可以被400整除，條件不符合時則進入else
print(s)
