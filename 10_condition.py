# # 1)if
# # 2)if....elif
# # 3)if..else


# # age = input()
# # if age>50:
# #     print("You are old")
# # else:
# #     print("you are not old")


# #WAP which take input as age and print they are old or not
# # Taking age input
# age = int(input("Enter your age: "))

# # Checking the condition
# if age > 50:
#  print("You are old.")
# else:
#  print("You are not old.")
 
# # condition,loop,function,class :


# # if condition
# # if condition......elif condition
# # else 


# age = 40
# # if 40<5:
# #     print("you are a kid")
# # else:
# #     print("you are not a kid")

# age  = 13
# if age<5:
#     print("you are a kid")
# elif age>5 and age<=12:
#     print("you are monkey")
# elif age>12 and age<=19:
#     print("you are a teenager")
# elif age>19 and age<=49: 
#     print("you are a adult")
# else:
#     print("you are old")



# age = 30
# if age>18:
#     print("you can vote")
#     print("you can drink")
# else:
#     print("you can not vot")
  

# write program to output like {child,adult....old}

# age = 0
# if age>5:
#     print("you are child")
# if age<10:
#     print("you are teenger")
# if age<14:
#     print("you are adult")
# if age<50:
#         print("you are old")
    


# age = "A"
# print("invlade age")
# if age<5:
#     print("you are a child")
# elif age>12 and age<=19:
#     print("you are a teenager")
# elif age>19 and age<=49: 
#     print("you are a adult")
# else:
#     print("you are old")



age = input("enter your age?")
age= int (age)

if isinstance(age,str) and age.isdigit() == False:
    print("invalid age")
    
elif age>0 and age <18:
    print("you are child")
    
elif age>=13 and age<20:
    print("you are teenagers")
    
elif age<0 or age>200:
    print("wrong input")
else:
    print("either you are adult or old")
    
    