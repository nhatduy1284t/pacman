"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from util import *
from game import Directions
import time
import math

n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST


def depthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 17
    start_state = problem.getStartState()
    stack = Stack()
    stack.push(start_state)
    visited = set()
    successors = problem.getSuccessors(start_state)
    print(successors)
    while stack:
        current_state = stack.pop()
        if problem.isGoalState(current_state):
            print("Thoat roi")
            return
        
        if current_state not in visited:
            visited.add(current_state)
            for successor, action, cost in problem.getSuccessors(current_state):
                print(successor)             
                stack.push(successor)
                break  # explore the first neighbor only
    


    # If we get here, the search failed to find a path to the goal
    return None   


def breadthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 18
    current_state = problem.getStartState()
    
    if problem.isGoalState(current_state):
        # return [current_state]
        return []
    
    frontier = Queue()
    explored = set()
    
    # each item in the frontier is a tuple of (state, path to state)
    # frontier.push((current_state, [current_state]))
    frontier.enqueue((current_state, []))
    
    while (frontier):
        state, path = frontier.dequeue()
        explored.add(state)
        successors = problem.getSuccessors(state)

        for successor, action, cost in successors:
            if successor not in explored and successor not in (s for s,_ in frontier.queue):
                if problem.isGoalState(successor):
                    # return path + [successor]
                    return path + [action]
                # frontier.push((successor, path + [successor]))
                frontier.enqueue((successor, path + [action]))

    return None


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
    heuristic =0
    xFood = -1
    yFood = -1
    xPac, yPac = state.getPacmanPosition()
    #state co food
    for i in range(len(list(state.getFood()))):
        for j in range(len(list(state.getFood()[i]))):
            if (state.hasFood(i, j)):
                xFood = i
                yFood = j
    heuristic = math.sqrt((xPac-xFood)**2 + (yPac - yFood)**2)

    return heuristic
        

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
