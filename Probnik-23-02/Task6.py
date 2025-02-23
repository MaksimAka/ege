from turtle import *
m = 30
tracer(0)
screensize(3000, 3000)
left(90)

for i in range(10):
    rt(120)
    fd(10*m)
down()
for i in range(7):
    fd(15*m)
    rt(90)
for i in range(5):
    rt(60)
    fd(20*m)
    rt(30)
up()
for x in range(-20, 20):
    for y in range(-50, 20):
        goto(x*m, y*m)
        dot(5, 'red')

update()
done()