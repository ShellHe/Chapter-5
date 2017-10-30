import turtle
wn= turtle.Turtle()
ali= turtle.Turtle()
ali.color("blue", "red")
ali.pensize(3)
def draw(ali,height,width):
    ali.begin_fill()
    ali.pendown()
    ali.lt(90)
    ali.forward(height)
    ali.right(90)
    ali.forward(width)
    ali.right(90)
    ali.fd(height)
    ali.left(90)
    ali.penup()
    ali.end_fill()
    ali.fd(width)
    
for i in [27, 42,-15,31,-40,2]:
    draw(ali,i,30)
