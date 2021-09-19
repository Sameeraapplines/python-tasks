vwlcount = 0;  
concount = 0;  
str = input("enter a sentence\n")
   

str = str.lower();  
for i in range(0,len(str)):   
      
    if str[i] in ('a',"e","i","o","u"):  
        vwlcount = vwlcount + 1;  
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        concount = concount + 1;  
print("Total number of vowel and consonant are" );  
print(vwlcount);  
print(concount);  

# other way of implementation

# vwlcount = 0;  
# concount = 0;  
# str = input("enter a sentence\n")
   

# str = str.lower();  
# for i in range(0,len(str)):   
      
#     if str[i] in ('a',"e","i","o","u"):  
#         vwlcount = vwlcount + 1;  
#     elif (str[i] != 'a',"e","i","o","u"):  
#         concount = concount + 1;  
# print("Total number of vowel and consonant are" );  
# print(vwlcount);  
# print(concount);  