def dell(num):                                    #Количество делителей числа
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1
    return cnt

with open('17_4329.txt') as file:
    data = [int(i) for i in file]

