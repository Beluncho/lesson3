# enter elements
elements = int(input('enter the number of list elements №1: '))

# variables
numbers_of_number = []
number = None

# cycle
while elements != len(numbers_of_number):
    for i in range(elements):
        print('Enter natural number №', i + 1, 'element:')
        number = int(input())
        numbers_of_number.insert(i, number)
        numbers_of_number.sort()

# ************* enter numbers second time**************
numbers_list = input('enter numbers of list elements №2, using following punctuation marks: ' '"," ; ' '"/" ; ' '";". ')

# unicum
numbers_set = set(numbers_list)

# del ';' '/' ','
numbers_set.discard(',')
numbers_set.discard('/')
numbers_set.discard(';')

# list for cycle
numbers_list = list(numbers_set)

# cycle
new_numbers_list = []
while len(new_numbers_list) != len(numbers_list):
    for i in range(len(numbers_list)):
        number = int(numbers_list[i])
        new_numbers_list.insert(i, number)

# for a list of unique elements of the entered list
answer_set = set(numbers_of_number)
answer_set_2 = set(new_numbers_list)
answer_set.symmetric_difference_update(answer_set_2)
answer_list = list(answer_set)

# cycle
finish_answer_list = []
while len(finish_answer_list) != len(answer_list):
    for i in range(len(answer_list)):
        finish_number = int(answer_list[i])
        finish_answer_list.insert(i, finish_number)

# conversion for required print
finish_answer_str = str(finish_answer_list)

# nice enter of the answer
print('*' * 150)
print(' ' * 150)

print('first list: ', numbers_of_number)
print('second list', new_numbers_list)

print('*' * 150)
print(' ' * 150)
# answer on homework
print('unicum elements from entering numbers: ', finish_answer_str[1:-1])
