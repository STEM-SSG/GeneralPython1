# Working with Lists – put data into a list, print, append​

# Populate a list with shopping items
shopping_list = ["Table", "Chair", "Cup", "Plate"]

# Show the whole shopping_list
print("Whole list = ")
print(shopping_list)

# Add a spoon to to the end of list​
shopping_list.append("Spoon")
print("Appended list = ")
print(shopping_list)

# Change an item in the list​
print("Item four was <" + shopping_list[3] + ">")
shopping_list[3] = "Bowl"
print("Item four now <" + shopping_list[3] + ">")
