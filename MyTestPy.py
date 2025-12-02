#First test
import turtle

drawing_board = turtle.Screen()

drawing_board.bgcolor("DarkMagenta")
drawing_board.title("My Py")
drawing_board.title("Hello World")
turtle_instance = turtle.Turtle()

for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)
turtle.done()

