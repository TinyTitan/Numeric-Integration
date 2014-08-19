#!/usr/bin/python

def func(x):
	y = x * x
	return y

def main():
    # Domain start and end
    xStart = 0.0
    xEnd = 2.0 * 3.1415

    # Number of total samples
    numRectangles = 100

    # Rectangle width
    width = (xEnd-xStart) / numRectangles

    # Empty list of Rectangle areas
    area_of_each_rectangle = []

    # Calculate the "Total" area
    total_area_under_curve = 0.0
    for i in range(0,numRectangles - 1):
	    x = i * width
	    rectangle_height = func(x)
	    rectangle_area = width * rectangle_height
	    total_area_under_curve += rectangle_area

    # Output the total area
    print total_area_under_curve

main()
