import csv
from typing import List
from Liste.List import List as NodeList
from Node import Node
from Output.Drawer import Drawer

class CSV_Drawer(Drawer):
    def _get_header(self,show_succesoors):
        #Gebe Kopfzeile von CSV-Datei zurück
        return ["Nr.","Nachfolger" if show_succesoors else "Vorgänger", "Bezeichnung","Dauer", "FAZ", "FEZ", "SAZ", "SEZ", "GP", "FP"]
    
    def __init__(self,list:NodeList):
        super().__init__(list)
        self._drawed = []
        
    def draw_node(self, nodes:List[Node],show_successors:bool):
        for node in nodes:
            if node.getNr() in self._drawed:
                continue
            self._csv_writer.writerow(self.getCsvForNode(node,show_successors))
            self._drawed.append(node.getNr())
            
        for node in nodes:
            self.draw_node(node.getNext(),show_successors)
            
    def draw(self,output_file,delimiter=';',show_successors:bool=True):
        #Schreibe CSV-Datei
        header = self._get_header(show_successors)
        with open(output_file, 'w', newline='') as csvfile:
            self._csv_writer = csv.writer(csvfile,delimiter=delimiter)
            self._csv_writer.writerow(header)
            self.draw_node(self._list.getFirst(),show_successors)                
        print("CSV file was created.")
        
    
    def getCsvForNode(self,node:Node,show_successors:bool=True):
        if show_successors:
            neighbours = [x.getNr() for x in node.getNext()]
        else:
            neighbours = [x.getNr() for x in node.getPrevious()]
        neighbours = "-" if len(neighbours)==0 else ",".join(neighbours)
        csv = [node.getNr(),str(neighbours),node.getBezeichnung(),str(node.getDauer()),str(node.getFaz()),str(node.getFez()),str(node.getSaz()),str(node.getSez()),str(node.getGp()),str(node.getFp())]
        return csv