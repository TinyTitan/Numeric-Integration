from mpi4py import MPI
import numpy
import scipy
import matplotlib.pyplot as pyplot
from matplotlib.patches import Circle
from scipy import integrate

def func(x) :
    y = numpy.sin(x)
    return y

def main() :
    # MPI variables
    size = MPI.COMM_WORLD.Get_size()
    rank = MPI.COMM_WORLD.Get_rank()
    name = MPI.Get_processor_name()

    # Domain start and end
    xStart = 0.0
    xEnd = 2.0 * scipy.pi

    # Number of total samples
    samplesPerRank = 10000

    # Create x,y pair array to hold each nodes work
    coordinates = numpy.empty([samplesPerRank, 2])

    # Create integer to hold number of points that fall under the function
    inside = numpy.zeros(1, dtype=int)

    # Create array on rank 0 to hold all results
    if rank == 0:
        allCoordinates = numpy.empty([samplesPerRank*size, 2])
        totalInside = numpy.zeros(1, dtype=int)
    else:
        allCoordinates  = None
        totalInside = None

    # Create random points
    yMin = -1.0
    yMax = 1.0

    xValues = numpy.random.uniform(xStart, xEnd, samplesPerRank)
    yValues = numpy.random.uniform(yMin, yMax, samplesPerRank)

    # Fill x,y coordinate pairs and find number inside
    for i in range(0, samplesPerRank) :
        x = xValues[i] 
        y = yValues[i]
        coordinates[i] = [x, y]
        if y < func(x) and y > 0:
            inside += 1
        if y > func(x) and y < 0:
            inside -= 1

    # Gather all coordinates on rank 0
    MPI.COMM_WORLD.Gather(coordinates, allCoordinates, root=0)    

    # Sum reduce area
    MPI.COMM_WORLD.Reduce(inside, totalInside, root=0)

    # Rank 0 will create plot
    if rank == 0:
        # Add subplot to place rectangles into
        ax = pyplot.figure().add_subplot(1,1,1)
      
        # Plot of function
        xSamples = numpy.arange(xStart, xEnd, 0.1);
        vecFunc = numpy.vectorize(func)
        ySamples = vecFunc(xSamples)
        pyplot.plot(xSamples, ySamples)

        # Plot random points
        for i in range(0, samplesPerRank*size) :
            # Change color based on node
            if i%samplesPerRank == 0 :
                randColor = numpy.random.rand(3, 1)

            ax.add_patch(Circle(allCoordinates[i], 0.03, color=randColor) )

        # Calculate integral
        actualArea = integrate.quad(func, xStart, xEnd)[0]

        # Calculate difference
        totalPoints = samplesPerRank*size
        totalArea = (xEnd - xStart)*(yMax-yMin)*totalInside/totalPoints
        error = actualArea - totalArea

        # Add annotation to show total area
        ax.text(4, 0.8, "Area Error: " + str(error) , fontsize=15)
       
        # Save plot
        pyplot.savefig("plot")    

# execute main
if __name__ == "__main__":
    main()
