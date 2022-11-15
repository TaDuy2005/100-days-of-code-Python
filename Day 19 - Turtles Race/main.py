from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
init_y_position = -75
all_turtle = []

for turtle_index in range (0,6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, init_y_position)
    init_y_position += 30
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            winner_turtle = turtle.pencolor()
            is_race_on = False

if winner_turtle == user_bet:
    print(f"You win. The {winner_turtle} is the winner.")
else:
    print(f"You lose. The {winner_turtle} is the winner.")

screen.exitonclick()
