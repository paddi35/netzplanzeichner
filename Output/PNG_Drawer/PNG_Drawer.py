from Output.PNG_Drawer.Canvas import Canvas
import cv2

from Output.Drawer import Drawer

class PNG_Drawer(Drawer):
    def __init__(self,list):
        super().__init__(list)
        self._canvas = Canvas()
        
    def _draw_nodes(self, nodes):
        for node in nodes:
            self._canvas.add_node(node)
            
        for node in nodes:
            self._draw_nodes(node.getNext())
        
        
        

    def draw(self, output_file: str="") -> None:
        first_elements = self._list.getFirst()
        self._draw_nodes(first_elements)
        self._canvas.create_image()
        self._canvas.draw_arrows()
        self._canvas.draw_nodes()
        image = self._canvas.getImage()
        cv2.imwrite(output_file,image)
        print("PNG file was created.")