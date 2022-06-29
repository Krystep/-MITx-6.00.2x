import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    p_rabbit = 1 - (CURRENTRABBITPOP/MAXRABBITPOP)
    for rabbit in range(CURRENTRABBITPOP):
        if 1000 > CURRENTRABBITPOP > 10:
        
            if random.random() <= p_rabbit:
                CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    
    p_eat = CURRENTRABBITPOP/MAXRABBITPOP
    for fox in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            if random.random() <= p_eat:
                CURRENTRABBITPOP -= 1
                if random.random() <= 1/3:
                    CURRENTFOXPOP += 1
            elif random.random() <= 0.9:
                CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    
    return (rabbit_populations, fox_populations)
        
    
#a, b = runSimulation(200)
#pylab.plot(a, 'bo')
#pylab.plot(b, 'r+')
#pylab.show()
rabbitPopulationOverTime, foxPopulationOverTime = runSimulation(500)
coeff = pylab.polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)
pylab.plot(pylab.polyval(coeff, range(len(rabbitPopulationOverTime))))
#coeff2 = pylab.polyfit(range(len(foxPopulationOverTime)), foxPopulationOverTime, 2)
#pylab.plot(pylab.polyval(coeff2, range(len(foxPopulationOverTime))))

