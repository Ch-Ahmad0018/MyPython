import math
# print("Hello World")
# firstName="Tony"
# lastName="Shark"
# age=51
# isGenius=True
# print(isGenius)
# # for Input
# name=input("What is your name?")
# print("Hello "+name)
# SuperheroName=input("What is your superhero Name ? ")
# print(SuperheroName)
# Two number sum
# num1=int(input("Enter number 1 :"))
# num2=int(input("Enter number 2 :"))
# Total=num1+num2
# print("The sum of two numbers is "+str(Total))
# Strings
# name="Chaudhry"
# print(name.upper())
# print(name.lower())
# print(name.find('a'))
# print(name.replace('Chaudhry','Ahmad'))
# print('C' in name)
# print(name)
# Arithmetic operators
# print(5+7)
# print(5-3)
# print(5*3)
# print(5/2)
# print(5//2)
# print(5%2)
# print(5**2)
# Comparison operators
# print(2>3)
# print(2<3)
# print(2==3)
# print(2!=3)
# Logical operators
# print(2>3 or 2<3)
# print(2>3 and 2<3)
# print(not 2>3)
# if else statements
# age=11
# if (age>=18):
#     print("u r an adult")
#     print("u can vote")
# elif(age<18):
#     print("Thank u")
# else:
#     print("chaudhry")    

#Mini Project 
# first = int(input("Enter first number"))
# second = int(input("Enter second number"))
# operator=input("Enter the operation")
# sum=0
# if(operator=='+'):
#     sum=first+second
# elif(operator=='-'):
#     if(first>second):
#         sum=first-second
#     else:
#         sum=second-first
# elif(operator=='*'):
#     sum=first*second
# elif(operator=='/'):
#     sum=first/second

# print(sum)
# while loop
# i=1
# while(i<=5):
#     print(i*"*")
#     i+=1
# # For loops
# # for item in range(5):
# #     print(item)
# # List
# marks=[85,86,87]
# print(marks[-1])
# print(marks[0:2])
# # for score in marks:
# #     print(score)
# # Append function
# marks.append(88)
# print(marks)
# # Insert function
# # for index
# marks.insert(0,84)
# print(marks)
# print(88 in marks)
# print(len(marks))
# marks.clear()
# print(marks)
# Break and Continue Keywords
# Break Keyword
# students=["Ahmad","Chaudhry","Mubashir","Seemab","Mansoor"]
# for item in students:
#     if item =="Seemab":
#         break
#     print(item) 
# Continue Keyword
# students=["Ahmad","Chaudhry","Mubashir","Seemab","Mansoor"]
# for item in students:
#     if item =="Seemab":
#         continue
#     print(item)    
# Tuple Keyword
# marks=(95,96,97,97,97,97,97)
# # print(marks.count(97))
# # print(marks.index(95))
# marks=marks+(0,'ahmad','ch')
# for elements in marks:
#     print(elements)
# Set Keyword
# marks={95,96,97,97,97,97,97}
# # # [] list
# # # () tuple
# # # {} Set
# marks.add(98)
# for score in marks:
#     print(score)
# Dictionary Keyword
# marks={
#     "English":95,"Urdu":97,"Maths":98
# }
# print(marks["Maths"])
# marks["Physics"]=99
# marks["Physics"]=89
# for key,value in marks.items():
#     print(f"Key : {key}, Value : {value}")
# print(marks)
# User Defined Functions
# def print_sum(first,second=4):
#     print(first+second)
      
# print_sum(1)
# Round
# division_result = 17 / 3

# # Round the division_result to 2 decimal places
# rounded_result = round(division_result, 6)

# # Print the rounded result
# print("Rounded Result:", rounded_result)
# lcm 
# num1=10
# num2 =5
# num3=2
# lcm_result = math.lcm(num1, num2,num3)
# print("lcm Result:", lcm_result)
# -------------------------------------Concatenation string-------------------------------------------
# string="Hello Ch"
# string2="Ahmad Mubashir"
# result=string+"     "+string2
# print(result)

# my_tuple = (1, 2, 3, 4, 5)

# for element in my_tuple:
#     print(element)
# -----------------------------------How to add------------------------------------------------
my_list = [1,2,3,4, 'a', 'b', 'c', 'd']
#sets
my_set = {1,2,3, 'a', 'b', 'c'}
#tuples
my_tuples = (1,2,3)
#dictionary 
my_dictionary = {'name': 'Ali', 'Age' : 25, 'City' : 'Karachi'}
my_list.append('e')
my_set.add('d')
my_tuples += (4, 'd')  # Concatenate a tuple
print(my_tuples)
my_dictionary['Country']='Pakistan'
print(my_list)
print(my_set)
print(my_dictionary)
# print(my_tuples)