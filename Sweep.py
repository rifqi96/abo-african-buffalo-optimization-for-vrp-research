from __future__ import division
import math
from Graph import Graph
import random
import sys
import bisect

class Sweep:
    def __init__(self):
        self.Graph = None

    #static method
    def run(self, graph):
        if isinstance(graph, Graph) is False:
            print "Please add correct graph"
            exit()
        return [graph]
