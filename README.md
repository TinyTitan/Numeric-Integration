Numeric Integration
===================

For many functions, the tools of calculus can be used to calculate their "definite integral", or the area under their curve on a certain region of the xy-plane.

However, some functions are too complicated, and don't have "closed form integrals" -- basically, this means they don't have a formula that we can write down for the integral. Functions like `e^-2x` and functions that model air resistance on a baseball are just two examples of functions that don't have closed form integrals.

For these functions, we have to integrate them numerically -- that is, we have to find a trick that uses basic arithmetic and a computer to _approximate_ these integrals.

## Riemann Integration

Most calculus courses cover "Riemann Integration", or the process of drawing infinitely many, infinitely small rectangles under the curve of a function in order to calculate its area. However, if we just want a good approximation, we only need finitely many rectangles -- perhaps only a few thousand or less. This type of Riemann Integration is perfect for a computer, because we can let it do the hard work of dividing up the interval into rectangles and summing their areas.

This tutorial is split into three parts:

1. `riemann.py`
1. `riemann-parallel.py`
1. `riemann-parallel-plotting.py`

In the `riemann.py` file, we go over how to approximate the definite integral of the `Sine` function over the interval `[0, 2 * Pi]`. We begin by splitting the interval into 10 rectangles, and the width of each rectangle is `2 * Pi / 10`. We calculate the height of each rectangle by finding the value of the `Sine` function at the left hand side of where we want the rectangle to be.

This will not be a perfect estimate, because the tops of the rectangles will be flat while the real `Sine` function continues to curve, but eventually we will make the rectangles so small that the difference between the rectangles and the actual curve is almost zero.

Once we have all of our rectangles set up, we can calculate each of their areas by multiplying their width times their height. Then once we have the areas of each of the individual rectangles, we can just add them up to find the "total" area (or our best approximation) under the `Sine` curve.
