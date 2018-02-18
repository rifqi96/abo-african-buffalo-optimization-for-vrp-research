class Graph:
    nodes = []
    demands = []
    distance = {}

    def __init__(self):
        Graph.nodes = [
            [5,5], #A
            [4,5], #B
            [2,2], #C
            [2,3], #D
            [3,1] #E
        ]
        self.createDistance(Graph.nodes)
        #A
        Graph.distance[0][0] = 0
        Graph.distance[0][1] = 5
        Graph.distance[0][2] = 8
        # Graph.distance[0][3] = 0
        Graph.distance[0][4] = 10

        #B
        Graph.distance[1][0] = 5
        Graph.distance[1][1] = 0
        # Graph.distance[1][2] = 0
        Graph.distance[1][3] = 6
        Graph.distance[1][4] = 11

        #C
        Graph.distance[2][0] = 8
        # Graph.distance[2][1] = 0
        Graph.distance[2][2] = 0
        Graph.distance[2][3] = 7
        Graph.distance[2][4] = 9

        #D
        # Graph.distance[3][0] = 0
        Graph.distance[3][1] = 6
        Graph.distance[3][2] = 7
        Graph.distance[3][3] = 0
        Graph.distance[3][4] = 12

        #E
        Graph.distance[4][0] = 10
        Graph.distance[4][1] = 11
        Graph.distance[4][2] = 9
        Graph.distance[4][3] = 12
        Graph.distance[4][4] = 0

    def createDistance(self, locations):
        """Initialize distance array."""
        size = len(locations)

        for from_node in xrange(size):
            Graph.distance[from_node] = {}
            for to_node in xrange(size):
                x1 = locations[from_node][0]
                y1 = locations[from_node][1]
                x2 = locations[to_node][0]
                y2 = locations[to_node][1]
                Graph.distance[from_node][to_node] = 0
                # It's supposed to be:
                # self.calcDistance(x1,y1,x2,y2)
    
    def calcDistance(self, x1, y1, x2, y2):
        # Manhattan distance
        dist = abs(x1 - x2) + abs(y1 - y2)
        return dist

    def setNodes(self, nodes):
        Graph.nodes = nodes
    
    def getNodes(self):
        return Graph.nodes

    def setDemands(self, demands):
        Graph.demands = demands
    
    def getDemands(self):
        return Graph.demands

    def setDistance(self, distance):
        Graph.distance = distance
    
    def getDistance(self):
        return Graph.distance