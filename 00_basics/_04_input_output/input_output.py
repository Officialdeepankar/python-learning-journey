# 🧠 Concept: Input and Output in Python
# 📥 input() – Taking Input from the User
# The input() function allows you to get user input as a string.

print("Enter num1:")
num1=input()
print("The type of num1 is" , type(num1))

num2=4

#Type conversion karna jarurui
print(int(num1)+num2)


name = "Alice"
score = 95
#print(name+"scored"+ score+"points")---->error    can only concatenate str (not "set") to str

#solution  f-string

print(f"{name} scored {score} points")  # f-string formatting

