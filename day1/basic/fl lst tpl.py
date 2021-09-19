lst=[]
m=input(" enter first name\n")
n=input("enter second name\n")

m,n = n,m
lst.append(m)
lst.append(n)
print (lst)
print(tuple(lst))

# another way to implement this program

# list =[]
# x= input("enter a word\n")
# y = input("enter another word\n")
# temp =  x
# x=y
# y= temp
# list.append(x)
# list.append(y)
# print(list)
# print(tuple(list))

