from turtle import *


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)



def move_up():
    if(user_block[-1].ycor() >= 280):
        return None
    for i in range(2, -1, -1):
        user_block[i].forward(20)
        
def move_down():
    if(user_block[0].ycor() <= -275):
        return None
    for i in range(3):
        user_block[i].backward(20)
        
def move_up_comp():
    if(comp_block[-1].ycor() >= 280):
        return None
    for i in range(2, -1, -1):
        comp_block[i].forward(20)
        
def move_down_comp():
    if(comp_block[0].ycor() <= -275):
        return None
    for i in range(3):
        comp_block[i].backward(20)
        

    
        



#creating two blocks one for user and the other for computer
user_block = []
comp_block = []
#this are the positions where we want to get user and computer blocks
us_bl_pos = [(-280,-20),(-280,0),(-280,20)]
co_bl_pos = [(275,-20),(275,0),(275,20)]


#this one is for user and there will be three blocks been created 
for i in us_bl_pos:
    use_block = Turtle("square")
    use_block.setheading(90)
    use_block.speed("fastest")
    use_block.penup()
    use_block.color("white")
    use_block.goto(i)
    user_block.append(use_block)
    screen.update()
    
#this one is for computer 
for i in co_bl_pos:
    co_block = Turtle("square")
    co_block.setheading(90)
    co_block.speed("fastest")
    co_block.penup()
    co_block.color("white")
    co_block.goto(i)
    comp_block.append(co_block)
    screen.update()

screen.listen()
#Now we will add functionality to move the user block according to the 
gameIsOn = True
while gameIsOn:
    # move_up_comp()
    # move_down_comp()
    screen.onkeypress(key="Up", fun=move_up)
    screen.onkeypress(key="Down", fun=move_down)
    screen.onkeypress(key="w", fun=move_up_comp)
    screen.onkeypress(key="s", fun=move_down_comp)
    screen.update()
    




screen.exitonclick()