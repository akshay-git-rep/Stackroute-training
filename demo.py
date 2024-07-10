# # dict1 = { "apple" : 10.00,
# #           "banana" : 8.00,
# #           "coconut" : {"big_coco" : 10.00,
# #                        "med_coco" : 08.00,
# #                        "small_coco" : [1, 3, 5, 7, 9]
# #                        }
# # }

# # print(len(dict1))

# # dict1 = {"key1" : ["a", "b", "c", "d"]}
# # dict1["key2"] = "akshay"
# # dict1["key1"] = "pawar"
# # print(dict1)
# # print(dict1.items())
# # #print(dict1["key1"][3].upper())

# # tup1 = ("a", "a", "b")
# # print(tup1.index("b"))

# # myset = set("Mississippi")
# # print(myset)
# # myset.add("akshay")
# # print(myset)

# # mylist = "Mississippi"
# # print(set(mylist))

# # a = True
# # b = False
# # print(type(b))

# # myfile = open('myfile.txt')

# # s = "hello"
# # print(s[-1])

# # list = [0]
# # print(list*3)

# # list3 = [1,2,[3,4,'hello']]
# # print(list3[2][2])
# # list3[2][2] = "good bye"
# # print(list3)

# # list4 = [5,3,4,6,1]
# # print(list4)
# # list4.sort()
# # print(list4)

# # d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# # print(d["k1"][2]["k2"][1]["tough"][2][0])

# # list5 = [1,2,2,33,4,4,11,22,3,3,2]
# # print(list5)
# # list5.reverse()
# # print(list5)

# # list = [1,2,3,4,5,6,7,8,9,10]

# # for num in list:
# #     if num == 5:
# #         break
# #     print(num)
# # print("done")

# # list = [(1,2,3),(4,5,6),(7,8,9)]

# # dict1 = {"k1" : "value1", "k2" : "value2"}
# # for i in dict1.items():
# #     print(i)

# x = 0

# # while x < 5:
# #     if x == 2:
# #         continue
# #     print(x)
# #     x += 1

# # list = list(range(1,11,1))

# # print(list)

# # list1 = ["a","b","c"]
# # list2 = [1,2,3]

# # print("a" in list1 )
# # item = (zip(list1,list2))
# # print(item)
# # for item in zip(list1,list2):
# #     print(item)

# # for i in enumerate(word):
# #     print(i)

# # x = "abcde"

# # if "z" in x:
# #     print("present")
# # else:
# #     print("not present")

# # result = input("enter value")

# # int1 = int(result)
# # print(type(result))
# # print(type(int1))

# # # mystr = "abcde"
# # mylist = [i for i in range(11) if i%2==1]

# # print(mylist)
# # # for i in mystr:
# # #     mylist.append(i)

# # # print(mylist)

# # mystr = 'Print only the words that start with s in this sentence'
# # mysplit = mystr.split()

# # for word in mystr.split(): 
# #     if word[0] == 's':
# #         print(word)

# # list = [x for x in range(51) if x%3==0]
# # print(list)

# # st = 'Print every word in this sentence that has an even number of letters'


# # for i in st.split(): 
# #     if len(i) % 2 == 0:
# #         print(f"even {i}")
# #     else:
# #         print(f"odd {i}")
# # st = []

# # for i in range(1,16):
# #     if i % 3 == 0 and i % 5 == 0:
# #         print("akshay")
# #     elif i % 3 == 0:
# #         print("fizz")
# #     elif i % 5 == 0:
# #         print("buzz")
# #     else:
# #         print(i)

# # st = 'Create a list of the first letters of every word in this string'
# # mylist = [x[0] for x in st.split()]
# # # for i in st.split():
# # #     mylist.append(i[0])

# # print(mylist)

# # import random

# # num = random.randint(1, 20)

# # guesses = 0

# # while True:

# #     guess = int(input("enter your guessing number: "))

# #     if guess > 100 or guess < 1:
# #         print("out of bound")
# #         continue


#     # if guess == num :
#     #     print("you selected correct number ")


#     # if guess > num :
#     #     print("please select lesser number")
#     # elif guess < num :
#     #     print("please select greater number")

# # def fun1(a, b):
# #     return (a + b)

# # result = fun1(3, 6)
# # print(result)

# # def even_check(num):
# #     return num % 2 == 0
# #     # if num % 2 == 0:
# #     #     print(True)
# #     # else:
# #     #     print(False)

# # result = even_check(2)
# # print(result)

# # def even_check_list(num_list):

# #     even_number = []

# #     for num in num_list:
# #         if num % 2 == 0:
# #             even_number.append(num)
            
# #         else:
# #             pass
# #     return even_number

# # print(even_check_list([2,2,5]))


# #from random import shuffle

# # def shuffle_list(mylist):
# #     shuffle(mylist)
# #     return mylist

# # def player_guess():
# #     guess = ""
# #     while guess not in ["0", "1", "2"]:
# #         guess = input("select your guess number from 0 1 2 ::")

# #     return int(guess)

# # def check_guess(mylist, guess):

# #     if mylist[guess] =="0":
# #         print("correct")
# #     else:
# #         print("wrong guess")
# #         print(mylist)


# # mylist = [" ", "0", " "]
# # mix_list = shuffle_list(mylist)
# # guess = player_guess()
# # check_guess(mix_list, guess)



# # from random import shuffle

# # def shuffle_list(mylist):
# #     shuffle(mylist)
# #     return mylist

# # def player_guess():
     
# #      guess = " "

# #      while guess not in ["0", "1", "2"]:
# #         guess = input("Please enter your Guessing number from 0, 1, 2")

# #      return int(guess)

