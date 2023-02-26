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

# def depthFirstSearch(problem, state, path):
#     path += [state]

#     successors = problem.getSuccessors(state)
#     for successor, action, cost in successors:
#         if (successor.getPacmanPosition() not in (state.getPacmanPosition() for state in path)):
#             path = depthFirstSearch(problem, successor, path)
        
#     return path
    

def depthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    current_state = problem.getStartState()
    
    if problem.isGoalState(current_state):
        return []
    
    frontier = Stack()
    explored = set()
    final_path = None
    
    # each item in the frontier is a tuple of (state, path to state)
    frontier.push((current_state, []))
    while(frontier):
        state, path = frontier.pop()
        # print(state)
        
        if (problem.isGoalState(state)):
            # return path
            final_path = path
            break
        
        # if state in explored:
        #     continue
        if state.getPacmanPosition() not in (s.getPacmanPosition() for s in explored):     
            explored.add(state)
        
        successors = problem.getSuccessors(state)
        for successor, action, cost in reversed(successors):
            if (successor not in explored):
                frontier.push((successor, path + [action]))
    
    if (final_path is not None):
        return final_path
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
            if (successor not in explored) and (successor not in (s for s,_ in frontier.queue)):
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
    current_state = problem.getStartState()
    frontier = PriorityQueue()
    frontier.push(0, (current_state, [])) # Push the state, the path and the priority value into the frontier
    explored = set()
    
    while (frontier):
        state, path = frontier.pop()
        
        if (problem.isGoalState(state)):
            return path
        explored.add(state)
        
        successors = problem.getSuccessors(state)
        for successor, action, cost in successors:
            if (successor not in explored) and (successor not in (s[0] for _,s in frontier.priority_queue)):
                current_path = path + [action]
                current_path_cost = problem.getCostOfActions(current_path)
                pair = (successor, current_path)
                frontier.push(current_path_cost, pair)
            else:
                if (successor in (s[0] for _,s in frontier.priority_queue)):
                    for item in frontier.priority_queue:
                        if (successor == item[0]):
                            current_path = path + [action]
                            current_path_cost = problem.getCostOfActions(current_path)
                            old_path = item[1]
                            old_path_cost = problem.getCostOfActions(old_path)
                            if (current_path_cost < old_path_cost):
                                # Remove the old state
                                index = frontier.getIndex(item)
                                frontier.removeIndex(index)
                                
                                # Push new state
                                pair = (successor, current_path)
                                frontier.push(current_path_cost, pair)
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
