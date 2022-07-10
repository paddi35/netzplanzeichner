from cv2 import add
from Output.PNG_Drawer.NodeImage import NodeImage
import cv2
import numpy as np
from Node import Node
from Output.PNG_Drawer.ArrowImage import ArrowImage

class Canvas:
    def __init__(self,width_recangle=200,space=60):
        self._space = space
        self._width = space
        self._height = space
        self._start_pos = (space,space)
        self._nodes = {}
        self._arrows = []
        self._image = []
    
    def isPosProven(self, pos)->bool:
        for node in self._nodes.values():
            top_left = node.topLeftCorner
            bottom_right = node.bottomRightCorner
            
            if top_left[0] <= pos[0] <= bottom_right[0] and top_left[1] <= pos[1] <= bottom_right[1]:
                return node
        
        return False
        
        
    def create_image(self):
        width = max([x.bottomRightCorner[0] for x in self._nodes.values()]) + self._space
        height = max([x.bottomRightCorner[1] for x in self._nodes.values()]) + self._space
        self._image = np.zeros((height,width,3),np.uint8)
        self._image[:,:] = (255,255,255)
    
    def draw_arrows(self):
        for arrow in self._arrows:
            ArrowImage(self._image,self._nodes[arrow[0]],self._nodes[arrow[1]]).draw()
    
    def draw_nodes(self):
        for node in self._nodes.values():
            self._image = node.draw(self._image)
            
    def getImage(self):
        return self._image
    
    def add_node(self,node:Node):
        if node.getNr() not in self._nodes:
            if len(node.getPrevious()) == 0:
                pos = self._start_pos
            else:
                pos = (0,0)
                positions = 0
                for n in node.getPrevious():
                    self._arrows.append((n.getNr(),node.getNr()))
                    if n.getNr() not in self._nodes:
                        continue
                    topRight = self._nodes[n.getNr()].topRightCorner
                    pos = (topRight[0],pos[1] + topRight[1])
                    positions = positions + 1
                    
                
                pos = (pos[0] + self._space, int(pos[1] / positions))
                
            pos_proven = self.isPosProven(pos)
            while pos_proven:
                bottom_left = pos_proven.bottomLeftCorner
                pos = (bottom_left[0], bottom_left[1] + self._space)
                pos_proven = self.isPosProven(pos)
                
                    
                    
            
            node_image = NodeImage(pos)
            node_image.dauer = str(node.getDauer())
            node_image.faz = str(node.getFaz())
            node_image.fez = str(node.getFez())
            node_image.freier_puffer = str(node.getFp())
            node_image.gesamtpuffer = str(node.getGp())
            node_image.saz = str(node.getSaz())
            node_image.sez = str(node.getSez())
            node_image.vorgangsname = node.getBezeichnung()
            node_image.vorgangsnummer = node.getNr()     
            self._nodes.update({node.getNr() : node_image})
            
                
            

            
    
            