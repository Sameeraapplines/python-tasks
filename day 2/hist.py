# list = [3,5,7,9]
# for i in list:
#     print('#'*i)
    
import matplotlib.pyplot as plt

x = [4,5,1,2,7,3,5,7,6,2,3,4,8,8,3,6,5]
plt.hist(x, bins =5)
plt.show()