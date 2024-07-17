# the abid.py file is created in the same directory as this file
print("Tajwar is a good boy")

s = '''# the abid.py file is created in the same directory as this file
print("Tajwar is a good boy")
'''

# context manager
# with open("abid.txt", "w") as f:
#     f.write(s)

# fp = open("abid.py", "w")
# fp.write(s)
# fp.close()

# with open("try_accept.py", "r") as f:
#     print(f.read())

fr = open("file io.py", "r")
# print(fr.read())
# fr.close()


fp = open("abid.py", "w")
fp.write(s)
# append to the file
fp = open("abid.py", "a")
fp.write('\n')
s = fr.read()
fp.write(s)
fp.close()
