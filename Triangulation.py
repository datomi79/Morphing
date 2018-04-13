#!/usr/bin/python

import cv2
import numpy as np
import random
import os, sys
import time

if __name__ == '__main__':
    
    path_for_average = 'E:/Capstone Project/New Video For Journal/5_FileAvg/ThresholdDyn/'
    path_for_images = 'E:/Capstone Project/New Video For Journal/2_DecodedImages/ThresholdDyn/'
    path_for_new_file = 'E:/Capstone Project/New Video For Journal/6_Triangulation/ThresholdDyn/'
    
    dirs = os.listdir( path_for_average )

    start = time.time()
    
    for file in dirs:
        lastname = os.path.splitext(file.split('_')[6])
        imagename = file.split('_')[1]  + '_' + file.split('_')[2] + '_' + file.split('_')[3]
        afterimagename = file.split('_')[4]  + '_' + file.split('_')[5] + '_' + lastname[0] #lastname[0]

        '''lastname = os.path.splitext(file.split('_')[2])
        imagename = file.split('_')[1]
        afterimagename = lastname[0]'''
        
        #print(imagename)
        #print(afterimagename)
        
        # Read in the image.
        img = cv2.imread(path_for_images + imagename + '.png');

        # Rectangle to be used with Subdiv2D
        size = img.shape
        rect = (0, 0, size[1], size[0])
        
        # Create an instance of Subdiv2D
        subdiv = cv2.Subdiv2D(rect);

        # Create an array of points.
        points = [];

        lineNo = 0 ;
        # Read in the points from a text file
        with open(path_for_average + file) as file :
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

        file = open(path_for_new_file + 'DP_' + imagename + '_' + afterimagename + '.txt','w+')
        
        for t in triangleList :
            
            pt1 = (t[0], t[1])
            pt2 = (t[2], t[3])
            pt3 = (t[4], t[5])

            line1 = dictionary.get( ( int(t[0]) , int(t[1]) ) )
            line2 = dictionary.get( ( int(t[2]) , int(t[3]) ) )
            line3 = dictionary.get( ( int(t[4]) , int(t[5]) ) )

            if(line1 != None and line2 != None and line3 != None):
                file.write("%d %d %d\n" % (line1 , line2 , line3))
                #print(line1 , line2 , line3)

        file.close()

    print ('Total Time Taken:' , time.time()-start)   
