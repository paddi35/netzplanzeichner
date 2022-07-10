from typing_extensions import Self

class List_Node:
    #Repräsenstation eines Knoten einer doppelt verketteten Liste
    
    def __init__(self):
        self._predeccessors = []
        self._successor = []
        
    def addNext(self, next)->None:
        #Fügt einen Nachfolgerknoten hinzu
        self._successor.append(next)
        
    def addPrevious(self, previous)->None:
        #Fügt einen Vorgängerknoten hinzu
        self._predeccessors.append(previous)
        
    def getNext(self):
        #Gibt alle Nachfolgerknoten zurück
        return self._successor
    
    def getPrevious(self):
        #Gibt alle Vorgängerknoten zurück
        return self._predeccessors
    
    def hasPrevious(self)->bool:
        return len(self._predeccessors) > 0
    
    def hasNext(self)->bool:
        return len(self._successor) > 0