#generated art with turtle module

import turtle 

WIDTH = 640
HEIGHT = 360
def setup_window( ):
    #set up the window
    turtle.title("Circles in my mind")
    turtle.setup(WIDTH, HEIGHT, 0, 0)

    turtle.colormode(255) #indicates RGB numbers will be in range 0 to 255
    turtle.tracer(2000)

    #speed up drawing process
    turtle.speed(2)
    turtle.penup()

def draw_circle(x, y, radius, red = 50, green = 255, blue = 10, width = 7):
    #draw a circle at a specific x, y location
    #then draw four smaller circle recursively 

    colour = (red, green, blue)

    #recursively drawn smaller circles
    if radius > 50:
        #calculate colours and line width for smaller circles 
        if red < 216:
            red = red + 33
            green = green - 42
            blue = blue + 10
            width -= 1
        else:
            red = 0
            green = 255
        #calculate the radius for the smaller circles
        new_radius = int (radius /1.3)
        #draw four circles
        draw_circle(int (x + new_radius), y, new_radius, red, green, blue, width) 
        draw_circle(x - new_radius, y, new_radius, red, green, blue, width)
        draw_circle(x, int(y + new_radius), new_radius, red, green, blue, width)
        draw_circle(x, int(y- new_radius), new_radius, red, green, blue, width)

    #draw the original circle
    turtle.goto(x,y)
    turtle.color(colour)
    turtle.width(width)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()

#run the program
print('Starting')
setup_window()
draw_circle(25, -100, 200)

#ensure that all the drawing is rendered
turtle.update()
print("Done")
turtle.done()