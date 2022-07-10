import csv
from Liste.List import List
from Liste.ListNode import List_Node
from Node import Node
from Output.Drawer import Drawer

class CSV_Drawer(Drawer):
    def _get_header(self,show_succesoors):
        #Gebe Kopfzeile von CSV-Datei zurück
        return ["Nr.","Nachfolger" if show_succesoors else "Vorgänger", "Bezeichnung","Dauer", "FAZ", "FEZ", "SAZ", "SEZ", "GP", "FP"]
    
    def __init__(self,nodes_dict,list:List):
        super().__init__(list)
        self._nodes_dict = nodes_dict
        
    def draw(self,output_file,delimiter=';',show_successors:bool=True):
        #Schreibe CSV-Datei
        header = self._get_header(show_successors)
        with open(output_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile,delimiter=delimiter)
            csv_writer.writerow(header)
            csv_writer.writerow(self.getCsvForNode(self._list.getFirst()[0]))
            if self._list.getFirst()[0].getNr() in self._nodes_dict.keys():
                del self._nodes_dict[self._list.getFirst()[0].getNr()]
            for node in self._nodes_dict.values():
                csv_writer.writerow(self.getCsvForNode(node,show_successors))
                
            if self._list.getLast()[0].getNr() not in self._nodes_dict.keys():
                csv_writer.writerow(self.getCsvForNode(self._list.getLast()[0],show_successors))
        print("CSV file was created.")
        
    
    def getCsvForNode(self,node:Node,show_successors:bool=True):
        if show_successors:
            neighbours = [x.getNr() for x in node.getNext()]
        else:
            neighbours = [x.getNr() for x in node.getPrevious()]
        neighbours = "-" if len(neighbours)==0 else ",".join(neighbours)
        csv = [node.getNr(),str(neighbours),node.getBezeichnung(),str(node.getDauer()),str(node.getFaz()),str(node.getFez()),str(node.getSaz()),str(node.getSez()),str(node.getGp()),str(node.getFp())]
        return csv