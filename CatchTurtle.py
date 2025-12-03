import turtle,random

screen = turtle.Screen()
screen.bgcolor("DarkBlue")
screen.title("CatchTurtle")
Font=("Times New Roman",24,"normal")

#turtle list
turtle_list=[]

#Score turtle
score_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("red")
    score_turtle.penup()

    top_height =screen.window_height()/2
    y=top_height*0.9
    score_turtle.setpos(0,y)
    score_turtle.write(arg="Score: 0",move=False,align="center",font=Font)

grid_size=10
def make_turtle(x,y):
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("yellow")
    t.goto(x * grid_size ,y * grid_size)
    turtle_list.append(t)

def setup_turtles():
    for i in range(5):
        for j in range(5):
            make_turtle(-20+(10*i), -20+(10*j))

def hide_turtle():
    for i in turtle_list:
        i.hideturtle()

def show_turtles_randomly():
    random.choice(turtle_list).showturtle()

turtle.tracer(0)
setup_score_turtle()
setup_turtles()
hide_turtle()
show_turtles_randomly()
turtle.tracer(1)

turtle.mainloop()
turtle.done()