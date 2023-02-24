"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from game import Directions

n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST


def depthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    
    # TODO 17
    visited = set()  # Set to keep track of visited states
    stack = [(problem.getStartState(), [])]  # Stack to keep track of states to visit
    print(stack)
    while stack:
        pass
        state, path = stack.pop()  # Get the next state to visit from the stack
        if problem.isGoalState(state):  # Check if the goal state has been reached
            return path  # Return the path to the goal
        # if state not in visited:  # Check if the state has already been visited
        #     visited.add(state)  # Mark the state as visited
        #     for next_state, action, cost in problem.getSuccessors(state):  # Get the possible next states
        #         next_path = path + [action]  # Update the path to the next state
        #         stack.append((next_state, next_path))  # Add the next state and path to the stack

    return None  # Return None if no path to the goal is found


def breadthFirstSearch(problem):
    '''
    return a path to the goal
    '''

    # TODO 18


def uniformCostSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 19


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def singleFoodSearchHeuristic(state, problem=None):
    """
    A heuristic function for the problem of single food search
    """
    # TODO 20
    pass


def multiFoodSearchHeuristic(state, problem=None):
    """
    A heuristic function for the problem of multi-food search
    """
    # TODO 21
    pass


def aStarSearch(problem, heuristic=nullHeuristic):
    '''
    return a path to the goal
    '''
    # TODO 22


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
