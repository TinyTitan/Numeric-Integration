#!/usr/bin/python

def func(x):
	y = x * x
	return y

def main():
    # Domain start and end
    xStart = 0.0
    xEnd = 2.0 * 3.1415

    # Number of total samples
    numRectangles = 10

    # Rectangle width
    width = (xEnd-xStart) / numRectangles

    # Empty list of Rectangle areas
    area_of_each_rectangle = []

    for i in range(0,numRectangles - 1):
	    x = i * width
	    y = func(x)
	    area_of_each_rectangle.append(x * y)

    # Calculate the "Total" area
    total_area = 0.0

    for i in range(0,numRectangles - 1):
	    total_area += area_of_each_rectangle[i]

    # Output the total area
    print total_area

main()
