from __future__ import division
import math
from ABO import ABO
import random
import sys

class Main:
    def __init__(self):
        print "Welcome to the main program"

ABO().setBgForFirstIter()
ABO().initParams([0.6, 0.5], 0.9)
buffalos = [ABO() for i in range(1,10)]

for buffalo in buffalos:
    while( 3 not in buffalo.getVisitedNodes() ):
        if len(buffalo.getAvailableIndex()) > 0:
            buffalo.buffaloMove()
        else:
            buffalo.buffaloBack()

    total = 0
    distances = []
    for distance in buffalo.getVisitedEdges():
        distances.append(buffalo.getDistance()[distance[0]][distance[1]])
    for distance in distances:
        total += distance

    print "Total jarak tempuh kerbau ke-",buffalos.index(buffalo)," = ", total
    print buffalo.getVisitedEdges()
    print buffalo.getVisitedNodes()