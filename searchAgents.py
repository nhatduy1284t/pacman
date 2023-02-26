import random
from problems import *
from search import *

from game import Agent
from game import Directions


class GoWestAgent(Agent):
    def getAction(self, state):
        if Directions.WEST in state.getLegalPacmanActions():
            return Directions.WEST
        else:
            return Directions.STOP


class RandomAgent(Agent):
    def getAction(self, state):
        actions = state.getLegalPacmanActions()
        random.shuffle(actions)
        return actions[0]

class DuyAgent(Agent):
    def registerInitialState(self, state):
        pass
        problem = SingleFoodSearchProblem(state)
        depthFirstSearch(problem)
       
        # self.randomAction = x.getAction(state)
                 
    def getAction(self, state):
        actions = state.getLegalPacmanActions()
        random.shuffle(actions)
        return Directions.STOP



class SearchAgent(Agent):
    def registerInitialState(self, state):
        """
        This is the first time that the agent sees the layout of the game
        board. Here, we choose a path to the goal. In this phase, the agent
        should compute the path to the goal and store it in a local variable.
        All of the work is done in this method!

        state: a GameState object (pacman.py)
        """
        
        # TODO 11
        problem = SingleFoodSearchProblem(state)
        
        
    def getAction(self, state):
        """
        Returns the next action in the path chosen earlier (in
        registerInitialState).  Return Directions.STOP if there is no further
        action to take.

        state: a GameState object (pacman.py)
        """
        # TODO 12


class BFSFoodSearchAgent(SearchAgent):
    # TODO 13
    pass
    def registerInitialState(self, state):
        pass
        problem = SingleFoodSearchProblem(state)
        self.path=  breadthFirstSearch(problem)
          
        
    def getAction(self, state):
        action = self.path[0]
        self.path= self.path[1:]
        return action    


class DFSFoodSearchAgent(SearchAgent):
    # TODO 14
    pass
    def registerInitialState(self, state):
        # problem = SingleFoodSearchProblem(state)
        #  breadthFirstSearch(problem)
        pass
        
    def getAction(self, state):
        
        pass



class UCSFoodSearchAgent(SearchAgent):
    # TODO 15
    pass


class AStarFoodSearchAgent(SearchAgent):
    # TODO 16
    pass
