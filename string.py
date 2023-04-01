name = "Abid&"
number = "10"

print(name)

print(name[0:2])  # slice the string
# start from 0 and go all the way till 1 (2-1)

print(name[0:3])  # slice the string

print(name.upper())  # convert to upper case


print(name.count("d"))  # count the number of times d is present in the string
print(name.count("A"))  # count the number of times A is present in the string

print(name.isalnum())  # check if the string is alphanumeric

print(name.isalpha())  # check if the string is alphabetic

print(name.isdigit())  # check if the string is digit

print(number.isdigit())  # check if the string is digit

print(number.isnumeric()) # check if the string is numeric

print(name.removeprefix("A"))  # remove the prefix from the string bid&

print(name.replace("A", "B"))  # replace A with B in the string Abid& 