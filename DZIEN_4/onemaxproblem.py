import random
from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax",base.Fitness,weights=(1.0,))
creator.create("Individual",list,fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool",random.randint,0,1)
toolbox.register("individual",tools.initRepeat,creator.Individual,toolbox.attr_bool,100)
toolbox.register("population",tools.initRepeat,toolbox.individual)

#funkcja fitness  - funkcja przystosowania - oceny
def evalOneMax(individual):
    return sum(individual)

#rejestracja funkcji przystosowania
toolbox.register("evaluate",evalOneMax)

#rejestracja operatora krzyżowania
toolbox.register("mate",tools.cxTwoPoint)

#rejestracja operatora mutacji
toolbox.register("mutate",tools.mutFlipBit,indpb=0.05)

#rejestracja operatora selekcji
toolbox.register("select",tools.selTournament,tournsize=3)

print("_"*70)

def main():
    random.seed(64)
    pop = toolbox.population(n=300)
    CXPB, MUTPB = 0.5,0.2

    print("Start ewolucji!")
    
