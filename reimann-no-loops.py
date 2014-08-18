#!/usr/bin/python

pi = 3.1415
xStart = 0.0
xEnd = 2.0 * pi

width = (xEnd-xStart) / 4

# Calculate first rectangle
x = 0
y = x * x
area1 = width * height

# Calculate second rectangle
x = x + width
y = x * x
area2 = width * height

# Calculate third rectangle
x = x + width
y = x * x
area3 = width * height

# Calculate the last rectangle
x = x + width
y = x * x
area4 = width * height

# Calculate the total area for
# all the rectangles together
total_area = area1 + area2 + area3 + area4

print total_area
