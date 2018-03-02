#!/usr/bin/python

import cv2
import numpy as np
import random

if __name__ == '__main__':

    # Read in the image.
    img = cv2.imread("2.58.jpg");

    # Rectangle to be used with Subdiv2D
    size = img.shape
    rect = (0, 0, size[1], size[0])

    print(size[1])
    print(size[0])
    # Create an instance of Subdiv2D
    subdiv = cv2.Subdiv2D(rect);

    # Create an array of points.
    points = [];

    lineNo = 0 ;
    # Read in the points from a text file
    with open("avg_2.58_2.60.txt") as file :
        for line in file :
            x, y = line.split()
            points.append((int(x), int(y)))
            if(lineNo == 0):
                dictionary = {(int(x), int(y)) : lineNo}
            else:
                dictionary.update({(int(x), int(y)) : lineNo})
                
            lineNo = lineNo + 1
            
    # Insert points into subdiv
    for p in points :
        subdiv.insert(p)

    triangleList = subdiv.getTriangleList();

    file = open('DelaunayPoints_2.58.txt','w+')
    
    for t in triangleList :
        
        pt1 = (t[0], t[1])
        pt2 = (t[2], t[3])
        pt3 = (t[4], t[5])

        line1 = dictionary.get( ( int(t[0]) , int(t[1]) ) )
        line2 = dictionary.get( ( int(t[2]) , int(t[3]) ) )
        line3 = dictionary.get( ( int(t[4]) , int(t[5]) ) )

        if(line1 != None and line2 != None and line3 != None):
            file.write("%d %d %d\n" % (line1 , line2 , line3))
            print(line1 , line2 , line3)

    file.close()
