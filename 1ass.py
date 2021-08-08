# 5. Write a Python program to print alphabet pattern 'L'.
print("5 Sol:\n")
str="";    
for Row in range(0,7):    
    for Col in range(0,7):     
        if (Col == 1 or (Row == 6 and Col != 0 and Col < 7)):  
            str=str+"*"    
        else:      
            str=str+" "    
    str=str+"\n"    
print(str);  

# 7. Write a Python program to print the even numbers from a given list.
print("7 Sol:\n")
# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 66, 0, 2, 278]
# iterating each number in list
for num in list1:
    # checking condition
    if num % 2 == 0:
       print(num, end = " ")