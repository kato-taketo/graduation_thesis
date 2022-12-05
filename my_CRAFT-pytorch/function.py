from PIL import Image, ImageFont, ImageDraw
import os

def find_big_bbox(i,poly,big_bbox_index,width,height,loc):
    '''
    update w,h,index if bbox is greater than max
    '''
    x_min=10000000
    x_max=-1
    y_min=10000000
    y_max=-1
    y_ave=0

    for node in poly:
        x_min = min(x_min, node[0])
        x_max = max(x_max, node[0])
        y_min = min(y_min, node[1])
        y_max = max(y_max, node[1])
        y_ave += node[1]

    p_width = x_max - x_min
    p_height = y_max - y_min

    if p_width > width : 
        width = p_width
        height = p_height
        big_bbox_index = i
        loc = (x_max, y_ave/len(poly))

    return big_bbox_index, width ,height,loc

def add_catch_copy(image_path, catch_copy, loc, font_size):
    '''
    Display the catchphrase in the right place with the right size
    '''

    font_path = '/usr/share/fonts/truetype/Gargi/Gargi.ttf'
    #font_size = 30
    color = (255,255,255)

    font = ImageFont.truetype(font_path, font_size)
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    draw.text(loc, catch_copy, font=font, fill=color)
    image.save(image_path)

def find_font_size(catch_copy, width ,height):
    length = len(catch_copy)
    font_size = min(height, width/length)

    return int(font_size)
    