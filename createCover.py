# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image as pilImg
import os
from pathlib import Path
from wand.color import Color
from wand.image import Image

cover_text = pilImg.open('C:/Users/mkrdi/Pictures/Iterative_Graphic_Design/coverText.png')



with os.scandir('C:/Users/mkrdi/Pictures/Iterative_Graphic_Design/pencils') as entries:
    for entry in entries:
        print(entry.name)
        color, image_format = entry.name.split('.')
       
       
        if image_format == 'png' :
            print (image_format)
            with Image(width = 328, height = 499, background = '#%s' % color) as img:
                img.save(filename ='%s.png' % color)
                background = pilImg.open('%s.png' % color)
                pencil=pilImg.open('C:/Users/mkrdi/Pictures/Iterative_Graphic_Design/pencils/%s.png' % color)
                pencil = pencil.rotate(90, resample=0, expand=True, center=None, translate=None, fillcolor=None)
                #pencil = pencil.rotate(90)
                dst = pilImg.new('RGBA', (328, 499))
                dst.paste(background, (0,0))
                dst.paste(pencil, (72,220), pencil)
                dst.paste(cover_text, (0,0), cover_text)
                
                dst.save('%s.png' % color)
                
            
     


