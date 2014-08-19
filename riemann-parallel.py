from mpi4py import MPI
import numpy
import scipy
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

    # Create area float
    area = numpy.zeros(1)

    # Create array on rank 0 to hold all results
    if rank == 0:
        totalArea = numpy.zeros(1)
    else:
        totalArea = None

    # Fill x,y coordinate pairs and sum area
    for i in range(0, samplesPerRank) :
        x = rankStart + i*width
        y = func(x)
        area = area + width*y

    # Sum reduce area
    MPI.COMM_WORLD.Reduce(area, totalArea, root=0)

    # Rank 0 will calculate error
    if rank == 0:

        # Calculate integral
        actualArea = integrate.quad(func, xStart, xEnd)[0]

        # Calculate difference 
        error = actualArea - totalArea

	print error


# execute main
if __name__ == "__main__":
    main()
