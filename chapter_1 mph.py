"""If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What
is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).
"""
km=float(input("Enter the kilometer: "))
time=float(input("enter the time in decimal: "))
op=((km/1.61)/(time/60))
print("the average speed in mph is: ",op)
