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

### Part 1

In the `riemann.py` file, we go over how to approximate the definite integral of the `Sine` function over the interval `[0, 2 * Pi]`. We begin by splitting the interval into 10 rectangles, and the width of each rectangle is `2 * Pi / 10`. We calculate the height of each rectangle by finding the value of the `Sine` function at the left hand side of where we want the rectangle to be.

This will not be a perfect estimate, because the tops of the rectangles will be flat while the real `Sine` function continues to curve, but eventually we will make the rectangles so small that the difference between the rectangles and the actual curve is almost zero.

Once we have all of our rectangles set up, we can calculate each of their areas by multiplying their width times their height. Then once we have the areas of each of the individual rectangles, we can just add them up to find the "total" area (or our best approximation) under the `Sine` curve.

#### Challenges

1. Numerically integrate the `Cosine` function over the same interval
1. Numerically integrate the `Cosine` function over the interval [1,2] -- does this match what you would expect from Calculus?
1. Numerically integrate `e^-2x` over the interval [1,2]
1. __Bonus__ Add an option that allows you to describe the interval boundaries on the command line

### Part 2

In the `riemann-parallel.py` file, we discuss how to _parallelize_ this problem -- that means, how to use more than one computer to solve it. This will give us a better approximation to the area under the curve. In this case, if we have access to 4 computers, we can calculate 4x as many rectangles, allowing us to have a much more accurate answer.

Each _rank_ (or computer) has a number associated with it -- 0,1,2 or 3. We multiply this number by 10 to figure out which rectangles each rank will be responsible for calculating. In this case:

1. Rank 0 will handle rectangles 1 through 10
1. Rank 1 will handle rectangles 11 through 20
1. Rank 2 will handle rectangles 21 through 30
1. Rank 3 will handle rectangles 31 through 40

Once each rank calculates the total area for its ten rectangles, we will use the `Reduce` command to add up the totals from each rank into a single Grand Total. This Grand Total will be our new approximation for the integral, and should be more accurate than our previous approximation.

#### Challenges

1. Scale the simulation up to 6 or 9 nodes if you have them.
2. Increase the number of rectangles calculated on each rank from 10 to 100
