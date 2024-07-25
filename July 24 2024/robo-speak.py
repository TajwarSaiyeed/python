import os

while True:
    text = input("Enter you text to speak : ")
    if text == 'q':
        break
    command = f"spd-say '{text}'"
    os.system(command)
