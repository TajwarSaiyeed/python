RANDOM_NUMBERS = [1, 50, 2, 49, 3, 48, 4, 47, 5, 46, 6, 45, 7, 44, 8, 43, 9, 42, 10, 41, 11, 40, 12, 39, 13, 38, 14, 37,
                  15, 36, 16, 35, 17, 34, 18, 33, 19, 32, 20, 31, 21, 30, 22, 29, 23, 28, 24, 27, 25, 26]

RANDOM_NUMBERS.sort()

target = int(input("Enter the number you want to search: "))
left, right, found = 0, len(RANDOM_NUMBERS), False

while left < right:
    mid = (left + right) / 2
    if RANDOM_NUMBERS[int(mid)] == target:
        found = True
        break
    elif RANDOM_NUMBERS[int(mid)] < target:
        left = mid + 1
    elif RANDOM_NUMBERS[int(mid)] > target:
        right = mid - 1

if found:
    print("Found the number")
else:
    print("Not found")
