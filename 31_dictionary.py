# my_data = {"name":"skill shikshya","location":"kathmandu","district":"bagmati"}
# keys = my_data.keys() #this return all keys 
# values = my_data.values() #this return all  values

# second_data = my_data.copy()
# my_data.pop("district")

# print(second_data)



# user_data = {"name":"skill shikshya", "number":"98080"}
# for key in user_data:
#     if key =="number":
#         user_data[key] = "977" + str(user_data[key])
#         print(user_data)  



# my_list = [10, 20, 30, 40]
# yourList = ['apple','ball',4.1,1,2,3,4,]
# my_listLength = len(my_list)
# yourListLength = len(yourList)
# print(my_listLength)    
# print(yourListLength)
# i = 0
# while i < len(my_list):
#     print(my_list[i])  # Access elements using index
#     i =i + 1


# Write a program to remove duplicate items from the list data = [2, 5, 5, 6, 2]
# list_data= [2,5,5,6,2]
# list_data.remove(2)
# print(list_data)


# How would you find the maximum value in the dictionary {"a": 10, "b": 20, "c": 15}?

# Convert the list [1, 2, 3, 4, 5] into a dictionary where the keys are the numbers and the values are their cubes.


# Write a program to skip all numbers divisible by 3 while looping from 1 to 10.
# for num in range(1, 11):  # 1 देखि 10 सम्म लूप
#     if num % 3 == 0:  # यदि संख्या 3 ले विभाजित हुन्छ भने
#         continue  # यो संख्या छोडेर अगाडि बढ्ने
#     print(num)  # बाँकी संख्या प्रिन्ट गर्ने

# Write a program to find whether 29 is a prime number or not.

def is_prime(num):
    if num <= 1:
        return False  
    for i in range(2, num):  
        if num % i == 0:  
            return False
    return True  

number = 29
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# Write a program to find the sum of all even numbers between 1 and 50. What will the output be?
# Function to check if a number is prime