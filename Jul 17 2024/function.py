def greet_hello(name, end):
    print("Hello", name)
    print(end)


# print("Before function")
# greet_hello("Abid", "Thank You")
# print("Done")
# greet_hello("Rahim", "Thanks!")
# print("Done")

def letter_generator(name, date):
    st = f"Hi sir, \n\tThis is {name}\n\tI'll not come to school on {date}"
    print(st)


# letter_generator("Tajwar Saiyeed", "21st July 2024")

'''
Hi sir, 
	This is Tajwar Saiyeed
	I'll not come to school on 21st July 2024
'''


def avg_int(x, y) -> int:
    return (x + y) // 2


def avg_float(x, y) -> float:
    return (x + y) / 2

# print(avg_int(5, 6))
# print(avg_float(5, 6))
