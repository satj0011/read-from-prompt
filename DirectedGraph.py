# -*- coding: latin-1 -*-

#Written by Johan Eliasson <johane@cs.umu.se> based on an original by
#Lena Kallin Westin <kallin@cs.umu.se>.
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.   

"""
Datatypen ordnad riktad graf med m�jlighet till att ha vikter p� noderna.
Datatypen f�ljer till stora delar med undantag f�r 3 funktioner f�r att hantera 
vikter p� kanterna definitionen av datatypen Graf p� sidan 339 i
Lars-Erik Janlert, Torbj�rn Wiberg Datatyper och algoritmer 2., [rev.] 
uppl.,Lund, Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7 

Variabler och funktioner som inleds med ett enkelt underscore "_" �r privata
f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.

Denna klass implementerar en Graf.
"""
from Edge import Edge
from DirectedList import DirectedList
"""
    Datatypen Node som �r en nod i en graf och som sj�lv h�ller reda p� sina grannar.
"""
"""
    Datatypen InternalEdge som �r informationen om en nods granne och vikten 
    mellan dessa.
"""
class InternalEdge:
    def __init__(self, v, label=None):
        self._vertice = v
        self._label = label    
        
class Node:
    def __init__(self, v):
        """
            Syfte: Skapar en ut�kad nod-defintition fr�n vertice v och en 
                   tom grannlista
            Pararmetrar: v - vertice i grafen 
        """         
        self._vertice = v
        self._noEdges = 0
        self._edges = []      
    
    def __str__(self):
        """
            Syfte: Skapar en str�ngrepresentation av Noden
        """
        return str(self._vertice)    

class DirectedGraph:
    def __init__(self, eqFcn):
        """
            Syfte: Skapar en tom graf
            Pararmetrar: eqFcn - en funktion som kan avg�ra om tv� vertices �r lika
            Returv�rde: 
            Kommentarer: En tom graf
        """   
        self._nodes = [] # En lista av noder
        self._eqFcn = eqFcn
    
    def insertNode(self, vertice):
        """
            Syfte: Stoppar in en nod vertice i grafen.
            Pararmetrar: vertice - en nod
            Returv�rde: 
            Kommentarer: 
        """     
        self._nodes.append(Node(vertice))
        
    def insertEdge(self, edge):
        """
            Syfte: Stoppar in en kant edge i grafen.
            Pararmetrar: edge - kanten som ska l�ggas till
            Returv�rde: 
            Kommentarer: F�ruts�tter att noderna i edge finns i grafen. 
        """ 
        (v1, v2) = edge.getVertices()
        for node in self._nodes:
            if self._eqFcn(node._vertice, v1):                               
                node._edges.append(InternalEdge(v2)) 
                node._noEdges = node._noEdges + 1
        
    def isEmpty(self):
        """
            Syfte: Kollar om grafen �r tom (utan noder)
            Pararmetrar: 
            Returv�rde: True om grafen �r tom, annars False
            Kommentarer: 
        """    
        return self._nodes == []
        
    def hasNoEdges(self):
        """
            Syfte: Kontrollerar om grafen saknar kanter
            Pararmetrar: 
            Returv�rde: True om grafen saknar kanter, annars False
            Kommentarer: 
        """    
        for node in self._nodes:
            if node._edges != []:
                return False  #Vi fann en kant!
        return True
        
    def chooseNode(self):
        """
            Syfte: V�ljer ut en av noderna i grafen och returnerar den
            Pararmetrar: 
            Returv�rde: En nod i grafen.
            Kommentarer: 
        """  
        return self._nodes[0]._vertice
        
    def neighbours(self, vertice):
        """
            Syfte: Letar reda p� grannarna till noden vertice
            Pararmetrar: vertice - en nod som man s�ker grannar till
            Returv�rde: En lista med noderna som �r grannar till noden vertice
            Kommentarer: 
        """   
        for node in self._nodes:
            if self._eqFcn(vertice, node._vertice):
                list = []
                for edge in node._edges:
                    list.append(edge._vertice)      
                return list                
        return []
    
    def deleteNode(self, vertice):
        """
            Syfte: Tar bort noden vertice ur grafen
            Pararmetrar: vertice - en nod som ska tas bort
            Returv�rde: 
            Kommentarer: F�ruts�tter att noden vertice inte ing�r i n�gra kanter
        """     
        for node in self._nodes:
            if self._eqFcn(node._vertice, vertice):        
                self._nodes.remove(node)
                return

    def deleteEdge(self, edge):
        """
            Syfte: Tar bort kanten edge ur grafen
            Pararmetrar: edge - kanten som ska tas bort
            Returv�rde: 
            Kommentarer: 
        """     
        (v1, v2) = edge.getVertices()
        for node in self._nodes:
            if self._eqFcn(node._vertice, v1):  
                for edge in node._edges:
                    if self._eqFcn(edge._vertice, v2): 
                        node._edges.remove(edge)
                        node._noEdges = node._noEdges -1
                        return                 
                
    def hasEdgeLabel(self, edge):
        """
            Syfte: Kontrollerar om kanten har en vikt/ett v�rde
            Pararmetrar: edge - kanten som kan kontrollerar
            Returv�rde: True om kanten har en vikt, annars False
            Kommentarer: Det f�ruts�tts att kanten finns i grafen
        """    
        (v1, v2) = edge.getVertices()
        for node in self._nodes:
            if self._eqFcn(node._vertice, v1):
                for edge in node._edges:
                    if self._eqFcn(edge._vertice, v2):
                        return edge._label != None                 

        
    def setEdgeLabel(self, edge, label):
        """
            Syfte: S�tter vikten/v�rdet p� kanten edge
            Pararmetrar: edge - kanten
                         label - etiketten
            Returv�rde: 
            Kommentarer: Det f�ruts�tts att kanten finns i grafen
        """  
        (v1, v2) = edge.getVertices()
        for node in self._nodes:
            if self._eqFcn(node._vertice, v1):
                for edge in node._edges:
                    if self._eqFcn(edge._vertice, v2):
                        edge._label = label   
        
    def inspectEdgeLabel(self, edge):
        """
            Syfte: Kontrollerar vikten/v�rdet p� kanten edge
            Pararmetrar: edge - kanten som man kontrollerar
            Returv�rde: Vikten/v�rdet p� kanten edge
            Kommentarer: 
        """   
        (v1, v2) = edge.getVertices()
        for node in self._nodes:
            if self._eqFcn(node._vertice, v1):
                for edge in node._edges:
                    if self._eqFcn(edge._vertice, v2):
                        return edge._label              
    
    def __str__(self):
        """
            Syfte: Skapar en str�ngrepresentation av grafen
        """
        myStr = "H�r kommer noderna och deras grannar!\n"
        for node in self._nodes:
            myStr = myStr + "\n" + str(node._vertice) + ", " 
            myStr = myStr + str(node._noEdges) + " grannar:\n"
            for edge in node._edges:
                myStr = myStr + str(edge._vertice) + ", " 
                if edge._label != None:
                    myStr = myStr + str(edge._label) + "\n"  
        myStr = myStr + "\n\n"              
        return myStr
