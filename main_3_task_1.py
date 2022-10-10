from random import randint
import time
hex_value = hex(randint(2**20,2**25))
start_time = time.time() * 1000
def main():
    array = []
    f = open("keys.txt")
    array = f.readlines()
    for keys in array: 
        keys = keys.strip()
        if(hex_value != keys):
            print('Не знайдено закономірності')
        else:
            break

main()    

print("Цей ключ " + hex_value + " було знайдено за --- %s miliseconds ---" % (time.time()*1000 - start_time))

# цей скрипт генерує рандомний ключ з діапазону 2^20-2^25 
# потім, він перевіряє наявність такого ключа методом перебору
# допоки скрипт не знайде такий самий ключ, программа буде працювати
# в кінці, программа видасть який ключ та за який час було знайдено
#
#
#
#
#
