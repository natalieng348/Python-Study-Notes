import turtle

# named constants
NUM_CIRCLES = 6    # Number of circles to draw
RADIUS = 100        # Radius of each circle
ANGLE = 62          # Angle to turn
ANIMATION_SPEED = 3 # Animation speed (1-slowest, 3-slow, 6-normal, 10-fast, 0-fastest)
COLORS = ['red', 'green', 'blue']


# Set the animation speed
turtle.speed(ANIMATION_SPEED)

# Draw 36 circles, with the turtle tilted by 10 degrees after each circle is drawn
# Alternate by red, green, blue

for x in range(NUM_CIRCLES):
    color_index = x % len(COLORS)   # Get each list item index in COLORS
    color = COLORS[color_index]     # Get color value by list slicing
    turtle.color(color)             # Assign color to turtle
    turtle.circle(RADIUS)           # Draw circle
    turtle.left(ANGLE)              # Tilt by [ANGLE] degree

turtle.done()
