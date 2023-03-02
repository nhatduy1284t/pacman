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

# References: https://github.com/thiadeliria/Pacman
UP = Directions.NORTH
DOWN = Directions.SOUTH
LEFT = Directions.WEST
RIGHT = Directions.EAST
ACTIONS = {UP, DOWN, LEFT, RIGHT}

class SingleFoodSearchProblem(SearchProblem):
    def __init__(self, startingGameState):
        # TODO 1
        self.initGameState = startingGameState
        self.walls = startingGameState.getWalls()
        
        # getFood() return a Grid
        # asList() of a Grid return a list of tuples in which each tuple contains the x, y location of the food
        self.goal = startingGameState.getFood().asList()[0]

    def getStartState(self):
        # TODO 2
        return self.initGameState.getPacmanPosition()

    def isGoalState(self, state): # state is the current pacman location: (x, y)
        # TODO 3
        # Check if the pacman current position is the food position
        return state == self.goal

    def getSuccessors(self, state):
        # TODO 4
        successors = []
        for action in ACTIONS: # ACTIONS definition above
            xPac, yPac = state # state is the current pacman location: (x, y)
            dx, dy = Actions.directionToVector(action) # Change the action (ex: move WEST (move LEFT)) -> vector
            # New pacman position (newX, newY) = old position (oldX, oldY) + the action's Vector (dx, dy)
            new_x, new_y = int(xPac + dx), int(yPac + dy)
            if not self.walls[new_x][new_y]: # check if the new position is wall. if not wall, move
                new_State = (new_x, new_y)
                cost = 1
                successors.append((new_State, action, cost))
        return successors
    

    def getCostOfActions(self, actions):
        # TODO 5
        return len(actions)


class MultiFoodSearchProblem(SearchProblem):
    def __init__(self, startingGameState):
        # TODO 6
        self.initGameState = startingGameState
        self.startingPosition = startingGameState.getPacmanPosition()
        self.foodList = startingGameState.getFood().asList()
        self.walls = startingGameState.getWalls()
        
    def getStartState(self):
        # TODO 7
        return (self.startingPosition, self.foodList) # return a tuple including (pacman position, a list of tuples of food position)
    
    def isGoalState(self, state):
        # TODO 8
        # check the current number of food. If 0, is goal
        return len(state[1]) == 0
    
    def getSuccessors(self, state):
        # TODO 9
        successors = []
        for action in ACTIONS:
            xPac, yPac = state[0]
            dx, dy = Actions.directionToVector(action)
            new_x, new_y = int(xPac + dx), int(yPac + dy)
            if not self.walls[new_x][new_y]:
                new_food = state[1][:] # get the list of food location
                # Check if the pacman location = 1 of the food locations. If yes, remove food location
                if (new_x, new_y) in new_food: 
                    new_food.remove((new_x, new_y))
                    
                new_state = ((new_x, new_y), new_food)
                cost = 1
                successors.append((new_state, action, cost))
        return successors
    
    def getCostOfActions(self, actions):
        # TODO 10
        return len(actions)
