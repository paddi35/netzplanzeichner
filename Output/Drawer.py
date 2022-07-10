from Liste.List import List


class Drawer:
    def __init__(self,list:List):
        self._list = list
        self._drawed_node = []
        
        if len(self._list.getFirst()) > 1:
            raise Exception("Graph has multiple initial nodes")
        
        if len(self._list.getLast()) > 1:
            raise Exception("Graph has multiple final nodes")
    
    def draw(self,output_file:str)->None:
        pass