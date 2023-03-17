from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=600)
user_bet = screen.textinput(title='Make your bet!', prompt='Whose turtle gonna win? ')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

screen.exitonclick()
