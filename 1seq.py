# enter elements
elements = int(input('enter the number of elements: '))

# variables
numbers_of_number = []
number = None

# cycle
while elements != len(numbers_of_number):
    for i in range(elements):
        print('Enter natural number №', i+1, 'element:')
        number = int(input())
        numbers_of_number.insert(i, number)
        numbers_of_number.sort()

# answer on homework
print('Numbers in ascending order: ', numbers_of_number)







