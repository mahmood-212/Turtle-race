from turtle import Turtle, Screen
import random

# tim = Turtle(shape="turtle")
# tom = Turtle(shape="turtle")
# jin = Turtle(shape="turtle")
# jon = Turtle(shape="turtle")
# mid = Turtle(shape="turtle")

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color? ")
colors = ["red", "blue", "yellow", "purple", "green", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for index_turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index_turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index_turtle])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:


    for turtle2 in all_turtles:
        if turtle2.xcor() > 230:
            is_race_on = False
            winning_color = turtle2.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {user_bet} turtle is the winner ")
            else:
                print(f"You've lost! The {winning_color} turtle is winning")
            print(turtle2.color())


        random_distance = random.randint(0,10)
        turtle2.forward(random_distance)



# tom.color(colors[1])
# tom.penup()
# tom.goto(-230,-60)
#
# jin.color(colors[2])
# jin.penup()
# jin.goto(-230,-20)
#
# jon.color(colors[3])
# jon.penup()
# jon.goto(-230,20)
#
# mid.color(colors[4])
# mid.penup()
# mid.goto(-230,60)
#
# mod.color(colors[5])
# mod.penup()
# mod.goto(-230,100)

screen.exitonclick()