from turtle import Turtle,Screen
import random
is_race_on = False
p = True
while p:
    t = Turtle()
    s = Screen()
    s.setup(height=400, width=500)
    participant =[]
    user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? red,green,blue,purple or orange ").lower()
    color = ["red","green","blue","purple","orange"]
    y_positions = [-70, -40, -10, 20, 50, 80]
    for i in range(0,5):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color[i])
        new_turtle.goto(x=-230, y=y_positions[i])
        participant.append(new_turtle)
    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in participant:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                    k = s.textinput(title="result",prompt=f"You've won! The {winning_color} turtle is the winner!")

                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                    k = s.textinput(title="result", prompt=f"You've lost! The {winning_color} turtle is the winner!")
            rand_distance = random.randint(5, 10)
            turtle.forward(rand_distance)
    s.exitonclick()

















s.exitonclick()