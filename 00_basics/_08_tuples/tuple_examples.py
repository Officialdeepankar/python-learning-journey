# ✅ What is a Tuple?
# A tuple is like a list, but immutable (you can’t change it after creation).

# It's ordered and allows duplicates


fruits = ("apple", "banana", "cherry")


print(fruits[0]) # it is ordered 

#fruits[0]="Guava" # tuple object does not support item assignment


# Operation | Example | Output
# Access item | fruits[1] | 'banana'
# Slicing | fruits[0:2] | ('apple', 'banana')
# Length | len(fruits) | 3
# Check existence | 'apple' in fruits | True
# Count | fruits.count('apple') | How many times 'apple' appears
# Index | fruits.index('cherry') | Returns index of 'cherry'
# Convert to list | list(fruits) | Makes it editable


print('apple' in fruits)
