import os
import cv2
import time

path = 'E:/Capstone Project/New Video For Journal/4_AddExtraPoints/ThresholdDyn/'
dirs = os.listdir( path )

height = 720
width = 1280

start = time.time()

for file in dirs:
        
    file = open(path + file,'a')
    
    line1 = 0
    line2 = 0
    file.write("%d %d\n" % (line1 , line2))

    line1 = width/2
    line2 = 0
    file.write("%d %d\n" % (line1 , line2))

    line1 = width-1
    line2 = 0
    file.write("%d %d\n" % (line1 , line2))

    line1 = width-1
    line2 = height/2
    file.write("%d %d\n" % (line1 , line2))

    line1 = width-1
    line2 = height-1
    file.write("%d %d\n" % (line1 , line2))
        
    line1 = width/2
    line2 = height-1
    file.write("%d %d\n" % (line1 , line2))

    line1 = 0
    line2 = height-1
    file.write("%d %d\n" % (line1 , line2))

    line1 = 0
    line2 = height/2
    file.write("%d %d\n" % (line1 , line2))
    
    file.close()

print ('Total Time Taken:' , time.time()-start)             
