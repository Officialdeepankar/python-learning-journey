# 📘 Python List Basics
# ✅ What is a List?
# A list is a collection of items in a single variable. 
# It's ordered, changeable (mutable), and allows duplicates.


fruits=["apple",2,"oranges"]



fruits[0]='grapes'



# Operation | Example | Result
# Access | fruits[0] | 'apple'
# Change | fruits[1] = "mango" | ["apple", "mango", "cherry"]
# Add (end) | fruits.append("kiwi") | Adds to end
# Insert | fruits.insert(1, "grape") | Inserts at index 1
# Remove (value) | fruits.remove("banana") | Removes by value
# Remove (index) | fruits.pop(0) | Removes by index
# Length | len(fruits) | Returns list size
# Slicing | fruits[1:3] | Slice elements
# Check in list | "apple" in fruits | True or False
# Clear list | fruits.clear() | Empties list


#functions
#fruits.pop()


# my_list = [3, 1, 4, 1, 5]
# my_list.sort()      # Sorts list
# my_list.reverse()   # Reverses list
# my_list.count(1)    # Counts occurrences of 1
# my_list.index(4)    # Finds index of 4

fruits.append("oranges")


fruits.remove("oranges")


#fruits.reverse()
fruits.index("oranges")
print(fruits)