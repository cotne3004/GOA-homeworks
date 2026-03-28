from turtle import *
speed(15)

# we want to paint a house

#step 1 draw a square

width(7)
color("brown")
forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)
#we end drawing square here

#start drawing door
begin_fill()

forward(70)
left(90)

color("blue")
forward(120)      #height of the door
right(90)
forward(60)

right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

#we satart here drawing the roof
color("red")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()
#we end drawing door here

penup()
goto(200, 130)
pendown()

#here we start drawing windows
begin_fill()
color("black")

right(60)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

color("brown")

right(90)
forward(80)
right(90)
forward(200)
right(90)
forward(80)

begin_fill()
color("black")

right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

end_fill()

#we end herea drawing windows

exitonclick()
