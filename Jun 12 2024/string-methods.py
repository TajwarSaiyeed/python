name = 'tajwar'

# name[0] = 'ab' # TypeError: 'str' object does not support item assignment


# Upper
print("Upper :", name.upper())  # TAJWAR
print("Capitalize :", name.capitalize())  # Tajwar
print("Count :", name.count('a'))  # 2
print("Count :", name.count('S'))  # 0
print("isalnum :", name.isalnum())  # True
print("isnumeric :", name.isnumeric())  # False
print("removeprefix :", name.removeprefix("t"))  # ajwar

num = "7"
print(num.isnumeric())  # True
