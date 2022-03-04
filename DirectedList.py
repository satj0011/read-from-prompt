# -*- coding: latin-1 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>.
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.

class MethodNotDefinedForThisPositionError(Exception):
    pass

"""
Datatypen Array enligt definitionen p� sidan 66 i Lars-Erik Janlert,
Torbj�rn Wiberg Datatyper och algoritmer 2., [rev.] uppl.,Lund,
Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7

Variabler och funktioner som inleds med ett enkelt underscore "_" �r privata
f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.

"""
from OneCell import OneCell

class DirectedList:

    def __init__(self):
        """
            Syfte: Skapar en tom riktad lista med en tom 1-Cell som "huvud" i listan.
            Returv�rde: -
            Kommentarer: I boken heter denna funktion Empty.
        """
        self._head= OneCell()

    def insert(self, position, obj):
        """
            Syfte: Stoppar in ett nytt element med v�rdet obj i listan f�re angiven position
            Parametrar: position - En position i listan
                        obj - v�rdet som ska in i listan
            Returv�rde: Positionen f�r det insatta elemenet
            Kommentarer: 
        """        
        tempCell = OneCell()
        tempCell.setValue(obj)
        tempCell.setLink(position.inspectLink())
        position.setLink(tempCell)
        return position

    def isempty(self):
        """
            Syfte: Returnerar sant om listan �r tom (saknar element)
            Parametrar: -
            Returv�rde: Sant om listan �r tom
            Kommentarer:
        """    
        return self._head.inspectLink() is None

    def inspect(self,position):
        """
            Syfte: Returnerar v�rdet som finns p� angiven position
            Parametrar: position - En position i listan
            Returv�rde: V�rdet som finns p� angiven position
            Kommentarer: Inte definierad f�r listans sista position
        """    
        if self.isEnd(position):
            raise MethodNotDefinedForThisPositionError("Error in inspect") 
        return position.inspectLink().inspectValue()

    def isEnd(self,position):
        """
            Syfte: Returnerar v�rdet true om den angivna positionen �r listans sista
            Parametrar: position - En position i listan
            Returv�rde: True om den givna positionen �r den sista i listan
            Kommentarer:
        """    
        return position.inspectLink() is None

    def first(self):
        """
            Syfte: Returnerar listans f�rsta position
            Parametrar: -
            Returv�rde: Listans f�rsta position
            Kommentarer:
        """    
        return self._head

    def next(self,position):
        """
            Syfte: Returnerar position efter den angivna positionen
            Parametrar: position - En position i listan
            Returv�rde: Positionen efter den angivna
            Kommentarer: Inte definierad f�r listans sista position
                        (som saknar element)
        """    
        if self.isEnd(position):
            raise MethodNotDefinedForThisPositionError("Error in next")       
        return position.inspectLink()

    def remove(self,position):
        """
            Syfte: Tar bort elementet p� den angivna positionen
            Parametrar: position - En position i listan
            Returv�rde: Positionen p� elementet direkt efter det som togs bort
            Kommentarer: �r inte definierad f�r listans sista position
                        (som saknar element)
        """    
        if self.isEnd(position):
            raise MethodNotDefinedForThisPositionError("Error in remove")        
        position.setLink(position.inspectLink().inspectLink())
        return position
