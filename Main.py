from __future__ import division
import math
from ABO import ABO
from Graph import Graph
from Sweep import Sweep
import random
import sys
import bisect
from pprint import pprint

class Main:
    def __init__(self):
        # Initiate Parameters
        self.graph = Graph()
        self.counter = 0
        self.depot_index = 0
        self.lp = [0.6, 0.5]
        self.speed = 0.9
        self.buffalo_size = 50
        self.trial_size = 50
        self.bg_not_updating = 3
        self.Abo = None
        self.update_counter = 0
        
        buffalos = self.runABO()
        self.printResult(buffalos)
        
    def runABO(self):
        buffalos = None
        while(self.counter < self.bg_not_updating):
            self.Abo = ABO(self.depot_index, self.graph)
            self.Abo.setFirstIter()
            self.Abo.initParams(self.lp, self.speed)
            buffalos = [ABO(self.depot_index, self.graph) for i in range(1,self.buffalo_size)]
            self.update_counter = 0
            for i in range(1, self.trial_size):
                for buffalo in buffalos:
                    if self.Abo.depot_index not in buffalo.getVisitedNodes(): #If buffalo has not finished the move, then do buffaloMove()
                        buffalo.buffaloMove()
                for buffalo in buffalos:
                    if buffalo.bgUpdate() is True:
                        self.update_counter += 1
                if self.update_counter > 0:
                    self.Abo.bg_update_counter += 1
                self.update_counter = 0

            self.counter = self.Abo.bg_update_counter
        return buffalos

    def printResult(self, buffalos):
        if buffalos is None or isinstance(buffalos, list) is False:
            print "Error"
            exit()

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
        print "bg", self.Abo.bg
        print "update counter", self.Abo.bg_update_counter
        print "Kerbau teroptimal adalah kerbau ke",optimal_index,"dengan total jarak",optimal_buffalo.getTotalDistance()

Main()