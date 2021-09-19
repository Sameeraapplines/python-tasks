num = input("enter num\n")
numlst  = num.split(",")
list =[]
for i in numlst:
    i = int(i)
    list = list+[i]
print(list)
print(tuple(list))
