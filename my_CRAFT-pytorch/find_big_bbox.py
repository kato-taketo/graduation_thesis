import numpy as np
import cv2

def find_big_bbox(i,poly,big_bbox_index,width,height):
    '''
    update w,h,index if bbox is greater than max
    '''
    x_min=10000000
    x_max=-1
    y_min=10000000
    y_max=-1

    for node in poly:
        x_min = min(x_min, node[0])
        x_max = max(x_max, node[0])
        y_min = min(y_min, node[1])
        y_max = max(y_max, node[1])

    p_width = x_max - x_min
    p_height = y_max - y_min

    if p_width > width : 
        width = p_width
        height = p_height
        big_bbox_index = i

    return big_bbox_index, width ,height
