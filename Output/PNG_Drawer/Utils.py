import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def getCuttedText(text,maxwidth=-1,font="Calibri",size=12) -> str:
    if maxwidth != -1:
        while getTextSize(text,font,size)[0] > maxwidth:
            text = text[0:len(text)-1]
    return text

def drawText(image,pos,text,color=(0,0,0),font="Calibri",size=12):
    font = ImageFont.truetype("Output/Fonts/" + font + ".ttf",size)
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    draw.text(pos,text,color,font)
    return np.array(img_pil)


def getTextSize(text,font="Calibri",size=12):
    font = ImageFont.truetype("Output/Fonts/" + font + ".ttf",size)
    return font.getsize(text)