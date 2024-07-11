# dict1 = {}
# a = set()
# print(dict1, type(dict1)) # {} <class 'dict'>
# print(a, type(a) ) # set() <class 'set'>

dictionary = {
    "Good": "Having the right qualities",
    "Bad": "Having the wrong qualities",
    "Ugly": "Unpleasant to look at",
    "Beautiful": "Pleasing the senses or mind aesthetically",
}

marks = {
    "Tajwar": 100,
    "Saiyeed": 90,
    "Abid": 80,
}

# print(dictionary['Good'])
# print(dictionary.get('Good'))

# print(marks['Tajwar'])

marks["X"] = 70
# print(marks)

# print(marks.get("x"))  # None
# print(marks['x'])  # KeyError: 'x'

print(marks.keys())
print(marks.values())
print(marks.items())
marks.pop("X")
print(marks)
print(marks.items())
