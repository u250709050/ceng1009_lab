# def marker(data):
#     if data >= 90:
#         return "A"
#     elif data >= 80:
#         return "B"
#     elif data >= 70:
#         return "C"
#     elif data >= 60:
#         return "D"
#     else:
#         return "F"
# note=int(input("Enter your note"))
# print(marker(note))




# import turtle
# def drawBar(t,height,gap):
#     t.penup()
#     t.left(90)
#     t.forward(height+gap)
#     t.write("" + str(height))
#     t.backward(height+gap)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     maxheight=max(data)
#     num_bars=len(data)
#     border=10
#
#     gap=(maxheight)
#
#     wn = turtle.Screen()# def drawBar(t,height,gap):
#     t.penup()
#     t.left(90)
#     t.forward(height+gap)
#     t.write("" + str(height))
#     t.backward(height+gap)
#     t.right(90)
#     t.pendown()
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     maxheight=max(data)
#     num_bars=len(data)
#     border=10
#
#     gap=(maxheight)
#
#     wn = turtle.Screen()
#     wn.bgcolor("Lightgreen")
#     right=40*num_bars+border
#     wn.bgcolor("Lightgreen")
#     right=40*num_bars+border
#     top= maxheight+ 4* border
#     wn.setworldcoordinates(-border, -border, right,top)
#     t=turtle.Turtle()
#     t.color("blue")
#
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t,height,4)
#     wn.exitonclick()
#
# def chooseColor(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# data=[48,117,200,240,160,260,220]
# barChart(data)


# import turtle
#
# def drawBar(t,height,gap):
#
#     if (height >= 0):
#         labelY = (height + gap)
#     else:
#         labelY = (gap)
#     t.penup()
#     t.left(90)
#     t.forward(labelY+gap)
#     t.write(" "+str(height))
#     t.backward(labelY+gap)
#     t.rt(90)
#     t.pendown()
#
#     t.fillcolor(choose_color(height))
#     t.begin_fill()
#     t.left(90)
#     t.fd(height)
#     t.rt(90)
#     t.fd(40)
#     t.rt(90)
#     t.fd(height)
#     t.lt(90)
#     t.end_fill()
#
# def bar(data):
#     maxheight = max(data)
#     minheight = min(data)
#     num_bars = len(data)
#     border = 10
#     gap = (maxheight-border)/25
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#
#     right = 40 * num_bars +border
#     top = maxheight +4 * border
#     bottom = min(minheight,0) - border
#
#
#     wn.setworldcoordinates(-border,bottom,right,top)
#     t = turtle.Turtle()
#     t.color("blue")
#
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#
#     wn.exitonclick()
#
# def choose_color(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
#
#
#
# data = [48,117,-200,240,160,260,220]
#
# bar(data)

# import math
# def findHypot(a,b):
#     hypot= (a**2 + b**2)**(1/2)
#     return hypot
# def calcWithMath(a,b):
#     hypot= math.sqrt(a**2 + b**2)
#     return hypot
# print (findHypot(3,4))
# print (calcWithMath(3,4))







