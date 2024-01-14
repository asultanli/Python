from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.title("Turtle Race")
screen.setup(700, 600)
screen.bgcolor("black") 

choice = screen.textinput(title="Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'purple', 'white', 'green', 'blue', 'orange']
y_positions = [-70, -30, 10, 50, 90, 130]
all_turtles = []

# Draw finish line
finish_line = Turtle()
finish_line.penup()
finish_line.color('white')
finish_line.goto(320, -300)
finish_line.pendown()
finish_line.goto(320, 300)
finish_line.hideturtle()

for i in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])

    
    new_turtle.shapesize(stretch_wid=1.2, stretch_len=1)

    new_turtle.goto(-320, y_positions[i])
    all_turtles.append(new_turtle)

if choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 300:
            winning_color = turtle.pencolor()
            is_race_on = False

            if winning_color == choice:
                result = "Congratulations! You won!"
            else:
                result = f"Sorry, you lost. The {winning_color} turtle won."

            # Display result in a pop-up
            screen.textinput(title="Race Result", prompt=result)
            break  # Break out of the loop once the race is finished

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
