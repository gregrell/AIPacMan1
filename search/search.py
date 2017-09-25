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
class State:
    def __init__(self,coords,remainingGoals):
        self.coords=coords
        self.remainingGoals=remainingGoals

    def getRemainingGoals(self):
        return self.remainingGoals
    def getCoords(self):
        return self.coords


class Node:

    def __init__(self,state,parent,path,cost):
        self.state=state
        self.parent=parent
        self.path=path
        self.cost=cost
        self.f=None
        self.h=None
        self.remainingGoals=None



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
    def getCost(self):
        return self.cost
    def getTotalCost(self):
        node=self
        total=0
        while not node == None:
            try:
                total=total+self.getCost()
                node=node.getParent()
            except AttributeError:
                #print "get total cost exception"
                break
        return total
    def getTotalPath(self):
        node=self
        path = []
        while not node == None:
            try:
                path.append(node.getPath())
                node = node.getParent()
            except AttributeError:
                #print "path generation exception"
                break
        path.reverse()
        return path

    def setF(self,f):
        self.f=f
    def getF(self):
        if not self.h==None:
            return self.h+self.cost
        else:
            return self.f
    def setH(self,h):
        self.h=h
    def getH(self):
        return self.h
    def getRemainingGoals(self):
        return self.remainingGoals
    def setRemainingGoals(self,newGoals):
        self.remainingGoals=newGoals
    def removeGoal(self,goal):
        self.remainingGoals.remove(goal)
    def getFirstGoal(self):
        return self.remainingGoals[0]













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

    start=Node(problem.getStartState(),None,['Begin'],0)
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
            successors=reversed(successors)
            for s in successors:
                t=Node(s[0],v,[],0)
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

    print "directions given from this algorithm ",directions.__sizeof__()

    return directions



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    start=Node(problem.getStartState(),None,['Begin'],0)

    #I implemented the non-recursive BFS algorithm that uses a set and a queue.

    def BFS(p,root):
        S=[]
        Q=util.Queue()
        S.append(root.getState())
        Q.push(root)
        while not Q.isEmpty():
            current=Q.pop()
            path=current.getPath()
            if p.isGoalState(current.getState()):
                return current
            for x in p.getSuccessors(current.getState()):
                if x[0] not in S:
                    TmpPath=path[:]
                    TmpPath.append(x[1])
                    S.append(x[0])
                    Q.push(Node(x[0],current,TmpPath,0))

    target=BFS(problem,start)

    print "the path of target ",target.getPath()

    #change the path into something the calling routine will actually be able to use
    directions = []
    for x in target.getPath():
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
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    start = Node(problem.getStartState(), 0, ['Begin'],0)

    #Uniform cost search algorithm implemented as in https://www.ics.uci.edu/~rickl/courses/cs-171/cs171-lecture-slides/cs-171-03-UninformedSearch.pdf
    #Priority Queue used from util.py

    def UCS(p,start):
        Q=util.PriorityQueue() #Use of priority queue
        explored=[]
        Q.push(start,start.getCost())
        while not Q.isEmpty():
            node=Q.pop()
            if p.isGoalState(node.getState()):
                return node
            explored.append(node.getState())
            successors=p.getSuccessors(node.getState())
            for x in successors:
                child=Node(x[0],node,x[1],x[2])
                if not explored.__contains__(child.getState()):
                    Q.push(child,child.getTotalCost())

    goal=UCS(problem,start)

    #print "goal found at ",goal.getState(),"total cost ",goal.getTotalCost()," and path ",goal.getTotalPath()

    directions = []
    for x in goal.getTotalPath():
        if x == 'East':
            directions.append(e)
        if x == 'West':
            directions.append(w)
        if x == 'North':
            directions.append(n)
        if x == 'South':
            directions.append(s)

    return directions


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #Modelled with reference to http://web.mit.edu/eranki/www/tutorials/search/
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    start = Node(problem.getStartState(), 0, 'Begin', 0)




    closedSet=[]
    openSet=[]
    start.setF(0)
    openSet.append(start)
    iteration=0
    goalN=None
    found=False



    while len(openSet)>0 and found==False:
        iteration+=1

        leastVal=float("inf")
        q=None
        for x in openSet:
            if x.getF()<leastVal:
                q=x
        theQ=q
        openSet.remove(q)

        successors=problem.getSuccessors(theQ.getState())
        sNodes=[]
        for y in successors:
            tmpNode=Node(y[0],theQ,y[1],theQ.getCost()+y[2])
            tmpNode.setH(heuristic(tmpNode.getState(),problem))
            sNodes.append(tmpNode)

        for z in sNodes:
            flagged=False
            if problem.isGoalState(z.getState()):
                print "found goal state", z.getState()
                goalN=z
                found=True

            for other in openSet:
                if other.getState()==z.getState():
                    #print "matched other in open set ",other.getState()," at cost ",other.getF(),"with Z ",z.getState()," at cost ",z.getF()
                    if other.getF()<z.getF():
                        #openSet.append(z)
                        flagged=True

            for other in closedSet:
                if other.getState()==z.getState():
                    #print "matched other in closed set ",other.getState()," at cost ",other.getF(),"with Z ",z.getState()," at cost ",z.getF()

                    if other.getF()<z.getF():
                        #openSet.append(z)
                        flagged=True

            if  flagged==False:
                openSet.append(z)
        #print "open Set Length: ",len(openSet), "closed Set Length: ", len(closedSet)
        closedSet.append(theQ)





    directions = []
    for x in goalN.getTotalPath():
        if x == 'East':
            directions.append(e)
        if x == 'West':
            directions.append(w)
        if x == 'North':
            directions.append(n)
        if x == 'South':
            directions.append(s)

    return directions









# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
