from turtle import Turtle

ALIGNMENT = "center"
FONT = (16, "Calibri")


class StateLabel(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def label_state(self, state_name, x_cor, y_cor):
        self.goto(x_cor, y_cor)
        self.write(state_name, align=ALIGNMENT)
