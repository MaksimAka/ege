from turtle import *

m = 10
lt(90)
tracer(0)

for i in range(10):
    fd(22*m)
    rt(90)
    fd(16*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(m)
lt(90)
down()
for i in range(10):
    fd(72*m)
    rt(90)
    fd(79*m)
    rt(90)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*m, y*m)
        dot(5, 'white')

update()
done()











