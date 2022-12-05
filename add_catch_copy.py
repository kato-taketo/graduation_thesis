from PIL import Image,ImageFont,ImageDraw
import os

def add_catch_copy(image_path, catch_copy, loc_catch_copy):
    '''
    Use the image path and catchphrase string as input to draw catchphrase on the image
    '''
    font_path = '/usr/share/fonts/truetype/Gargi/Gargi.ttf'
    font_size = 30 #文字の大きさ
    color = (255,255,255)#文字の色
    
    loc = find_loc_catch_copy(loc_catch_copy)
    font = ImageFont.truetype(font_path,font_size)#フォントの指定
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    draw.text(loc,catch_copy,font=font,fill=color)
    image.save(image_path)

def find_loc_catch_copy(loc_catch_copy):
    locs_str = ["Top_Left", "Top", "Top_Right", "Center_Left", "Center", "Center_Right", "Bottom_Left", "Bottom", "Bottom_Right"]
    locs = [(10,10),(140,10),(275,10),
            (10,140),(140,140),(275,140),
            (10,275),(140,275),(275,275) ]
    for i in range(len(locs_str)):
        if loc_catch_copy == locs_str[i]:
            loc = locs[i]

    return loc


 
