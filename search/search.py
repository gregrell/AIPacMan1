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

# This class generated by Greg Rell for use in further searching algorithms
class Node:
    def __init__(self,state,parent,path):
        self.state=state
        self.parent=parent
        self.path=path

    def setState(self,x):
            self.state=x
    def getState(self):
        return self.state
    def setParent(self,x):
        self.parent=x
    def getParent(self):
        return self.parent
    def setPath(self,x):
        self.path=x
    def getPath(self):
        return self.path
    def appendPath(self,x):
        self.path.append(x)


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
    #DFS
    #Uses class Node from above. Depth First Seach algorithm - when goal is found it is appended to a nodebin list. The path is re-constructed from the goal back
    #through all parent nodes to the origin.

    start=Node(problem.getStartState(),None,['Begin'])
    discovered=[]
    nodebin=[]

    #Recursive DFS implemented
    def DFS(p,v):
        discovered.append(v.getState())
        if p.isGoalState(v.getState()):
            nodebin.append(v)
            return
        else:
            successors=p.getSuccessors(v.getState())
            for s in successors:
                t=Node(s[0],v,[])
                t.appendPath(s[1])
                if not discovered.__contains__(t.getState()):
                    DFS(p,t)

    #initial DFS call
    DFS(problem,start)

    #because the algorithm is complete the goal will have been found. Reconstruct path from goal to origin
    node=nodebin[0]
    path=[]
    while not node==None:
        path.append(node.getPath())
        node=node.getParent()
    path.reverse()

    #Take path and generate directions for return of algorithm to calling routine
    directions = []
    for x in path:
        if x[0]=='East':
            directions.append(e)
        if x[0]=='West':
            directions.append(w)
        if x[0]=='North':
            directions.append(n)
        if x[0]=='South':
            directions.append(s)

    print "directions given from this algorithm ",directions

    return directions



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    start=Node(problem.getStartState(),None,['Begin'])

    #I implemented the non-recursive BFS algorithm that uses a set and a queue.

    def BFS(p,root):
        S=[]
        Q=util.Queue()
        S.append(root.getState())
        Q.push(root)
        while not Q.isEmpty():
            current=Q.pop()
            if p.isGoalState(current.getState()):
                return current
            for x in p.getSuccessors(current.getState()):
                if not S.__contains__(x[0]):
                    S.append(x[0])
                    Q.push(Node(x[0],current,x[1]))

    target=BFS(problem,start)

    #Target has been acquired, now reconstruct the path from the target back to the root
    node=target
    path = []
    while not node == None:
        path.append(node.getPath())
        node = node.getParent()
    path.reverse()

    #change the path into something the calling routine will actually be able to use
    directions = []
    for x in path:
        if x == 'East':
            directions.append(e)
        if x == 'West':
            directions.append(w)
        if x == 'North':
            directions.append(n)
        if x == 'South':
            directions.append(s)

    print "directions given from this algorithm ", directions

    return directions







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
