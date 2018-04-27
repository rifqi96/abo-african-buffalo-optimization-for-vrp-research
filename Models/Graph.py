from __future__ import division
import math

class Graph:

    def __init__(self):
        self.nodes = [
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
        self.demands = [
            0,
            189,
            270,
            830,
            560,
            700,
            540,
            204,
            995,
            405
        ]
        self.distance = {}

        if len(self.nodes) != len(self.demands):
            print "Demands and nodes must be related"
            exit()

        # self.longLatToXY(self.nodes, 3) # Because the data are XY already
        self.createDistance(self.nodes)

    def createDistance(self, locations):
        """Initialize distance array."""
        size = len(locations)

        for from_node in xrange(size):
            self.distance[from_node] = {}
            for to_node in xrange(size):
                x1 = locations[from_node][0]
                y1 = locations[from_node][1]
                x2 = locations[to_node][0]
                y2 = locations[to_node][1]
                self.distance[from_node][to_node] = self.calcDistance(x1,y1,x2,y2)

    def longLatToXY(self, coors, center_arr):
        center_coor = coors[center_arr]
        xy_nodes = []
        for coor in coors:
            x = coor[0] - center_coor[0]
            y = coor[1] - center_coor[1]
            xy_nodes.append([x,y])
        self.nodes = xy_nodes
    
    def calcDistance(self, x1, y1, x2, y2):
        # Manhattan distance
        dist = abs(x1 - x2) + abs(y1 - y2)
        return dist

    def setNodes(self, nodes):
        self.nodes = nodes
    
    def getNodes(self):
        return self.nodes

    def setPolar(self, polar):
        self.polar = polar

    def getPolar(self):
        return self.polar

    def setDemands(self, demands):
        self.demands = demands
    
    def getDemands(self):
        return self.demands

    def setDistance(self, distance):
        self.distance = distance
    
    def getDistance(self):
        return self.distance