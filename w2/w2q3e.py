#w2q3e
def multiplyList(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

numbers = [1, 2, 3, 4, 5]
total_product = multiplyList(numbers)
print("The product of all numbers in the list is:", total_product)
