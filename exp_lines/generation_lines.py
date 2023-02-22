# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 13:52:18 2023

@author: Yoga
"""

import random
import func_three_lines as func
import os
import csv

from PIL import Image, ImageDraw, ImageFont
l_colors = ["blue","red","green"]
l_shapes = ["square","circle","triangle"]
random.seed(2023)


l_size = 300




l_cond = [["faux_1","faux_2","existentiel","unicite","universel"],["faux_1","faux_2","one","two","mixte"]]
l_set = ["set1","set2"]

def generer_images_and_sentences_set1_lines(nb_set, l_shapes, l_colors, l_size, nb, csv_writer, condition):
    """
    

    Parameters
    ----------
    nb_set : int
        1 for set 1, 2 for set 2
    l_shapes : list of str
        ["square","circle","triangle"]
    l_colors : list of str
        ["green","red","blue"]
    l_size : int
        resolution
    nb : int
        nb of images to generate for each condition
       
    file : str
        name of datafile where to write sentences, names of images, ect. This file as to be uploaded in pcibex
    condition : str
        condition name, i.e.
        for set 1:
        "faux_1","faux_2","existentiel","unicite","universel"
        for set 2:
        "faux_1","faux_2","one","two","mixte"

    Returns
    -------
    None.

    """
    global item
    L_size = int(l_size/7*10)
    size = (l_size,L_size)
    s=l_size/14
    c1,c2,c3 = func.coord_three_line(l_size,L_size) 
    
    for j in range(nb): 
        
        img = func.fond_three_lines(size,outline_wdt = 2)
        
        if nb_set == "set1":
            s,c = func.set1(condition,l_shapes,l_colors,l_size,img)
            text = "In every row either there isn't a "+s+" or it is "+c
        if nb_set == "set2":
            s1,s2,s3,c = func.set2(condition,l_shapes,l_colors,l_size,img)
            text = "In every row either there isn't a "+s1+" or the "+s2+" is "+c
        img.save(nb_set+"/"+condition+str(j)+"_"+nb_set+"test.png")
        item+=1

        csv_writer.writerow({
            "item"    : item,
            "text"    : text,
            "picture" : "{}_{}.png".format(condition + str(j), nb_set),
            "type"    : "{}_{}".format(nb_set, condition + str(j))
        })

file = "data.csv"
fields_csv = ["item", "text", "picture", "type"]

    
    
with open(file, 'w', encoding = 'UTF8') as f:
    csv_writer = csv.DictWriter(f, fieldnames = fields_csv)
    csv_writer.writeheader()

    item = 0
    for i in [0, 1]:
        nb_set=l_set[i]
        conditions = l_cond[i]
        
        for cond in conditions:
            generer_images_and_sentences_set1_lines(nb_set,l_shapes,l_colors,l_size,3, csv_writer,cond)