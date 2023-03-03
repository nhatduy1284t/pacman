"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from util import *
from game import Directions
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
    if problem.isGoalState(start_state):
        return []
    frontier = Stack()
    explored = []

    frontier.push((start_state, []))
    while (frontier):
        state, path = frontier.pop()

        if problem.isGoalState(state):
            return path
        explored.append(state)

        successors = problem.getSuccessors(state)
        for successor, action, cost in reversed(successors):
            if successor not in explored and successor not in (s for s,_ in frontier.stack):
                frontier.push((successor, path + [action]))

    return None


def breadthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 18
    start_state = problem.getStartState()

    if problem.isGoalState(start_state):
        return []

    frontier = Queue()
    explored = []

    # each item in the frontier is a tuple of (state, path to state)
    frontier.enqueue((start_state, []))

    while (frontier):
        state, path = frontier.dequeue()
        if problem.isGoalState(state):
            return path

        if state not in explored:
            explored.append(state)
            
            for successor, action, cost in problem.getSuccessors(state):
                if successor not in explored:
                    frontier.enqueue((successor, path + [action]))

    return None


def uniformCostSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 19
    start_state = problem.getStartState()
    if problem.isGoalState(start_state):
        return []

    frontier = PriorityQueue()
    # frontier is a priorityQueue. In this project, the priorityQueue is hand-written.
    # the value input into the priorityQueue must follow this form: (priority value, value) 
    # (the least value will be pop out first)
    frontier.push(0, (start_state, [], 0))
    explored = []
    
    while (frontier):
        state, path, current_cost = frontier.pop()
        if problem.isGoalState(state):
            return path

        # If state in explored, move on to another state in frontier
        if state not in explored:
            explored.append(state)
            for successor, actions, cost in problem.getSuccessors(state):
                newPath = path + [actions]
                newCost = current_cost + cost
                frontier.push(newCost, (successor, newPath, newCost))

    return None

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
    heuristic = 0
    xFood, yFood = problem.goal
    xPac, yPac = state
    heuristic = math.sqrt((xPac-xFood)**2 + (yPac - yFood)**2)
    return heuristic


def multiFoodSearchHeuristic(state, problem=None):
    """
    A heuristic function for the problem of multi-food search
    """
    # TODO 21
    pass
    heuristics = []
    xPac, yPac = state[0]
    foodPositions = state[1]
    for foodPos in foodPositions:
        heuristic = math.sqrt((xPac-foodPos[0])**2 + (yPac - foodPos[1])**2)
        heuristics.append(heuristic)
    
    return min(heuristics)    

def aStarSearch(problem, heuristic=nullHeuristic):
    '''
    return a path to the goal
    '''
    # TODO 22
    start_state = problem.getStartState()
    if problem.isGoalState(start_state):
        return []

    frontier = PriorityQueue()
    # frontier is a priorityQueue. In this project, the priorityQueue is hand-written.
    # the value input into the priorityQueue must follow this form: (priority value, value) 
    # (the least value will be pop out first)
    frontier.push(0, (start_state, [], 0))
    explored = []
    
    while (frontier):
        state, path, current_cost = frontier.pop()
        if problem.isGoalState(state):
            return path

        # If state in explored, move on to another state in frontier
        if state not in explored:
            explored.append(state)
            for successor, actions, cost in problem.getSuccessors(state):
                newPath = path + [actions]
                newCost = current_cost + cost + heuristic(state, problem)
                frontier.push(newCost, (successor, newPath, newCost))
    
    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
