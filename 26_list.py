# name_list = ["ram","hari",1,5,9]

# print(name_list[0])

# print(name_list[-2])

# print(name_list[start:end:step])

# print(name_list[5::-2])

#add element in list
# name_list.append("kathmandu")
# name_list.append("biratnagar")


# #insert item in list
# name_list.insert(2,"bhaktapur")


# #pop item from list by positioin
# name_list.pop(0)


# #remove item from list
# name_list.remove("hari")


# #find length of list
# print(len(name_list))

# #replace item from element
# name_list[0] = "india"
# print(name_list)


#Accessing item using loop




# #class work find highes digit from list [1,5,9,6,89,1203,4,23]
# list_number = [1,5,9,6,89,1203,4,23]
# # print(max(list_number))

# #class work to short given list [1,5,9,6,89,1203,4,23]
# list_number.sort()
# print(list_number)



# first_list=["apple","ball","shyam",99,"9.0",4.3]
# #print(first_list[-2])
# print(first_list[1:4] )#start stop step)
# print(first_list[::-1])#reverse

# #add item to list(append)
# first_list.append("cat")
# print(first_list)

# second_list=list((5,9,"cat","dog"))
# print(second_list)



# name_list =["apple", "ball", "cat", "ball","5","7","5"]
# second_list= []
# for item in name_list:
#     if item in second_list:
#         pass
#     else:
#         second_list.append(item)
# print(second_list)


# wap  to take user input "first name", "mobile number", "address" and add it to list



# # WAP to take user input 5 friends data and store it in total_list
# total_data = [['ram', '9808', 'ktm'],
#               ['shyam', '987', 'pokhara'],
#               ['hari', '987', 'pokhara']]

# for i in range(5):
#     print(f"deatils your  friend {i+1}:")
#     name = input("Name: ")
#     phone = input("Phone Number: ")
#     address = input("Address: ")
    
#     friend_data = [name, phone, address]
    
#     total_data.append(friend_data)
# print(total_data)


 
# total_data = [['ram', '9808', 'ktm'],
#                ['shyam', '987', 'pokhara'],
#                ['hari', '987', 'dhangdi'],
#                ['sita', '98764', 'chitwan'],
#                ['sangita', '97653', 'jhapa']]

# for i in range(5):
#     print(f"details your friend {i+1}: ")
#     name = input("enter your friend  name: ")
#     mobile_number = input("enter mobile number: ")
#     Address= input("your friend address: ")
    
#     list_data= []
#     list_data.append(name)
#     list_data.append(mobile_number)
#     list_data.append(Address)
# print(total_data)


total_list = []
print(total_list)
for i in range(1,6):
    name=input("enter user name:")
    mobile_number=  input("enter mobile number:")
    location = input("enter location: ")

    user_data=[]
    user_data.append(name)
    user_data.append(mobile_number)
    user_data.append(location)

    total_list.append(user_data)
    
print(total_list)