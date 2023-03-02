import random
from problems import *
from search import *
import search
import searchAgents
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
        self.path= aStarSearch(problem,singleFoodSearchHeuristic)

                 
    def getAction(self, state):
        action = self.path[0]
        self.path= self.path[1:]
        return action


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
        self.problem = MultiFoodSearchProblem(state)
        # self.problem = SingleFoodSearchProblem(state)
        
        
    def getAction(self, state):
        """
        Returns the next action in the path chosen earlier (in
        registerInitialState).  Return Directions.STOP if there is no further
        action to take.

        state: a GameState object (pacman.py)
        """
        # TODO 12
        action = self.path[0]
        self.path= self.path[1:]
        return action


class BFSFoodSearchAgent(SearchAgent):
    # TODO 13
    def registerInitialState(self, state):
        super().registerInitialState(state)
        self.path = breadthFirstSearch(self.problem)
        print(self.path)

class DFSFoodSearchAgent(SearchAgent):
    # TODO 14
    def registerInitialState(self, state):
        super().registerInitialState(state)
        self.path = depthFirstSearch(self.problem)         


class UCSFoodSearchAgent(SearchAgent):
    # TODO 15    
    def registerInitialState(self, state):
        super().registerInitialState(state)
        self.path = uniformCostSearch(self.problem)  

class AStarFoodSearchAgent(SearchAgent):
    # TODO 16
    def registerInitialState(self, state):
        super().registerInitialState(state)
        self.path = aStarSearch(self.problem)

