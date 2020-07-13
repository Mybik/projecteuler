'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''
def nod (a,b):
    while b > 0:
        a,b = b, a % b # Формула НОД
    return a

def nok (a,b):
    return a*b // nod(a,b) # Нок по формуле а*b // на нод a,b

d = 1 # В нем будет хранится значение предыдущего НОК
for i in range (2,21): #Перебераем делители
    d = nok(d,i) # Ищем их НОК
print (d)