
src = input("enter strings\n")
src1 = src.split("-")
list=[]
for i in src1:
    i = str(i)
    list = list+[i]

print(list[0])
print(list[-1])
