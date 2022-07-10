import sys
from CSV_Parser import CSV_Parser
from Liste.ListNode import List_Node
from Node import Node
from Liste.List import List
from Output.CSV_Drawer import CSV_Drawer
from Output.PNG_Drawer.PNG_Drawer import PNG_Drawer

input_file = sys.argv[1]
#input_file = "inputs/input_v.csv"
output_file = sys.argv[2]

draw_png = False
file_extension = output_file.split(".")[-1]

if file_extension == "png":
    draw_png = True
elif file_extension != "csv":
    print("Error: Unsupported file extension " + file_extension)
    exit()
    

#CSV-Datei einelsen
csv = CSV_Parser(input_file)

#Ermitteln, ob Nachfolger oder Vorgänger angegeben sind
use_successor = csv.header[1][0] == "N"

list = List()
nodes_dict = {}

#Objekte für Knoten erstellen
for row in csv.rows:
    if row[0] in nodes_dict.keys():
        print("Error: Duplicate Nr. " + row[0] + " in input file.")
        exit()
    nodes_dict.update({row[0]:Node(row[0],row[2],row[3])}) 

#Verknüpfen der zusammenhängenden Knoten / Aufbau der internen Repräsentation des Netzplans
for row in csv.rows:
    #Überspringen, falls kein Vorgänger oder Nachfolger angegeben ist
    if row[1]=="-" or row[1]=="0":
        continue
    affected_nodes = row[1].split(",")
    
    #Knoten mit Vorgänger oder Nachfolger verknüpfen
    for dummy in affected_nodes:
        node_key = dummy.strip()
        if use_successor: 
            nodes_dict[row[0]].addNext(nodes_dict[node_key])
            nodes_dict[node_key].addPrevious(nodes_dict[row[0]])
        else:
            nodes_dict[row[0]].addPrevious(nodes_dict[node_key])
            nodes_dict[node_key].addNext(nodes_dict[row[0]])

            
#Knoten in Liste hinzufügen, um Ersten und Letzen Knoten zu ermitteln
for row in csv.rows:
    list.addNode(nodes_dict[row[0]])

if len(list.getFirst()) > 1:
    dummy = Node.dummy("Start")
    for s in list.getFirst():
        dummy.addNext(s)
        s.addPrevious(dummy)
    list.addNode(dummy)

if len(list.getLast()) > 1:
    dummy = Node.dummy("Ende")
    for p in list.getLast():
        dummy.addPrevious(p)
        p.addNext(dummy)
    list.addNode(dummy)
    

try:
    if draw_png:
        png_drawer = PNG_Drawer(list)
        png_drawer.draw(output_file)
    else:   
        csv_drawer = CSV_Drawer(nodes_dict,list)
        csv_drawer.draw(output_file,show_successors=use_successor)
except RecursionError as e:
    print("Error: Graph is cyclic.")
    exit()
