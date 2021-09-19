# a=input("enter the name\n")
# count=0
# for i in a:
#     if i== 'm':
#         count=count+1
        
# print(count)


#other way of implementation


word = input("Enter string: ")
ltr = input("Enter the letter: ")

c = 0
for i in range(len(word)):
    if(word[i] == ltr):
        c = c + 1

print("the total count is", c)

