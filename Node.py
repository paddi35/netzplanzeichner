from inspect import classify_class_attrs
import string
from Liste.ListNode import List_Node


class Node(List_Node):
    #Repräsentation eines Netzplanknotens. Erbt von ListNode
    
    @classmethod
    def dummy(cls:"Node",bezeichnung:str):
        #Erstellt einen Dummy-Node
        node = cls("0",bezeichnung,"0")
        node._nr = bezeichnung[0]
        return node 
    
    def __init__(self,nr:str,bezeichnung:str,dauer:str):
        super().__init__()
        

        if not dauer.isdigit():
            print("Error: Value in field \"Dauer\" is no digit.")
            exit()
        
        self._nr = nr
        self._bezeichnung = bezeichnung
        self._dauer = int(dauer)
        self._faz = 0
        self._fez = 0
        self._saz = 0
        self._sez = 0
        self._gp = (False,0)
        self._fp = (False,0)
        
        if self._dauer < 0:
         print("Error: Invalid value in field \"Dauer\".")
         exit()
        
    def getFaz(self)->int:
        if self.hasPrevious() and self._faz==0:
            fezs = [x.getFez() for x in self.getPrevious()] 
            self._faz =  max(fezs)
        return self._faz
    
    def getFez(self)->int:
        if self._fez==0:
            self._fez = self.getFaz() + self._dauer
        return self._fez
    
    def getSaz(self)->int:
        if self._saz==0:
            self._saz = self.getSez() - self._dauer
        return self._saz
    
    def getSez(self)->int:
        if self._sez != 0:
            return self._sez
        
        if self.hasNext():
            sezs = [x.getSaz() for x in self.getNext()]
            self._sez = min(sezs)
        else:
            self._sez = self.getFez()
            
        return self._sez
        
    def getGp(self)->int:
        #Berechnung des GP
        if not self._gp[0]:
            self._gp = (True,self.getSaz() - self.getFaz())
        return self._gp[1]
    
    def getFp(self)->None:
        #Berechnung des FP
        if not self._fp[0]:
            if self.hasNext():
                fazs = [x.getFaz() for x in self.getNext()]
                self._fp = (True,min(fazs) - self.getFez())
            else:
                self._fp = (True,0)
        return self._fp[1]
    
    def getDauer(self)->int:
        return self._dauer
    
    def getNr(self)->string:
        return self._nr
    
    def getBezeichnung(self)->string:
        return self._bezeichnung


   
    


            
    
