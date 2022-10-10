from random import randint


i = 1
a = 8
while i < 10:
    a = a * 2
    value = 2**a
    hex_value = hex(randint(0,value))
    print("наразі маємо 2^" + str(a) + " вхідних данних та отримайний ключ: " + str(hex_value) + " " + str(i))
    i= i+1


# цей скрипт поєднує 1 та 2 таск завдання
# він спочатку показує скільки бітів ключ має, і потім рандомний ключ в цьому діапазоні
