# list of numbers
list1 = [-12, 71, -4, 67, -63, 53]
num = 0

# using while loop
while (num < len(list1)):

    # checking condition
    if list1[num] >= 0:
        print(list1[num], end=" ")

    # increment num
    num += 1