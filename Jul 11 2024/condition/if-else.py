# @ref https://www.w3schools.com/python/python_conditions.asp
age = int(input("Enter your age: "))

if age >= 18:
    print("You can drive.")
elif age == 1:
    print("You are a baby.")
elif age == 10:
    print("You are a kid.")
else:
    print("You can't drive.")

print("End of program.")
