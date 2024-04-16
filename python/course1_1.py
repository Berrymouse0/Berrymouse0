#python turtle : Ammonoidea

import turtle as t
#t.left(90)
i = 100
k = 2*i
t.bgcolor("black")
t.pencolor("white")
t.speed(1000)
t.penup()
t.setposition(-i,i)
t.pendown()
while i >=1 :    
    t.right(90)
    #t.begin_fill()
    t.circle(i,-160)   #t.circle(반지름, 각도)
    t.left(180)
    t.forward(k)
    t.right(90)
    t.forward(k)
    t.right(90)
    t.forward(k)
    #t.end_fill()
    i=i-2
    k=k-4
    t.right(90)
t.hideturtle()
t.done()