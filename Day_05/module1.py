def welcome():
    print("Hi welcome to main module")

my_name = "Akshay"

print("Name :" ,my_name)

if  __name__  == "__main__":
   print("I am directly in module1") 
    
else:
    welcome()
    #print("Name :" ,my_name)
   # print("i am in another module")    