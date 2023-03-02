import util
from game import Directions
from game import Actions


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """

        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


class SingleFoodSearchProblem(SearchProblem):
    def __init__(self, startingGameState):
        # TODO 1
        self.startingState = startingGameState
        self.walls = startingGameState.getWalls()
        self.costFn = lambda x: 1
        self.goal = startingGameState.getFood().asList()[0]

    def getStartState(self):
        # TODO 2
        return self.startingState.getPacmanPosition()

    def isGoalState(self, state):
        # TODO 3
        return state == self.goal

    def getSuccessors(self, state):
        # TODO 4
        
        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x, y = state
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextState = (nextx, nexty)
                cost = self.costFn(nextState)
                successors.append((nextState, action, cost))
        return successors
    

    def getCostOfActions(self, actions):
        # TODO 5
        return len(actions)


class MultiFoodSearchProblem(SearchProblem):
    def __init__(self, startingGameState):
        self.startingGameState = startingGameState
        self.startingPosition = startingGameState.getPacmanPosition()
        self.food = startingGameState.getFood()
        self.foodList = self.food.asList()
        self.walls = startingGameState.getWalls()
        
    def getStartState(self):
        return (self.startingPosition, self.foodList)
    
    def isGoalState(self, state):
        return len(state[1]) == 0
    
    def getSuccessors(self, state):
        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x, y = state[0]
            dx, dy = Actions.directionToVector(action)
            next_x, next_y = int(x + dx), int(y + dy)
            if not self.walls[next_x][next_y]:
                next_food = state[1][:]
                if (next_x, next_y) in next_food:
                    next_food.remove((next_x, next_y))
                next_state = ((next_x, next_y), next_food)
                cost = 1
                successors.append((next_state, action, cost))
        return successors
    
    def getCostOfActions(self, actions):
        return len(actions)
