#w2q3f
def print_less_than_five(numbers):
    for number in numbers:
        if number < 5:
            print(number)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 85]
print("Elements less than 5 are:")
print_less_than_five(a)
