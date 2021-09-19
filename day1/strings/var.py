w1=int(input("enter number:\n"))
w2=int(input("enter number:\n"))
w3= (abs(w1-w2)/w1)*100
print(w3)
w4=int(input("enter a number"))
if(w4<w3):
    print("given number is within the variance of range limits")
else:
     print("given number is not within the variance of range limits")