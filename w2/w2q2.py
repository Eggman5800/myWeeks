#w2q2
def find_numbers():
    result = []
    for number in range(1500, 2701):
        if number % 7 == 0 and number % 5 == 0:
            result.append(number)
    return result

numbers = find_numbers()
print("Numbers divisible by 7 and multiple of 5 between 1500 and 2700:")
print(numbers)
print(type(numbers))