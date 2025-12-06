import turtle,random

screen = turtle.Screen()
screen.bgcolor("DarkBlue")
screen.title("CatchTurtle")
Font=("Times New Roman",24,"normal")
score =0
game_over=False

#turtle list
turtle_list=[]

#Score turtle
score_turtle = turtle.Turtle()

#countdown turtle
countdown_turtle = turtle.Turtle()

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

    def handle_click(x,y):
        global score
        #print("click" + str(x)  +","+ str(y))
        score+=1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=Font)

    t.onclick(handle_click)
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
    if not game_over:
        hide_turtle()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("red")
    countdown_turtle.penup()

    top_height =screen.window_height()/2
    y=top_height*0.8
    countdown_turtle.setpos(0,y)
    countdown_turtle.clear()

    if time>0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time),move=False,align="center",font=Font)
        screen.ontimer(lambda: countdown(time-1), 1000)
    else:
        game_over =True
        countdown_turtle.clear()
        hide_turtle()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=Font)

def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtle()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)

start_game_up()
turtle.mainloop()
turtle.done()


# Makro mause ile tıklarsak fazladan skor alabiliyoruz :)