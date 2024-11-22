#w2q1e
def daysMonth(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return "Invalid month"


m = int(input("Enter the month no.:"))
y = int(input("Enter the year:"))
d = daysMonth(m, y)
print("The number of days in",m,",",y," is: ",d)
