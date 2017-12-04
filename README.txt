THIS APPLICATION IS AN EXPERIMENT WITH OPENCV


USAGE:

VEC GENERATION:

opencv_createsamples \
-vec /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/positive.vec \
-img /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/images/sevenhearts.png \
-bg /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/bg.txt \
-maxxangle 0.1 \
-maxyangle 0.1 \
-maxzangle 0.1 \
-w 20 \
-h 30




CASCADE TRAINING:

opencv_traincascade \
-data /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/cascade \
-vec /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/positive.vec \
-bg /Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/bg2.txt \
-numPos 40 \
-numNeg 40 \
-numStages 7 \
-featureType HAAR \
-minHitRate 1 \
-maxFalseAlarmRate 0.4 \
-w 20 \
-h 30





TROUBLSHOOTING DOCS:

https://stackoverflow.com/questions/16058080/how-to-train-cascade-properly
http://answers.opencv.org/question/10872/cascade-training-error-opencv-244-train-dataset-for-temp-stage-can-not-filled-branch-training-terminated-cascade-classifier-cant-be-trained-check-the/