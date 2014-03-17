from mpi4py import MPI
import numpy
import scipy
import matplotlib.pyplot as pyplot
from matplotlib.patches import Rectangle
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
    samplesPerRank = 10

    # Rectangle width
    width = (xEnd-xStart) / (samplesPerRank*size)

    # Node start and end
    rankStart = xStart + width*samplesPerRank*rank
    rankEnd   = rankStart + width*samplesPerRank

    # Create x,y pair array to hold each nodes work
    coordinates = numpy.empty([samplesPerRank, 2])

    # Create area float
    area = numpy.zeros(1)

    # Create array on rank 0 to hold all results
    if rank == 0:
        allCoordinates = numpy.empty([samplesPerRank*size, 2])
        totalArea = numpy.zeros(1)
    else:
        allCoordinates  = None
        totalArea = None

    # Fill x,y coordinate pairs and sum area
    for i in range(0, samplesPerRank) :
        x = rankStart + i*width
        y = func(x)
        coordinates[i] = [x, y]
        area = area + width*y

    # Gather all coordinates on rank 0
    MPI.COMM_WORLD.Gather(coordinates, allCoordinates, root=0)    

    # Sum reduce area
    MPI.COMM_WORLD.Reduce(area, totalArea, root=0)

    # Rank 0 will create plot
    if rank == 0:
        # Add subplot to place rectangles into
        ax = pyplot.figure().add_subplot(1,1,1)
      
        # Plot of all points
        pyplot.plot(*zip(*allCoordinates))

        # Plot rectangles
        for i in range(0, samplesPerRank*size) :
            lowerLeft = allCoordinates[i][0]
            height = allCoordinates[i][1]

            # Change color based on node
            if i%samplesPerRank == 0 :
                randColor = numpy.random.rand(3, 1)

            ax.add_patch(Rectangle((lowerLeft,0), width, height, facecolor=randColor, edgecolor='black') )

        # Calculate integral
        actualArea = integrate.quad(func, xStart, xEnd)[0]

        # Calculate difference 
        error = actualArea - totalArea

        # Add annotation to show total area
        ax.text(4, 0.8, "Area Error: " + str(error) , fontsize=15)
       
        # Save plot
        pyplot.savefig("plot")    

# execute main
if __name__ == "__main__":
    main()
