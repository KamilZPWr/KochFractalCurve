import turtle as tu
def Koch(length):
    """draw a Koch fractal curve recursively"""
    if length <= 2 :
        tu.fd(length)
        return
    Koch(length/3)
    tu.lt(60)
    Koch(length/3)
    tu.rt(120)
    Koch(length/3)
    tu.lt(60)
    Koch(length/3)
tu.speed(0)
length = 600.0
# move to starting position
tu.penup()
tu.backward(length/2.0)
tu.pendown()
tu.title('Koch fractal curve')
Koch(length)
    # keep showing until window corner x is clicked
tu.done()
