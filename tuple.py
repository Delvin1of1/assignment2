# write a python program to remove duplicates from a list.
# given list of tuples,write a program to sort the list based on the second element in each tuple
# write a python function that takes a tuple as input and returns the sum of all its elements.
# create a list of numbers from 1 to 10 and generate a tuple with their squares
#     write a oython program to find the index of an element in a list and a tuple

# for duplicate in students:
#     if "Roland" in students:
#         students.remove("Roland")
# print(students)

# write a python program to remove duplicates from a list.
students = ["Roland", "John", "James", "Don", "Roland"]
new_list = list(set(students))
print(new_list)

#  given list of tuples,write a program to sort the list based on the second element in each tuple
countries = [("Country", "Ghana"), ("car", "GLE"), ("Phone", "Iphone")]
sorted_list = sorted(countries, key=lambda x: x[1])
# print("sorted list :", sorted_list)
print(f"sorted list: {sorted_list}")

#print the squares of the numbers in a list
new_numbers = [1, 2, 3, 4, 5]
squared =list(map(lambda x: x**2, new_numbers))
print(squared)

fruits = ["apple","mango", "orange","banan"]
fruits.sort()
print(fruits)

kitchen = ("pot", "bowl", "spoon")
new_kitchen = sorted(kitchen)
print(new_kitchen)


tuple_list = (1, 2, 3, 4, 5)
def sum_of_tuple_list(tuple_list):
    return sum(tuple_list)
result = sum_of_tuple_list(tuple_list)
print("sum of tuple list:", result)

# # create a list of numbers from 1 to 10 and generate a tuple with their squares
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# multiplying each value by itself for the square
squares = tuple(_**2 for _ in list_of_numbers)
print("square of tuple:", squares)


# # write a python program to find the index of an element in a list and a tuple
countries = [("Country", "Ghana"), ("car", "GLE"), ("Phone", "Iphone")]
print(countries[0][0])
print(countries[0][1])
print(countries[1][0])
print(countries[1][1])
print(countries[2][0])
print(countries[2][1])

