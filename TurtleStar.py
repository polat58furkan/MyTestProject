import turtle

drawing_board = turtle.Screen()

drawing_board.bgcolor("DarkViolet")
drawing_board.title("Star")

turtle_instance = turtle.Turtle()

for i in range(5):
    turtle_instance.left(144)
    turtle_instance.forward(150)

turtle.done()
