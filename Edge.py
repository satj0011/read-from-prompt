# -*- coding: latin-1 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>.
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.   
"""
    Datatypen Edge som �r en kant i en graf och definieras som de tv� 
    noder som �r �ndpunkter i kanten.
"""
class Edge:
    def __init__(self, v1, v2):
        """
            Syfte: Skapar en kant mellan v1 och v2
            Pararmetrar: v1 - nod 1
                         v2 - nod 2
            Returv�rde: 
            Kommentarer: En tom graf
        """          
        self._v1 = v1
        self._v2 = v2
    
    def getVertices(self):
        """
            Syfte: Returnerar noderna som definierar kanten
            Pararmetrar: 
            Returv�rde: Noderna som definierar kanten
            Kommentarer: 
        """          
        return (self._v1, self._v2)
    