# # def guess_choice(mylist, guess):
    
# #     if mylist[guess] == "0":
# #         print("you answer is correct")
# #     else:
# #         print("wrong guess")
# #         print(mylist)

# # mylist = [" ", "0", " "]

# # mix_shuffle = shuffle_list(mylist)

# # player_guess = player_guess()

# # guess_choice(mix_shuffle, player_guess)

# # def myfunc(a):
# #     print("my name is {name}".format(name = "akshay"))

# # myfunc()

# def myfunc(**kwargs):
#     print(kwargs)

# myfunc(fruit = "apple", Veggies = "banana")
    
# def myfunc(s):
#     new_str = ""
#     for i, char in enumerate(s):
#         if i % 2 == 0:
#             new_str += char.lower()
#         else:
#             new_str += char.upper()
#     return new_str

# print(myfunc("abcdef"))

# def lesser_of_two_evens(a,b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a, b)
        
# print(lesser_of_two_evens(4, 7))

# def animal_crackers(text):
#     result = text.split()
#     return result[0][0] == result[1][0]
        

# print(animal_crackers("lovely lion"))

# def makes_twenty(a,b):
#     return (a + b == 20) or (a == 20 or b == 20)

# print(makes_twenty(2, 10))

# def old_macdonald(name):
#     return name[:3].capitalize() + name[3:].capitalize()

# print(old_macdonald("macdonalds"))

# def master_yoda(text):
#     result = text.split()
#     result1 = (result)[::-1]
#     return " ".join(result1)

# print(master_yoda("akshay is back"))

# def has_33(nums):
#     for i in range(0, len(nums)-1):
#         if nums[i:i+2] == [3,3]:
#             return True  
     
#     return False

# print(has_33([1, 3, 1, 3]))

# def square(num):
#     return num**2
# my_num = [1, 2, 3, 4, 5]
# for num in my_num:
#     print(square(num),end=" ")
# print("===========")
# for i in map(square,my_num):
#     print(i)
# new1 = list(map(square,my_num))
# print(new1)

# def splicer(mystring):
#     if len(mystring) % 2 == 0:
#         return "EVEN"
#     else:
#         return mystring[0]
# names = ["Akshay", "Any", "Anand"]
# for i in map(splicer,names):
#     print(i)
# new1 = list(map(splicer,names))
# print(new1)

# def chk_even(num1):
#     return num1 % 2 == 0
    
# num1 = [1,2,3,4,5,6]

# for i in filter(chk_even,num1):
#     print(i)

# new1=list(filter(chk_even,num1))
# print(new1)

# my_num = [1, 2, 3, 4, 5, 6]
# square =  list(filter(lambda num: num%2==0,my_num))
# print(square)

# def volume(list1):
#     return list1[0] > list1[1] 

# a = [1,5,10]

# print(volume(a))


# class dog():
#     def __init__(self,breed,name,spots):
#         self.breed = breed
#         self.name = name
#         self.spots = spots

#     def bark(self,number):
#         print(f"woof!, my name is {self.name} and my number is {number}")

# my_dog = dog(breed="Lab", name="James", spots="no spots")

# print(my_dog.breed)
# print(my_dog.name)
# print(my_dog.spots)
# print(my_dog.bark(10))


# class circle():

#     pi = 3.14

#     def __init__(self,radius=1):
#         self.radius = radius
    
#     def get_circumfrence(self):
#         return self.radius * self.pi * 2
    
# my_circle = circle(30)

# print(my_circle.pi)
# print(my_circle.radius)
# print(my_circle.get_circumfrence())


# class animal():
#     def __init__(self):
#         print("Animal created")
        
#     def who_am_i(self):
#         print("Im an animal")
#     def eat(self):
#         print("im eating something")

# class dog(animal):
#     # def __init__(self):
#     #     animal.__init__(self)

#     def bark(self):
#         print("Im from dog class")
# my_dog = dog()
# print(my_dog.bark())






# class dog():
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(self.name + " i say Woof!")

# class cat():
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(self.name + " i say meow!")

# james = dog(name = "james")
# joy = cat(name = "joy")

# # for pet in [james,joy]:
# #     print(pet.bark())

# def pet_speak(pet):
#     print(pet.bark())

# print(pet_speak(joy))



# class animal():
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         raise NotImplementedError("In animal class we cant impliment speak method")
    
# class dog(animal):

#     def speak(self):
#         print(f"{self.name} say i bark as Boww!")

# class cat(animal):
    
#     def speak(self):
#         print(f"{self.name} say i bark as Boww!")
    
# james = dog(name = "james")
# joy = dog(name = "joy")

# for pet in [james,joy]:
#     print(pet.speak())



# class book():

#     def __init__(self,name,author,page):
#         self.name = name
#         self.author = author
#         self.page = page

#     def __str__(self):
#         return f"{self.name} is written by {self.author}"
    
#     def __len__(self):
#         return self.page
    
#     # def __del__(self):
#     #      print("the variable has been deleted")

# my_book = book("Science","Akshya",200)

# len(my_book)




# class bank_account():

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, dept_amt):
#         self.balance += dept_amt
#         print("Deposit accepted") 

#     def withdrawal(self, withdraw_amt):
#         if self.balance >= withdraw_amt:
#             self.balance -= withdraw_amt
#             print("withdrawal done")
#         else:
#             print("insufficient fund")

#     def __str__(self):
#         return f"hello {self.owner} your remaining balance amount is {self.balance}"

# account = bank_account(owner="akshay", balance=20000)
# account.withdrawal(2000)

# print(account)


# my_dict = {
#     "name": "akshay",
#     "age": 25
# }
# my_dict.append()
# print(my_dict)


