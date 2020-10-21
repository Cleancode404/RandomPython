import turtle

def setup( ):
    #provide the config for the screen#
    turtle.title('Multiple Squares Animation')
    turtle.setup(100, 100, 0, 0)
    turtle.hideturtle( )


def draw_square(size):
    #draw a square in the current direction
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
setup( )

for _ in range(0, 13):
    draw_square(50)
    #rotate the starting direction
    turtle.right(120)

    #add this so that the window will close when clicked on
turtle.exitonclick( )

