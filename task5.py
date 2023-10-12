#Task 5
"""
Iterate through the list of numbers.
If the number is positive, determine the square root of the number.
State the number and the square root value
"""
nums = (5,-2,12,-8,14,16)
for i in nums:
    i = str(i)
    if "-" in i:
        i = int(i)
        continue
    i = int(i)
    i2 = i ** 0.5
    i2 = round(i2, 3)
    print(i2)