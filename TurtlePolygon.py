import turtle

drawing_board = turtle.Screen()

drawing_board.bgcolor("#7719aa")
drawing_board.title("Polygon")

turtle_instance = turtle.Turtle()
side_num = 6
angle = 360.0/side_num
length_side = 100

for i in range(side_num):
    turtle_instance.left(angle)
    turtle_instance.forward(length_side)

turtle.done()