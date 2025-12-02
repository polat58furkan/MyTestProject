import turtle

drawing_board = turtle.Screen()

drawing_board.bgcolor("#7719aa")
drawing_board.title("Shrinking")

turtle_instance = turtle.Turtle()

turtle_instance.color("yellow")

def shrinking_square(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size -5

sides = 200
while sides > 0:
    shrinking_square(sides)
    sides  = sides - 20
turtle.done()