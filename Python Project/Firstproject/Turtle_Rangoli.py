# Python program to draw a Rangoli, erase and re-draw infinite times until canvas closed.
# using Turtle Programming
import turtle
rangoli = turtle.Turtle()
turtle.speed(0)
colors = ['yellow','gold','orange','red','maroon','violet','magenta','purple','navy','blue','skyblue','cyan','lightgreen','green','darkgreen','white']
turtle.bgcolor('black')

k=1
while k>0:
    rangoli.width(1)
    rangoli.pendown()
    for j in range(100):
        for i in range(4):
            rangoli.pencolor(colors[j%len(colors)])
            if i==0 or i==3:
                rangoli.penup()
            else:
                rangoli.pendown()
            rangoli.forward(150)
            rangoli.left(90)  
        rangoli.pendown()
        rangoli.circle(70)
        rangoli.right(3.6)
    
    rangoli.left(90)  
       
    for i in range(217,283,6):
        rangoli.width(2)
        rangoli.pencolor(colors[i%len(colors)])
        rangoli.penup()
        rangoli.setpos(i,0)
        rangoli.pendown()          
        rangoli.circle(i)
    
    rangoli.penup()
    rangoli.goto(0,0)
    rangoli.right(90)
    rangoli.clear()
   
