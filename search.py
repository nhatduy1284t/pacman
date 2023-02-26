"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from util import *
from game import Directions
import time
import math
import heapq
n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST

def depthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 17
    current_state = problem.getStartState()

    if problem.isGoalState(current_state):
        return []

    frontier = Stack()
    explored = set()
    final_path = None

    # each item in the frontier is a tuple of (state, path to state)
    frontier.push((current_state, []))
    while (frontier):
        state, path = frontier.pop()
        # if state in explored:
        #     continue
        if state.getPacmanPosition() in (s.getPacmanPosition() for s in explored):
            # explored.add(state)
            continue
        explored.add(state)

        if (problem.isGoalState(state)):
            # return path
            final_path = path
            break

        successors = problem.getSuccessors(state)
        for successor, action, cost in reversed(successors):
            if (successor.getPacmanPosition() not in (s.getPacmanPosition() for s in explored)):
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
            successor_pacman_pos = successor.getPacmanPosition()
            frontier_states = list(s for s, _ in frontier.queue)
            frontier_pacman_pos = list(s.getPacmanPosition()
                                       for s in frontier_states)
            explored_pacman_pos = list(s.getPacmanPosition() for s in explored)

            # if (successor.getPacmanPosition() not in (s.getPacmanPosition() for s in explored)):
            #     if (successor.getPacmanPosition() not in (s.getPacmanPosition() for s in frontier_states)):
            #         if problem.isGoalState(successor):
            #             return path + [action]
            #         frontier.enqueue((successor, path + [action]))

            if (successor_pacman_pos not in explored_pacman_pos) and (successor_pacman_pos not in frontier_pacman_pos):
                if problem.isGoalState(successor):
                    return path + [action]
                frontier.enqueue((successor, path + [action]))

    return None


def uniformCostSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 19
    current_state = problem.getStartState()
    frontier = PriorityQueue()
    # Push the state, the path and the priority value into the frontier
    frontier.push(0, (current_state, []))
    explored = set()

    while (frontier):
        state, path = frontier.pop()

        if (problem.isGoalState(state)):
            return path
        explored.add(state)

        successors = problem.getSuccessors(state)
        for successor, action, cost in successors:
            successor_pacman_pos = successor.getPacmanPosition()
            frontier_states = list(s[0] for _, s in frontier.priority_queue)
            frontier_pacman_pos = list(s.getPacmanPosition()
                                       for s in frontier_states)
            explored_pacman_pos = list(s.getPacmanPosition() for s in explored)

            if (successor_pacman_pos not in explored_pacman_pos) and (successor_pacman_pos not in frontier_pacman_pos):
                current_path = path + [action]
                current_path_cost = problem.getCostOfActions(current_path)
                pair = (successor, current_path)
                frontier.push(current_path_cost, pair)
            else:
                if (successor_pacman_pos in frontier_pacman_pos):
                    # value in frontier: (priority,(state, path))
                    for priority, item in frontier.priority_queue:
                        if (successor_pacman_pos == item[0].getPacmanPosition()):
                            current_path = path + [action]
                            current_path_cost = problem.getCostOfActions(
                                current_path)
                            old_path = item[1]
                            old_path_cost = priority
                            # old_path_cost = problem.getCostOfActions(old_path)
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
    heuristic = 0
    xFood = -1
    yFood = -1
    xPac, yPac = state.getPacmanPosition()
    # state co food
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
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    pq = PriorityQueue()
    pq.push(0, (startState, []))
    
    visited = set()
    
    while pq:
        state, path = pq.pop()
        if problem.isGoalState(state):         
            return path            
        if state.getPacmanPosition() not in visited:
            visited.add(state.getPacmanPosition())
            for successor, action, cost in problem.getSuccessors(state):
                totalCost = problem.getCostOfActions(
                    path + [action]) + heuristic(successor, problem)
                pq.push(totalCost,(successor, path+ [action]))

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
