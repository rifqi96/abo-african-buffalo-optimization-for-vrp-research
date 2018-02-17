from __future__ import division
import math
from ABO import ABO
import random
import sys

class Main:
    def __init__(self):
        print "Welcome to the main program"

Abo = ABO(3) # 3 is the index of D
Abo.setFirstIter()
Abo.initParams([0.6, 0.5], 0.9)
buffalos = [ABO(3) for i in range(1,10)]

for i in range(1, 10):
    for buffalo in buffalos:
        if Abo.depot_index not in buffalo.getVisitedNodes(): #If buffalo has not finished the move, then do buffaloMove()
            buffalo.buffaloMove()
            # if len(buffalo.getAvailableIndex()) > 0:
            #     buffalo.buffaloMove()
            # else:
            #     buffalo.buffaloBack()
        # while( 3 not in buffalo.getVisitedNodes() ):
        #     if len(buffalo.getAvailableIndex()) > 0:
        #         buffalo.buffaloMove()
        #     else:
        #         buffalo.buffaloBack()

for buffalo in buffalos:
    buffalo.calculateTotalDistance()

    print "Total jarak tempuh kerbau ",buffalos.index(buffalo)," = ", buffalo.getTotalDistance()
    print buffalo.getVisitedNodes()
    print "bp = ", buffalo.bp

print "bg ", Abo.bg