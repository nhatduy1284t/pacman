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
        if(state.getNumFood() == 1):
            self.problem = SingleFoodSearchProblem(state)
        else:
            self.problem = MultiFoodSearchProblem(state)

        self.step = 0

    def getAction(self, state):
        """
        Returns the next action in the path chosen earlier (in
        registerInitialState).  Return Directions.STOP if there is no further
        action to take.

        state: a GameState object (pacman.py)
        """
        # TODO 12
        action = self.path[0]
        self.path = self.path[1:]
        self.step += 1

        if (len(self.path) == 0):  # end game
            print("Total steps:", self.step)
        return action


class BFSFoodSearchAgent(SearchAgent):
    # TODO 13
    def registerInitialState(self, state):
        super().registerInitialState(state)
        self.path = breadthFirstSearch(self.problem)


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
        problemName = self.problem.__class__.__name__

        if (problemName == "MultiFoodSearchProblem"):
            self.path = aStarSearch(self.problem, multiFoodSearchHeuristic)
        else:
            self.path = aStarSearch(self.problem, singleFoodSearchHeuristic)
