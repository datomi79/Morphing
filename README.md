# Morphing

## Facial Feature Detection:

  1. git clone https://github.com/spmallick/dlib
  2. cd dlib/examples
  3. mkdir build
  4. cd build
  5. cmake .. 
  6. cmake --build . --config Release

  Download the file from https://github.com/spmallick/dlib and extract it. <br/> <br/>
  Update your _face_landmark_detection_to_file.cpp_ with the one mentioned above. <br/> <br/>
  Desktop$ cd JournalNewVideos/ <br/>
  Desktop/JournalNewVideos$ cd dlib-master/examples/ <br/>
  Desktop/JournalNewVideos/dlib-master/examples$ mkdir build <br/>
  Desktop/JournalNewVideos/dlib-master/examples$ cd build <br/>
  Desktop/JournalNewVideos/dlib-master/examples/build$ cmake .. <br/>
  Desktop/JournalNewVideos/dlib-master/examples/build$ cmake --build . --config Release <br/>

  Download file from "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2" and save it on desktop. Extract this file and save the extracted file "http://dlib.net/files/shape_predictor_68_face_landmarks.dat." in Desktop/JournalNewVideos/dlib-master/examples/build <br/>

  Now put the folder containing images in Desktop/JournalNewVideos/dlib-master/examples/build/YourFolder <br/>

  Run the following command : <br/>
  Desktop/Journal/dlib-master/examples/build$ ./face_landmark_detection_to_file shape_predictor_68_face_landmarks.dat ThresholdDynamic/*.png

## Add Extra Points:
  
  DLib gives 68 facial points as output. We need to add 8 extra points of image boundary. Run _AddExtraPoints.py_ for this.
  
## Average of File:
  We want to calculate a morphed image between _img1_ and _img2_, then obatin the average of facial points of _img1.txt_ and _img2.txt_. Use file _AverageFileContentNew.java_ for this.
  
## Triangulation:
  We obtain delaunay triangles using file _Triangulation.py_.

## Morphing:
  Last step is to obtain morphed frames, use file _FaceMorph.py_ for this.
  
## Reference :
  https://www.learnopencv.com/facial-landmark-detection/ <br/>
  https://github.com/spmallick/dlib/ <br/>
