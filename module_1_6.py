my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict:', my_dict)
print('Existing value:', my_dict['Vasya'])
print('Not existing value:', my_dict.get('Denis'))
my_dict.update({'Sahsa': 1982,'Nata': 1987})
a = my_dict.pop ('Egor')
print('Deleted value:', a)
print('Modified dictonary:', my_dict)


my_set = {1, 3, 5, 1, 3, 5, 'String', (1, 3, 5)}
print('Set:', my_set)
my_set.add('Sun')
my_set.add(7)
my_set.discard((1, 3, 5))
print('Modified Set:', my_set)


