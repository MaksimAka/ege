from turtle import *

m = 10
tracer(0)
left(90)

for i in range(4):
    fd(10*m)
    rt(90)
    fd(16*m)
    rt(90)
up()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
down()
for i in range(4):
    fd(73*m)
    rt(90)
    fd(67*m)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5, 'white')

update()
done()

#Ответ: 60