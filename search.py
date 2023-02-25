"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from util import *
from game import Directions
import time

n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST


def depthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 17
    stack = Stack()
    node = problem.getStartState()
    visited = [node]
    stack.push(node)
    while(stack):
        node = stack.pop()
        neighbors = problem.getSuccessors(node)
        for tuple in neighbors:
            i=0
            n,action, cost = tuple
            print(n)
            if(n not in visited):
                print("Go",action)
                visited.append(n)
                stack.push(n)
                break   


    print("da ra khoi while")       

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
