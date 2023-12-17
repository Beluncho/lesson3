# enter numbers
numbers_list = input('enter numbers, using following punctuation marks: ' '"," ; ' '"/" ; ' '";". ')

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
        
# conversion for required print
new_numbers_str = str(new_numbers_list)

# answer on homework
print('unicum elements from entering numbers: ', new_numbers_str[1:-1])
