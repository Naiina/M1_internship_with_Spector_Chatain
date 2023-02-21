# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:03:07 2023

@author: Yoga
"""

from PIL import Image, ImageDraw, ImageFont
import math as m
import random
import csv


def fond_three_lines(size,outline_wdt):
    """
    

    Parameters
    ----------
    size : int
        resolution
    outline_wdt : int
        nb pixels of outline around boxes

    Returns
    -------
    img : image
        image with boxes in white grey and black.

    """
    l_size,L_size = size
    img = Image.new("RGB", (L_size, l_size), (128, 128, 128))
    coord1, coord2, coord3 = coord_three_line(l_size,L_size)
    draw = ImageDraw.Draw(img)
    draw.rectangle(coord1, fill ="white", outline ="black", width = outline_wdt)
    draw.rectangle(coord2, fill ="white", outline ="black", width = outline_wdt)
    draw.rectangle(coord3, fill ="white", outline ="black", width = outline_wdt)
    
    return img

def coord_three_line(l_size,L_size):
    """
    

    Parameters
    ----------
    l_size : TYPE
        DESCRIPTION.
    L_size : TYPE
        DESCRIPTION.

    Returns
    -------
    c1 : l of int
        coord of line 1 (4 angles of the box)
    c2 : l of int
        coord of line 2
    c3 : l of int
        coord of line 3

    """
    margin = l_size/7
    end_line = L_size-margin
    c1 = [margin,margin,end_line,2*margin] 
    c2 = [margin,margin*3,end_line,4*margin] 
    c3 = [margin,margin*5,end_line,6*margin] 
    return c1,c2,c3


class objet:
    
    def __init__(self,shape,color,coord,to_plot):
        self.shape = shape
        self.color = color
        self.coord = coord
        self.to_plot = to_plot #bool
    def disp(self):
        print(self.color,self.shape,self.coord,self.to_plot)
        
        
def plot_shape(shape,coord,color,size,draw):
    if shape == "triangle":
        triangle(coord,color,size,draw)
    if shape == "circle":
        cercle(coord,color,size,draw)
    if shape == "square":
        square(coord,color,size,draw)
        
      
def triangle(coord,color,size,draw):
    """
    draw the shape on the object draw

    Parameters
    ----------
    coord : couple of int:
        top left corner of where to plot the shape
        
    color : str
        DESCRIPTION.
    size : int
        size of the shape.
    draw : image object
        

    Returns
    -------
    None.

    """
    x = coord[0]
    y = coord[1]
    draw.polygon(((x, y+size), (x+size, y+size), (x+size//2,y)), fill=color, outline=color)
    
def cercle(coord,color,size,draw):
    """
    draw the shape on the object draw

    Parameters
    ----------
    coord : couple of int:
        top left corner of where to plot the shape
        
    color : str
        DESCRIPTION.
    size : int
        size of the shape.
    draw : image object
        

    Returns
    -------
    None.

    """
    x1,y1= coord
    x2 = x1 + size
    y2 = y1 + size
    draw.ellipse((x1,y1,x2,y2), fill=color, outline=color)
    
def square(coord,color,size,draw):
    """
    draw the shape on the object draw

    Parameters
    ----------
    coord : couple of int:
        top left corner of where to plot the shape
        
    color : str
        DESCRIPTION.
    size : int
        size of the shape.
    draw : image object
        

    Returns
    -------
    None.

    """
    x1,y1= coord
    x2 = x1 + size
    y2 = y1 + size
    draw.rectangle((x1,y1,x2,y2), fill=color, outline=color)
    
def l_coord_of_shape(l_size):
    """
    creates the 6*3 objects (6 objects and 3 lines)
    The obects contain the position where they must be plotted and the corresponding shape. 
    The real color and whether they will be plotted or not will be decided later
    For now they are all "black" and to_plot is set as False
    
    Parameters
    ----------
    l_size : int
        resolution

    Returns
    -------
    list
        list of lists
        The i_th sub list contains the objects of the line i

    """
    margin = l_size/7
    mm = margin/5
    l_tri = []
    l_squ = []
    l_cir = []
    
    
    for i in range(3):
        for j in range(2):
            x1 = margin*4+mm +j*(margin-mm)
            y1 = margin*(1+2*i)+mm 
            o = objet("triangle",'black',(x1,y1),False)
            l_tri.append(o)
     
    for i in range(3):
        for j in range(2):
            x1 = margin+mm +j*(margin-mm) + margin/2
            y1 = margin*(1+2*i)+mm 
            o = objet("square",'black',(x1,y1),False)
            l_squ.append(o)
            
    for i in range(3):
        for j in range(2):
            x1 = margin*6.5+mm +j*(margin-mm)
            y1 = margin*(1+2*i)+mm 
            o = objet("circle",'black',(x1,y1),False)
            l_cir.append(o)
    l1 = ligne(l_tri[:2],l_cir[:2],l_squ[:2])
    l2 = ligne(l_tri[2:4],l_cir[2:4],l_squ[2:4])
    l3 = ligne(l_tri[4:],l_cir[4:],l_squ[4:])
    return [l1,l2,l3]
    
    
def plot_all_shapes(l_o,l_size,draw):
    s = l_size/14
    for elem in l_o:
        if elem.to_plot: 
            plot_shape(elem.shape,elem.coord,elem.color,s,draw)
    

class ligne:
    """
    contains the list of objects of each shape of this line
    """
    def __init__(self,l_tri,l_squ,l_cir):
        self.tri = l_tri
        self.cir= l_cir
        self.squ = l_squ
    

def line_setup_with_list_4_obj(l_o_to_plot,l):
    """
    The empty object l (Line) is filled according to l_o_to_plot, the list of objects to plot in this line      
    
    Parameters
    ----------
    l_o_to_plot : list of objects to be plotted in line l
        DESCRIPTION.
    l : Line object
        

    Returns
    -------
    l : Line object updated 
        DESCRIPTION.

    """

    t = 0
    cc = 0
    ss = 0
    
    for elem in l_o_to_plot:
        shape = elem[0]
        if shape == "triangle":
            
            l.tri[t].shape = elem[0] 
            l.tri[t].color = elem[1]
            l.tri[t].to_plot = True
            t +=1
        if shape == "circle":
            l.cir[cc].shape = elem[0] 
            l.cir[cc].color = elem[1]
            l.cir[cc].to_plot = True
            cc += 1
        if shape == "square":
            l.squ[ss].shape = elem[0] 
            l.squ[ss].color = elem[1]
            l.squ[ss].to_plot = True
            ss += 1
    
    return l

def generer_objects_set1_existentiel(shape,color,l_shapes,l_colors):
    """
    given a shape S and a color C, retuen the set of objects to plot in order to obtain 
    a line corresponding to an exostential condition with a sentence of type:
        Either there isn't a S or it is C

    Parameters
    ----------
    shape : TYPE
        DESCRIPTION.
    color : TYPE
        DESCRIPTION.
    l_shapes : TYPE
        DESCRIPTION.
    l_colors : TYPE
        DESCRIPTION.

    Returns
    -------
    l_o_to_plot: list of 4 objects to plot 

    """
    l_o_to_plot=[]
    random.shuffle(l_colors)
    random.shuffle(l_shapes)
    color2 = l_colors[0]
    if color2==color:
        color2 = l_colors[1]
    o1 = (shape,color)
    l_o_to_plot.append(o1)
    o2 = (shape,color2)
    l_o_to_plot.append(o2)
    for i in range(2):
        random.shuffle(l_colors)
        c = l_colors[0]
        random.shuffle(l_shapes)
        s = l_shapes[0]
        if s == shape:
            s = l_shapes[1]
        o = (s,c)
        l_o_to_plot.append(o)
    random.shuffle(l_o_to_plot)
    return(l_o_to_plot)

def generer_objects_set2_two(shape1,shape2,shape3,color,l_shapes,l_colors):
    #two shapes 1 random color
    #one shape 2 color "color"
    #one shape 3 random color
    l_o_to_plot=[]
    random.shuffle(l_colors)
    color2 = l_colors[0]
    random.shuffle(l_colors)
    color1 = l_colors[0]
    o1 = (shape1,color1)
    l_o_to_plot.append(o1)
    o2 = (shape1,color2)
    l_o_to_plot.append(o2)
    
    random.shuffle(l_colors)
    c = l_colors[0]
    o = (shape3,c)
    l_o_to_plot.append(o)
    

    o = (shape2,color)
    l_o_to_plot.append(o)

    return(l_o_to_plot)

def generer_objects_set1_universel(shape,color,l_shapes,l_colors):
    l_o_to_plot=[]
    random.shuffle(l_colors)
    random.shuffle(l_shapes)
    l_o_to_plot.append((shape,color))
    l_o_to_plot.append((shape,color))
    for i in range(2):
        random.shuffle(l_colors)
        c = l_colors[0]
        random.shuffle(l_shapes)
        s = l_shapes[0]
        if s == shape:
            s = l_shapes[1]
        o = (s,c)
        l_o_to_plot.append(o)
    random.shuffle(l_o_to_plot)
    return(l_o_to_plot)

def generer_objects_set1_no_shape(shape,color,l_shapes,l_colors):
    l_o_to_plot=[]
    for s in l_shapes:
        if s != shape:
            for i in range(2):
                random.shuffle(l_colors)
                c = l_colors[0]
                o = (s,c)
                l_o_to_plot.append(o)
    random.shuffle(l_o_to_plot)
    return(l_o_to_plot)

def generer_objects_set2_no_shape(shape1,shape2,shape3,color,l_shapes,l_colors):
    #no triangle, circle random color
    l_o_to_plot=[]
    
    random.shuffle(l_colors)
    c = l_colors[0]
    if c == color:
       c = l_colors[1] 
    o = (shape2,c)
    l_o_to_plot.append(o)
    
    for i in range(2):
        random.shuffle(l_colors)
        c = l_colors[0]
        o = (shape3,c)
        l_o_to_plot.append(o)
    random.shuffle(l_o_to_plot)
    return(l_o_to_plot)

def generer_objects_set1_unicite(shape,color,l_shapes,l_colors):
    l_o_to_plot=[]
    l = []
    random.shuffle(l_colors)
    random.shuffle(l_shapes)

    o = (shape,color)
    l_o_to_plot.append(o)
    
    random.shuffle(l_shapes)
    for elem in l_shapes:
        if elem != shape:
            l.append(elem)
    for i in range(2):
        random.shuffle(l_colors)
        c = l_colors[0]
        o = (l[0],c)
        l_o_to_plot.append(o)
    random.shuffle(l_colors)
    c = l_colors[0]
    o = (l[1],c)
    random.shuffle(l_o_to_plot)
    return(l_o_to_plot)

def generer_objects_set2_one(shape1,shape2,shape3,color,l_shapes,l_colors):
    #one shape1 random color
    #one shape2 color color
    #two shape3 random color
    l_o_to_plot=[]
    random.shuffle(l_colors)
    random.shuffle(l_shapes)

    o = (shape2,color)
    l_o_to_plot.append(o)
    c = l_colors[0]
    o = (shape1,c)
    l_o_to_plot.append(o)
    
    
    for i in range(2):
        random.shuffle(l_colors)
        c = l_colors[0]
        o = (shape3,c)
        l_o_to_plot.append(o)

    random.shuffle(l_o_to_plot)
    return(l_o_to_plot)

def generer_objects_set1_faux(shape,color,l_shapes,l_colors):
    l_o_to_plot=[]
    l = []
    random.shuffle(l_colors)
    random.shuffle(l_shapes)
    color_w = l_colors[0]
    if color_w == color:
        color_w = l_colors[1]
    o = (shape,color_w)
    l_o_to_plot.append(o)
    
    random.shuffle(l_shapes)
    for elem in l_shapes:
        if elem != shape:
            l.append(elem)
    for i in range(2):
        random.shuffle(l_colors)
        c = l_colors[0]
        o = (l[0],c)
        l_o_to_plot.append(o)
    random.shuffle(l_colors)
    c = l_colors[0]
    o = (l[1],c)
    random.shuffle(l_o_to_plot)
    return(l_o_to_plot)

def generer_objects_set2_faux(shape1,shape2,shape3,color,l_shapes,l_colors):
    
    n = random.randint(1, 2)
    #un triangle et cercle mauvaise couleur
    l_o_to_plot=[]
    random.shuffle(l_colors)
    random.shuffle(l_shapes)
    #shape2 wrong color
    color_w = l_colors[0]
    if color_w == color:
        color_w = l_colors[1]
    o = (shape2,color_w)
    l_o_to_plot.append(o)
    
    #n elem of shape 3, random color 
    for i in range(n):
        random.shuffle(l_colors)
        c = l_colors[0]
        o = (shape3,c)
        l_o_to_plot.append(o)
        
    #shape 1, random color    
    random.shuffle(l_colors)
    c = l_colors[0]
    o = (shape1,c)
    l_o_to_plot.append(o)
    random.shuffle(l_o_to_plot)
    return(l_o_to_plot)



def set1(condition,l_shapes,l_colors,l_size,img):
    """
    plots a image of the condition "condition" of type "Either there isn't a S or it is C"
    return S and C the corresponding shape and color

    Parameters
    ----------
    condition : str
        among "unicite", "universel", "existentiel", "faux_2","faux_1"
    l_shapes : TYPE
        DESCRIPTION.
    l_colors : TYPE
        DESCRIPTION.
    l_size : int
        resolution
    img : darw object
        image without shapes, only whither grey and black drawing of boxes

    Returns
    -------
    shape : str
        
    color : str
        DESCRIPTION.

    """
    draw = ImageDraw.Draw(img)
    random.shuffle(l_colors)
    random.shuffle(l_shapes)
    shape = l_shapes[0]
    color = l_colors[0]
    l = l_coord_of_shape(l_size) #l[i] : ligne i
    random.shuffle(l)
    l1 = l[0]
    l2 = l[1]
    l3 = l[2]
    
    l_o_to_plot = generer_objects_set1_no_shape(shape,color,l_shapes,l_colors)
    ll1 = line_setup_with_list_4_obj(l_o_to_plot,l1)
    plot_l_shapes(ll1,l_size,draw)
    
    if condition == "unicite":
        l_o_to_plot = generer_objects_set1_unicite(shape,color,l_shapes,l_colors)
    if condition == "universel":
        l_o_to_plot = generer_objects_set1_universel(shape,color,l_shapes,l_colors)
    if condition == "existentiel":
        l_o_to_plot = generer_objects_set1_existentiel(shape,color,l_shapes,l_colors)
    if condition == "faux_2":
        l_o_to_plot = generer_objects_set1_faux(shape,color,l_shapes,l_colors)
    if condition == "faux_1":
        l_o_to_plot = generer_objects_set1_unicite(shape,color,l_shapes,l_colors)
    ll2 = line_setup_with_list_4_obj(l_o_to_plot,l2)
    plot_l_shapes(ll2,l_size,draw)
    
    if condition == "unicite":
        l_o_to_plot = generer_objects_set1_unicite(shape,color,l_shapes,l_colors)
    if condition == "universel":
        l_o_to_plot = generer_objects_set1_universel(shape,color,l_shapes,l_colors)
    if condition == "existentiel":
        l_o_to_plot = generer_objects_set1_existentiel(shape,color,l_shapes,l_colors)
    if condition == "faux_2":
        l_o_to_plot = generer_objects_set1_faux(shape,color,l_shapes,l_colors)
    if condition == "faux_1":
        l_o_to_plot = generer_objects_set1_faux(shape,color,l_shapes,l_colors)
    ll3 = line_setup_with_list_4_obj(l_o_to_plot,l3)
    plot_l_shapes(ll3,l_size,draw)
    
    return shape,color

def universel(l_shapes,l_colors,l_size,img):
    draw = ImageDraw.Draw(img)
    random.shuffle(l_colors)
    random.shuffle(l_shapes)
    shape = l_shapes[0]
    color = l_colors[0]
    l = l_coord_of_shape(l_size) #l[i] : ligne i
    random.shuffle(l)
    l1 = l[0]
    l2 = l[1]
    l3 = l[2]
    
    l_o_to_plot = generer_objects_set1_no_shape(shape,color,l_shapes,l_colors)
    ll1 = line_setup_with_list_4_obj(l_o_to_plot,l1)
    plot_l_shapes(ll1,l_size,draw)
    
    l_o_to_plot = generer_objects_set1_universel(shape,color,l_shapes,l_colors)
    ll2 = line_setup_with_list_4_obj(l_o_to_plot,l2)
    plot_l_shapes(ll2,l_size,draw)
    
    l_o_to_plot = generer_objects_set1_universel(shape,color,l_shapes,l_colors)
    ll3 = line_setup_with_list_4_obj(l_o_to_plot,l3)
    plot_l_shapes(ll3,l_size,draw)
    return shape,color

def plot_l_shapes(l,l_size,draw):
    """
    

    Parameters
    ----------
    l : Line object
        DESCRIPTION.
    l_size : int
        resolution
    draw : draw obj
        seulement fond

    Returns
    -------
    None.

    """
    s = l_size/14
    l_o = []
    l_tri = l.tri
    for elem in l_tri:
        l_o.append(elem)
    l_cir = l.cir
    for elem in l_cir:
        l_o.append(elem)
    l_squ = l.squ
    for elem in l_squ:
        l_o.append(elem)
    for elem in l_o:
        if elem.to_plot: 
            plot_shape(elem.shape,elem.coord,elem.color,s,draw)
            
            
            
def set2(condition,l_shapes,l_colors,l_size,img):
    draw = ImageDraw.Draw(img)
    random.shuffle(l_colors)
    random.shuffle(l_shapes)
    shape1 = l_shapes[0]
    shape2 = l_shapes[1]
    shape3 = l_shapes[2]
    color = l_colors[0]
    l = l_coord_of_shape(l_size) #l[i] : ligne i
    random.shuffle(l)
    l1 = l[0]
    l2 = l[1]
    l3 = l[2]
    
    l_o_to_plot = generer_objects_set2_no_shape(shape1,shape2,shape3,color,l_shapes,l_colors)
    ll1 = line_setup_with_list_4_obj(l_o_to_plot,l1)
    plot_l_shapes(ll1,l_size,draw)
    
    if condition == "one":
        l_o_to_plot1 = generer_objects_set2_one(shape1,shape2,shape3,color,l_shapes,l_colors)
        l_o_to_plot2 = generer_objects_set2_one(shape1,shape2,shape3,color,l_shapes,l_colors)
    if condition == "two":
        l_o_to_plot1 = generer_objects_set2_two(shape1,shape2,shape3,color,l_shapes,l_colors)
        l_o_to_plot2 = generer_objects_set2_two(shape1,shape2,shape3,color,l_shapes,l_colors)
    if condition == "mixte":
        l_o_to_plot1 = generer_objects_set2_two(shape1,shape2,shape3,color,l_shapes,l_colors)
        l_o_to_plot2 = generer_objects_set2_one(shape1,shape2,shape3,color,l_shapes,l_colors)
    if condition == "faux_2":
        l_o_to_plot1 = generer_objects_set2_faux(shape1,shape2,shape3,color,l_shapes,l_colors)
        l_o_to_plot2 = generer_objects_set2_faux(shape1,shape2,shape3,color,l_shapes,l_colors)
    if condition == "faux_1":
        l_o_to_plot1 = generer_objects_set2_no_shape(shape1,shape2,shape3,color,l_shapes,l_colors)
        l_o_to_plot2 = generer_objects_set2_faux(shape1,shape2,shape3,color,l_shapes,l_colors)
    ll2 = line_setup_with_list_4_obj(l_o_to_plot1,l2)
    plot_l_shapes(ll2,l_size,draw)
    ll3 = line_setup_with_list_4_obj(l_o_to_plot2,l3)
    plot_l_shapes(ll3,l_size,draw)
    
    return shape1,shape2,shape3,color