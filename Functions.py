import turtle as t
t.width(4)

def triangle (l,c):
    t.color(c)
    t.begin_fill()
    for x in range (3):
        t.forward(l)
        t.left(120)
    t.end_fill()

triangle (100,"red")

t.penup()
t.goto (-150,-100)
t.pendown()
triangle (250,"blue")

t.penup()
t.goto (-150,100)
t.pendown()
triangle (25,"green")

t.penup()
t.goto (150,-100)
t.pendown()
triangle (50,"yellow")

t.penup()
t.goto (100,50)
t.pendown()
triangle (500,"black")

t.penup()
t.goto (-50,150)
t.pendown()
triangle (100,"orange")

t.mainloop()

