
import os
import turtle

wn = turtle.Screen()
call = turtle.Turtle()



def draw_square():

 call.forward(100)
 call.right(1)


def draw_Art():
 for i in range(1,37):
  draw_square()
  call.back(100)
draw_Art()


wn.exitonclick()
#turtle.penup()


#file = "C:\Requests\KC_375 Sales.xlsx"

#os.startfile(file)
#file.close()
