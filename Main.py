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
        self.depot_index = 0
        self.lp = [0.6, 0.5]
        self.speed = 0.9
        self.buffalo_size = 50
        self.trial_size = 50
        self.bg_not_updating = 3
        
        # Sweep the graph, run the ABO and print the result, that's all :)
        graph = Graph()
        sweep = Sweep()
        sweeped_graphs = sweep.run( graph, self.depot_index )
        sweeped_buffalos = []
        if isinstance(sweeped_graphs, list) is False or len(sweeped_graphs) < 1:
            print "Error on sweeped graphs"
            exit()

        for sweeped_graph in sweeped_graphs:
            abo = self.runABO( sweeped_graph )
            sweeped_buffalos.append(abo)

        if isinstance(sweeped_buffalos, list) is False or len(sweeped_buffalos) < 1:
            print "Error on sweeped buffalos"
            exit()
        for buffalo in sweeped_buffalos:
            self.printResult(buffalo)
        
    def runABO(self, graph):
        buffalos = None
        counter = 0
        while(counter < self.bg_not_updating):
            Abo = ABO(self.depot_index, graph)
            Abo.setFirstIter()
            Abo.initParams(self.lp, self.speed)
            buffalos = [ABO(self.depot_index, graph) for i in range(1,self.buffalo_size)]
            update_counter = 0
            for i in range(1, self.trial_size):
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
        return {
            'abo': Abo,
            'buffalos': buffalos
        }

    def printResult(self, Abo):
        if Abo is None or Abo['buffalos'] is None or isinstance(Abo['buffalos'], list) is False:
            print "Error"
            exit()

        optimal_buffalo = Abo['buffalos'][0]
        optimal_index = 0
        for buffalo in Abo['buffalos']:
            buffalo.calculateTotalDistance()

            print "Total jarak tempuh kerbau",Abo['buffalos'].index(buffalo),"=", buffalo.getTotalDistance()
            print buffalo.getVisitedNodes()
            print "bp =", buffalo.bp
            if optimal_buffalo.getTotalDistance() > buffalo.getTotalDistance():
                optimal_buffalo = buffalo
                optimal_index = Abo['buffalos'].index(buffalo)
        print "bg", Abo['abo'].bg
        print "update counter", Abo['abo'].bg_update_counter
        print "Kerbau teroptimal adalah kerbau ke",optimal_index,"dengan total jarak",optimal_buffalo.getTotalDistance()

Main()