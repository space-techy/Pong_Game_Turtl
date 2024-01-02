from turtle import *


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)



#creating two blocks one for user and the other for computer
user_block = []
comp_block = []
#this are the positions where we want to get user and computer blocks
us_bl_pos = [(-280,-20),(-280,0),(-280,20)]
co_bl_pos = [(275,-20),(275,0),(275,20)]


#this one is for user and there will be three blocks been created 
for i in us_bl_pos:
    use_block = Turtle("square")
    use_block.speed("fastest")
    use_block.penup()
    use_block.color("white")
    use_block.goto(i)
    user_block.append(use_block)
    screen.update()
    
#this one is for computer 
for i in co_bl_pos:
    co_block = Turtle("square")
    co_block.speed("fastest")
    co_block.penup()
    co_block.color("white")
    co_block.goto(i)
    comp_block.append(co_block)
    screen.update()


#Now we will add functionality to move the user block according to the 





screen.exitonclick()