# ✅ What is a Dictionary?
# A dictionary stores data in key-value pairs.

# It's unordered (before Python 3.7), mutable, and does not allow duplicate keys.


# Operation | Example | Result
# Access value | person["name"] | 'Alice'
# Change value | person["age"] = 30 | Changes age to 30
# Add new pair | person["job"] = "Engineer" | Adds new key-value
# Delete a key | del person["city"] | Removes "city"
# Get value safely | person.get("country", "N/A") | Returns "N/A" if not found
# Get all keys | person.keys() | Returns keys
# Get all values | person.values() | Returns values
# Get all items | person.items() | Returns key-value pairs
# Clear dictionary | person.clear() | Empties the dictionary



dict1={
    "name":"Deepankar Singh",
    "age":23,
    
}

print(dict1)


print(dict1["name"])#access




dict1["city"]="delhi" #add new element 

#del dict1["city"]-->Delete the key 


dict1["name"]="sanju"
#print(dict1)



#loop

for key,value in dict1.items():
  print(f"{key}:{value}")
