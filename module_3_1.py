calls = 0
def count_calls(): # Функция счётчик вызова функций
    global calls
    calls = calls + 1
    return calls

def string_info(string):# Функция считающая длину строки и изменения регистра строки
    global calls
    set_ = len(string)
    nr = string.upper()
    VR = string.lower()
    count_calls()
    return set_, nr, VR

def is_contains(string,list_to_search):# Функция поиска строки в списке
    global calls
    count_calls()
    string = string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string in list_to_search:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)