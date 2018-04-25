from __future__ import division
import math
from ABO import ABO
import random
import sys
import bisect
from pprint import pprint

class Main:
    def __init__(self):
        print "Welcome to the main program"
counter = 0
while(counter < 3):
    Abo = ABO(0) # 3 is the index of D
    Abo.setFirstIter()
    Abo.initParams([0.6, 0.5], 0.9)
    buffalos = [ABO(0) for i in range(1,50)]
    update_counter = 0
    for i in range(1, 50):
        for buffalo in buffalos:
            if Abo.depot_index not in buffalo.getVisitedNodes(): #If buffalo has not finished the move, then do buffaloMove()
                buffalo.buffaloMove()
        for buffalo in buffalos:
            if buffalo.bgUpdate() is True:
                update_counter += 1
        if update_counter > 0:
            Abo.bg_update_counter += 1
        update_counter = 0

    counter = Abo.bg_update_counter

optimal_buffalo = buffalos[0]
optimal_index = 0
for buffalo in buffalos:
    buffalo.calculateTotalDistance()

    print "Total jarak tempuh kerbau",buffalos.index(buffalo),"=", buffalo.getTotalDistance()
    print buffalo.getVisitedNodes()
    print "bp =", buffalo.bp
    if optimal_buffalo.getTotalDistance() > buffalo.getTotalDistance():
        optimal_buffalo = buffalo
        optimal_index = buffalos.index(buffalo)
print "bg", Abo.bg
print "update counter", Abo.bg_update_counter
print "Kerbau teroptimal adalah kerbau ke",optimal_index,"dengan total jarak",optimal_buffalo.getTotalDistance()
pprint(Abo.getPolar())