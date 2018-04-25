from __future__ import division
import math
import sys
import bisect

class Graph:
    nodes = []
    polar = {}
    demands = []
    distance = {}

    def __init__(self):
        Graph.nodes = [
            # [5,5], #A
            # [4,5], #B
            # [2,2], #C
            # [2,3], #D
            # [3,1], #E
            [0, 0],
            [-0.009275, -0.033396],
            [-0.00138, -0.052539],
            [-0.075424, -0.014738],
            [-0.073711, -0.080702],
            [-0.128617, -0.116675],
            [-0.165344, -0.169464],
            [-0.155306, -0.189746],
            [-0.167362, -0.179096],
            [-0.167075, -0.175814]
        ]
        # self.longLatToXY(Graph.nodes, 3) # Because the data are XY already
        self.createPolar(Graph.nodes, 0)
        self.createDistance(Graph.nodes)
        # #A
        # Graph.distance[0][0] = 0
        # Graph.distance[0][1] = 5
        # Graph.distance[0][2] = 8
        # Graph.distance[0][3] = 0
        # Graph.distance[0][4] = 10

        # #B
        # Graph.distance[1][0] = 5
        # Graph.distance[1][1] = 0
        # Graph.distance[1][2] = 0
        # Graph.distance[1][3] = 6
        # Graph.distance[1][4] = 11

        # #C
        # Graph.distance[2][0] = 8
        # Graph.distance[2][1] = 0
        # Graph.distance[2][2] = 0
        # Graph.distance[2][3] = 7
        # Graph.distance[2][4] = 9

        # #D
        # Graph.distance[3][0] = 0
        # Graph.distance[3][1] = 6
        # Graph.distance[3][2] = 7
        # Graph.distance[3][3] = 0
        # Graph.distance[3][4] = 12

        # #E
        # Graph.distance[4][0] = 10
        # Graph.distance[4][1] = 11
        # Graph.distance[4][2] = 9
        # Graph.distance[4][3] = 12
        # Graph.distance[4][4] = 0

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
                Graph.distance[from_node][to_node] = self.calcDistance(x1,y1,x2,y2)

    def createPolar(self, locations, center_arr):
        """Initialize nodes polar."""
        size = len(locations)

        for i in xrange(size):
            r = self.calcPolar(locations[i])
            deg = self.calcPolarDeg(locations[i])
            depot = Graph.nodes[center_arr]
            if depot != locations[i]:
                angle = self.calcAngle(locations[i], depot)
            else:
                angle = 0.0
            Graph.polar[i] = {}
            Graph.polar[i]['r'] = r
            Graph.polar[i]['deg'] = deg
            # Graph.polar[i]['angle'] = angle

    def longLatToXY(self, coors, center_arr):
        center_coor = coors[center_arr]
        xy_nodes = []
        for coor in coors:
            x = coor[0] - center_coor[0]
            y = coor[1] - center_coor[1]
            xy_nodes.append([x,y])
        Graph.nodes = xy_nodes
    
    def calcDistance(self, x1, y1, x2, y2):
        # Manhattan distance
        dist = abs(x1 - x2) + abs(y1 - y2)
        return dist
    
    def calcPolarDeg(self, x):
        radian = math.atan2(x[1],x[0])
        degrees = math.degrees(radian)
        if degrees < 0:
            degrees = degrees * (-1) + 90 # It converts minus degree to be over 90 degrees basis
        return degrees

    def calcPolar(self, x):
        return math.sqrt(x[0]**2 + x[1]**2)

    #Currently not being used
    def calcAngle(self, ver, depot):
        sin_a = (ver[1] - depot[1] ) / (math.sqrt( (ver[0] - depot[0])**2 + (ver[1] - depot[1])**2 ))
        radian = math.asin(sin_a)
        return math.degrees(radian)

    def setNodes(self, nodes):
        Graph.nodes = nodes
    
    def getNodes(self):
        return Graph.nodes

    def getPolar(self):
        return Graph.polar

    def setDemands(self, demands):
        Graph.demands = demands
    
    def getDemands(self):
        return Graph.demands

    def setDistance(self, distance):
        Graph.distance = distance
    
    def getDistance(self):
        return Graph.distance