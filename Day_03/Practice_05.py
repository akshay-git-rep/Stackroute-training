def func():
    num=int(input("enter a number:"))
    lower_value=1
    higher_value=num
   
    while lower_value<=num:
        while higher_value>=1:
           print(lower_value,end=" ")
           print(higher_value,end=" ")
           lower_value+=1
           higher_value-=1
 
func()
