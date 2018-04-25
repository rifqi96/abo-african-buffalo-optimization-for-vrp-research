from __future__ import division
import math
from Graph import Graph
import random
import sys
import bisect
from pprint import pprint

class Sweep:
    polar = {}
    
    def __init__(self):
        self.Graph = None

    def run(self, graph, center_node):
        if isinstance(graph, Graph) is False:
            print "Please add correct graph"
            exit()
        sweeped_graphs = []
        self.createPolar(graph, center_node)
        
        return sweeped_graphs

    def createPolar(self, graph, center_node):
        """Initialize nodes polar."""
        locations = graph.getNodes()
        size = len(locations)
        polar = []
        for i in xrange(size):
            r = self.calcPolar(locations[i])
            deg = self.calcPolarDeg(locations[i])
            depot = locations[center_node]
            if depot != locations[i]:
                angle = self.calcAngle(locations[i], depot)
            else:
                angle = 0.0
            polar.append({
                'r':r, 'deg':deg
            })
            # polar[i]['angle'] = angle
        graph.setPolar(polar)

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