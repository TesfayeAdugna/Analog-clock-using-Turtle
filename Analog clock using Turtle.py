import turtle
import time

print("hint:- you should write a number from 1 to 12")
a = int(input("enter the hour:  "))

print("hint:- you should write a number from 1 to 60")
b = int(input("enter the minute: "))

if a == 1 :
    x = a*60 - 0.5*b
elif a == 2:
    x = a*15 - 0.5*b
elif a == 3:
    x = a*0 - 0.5*b
elif a == 4:
    x = a*82.5 - 0.5*b
elif a == 5:
    x = a*60 - 0.5*b
elif a == 6:
    x = a*45 - 0.5*b
elif a == 7:
    x = a*34.3 - 0.5*b
elif a == 8:
    x = a*26.25 - 0.5*b
elif a == 9:
    x = a*20 - 0.5*b
elif a == 10:
    x = a*15 - 0.5*b
elif a == 11:
    x = a*10.9 - 0.5*b
elif a == 12:
    x = a*7.5 - 0.5*b
else:
    print("sorry! you entered a wrong number! the clock is not going to work! you should run the program again and enter a correct number")


if b>=0 and b<=15:
    y = 90 - b*6
elif b>=16 and b<=60:
    y = 360 - (b-15)*6
else:
    print("sorry! you entered a wrong number! the clock is not going to work! you should run the program again and enter a correct number")

faf = turtle.Screen()
mini = turtle.Turtle()
mini_min = turtle.Turtle()
mini_hr = turtle.Turtle()
mini_sec = turtle.Turtle()

faf.bgcolor("#84516B")
mini.speed(0)

def The_circle(mini):
    
    mini.hideturtle()
    mini.pensize(3)
    mini.begin_fill()
    mini.circle(100)
    mini.hideturtle()
    mini.write(6)
    mini.penup()
    mini.left(90)
    mini.forward(100)
    mini.right(180)
    mini.pendown()

    mini.dot(90, "red")
    mini.dot(60, "yellow")
    mini.dot(30, "#01FF34")
    mini.dot()

    for i in range(11):
        mini.penup()
        mini.pensize(3)
        mini.left(30)
        mini.forward(87)
        mini.pendown()
        if i<=4:
            mini.write(5-i)
        elif i>=5:
            mini.write(17-i)    
        mini.penup()
        mini.backward(87)
        mini.pendown()

    mini.right(150)
    mini.color("#CBE1CF")
    mini.end_fill()


The_circle(mini)

mini_hr.setheading(x)

def for_hour(mini_hr):
    mini_hr.hideturtle()
    mini_hr.pensize(5)
    mini_hr.goto(0,100)
    mini_hr.color("black")
    mini_hr.right(0.5)
    mini_hr.clear()
    mini_hr.forward(50)

mini_min.setheading(y+6)

def for_minute(mini_min):
    mini_min.hideturtle()
    mini_min.pensize(3)
    mini_min.goto(0,100)
    mini_min.color("#0D14E6")
    mini_min.right(6)
    mini_min.clear()
    mini_min.forward(65)

mini_sec.setheading(90)

while(1):
    for_hour(mini_hr)
    for_minute(mini_min)
    
    for i in range(60):
        mini_sec.hideturtle()
        mini_sec.penup()
        mini_sec.pensize(2)
        mini_sec.color("#6E0D25")
        mini_sec.goto(0,100)
        time.sleep(1)
        mini_sec.right(6)
        mini_sec.pendown()
        mini_sec.forward(85)
        mini_sec.undo()

turtle.done()
