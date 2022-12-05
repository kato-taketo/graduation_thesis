from PIL import Image,ImageFont,ImageDraw
import os

def add_catch_copy(image_path, catch_copy):
    '''
    Use the image path and catchphrase string as input to draw catchphrase on the image
    '''
    font_path = '/usr/share/fonts/truetype/Gargi/Gargi.ttf'
    font_size = 30 #文字の大きさ
    color = (255,255,255)#文字の色

    font = ImageFont.truetype(font_path,font_size)#フォントの指定
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    draw.text((50,100),catch_copy,font=font,fill=color)
    image.save(image_path)

 
