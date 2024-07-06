# operators in python

# Arithmetic operators
print(2 + 3)  # addition output: 5
print(2 - 3)  # subtraction output: -1
print(2 * 3)  # multiplication output: 6
print(2 / 3)  # division output: 0.6666666666666666
print(2 % 3)  # modulus output: 2
print(2 ** 3)  # exponent output: 8
print(2 // 3)  # floor division output: 0

# Assignment operators
a = 2  # a = 2
a += 3  # a = a + 3
print(a)  # 5
a -= 3  # a = a - 3
print(a)  # 2
a *= 3  # a = a * 3
print(a)  # 6
a /= 3  # a = a / 3
print(a)  # 2.0
a %= 3  # a = a % 3
print(a)  # 2.0
a **= 3  # a = a ** 3
print(a)  # 8.0
a //= 3  # a = a // 3
print(a)  # 2.0

# Comparison operators
print(2 == 3)  # equal to | output: False
print(2 != 3)  # not equal to | output: True
print(2 > 3)  # greater than | output: False
print(2 < 3)  # less than | output: True
print(2 >= 3)  # greater than or equal to | output: False
print(2 <= 3)  # less than or equal to | output: True

# Logical operators
print(2 == 3 and 2 < 3)  # and | output: False
print(2 == 3 or 2 < 3)  # or | output: True
print(not 2 == 3)  # not | output: True

# Bitwise operators
print(2 & 3)  # bitwise and | output: 2
print(2 | 3)  # bitwise or | output: 3
print(2 ^ 3)  # bitwise xor | output: 1
print(~2)  # bitwise not | output: -3
print(2 << 3)  # bitwise left shift | output: 16
print(2 >> 3)  # bitwise right shift | output: 0

# Membership operators
print(2 in [1, 2, 3])  # in | output: True
print(2 not in [1, 2, 3])  # not in | output: False

# Identity operators
print(2 == 3)  # is | output: False
print(2 != 3)  # is not | output: True

# Operator precedence
print(2 + 3 * 4)  # 14 (multiplication has higher precedence than addition)
print((2 + 3) * 4)  # 20 (parentheses have the highest precedence)
