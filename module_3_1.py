calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return(len(string), string.upper(),string.lower())
def is_contains(string, list_to_search):
    count_calls()
    if string in list_to_search:
        return(True)
    else:
        return(False)
print(string_info('Capybara'))
print(string_info('Armagedon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)