# -*- coding: latin-1 -*-

#Written by Sabina Tjärnlund <satj0011@student.umu.se>. 
#May be used in the course Datastrukturer och Algoritmer (Python) at Umeå University.
#Usage exept those listed above requires permission by the author.

from DirectedGraph import DirectedGraph
from Edge import Edge
import sys

def eqFcn(node,node2):
    """
        Syfte: Takes two nodes and checks if they are equal
        Returvärde: True/False
        Kommentarer: 
    """    
    if node==node2:
        return True
    else:
        return False

def makeMap(txtfile):
    """
        Syfte: Transforms textfile into graph
        Pararmetrar: texfile/mapfile
        Returvärde: my_graph - Graph from textfile
        Kommentar: if textfile is empty an empty graph will be returned
        ##Obs ändra till felmeddelande att den är tom
    """    
    destinations=[]
    f = open(txtfile)
    my_graph=DirectedGraph(eqFcn)
    edges=0
    nodelist=[]
    while True:
        line = f.readline()
        if not line.startswith("#"): # 
            break
    while line.rstrip():
        if edges==0:
            edges=int(line.rstrip())
        else:
            line = line.rstrip()
            linelist=line.split()
            first=linelist[0]## nod1
            second=linelist[1] ## nod2
            if first not in destinations:
                destinations.append(first)
            if second not in destinations:
                destinations.append(second)
            if my_graph.isEmpty():
                my_graph.insertNode(first)
                nodelist.append(first)
                my_graph.insertNode(second)
                nodelist.append(second)
                edge = Edge(first,second)
                my_graph.insertEdge(edge)
            else:
                if first not in nodelist:
                    my_graph.insertNode(first)
                    nodelist.append(first)
                if second not in nodelist:
                    my_graph.insertNode(second)
                    nodelist.append(second)
                edge = Edge(first,second)
                my_graph.insertEdge(edge)
        line = f.readline()
    f.close()
    return (my_graph,destinations)

    
def checkIfNeighboor(node1,node2,graph):
    """
        Syfte: Checks if you can get from node1 to node2 by breadth-first search of the graph
        Pararmetrar: node1-origin, node2-destination, graph-map
        Returvärde: True/False
        Kommentar: if the graph is empty it will return false
    """
    check_nbour = node1
    visited = []
    queue = []    
    if graph.isEmpty():
        return False
    
    visited.append(node1)
    queue.append(node1)
    
    while queue:
        first_in_queue = queue.pop(0)      
        for neighbour in graph.neighbours(first_in_queue):
            if neighbour not in visited:
                if neighbour == node2:
                    return True
                else:
                    visited.append(neighbour)
                    queue.append(neighbour)
    return False




"""Main"""
#file= "airmap1.map"

"""STYCKET JAG INTE VET OM/ HUR DET FUNKAR"""
#  ska läsas in direkt till prompt bifogar en printsqreen av förklaring
# filen heter airmap1.map och du kan testa exempel UME BMA
if len(sys.argv) == 2:
            file = sys.argv[1]
else:
            file = input("Give filename for the map you want to read: ")
            

userChoise= " Hello "
while userChoise != "quit":
    userChoise = input("Enter origin and destination (quit to exit): ")
    if userChoise =="quit":
        print("Thank you, we are done!")
        break
    try:
            (graph,destinations)= makeMap(file)
                 
    except ValueError:
            print("\n\n ERROR: you need to choose an existing file in the correct format.") 
            
    (graph,destinations)= makeMap(file)
    userChoise = userChoise.split()
    if userChoise[0] not in destinations:
        print("The origin is not found")

    if userChoise[1] not in destinations:
        print("The destination is not found")

    connected = checkIfNeighboor(userChoise[0],userChoise[1],graph)
    if connected:
        print(userChoise[0], "and", userChoise[1], "are connected")
    if not connected:
        print(userChoise[0], "and", userChoise[1], "are not connected")
    

        
#Kvar att göra
#Utelämnat filnamn
#Fil som inte finns
#Fil som har ett felaktigt format
