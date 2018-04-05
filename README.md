# Morphing

## Facial Feature Detection:

  1. git clone https://github.com/spmallick/dlib
  2. cd dlib/examples
  3. mkdir build
  4. cd build
  5. cmake .. 
  6. cmake --build . --config Release

  Download the file from https://github.com/spmallick/dlib and extract it. <br/> <br/>
  Update your face_landmark_detection_to_file.cpp with the one mentioned above. <br/> <br/>
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

  
  
## Reference :
  https://www.learnopencv.com/facial-landmark-detection/ <br/>
  https://github.com/spmallick/dlib/ <br/>
