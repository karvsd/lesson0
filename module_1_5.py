immutable_var = 1, 3, 5, 7, True,'Sorry'
print('Immutable tuple:', immutable_var)
#immutable_var [1] = 8

mutable_list = [1, 3, 5, 7, True, 'Sorry']
mutable_list[1] = 8
mutable_list.append('Thanks')
mutable_list.remove('Sorry')
print('Mutablr list:', mutable_list)