from Output.PNG_Drawer.NodeImage import NodeImage
import cv2
import numpy as np
class ArrowImage:
    def __init__(self,image, start:NodeImage,destination:NodeImage):
        self._start = start
        self._destination = destination
        self._image = image
    
    def draw(self,tip_pixel=10):
        if self._start.topLeftCorner[0] < self._destination.topLeftCorner[0]:
            start_point = self._start.middleRight  
        else:
            start_point = self._start.middleLeft
        if abs(self._start.topRightCorner[1]-self._destination.topRightCorner[1]) <= self._start.getHeight():
            destination_point = self._destination.middleLeft
        elif self._start.topLeftCorner[1] > self._destination.topLeftCorner[1]:
            destination_point = self._destination.bottomMiddle
        elif self._start.topLeftCorner[1] < self._destination.topLeftCorner[1]:
            destination_point = self._destination.topMiddle                  
        

        length = np.sqrt(pow(destination_point[0]-start_point[0],2) + pow(destination_point[1]-start_point[1],2))
        tipLength = tip_pixel / length
        self._image = cv2.arrowedLine(self._image,start_point,destination_point,(0,0,0),1,tipLength=tipLength)