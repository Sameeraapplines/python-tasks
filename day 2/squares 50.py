
#possible ways
# s# input =[1,11,21,31,41,51,61]
# list =[i*i for i  in input  if i>10 and i<50]
# print(list)

# list=[]
# lst=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
# for i in lst:
#     ssq= i**2
#     app = list.append(ssq)
# print(list)


list=[]
l1 = [0,3,5,8,11,44,22,66,33,21,5]
for i in l1:
    if i>10 and i<50:
     res = pow(i,2)
     new=list.append(res)
print(list)


