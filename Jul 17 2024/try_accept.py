try:
    a = int(input("Enter you number : "))
    print(a + 5)
except Exception as e:
    print("Please enter a valid number", e)
