#Importing Turtle
import turtle as t
import random
t.width(4)
t.speed(0)

#Defining functions
def triangle (l,c,d):
    t.color(c,d)
    t.begin_fill()
    for x in range (3):
        t.forward(l)
        t.left(120)
    t.end_fill()

def rect (l,h,c,d):
    t.color(c,d)
    t.begin_fill()
    for x in range (2):
        t.forward(l)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def circle (r,c,d):
    t.color(c,d)
    t.begin_fill()
    for x in range(1):
        t.circle(r)
    t.end_fill()
        
def go (x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def window(c, d):
    t.color(c, d)
    t.pendown()
    for x in range (3):
        t.begin_fill()
        t.pendown()
        for x in range(4):
            t.forward(10)
            t.left(90)
        t.end_fill()
        t.penup()
        t.forward (25)
    


#Setting the scene
t.bgcolor("#00008B")
for x in range (50):
    t.penup()
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    t.goto (x,y)
    t.pendown()
    t.color("white")
    t.dot()

for x in range (50):
    t.penup()
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    t.goto (x,y)
    t.pendown()
    t.color("yellow")
    t.dot()

for x in range (50):
    t.penup()
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    t.goto (x,y)
    t.pendown()
    t.color("red")
    t.dot()


#Faded buildings

t.penup()
t.goto(-380, -315)  


t.pendown()
rect(90, 400, "#191970", "#191970")  
t.penup()
t.forward(170)  


t.pendown()
rect(90, 450, "#191970", "#191970")  
t.penup()
t.forward(170)

t.pendown()
rect(90, 500, "#191970", "#191970")  
t.penup()
t.forward(170)

t.pendown()
rect(90, 300, "#191970", "#191970")  
t.penup()
t.forward(170)

t.pendown()
rect(90, 350, "#191970", "#191970")  
t.penup()
t.forward(170)

t.goto(-365, -305)
for x in range (11):
    window("yellow","yellow")
    t.back(75)
    t.seth(90)
    t.penup()
    t.forward(35)
    t.seth(0)

t.goto(-195, -305)
for x in range (13):
    window("yellow","yellow")
    t.back(75)
    t.seth(90)
    t.penup()
    t.forward(35)
    t.seth(0)

t.goto(-25,-305)
for x in range (14):
    window("yellow","yellow")
    t.back(75)
    t.seth(90)
    t.penup()
    t.forward(35)
    t.seth(0)

t.goto(145,-305)
for x in range (8):
    window("yellow","yellow")
    t.back(75)
    t.seth(90)
    t.penup()
    t.forward(35)
    t.seth(0)

t.goto(315,-305)
for x in range (10):
    window("yellow","yellow")
    t.back(75)
    t.seth(90)
    t.penup()
    t.forward(35)
    t.seth(0)

#Dark Buildings
t.penup()
t.goto(-310, -315)


t.pendown()
rect(120, 300, "#222222","#222222")
t.penup()
t.forward(170)  

t.pendown()
rect(120, 350, "#222222","#222222")
t.penup()
t.forward(170)  

t.pendown()
rect(120, 250, "#222222","#222222")
t.penup()
t.forward(170)  

t.pendown()
rect(120, 480, "#222222","#222222")
t.penup()
t.forward(170) 

t.goto(-280, -305)
for x in range (8):
    window("white","white")
    t.back(75)
    t.seth(90)
    t.penup()
    t.forward(35)
    t.seth(0)

t.goto(-110, -305)
for x in range (10):
    window("white","white")
    t.back(75)
    t.seth(90)
    t.penup()
    t.forward(35)
    t.seth(0)

t.goto(60,-305)
for x in range (7):
    window("white","white")
    t.back(75)
    t.seth(90)
    t.penup()
    t.forward(35)
    t.seth(0)

t.goto(230,-305)
for x in range (13):
    window("white","white")
    t.back(75)
    t.seth(90)
    t.penup()
    t.forward(35)
    t.seth(0)


#Final Buildings
go(-330,-315)
rect(400,60,"#000000","#000000")

go(170,-315)
rect(400,60,"#000000","#000000")

go(-285,-290)
window("red","red")

t.forward(5)
window("red","red")

t.forward(5)
window("red","red")

t.forward(5)
window("red","red")

go(200,-290)
window("red","red")
t.forward(5)
window("red","red")

t.mainloop()
