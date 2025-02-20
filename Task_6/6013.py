from turtle import *
m = 30
tracer(0)

for i in range(2):
    rt(120)
    fd(7*m)
rt(300)
for i in range(2):
    rt(120)
    fd(7*m)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'red')

up()
done()

