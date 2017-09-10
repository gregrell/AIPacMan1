# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST

    return  [s, s, w, s, w, w, s, w]
    """return [w,w,w,w,s,n,s,n,s,s,n,n,s,s,n,n,s,n,s,n,e,w,e,w,e,w,e,w,e,e,e,e,e,e,e]"""

def depthFirstSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:"""


    print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    #print "Next's successors:", problem.getSuccessors((5,4))
    #print problem

    "*** YOUR CODE HERE ***"
    #Implementing the non-recursive DFS algorithm. this algorithm uses a stack instead of a Queue.
    #The stack will be of the class from util.py



    #DFS
    discovered=[]
    def DFS(p,v,fringe):
        discovered.append(v[0])
        fringe.append(v[1])
        successors=p.getSuccessors(v[0])
        for w in successors:
            if not discovered.__contains__(w[0]):

                if p.isGoalState(w[0]):
                    print "goal state found", w
                    print "temp fringe",fringe
                    return fringe
                DFS(p,w,fringe)


    startState=((problem.getStartState()),'x',1)
    fringe=[]
    path=DFS(problem,startState,fringe)

    #print discovered
    print "path", path
    print "fringe",fringe






    """
    stateStack = util.Stack()
    visitedArray =[]
    initialState=((problem.getStartState()),'null',0)
    path=[]
    stateStack.push(initialState)
    while not stateStack.isEmpty():
        v=stateStack.pop()
        if not visitedArray.__contains__(v[0]):
            visitedArray.append(v[0])
            print visitedArray
            successors=problem.getSuccessors(v[0])
            for x in successors:
                stateStack.push(x)
    """

    #print path

    directions=[]
    """
    for x in path:
        if x[1][0]=='E':
            directions.append(e)
        if x[1][0]=='W':
            directions.append(w)
        if x[1][0]=='N':
            directions.append(n)
        if x[1][0]=='S':
            directions.append(s)"""





    print directions




    return directions



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
