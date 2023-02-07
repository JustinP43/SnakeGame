from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for index in range(len(self.segments)-1,0,-1):
            new_x = self.segments[index-1].xcor()
            new_y = self.segments[index-1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(0)
    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(90)
    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(180)
    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(270)
    
    
        


