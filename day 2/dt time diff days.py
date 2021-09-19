from datetime import date
f_date = date(2000, 1 , 1)
l_date = date(2000,3,31)
delta = l_date - f_date
print(delta.days)