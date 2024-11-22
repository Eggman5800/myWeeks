#w2q3g
def even_elements(numbers):
    e = []
    for number in numbers:
        if number % 2 == 0:
            e.append(number)
    return e

# Example usage
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 85]
even_list = even_elements(a)
print("Even elements in the list are:", even_list)
