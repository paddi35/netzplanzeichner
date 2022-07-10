from Liste.ListNode import List_Node


class List:
    def __init__(self):
        self._head = []
        self._tail = []
    
    def addNode(self,node:List_Node)->None:
        to_remove = []
        
        if not node.hasNext():
            for n in self._tail:
                
                if n.hasNext():
                    to_remove.append(n)
                    
            for n in to_remove:
                self._tail.remove(n)
                
            self._tail.append(node)
            
        if not node.hasPrevious():
            for n in self._head:
                if n.hasPrevious():
                    to_remove.append(n)
            
            for n in to_remove:
                self._head.remove(n)
                
            self._head.append(node)
        
            
    def getFirst(self)->List_Node:
        return self._head
    
    def getLast(self)->List_Node:
        return self._tail