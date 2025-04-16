# 📘 Python Set Basics
# ✅ What is a Set?
# A set is an unordered collection of unique items.

# It's mutable, but the items inside must be immutable (like strings, numbers, tuples).

fruits = {"apple", "banana", "cherry"}


#print(fruits[0])# 'set' object is not subscriptable

print(fruits)

#if i will try to add duplicate elements

fruits = {"apple", "banana", "cherry","cherry"}


# this is the oupput {'banana', 'cherry', 'apple'}
print(fruits)



# Operation | Example | What it Does
# Add item | s.add("mango") | Adds "mango"
# Remove item | s.remove("apple") | Removes "apple" (error if not found)
# Discard item | s.discard("apple") | Removes "apple" (no error if not found)
# Clear set | s.clear() | Empties the set
# Union | s1.union(s2) | Combines both sets (no duplicates)
# Intersection | s1.intersection(s2) | Keeps only common elements
# Difference | s1.difference(s2) | Items only in s1 not in s2
# Check membership | "apple" in s | Returns True or False



s1={1,2,3,4,5}

s2={1,3,7,8}

#union

print(s1.union(s2))

#{1, 2, 3, 4, 7, 8} output( duplicate elements will be removed )

#intersection

print(s1.intersection(s2)) #{1, 3}


#difference 

print(s1.difference(s2))