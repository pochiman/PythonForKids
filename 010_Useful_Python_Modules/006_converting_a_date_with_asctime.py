import time
print(time.asctime())

# The values in the sequence are year, month, day, hours, minutes, seconds, 
# day of the week (0 is Monday, 1 is Tuesday, and so on), day of the year 
# (we put 0 as a placeholder), and whether or not it is daylight saving time 
# (0 if it isn't; 1 if it is).
t = (2020, 2, 23, 10, 30, 48, 6, 0, 0)
print(time.asctime(t))

# Getting the Date and Time with localtime
import time
print(time.localtime())

t = time.localtime()
year = t[0]
month = t[1]
print(year)
print(month)