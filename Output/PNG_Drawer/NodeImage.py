import cv2
import Output.PNG_Drawer.Utils as Utils



class NodeImage:
    
    def __init__(self,start_point,width=240,font=cv2.FONT_HERSHEY_COMPLEX):
        self._font = font
        self._width_rectangle = width
        self._height_rectangle = int(self._width_rectangle*0.541666)
        self._start_point = start_point
        
        self._height_first_section = 0.17391*self._height_rectangle
        self._height_second_section = 0.3846*self._height_rectangle
        self._width_small_box = 0.25*self._width_rectangle
        self._width_middle_sized_box = 0.5*self._width_rectangle
        self._fontScale = int(width*0.05)
        
        self.vorgangsnummer = ""
        self.vorgangsname = ""
        self.dauer = ""
        self.gesamtpuffer = ""
        self.freier_puffer = ""
        self.faz = ""
        self.fez = ""
        self.saz = ""
        self.sez = ""
    
    def getWidth(self)->int:
        return self._width_rectangle
    
    def getHeight(self)->int:
        return self._height_rectangle
    
    def getTopLeftCorner(self):
        return self._start_point
    
    topLeftCorner = property(getTopLeftCorner)
    
    def getTopMiddle(self):
        return (int(self._start_point[0]+self._width_rectangle/2),self._start_point[1])

    topMiddle = property(getTopMiddle)
    
    def getTopRightCorner(self):
        return (self._start_point[0]+self._width_rectangle,self._start_point[1])
    
    topRightCorner = property(getTopRightCorner)
    
    def getMiddleLeft(self):
        return (self._start_point[0],self._start_point[1]+int(self.getHeight()/2))
    
    middleLeft = property(getMiddleLeft)
    
    def getBottomLeftCorner(self):
        return (self.topLeftCorner[0], self.topLeftCorner[1]+self.getHeight())
    
    bottomLeftCorner = property(getBottomLeftCorner)
    
    def getBottomMiddle(self):
        return (int(self.topLeftCorner[0]+self.getWidth()/2), self.topLeftCorner[1]+self.getHeight()) 
    
    bottomMiddle = property(getBottomMiddle)


    
    def getMiddleRight(self):
        return (self.topRightCorner[0],self.topRightCorner[1]+int(self.getHeight()/2))
        
    middleRight = property(getMiddleRight)
    
    def getBottomRightCorner(self):
        return (self.topRightCorner[0],self.topRightCorner[1]+self.getHeight())
    
    bottomRightCorner = property(getBottomRightCorner)

    def draw(self,image):
    
        # Green color in BGR
        color_black = (0, 255, 0)
        
        # Line thickness of 9 px
        thickness = 2
        
        # Using cv2.line() method
        # Draw a diagonal green line with thickness of 9 px
        #image = cv2.arrowedLine(img, start_point, end_point, color, thickness)

        
        # Window name in which image is displayed
        window_name = 'Image'

        
        # Ending coordinate, here (220, 220)
        # represents the bottom right corner of rectangle

        #Zeichne Rechteck

        end_point = (self._start_point[0]+self._width_rectangle, self._start_point[1]+self._height_rectangle)
        start_point_rectangle = self._start_point
        end_point_rectangle = end_point
        
        # Blue color in BGR
        color_black = (255, 0, 0)
        
        # Line thickness of 2 px
        thickness = 1

        # Using cv2.rectangle() method
        # Draw a rectangle with blue line borders of thickness of 2 px
        image = cv2.rectangle(image, self._start_point, end_point, (255,255,255), -1)
        image = cv2.rectangle(image, self._start_point, end_point, (0,0,0), thickness)

        #FAZ ausgeben
        org = (self._start_point[0],self._start_point[1]-int(self._fontScale))
        image = Utils.drawText(image,org,self.faz,size=self._fontScale)

        #FEZ ausgeben
        size = Utils.getTextSize(self.fez,size=self._fontScale)
        org = (end_point[0]-size[0],self._start_point[1]-int(self._fontScale))
        image = Utils.drawText(image,org,self.fez,size=self._fontScale)


        #Vorgansnummer ausgeben
        size = Utils.getTextSize(self.vorgangsnummer,size=self._fontScale)
        org = (int(self._start_point[0]+(self._width_rectangle-size[0])/2),int(self._start_point[1]+(self._height_first_section-size[1])/2)+1)
        image = Utils.drawText(image,org,self.vorgangsnummer,size=self._fontScale)

        #Zeichne horizontale  Linien


        self._start_point = (self._start_point[0], self._start_point[1]+int(self._height_first_section))
        
        # End coordinate, here (250, 250)
        # represents the bottom right corner of image
        end_point = (end_point[0], self._start_point[1])
        
        color_black = (0, 0, 0)
        thickness = 1
        
        # Using cv2.line() method
        # Draw a diagonal green line with thickness of 9 px
        image = cv2.line(image, self._start_point, end_point, color_black, thickness)
        
        text = Utils.getCuttedText(self.vorgangsname, self._width_rectangle,size=self._fontScale)
        size = Utils.getTextSize(text,size=self._fontScale)
        org = (int(self._start_point[0]+(self._width_rectangle-size[0])/2),int(self._start_point[1]+(self._height_second_section-size[1])/2)+1)
        image = Utils.drawText(image,org,text,size=self._fontScale)

        self._start_point = (self._start_point[0],self._start_point[1]+int(self._height_second_section))
        end_point = (end_point[0], self._start_point[1])

        image = cv2.line(image, self._start_point, end_point, color_black, thickness)

        #Zeichne vertikale Linien

        self._start_point = (self._start_point[0]+int(self._width_small_box),end_point[1])
        end_point = (self._start_point[0], end_point_rectangle[1])

        #Zeichne erste vertikale Linie
        image = cv2.line(image, self._start_point, end_point, color_black, thickness)


        #Dauer ausgeben

        size = Utils.getTextSize(self.dauer,size=self._fontScale)
        org = (int(start_point_rectangle[0]+(self._width_small_box-size[0])/2),int(self._start_point[1]+(self._height_second_section-size[1])/2)+1)
        image = Utils.drawText(image,org,self.dauer,size=self._fontScale)

        #Gesamtpuffer ausgeben

        size = Utils.getTextSize(self.gesamtpuffer,size=self._fontScale)
        org = (int(self._start_point[0]+(self._width_middle_sized_box-size[0])/2),int(self._start_point[1]+(self._height_second_section-size[1])/2)+1)
        image = Utils.drawText(image,org,self.gesamtpuffer,size=self._fontScale)

        #Zweite vertikale Linie zeichnen
        self._start_point = (end_point_rectangle[0]-int(0.25*self._width_rectangle),self._start_point[1])
        end_point = (self._start_point[0], end_point_rectangle[1])
        image = cv2.line(image, self._start_point, end_point, color_black, thickness)

        #Freien Puffer ausgeben

        size = Utils.getTextSize(self.freier_puffer,size=self._fontScale)
        org = (int(self._start_point[0]+(self._width_small_box-size[0])/2),int(self._start_point[1]+(self._height_second_section-size[1])/2)+1)
        image = Utils.drawText(image,org,self.freier_puffer,size=self._fontScale)

        #SAZ ausgeben
        size = Utils.getTextSize(self.saz,size=self._fontScale)
        org = (start_point_rectangle[0],end_point_rectangle[1]+int(self._fontScale/4))
        image = Utils.drawText(image,org,self.saz,size=self._fontScale)

        #SEZ ausgeben
        size = Utils.getTextSize(self.saz,size=self._fontScale)
        org = (end_point_rectangle[0]-size[0],end_point_rectangle[1]+int(self._fontScale/4))
        image = Utils.drawText(image,org,self.sez,size=self._fontScale)

        return image