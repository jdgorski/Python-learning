#collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana","coconut" ]
# # print(dir(fruits))#gives options on what you can do with the list
# # print(help(fruits))#helpful information about the function
# # print(len(fruits)) #length of the list


# # print(fruits[::2])  #every second fruit
# print(fruits[::-1]) #makes the list reversed


# for fruit in fruits:
#     print(fruit) 

# print("apple" in fruits) 

# # fruits[0] = "pineapple" #Changes the value in () to the word in the ""
# fruits.append("pineapple") # Appends/Adds the word to the end of the list
# fruits.remove("apple")#Removes said word from the list
# fruits.insert(0,"pineapple") #Inserts it into that position, moving everything over by one
# fruits.sort#Puts everything in alphabetical order
# fruits.reverse() #reverses list

# for fruit in fruits:
#     print(fruit)    #prints the entire list one over the other
# cars = ["Ford", "Volvo", "BMW"]
# #add 4 new cars in the list
# cars.append("Porsche")
# cars.append("Subaru")
# cars.append("Toyota")
# cars.append("Honda")
# print(f'The cars in the list are: {cars}')
# cars[2] = "Aston Martin"
# print(f'The cars in the list are: {cars}')
# cars.insert(2, "Lamborghini")
# print(f'The cars in the list are: {cars}')
# cars.remove("Lamborghini")
# print("Ford" in cars)

# for car in cars:
#     requestCar = input("Enter a car: ")
#     cars.append(requestCar)
#     print(f'The cars in the list are: {cars}')
#     if len(cars) > 10:
#         print("You have reached the maximum number of cars")
#         break

# friends = ["Marvin"]

# for friend in friends:
#     requestfriends = input("Enter a friend: ")
#     friends.append(requestfriends)
#     print(f'The friends in the list are: {friends}')
#     if len(friends) > 4:
#          print("You have reached the maximum number of friends")
#          break
# friends[-1] = "Sitkoski"
# print(f'The friends in the list are: {friends}')
# friends[2] = "Chapman"
# print(f'The friends in the list are: {friends}')
# friends.insert(0, "Catomer")
# # print(f'The friends in the list are: {friends}')

# ##########sets#########
# #sets are unordered and unindexed
# # #they are defined using curly brackets
# # #they do not allow duplicates
# fruits = {"apple", "banana", "mango", "cherry", "watermelon"}
# # print(fruits)
# # # print(dir(fruits))#attributes can be used with sets
# # # print(help(fruits))#documentation/methods that can be used with sets
# # print(len(fruits))
# # print("volvo" in fruits)




# # print(fruits.add("orange"))
# # print(fruits)
# # print(fruits.add("kiwi"))

# # print(fruits.update(["orange", "kiwi", "pineapple"]))
# # print(fruits)


# print(fruits.remove("banana"))
# print(fruits)
# print(fruits.pop()) Last element in the set removed
# print(fruits)
# print(fruits.clear()) clears the set
# print(fruits)




# social_security_numbers = {123456789, 987654321, 123456689}

# # print(social_security_numbers.pop())
# # print(social_security_numbers)
# print(social_security_numbers.add(395628565))
# print(social_security_numbers)









#################tuples###############
#tuples are immutable and are defined using parenthesis
# #Create a tuple called my_tuple with the following values
example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# # print(example_tuple)
# # print(example_tuple.count(2)) #count the number of times the value 2 shows up

# # print(dir(example_tuple))#attributes that can be used with tuples
# # print(help(example_tuple))# methods that can be used

# # print(len(example_tuple))
# # print(2 in example_tuple)

# # #Tuples are useful when wanting to store a collection of items that should not be changed

print(example_tuple.index(2))
# lymeric = "peter pipe picked a peck of pickled peppers peppers" 



# # #convert the string to a tuple
# # #split it first
# # lymeric_tuple = tuple(lymeric.split())
# # print(lymeric_tuple)

# # print(lymeric_tuple.count("peppers"))

# #loops in tuples
# for item in example_tuple:
#     print(item)
capitals = { "Kenya":"Nairobi",
            "Uganda":"Kampala",
            "Tanzania":"Dodoma",
            "Rwanda":"Kigali",
            "China":"Beijing",
            "USA":"Washington DC"}
print(capitals)
# print(len(capitals))
# print(capitals["Kenya"])
# print(capitals.get("Kenya"))

# capitals.update({"Nigera":"Abuja"})
# capitals.update({"Poland":"Warsaw"})
# capitals.update({"Canada":"Ottawa"})
# capitals.pop("China")
# print(capitals)
# for key in capitals:
#     print(key)
for key in capitals:
    print(f'these are the {key}')


for value in capitals.values():
    print(value)

items_all = capitals.items() #key value pairs
for key, value in items_all:
    print(f'{key} is the capital of {value}')





