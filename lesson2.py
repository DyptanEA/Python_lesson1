'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
for i in range(1,6):
    print(i,'.','0 '*10,end='\n')
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
s=0
for i in range(10):
   if int(input('введите цифру '))==5:
       s+=1
print('количество пятерок ',s)
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
s=0
for i in range(1,101):
    s+=i
print('сумма чисел ',s)
'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
p=1
for i in range(1,11):
    p*=i
print('произведение равно ',p)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
n=int(input('введите целое число '))
while n>0:
    print(n%10,end='\n')
    n=n//10
'''
Задача 6
Найти сумму цифр числа.
'''
s=0
n=int(input('введите целое число '))
while n>0:
   s+=n%10
   n=n//10
print('сумма цифр числа=',s)
'''
Задача 7
Найти произведение цифр числа.
'''
p=1
n=int(input('введите целое число '))
while n>0:
   p*=n%10
   n=n//10
print('произведение цифр числа=',p)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
p=0
n=int(input('введите целое число '))
while n>0 and p==0:
   if n%10==5:
       p+=1
   n=n//10
if p==1:
    print('в числе есть цифра 5')
else:print('в числе нет цифры 5')
'''
Задача 9
Найти максимальную цифру в числе
'''
max=0
n=int(input('введите целое число '))
while n>0 :
   if n%10>max:
       max=n%10
   n=n//10
print('максимальная цифра числа ',max)
'''
Задача 10
Найти количество цифр 5 в числе
'''
p=0
n=int(input('введите целое число '))
while n>0 :
   if n%10==5:
       p+=1
   n=n//10
if p==0:
    print('в числе нет цифры 5')
else:print('в числе',p,'пятерок')
